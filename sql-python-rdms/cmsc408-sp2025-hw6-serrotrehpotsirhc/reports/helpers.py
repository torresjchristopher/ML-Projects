"""
Helper scripts for quarto
"""

import os
import re
import sys
import copy
import pandas as pd
from tabulate import tabulate
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ArgumentError, NoSuchModuleError, OperationalError, ProgrammingError


def run_sql_and_return_df(cnx, sql, show_size=True):
    """Given an SQL command and connection string, return a DataFrame."""

    # Check if the connection is None
    if cnx is None:
        error_message = "No valid connection. See above."
        df = pd.DataFrame({'ErrorType': ['ConnectionError'], 'ErrorMessage': [error_message]})

    try:
        df = pd.read_sql(sql, cnx)
        if df.empty:
            # Create a single-row DataFrame with all columns as None
            df = pd.DataFrame([["no records returned"]+ [''] * (len(df.columns) - 1) ], columns=df.columns)

        df = df.replace("None","NULL")
        return df

    except OperationalError as e:
        # Catch connection or database errors
        error_message = f"Operational Error: {str(e)}"
        df = pd.DataFrame({'ErrorType': ['OperationalError'], 'ErrorMessage': [error_message]})
    except ProgrammingError as e:
        # Catch SQL syntax errors or issues with the command
        error_message = f"Programming Error: {str(e)}"
        df = pd.DataFrame({'ErrorType': ['ProgrammingError'], 'ErrorMessage': [error_message]})
#    except mysql.connector.Error as e:
#        # Catch MySQL-specific errors
#        error_message = f"MySQL Connector Error: {str(e)}"
#        df = pd.DataFrame({'ErrorType': ['MySQL Connector Error'], 'ErrorMessage': [error_message]})
    except Exception as e:
        # Catch all other exceptions
        error_message = f"Unknown Error: {str(e)}"
        df = pd.DataFrame({'ErrorType': ['UnknownError'], 'ErrorMessage': [error_message]})
    
    return df

def run_sql_and_return_html( cnx, sql, show_size=True):
    """ """
    df = run_sql_and_return_df( cnx, sql, show_size )

    # Convert the DataFrame to HTML and use custom styling to span columns if needed
    html_output = df.to_html(index=False, na_rep="NULL", justify="center")
    html_output = re.sub(r'\bNone\b', 'NULL', html_output)
    
    # Add colspan attribute to span columns if rendering in an environment that supports it
    html_output = html_output.replace('<td>no records found</td>', f'<td colspan="{len(df.columns)}">no records found</td>')
    
    # Append a row at the bottom with row and column count information
    if show_size and (len(df)>0):
        row_count = len(df)
        col_count = len(df.columns)
        count_row = f'<tr><td colspan="{col_count}" style="text-align: left;">Total Rows: {row_count}, Total Columns: {col_count}</td></tr>'
        html_output = html_output.replace('</tbody>', f'{count_row}</tbody>')

    return html_output

def create_database_engine(uri):
    """Create an SQLAlchemy engine with error handling and test the connection."""

    try:
        # Attempt to create the engine
        engine = create_engine(uri)
        engine.autocommit = True

        # Test the connection with a lightweight query

        run_sql_and_return_df(engine,"select 1 from dual")

#        with engine.connect() as connection:
#            connection.execute(text("SELECT 1"))
        
        return engine  # Return the engine if connection test is successful

    except ArgumentError as e:
        error_message = f"URI Error: {e}"
    except NoSuchModuleError as e:
        error_message = f"Database driver not found: {e}"
    except OperationalError as e:
        error_message = f"Operational error: {e}"
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
    
    return None  # Return None if any error occurs


