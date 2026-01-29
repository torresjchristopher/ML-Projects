# Creating source code for HW9

This folder contains the code used to populate the MYSQL server with data for homework assignment 9.

The folder starts pretty empty, with just the Makefile and python source code.

If all the appropriate tools are installed, a simple MAKE ALL will populate the mysql server on CMSC508 with the appropriate tables.

I included this so that the interested students in class see can see a real-world data pipeline in action.

This pipeline:

1. downloads source data in ZIP format from world bank data store.
2. unzips required CSV files.
3. load CSVs into MYSQL using Pandas and sqlalchemy.

