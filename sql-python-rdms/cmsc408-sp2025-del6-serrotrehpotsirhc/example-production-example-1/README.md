# Production example for web system


## Folder structure

Below is the folder structure for this example

```
./
├── db/
│   └── my-ddl.sql
├── site/
│   ├── index.php
│   └── show-table.php
├── nginx.conf
└── docker-compose.yml
└── docker-apache-php
```

*./db* - contains the DDL code to initialize the database

*./site* - contains the web site code with appropriate connection code to use a local container with mysql.

## Running the example

```
docker-compose up -d
```

If all goes well, visit:  <http://localhost> to see the website and <http://localhost/phpmyadmin> to view phpmyadmin for the local copy of the database.