def create_db_wrapper( config_map ):

    # load and store credentials
    load_dotenv()
    config = {}
    for key in config_map.keys():
        config[key] = os.getenv(config_map[key])

    errors = []
    for param in config.keys():
        if config[param] is None:
            flag = True
            errors.append(f"Missing {config_map[param]} in .env file.")

    cnx = None
    error_df=""
    if errors:
        errors.append("All subsequent SQL commands will fail.")
        errors.append("Fix the .env file and rerun quarto ...")
        # Convert errors to a DataFrame
        error_df = pd.DataFrame({'Errors loading .env file': errors})
        print(f"{'\n'.join(errors)}")
    else:
    # build a sqlalchemy engine string
        engine_uri = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"

        # create and test the database connection.
        cnx = create_database_engine( engine_uri )
    return cnx,config

   

def split_sql_commands(sql):
    # Initialize default delimiter
    delimiter = ';'
    statements = []
    buffer = []

    # Split on newline to process line by line
    lines = sql.splitlines()
    
    for line in lines:
        # Check if the line is a DELIMITER command
        delimiter_match = re.match(r'^DELIMITER\s+(\S+)', line.strip(), re.IGNORECASE)
        
        if delimiter_match:
            # If there's a buffer with previous statements, join them and add to statements
            if buffer:
                statements.append(" ".join(buffer).strip())
                buffer = []
            # Set the new delimiter from DELIMITER command
            delimiter = delimiter_match.group(1)
            continue

        # Use the current delimiter to split statements
        parts = re.split(re.escape(delimiter), line)
        
        # Process all parts except the last (incomplete) part
        for part in parts[:-1]:
            buffer.append(part)
            statements.append(" ".join(buffer).strip())
            buffer = []

        # The last part may be incomplete, so add it to the buffer
        buffer.append(parts[-1])

    # Add any remaining buffer as the last statement
    if buffer:
        statements.append(" ".join(buffer).strip())
        
    return [stmt for stmt in statements if stmt]


def execute_ddl(cnx,ddl_commands):
    """
    Executes DDL statements from a file on a given SQLAlchemy connection, 
    capturing any errors and results.
    """
    messages = []
    errors = []

    # Check if the connection is None
    if cnx is None:
        error_message = "No valid connection. See above."
        df = pd.DataFrame({'ErrorType': ['ConnectionError'], 'ErrorMessage': [error_message]})
        return df.to_html(index=False)

    # Split commands if needed
    ddl_statements = split_sql_commands( ddl_commands )
#    ddl_statements = [cmd.strip() for cmd in ddl_commands.split(';') if cmd.strip()]

    with cnx.connect() as connection:
        for statement in ddl_statements:
            try:
                result = connection.execute(text(statement))
                # Capture the result, if any
                result_info = result.rowcount if result.rowcount != -1 else "No rows affected"
                messages.append(f"Executed statement: {statement}<br/>Result: {result_info}<br/>")
            except Exception as e:
                # Capture the error message if execution fails
                errors.append(f"<hr/>Error executing statement: <b>{statement}</b><br/>    Error: {str(e)}<br/>")

#    return messages, errors

    if errors:
        df = pd.DataFrame({'Errors': errors})
        return df.to_html(index=False)

    return None

def execute_ddl_from_file(filename, cnx):
    """
    Executes DDL statements from a file on a given SQLAlchemy connection, 
    capturing any errors and results.
    """
    messages = []
    errors = []

    with open(filename, 'r', encoding='utf-8-sig') as file:
        ddl_commands = file.read()

    # Split commands if needed, such as if commands are separated by semicolons
    ddl_statements = [cmd.strip() for cmd in ddl_commands.split(';') if cmd.strip()]

    with cnx.connect() as connection:
        for statement in ddl_statements:
            try:
                result = connection.execute(text(statement))
                # Capture the result, if any
                result_info = result.rowcount if result.rowcount != -1 else "No rows affected"
                messages.append(f"Executed statement: {statement}<br/>Result: {result_info}<br/>")
            except Exception as e:
                # Capture the error message if execution fails
                errors.append(f"<hr/>Error executing statement: <b>{statement}</b><br/>    Error: {str(e)}<br/>")

    return messages, errors

if __name__=="__main":
    print(f"{__name__}")
    