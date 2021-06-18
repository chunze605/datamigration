# Reference
# https://mariadb.com/kb/en/load-data-infile/
# https://mariadb.com/kb/en/importing-data-into-mariadb/


def load_data(connector, table, path):


    print(table)
    path = path.replace("\\",'/')
    # replace to local infile from infile
    # path is fixed localmachine's path
    statement = f"""LOAD DATA LOCAL INFILE '{path}'
    INTO TABLE {table}
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\r\n'"""

    connector.execute(statement)
    return



