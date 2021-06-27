from dbservice.oracle.oracleconnector import OracleConnector
from dbservice.mariadb.mariadbconnector import MariadbConnector
from dbservice.oracle.schemamapping import create_table_statement_migrate

def migrate_schema():
    # Extraction on table description
    list_tables_query = """SELECT DBMS_METADATA.GET_DDL('TABLE',u.table_name)
         FROM USER_ALL_TABLES u
         WHERE u.nested='NO'
         AND (u.iot_type is null or u.iot_type='IOT')"""

    create_table_statement_list = []

    # Instantiate an Oracle connection
    oracle_connector = OracleConnector()

    # Schema Transformation
    for row in oracle_connector.execute(list_tables_query):
        create_table_statement_list.append(create_table_statement_migrate(row[0]))

    # Instantiate an MariaDB connection
    mariadb_connector = MariadbConnector()

    # Schema loading
    for create_table_statements in create_table_statement_list:
        for statement in create_table_statements:
            if statement is not None:
                mariadb_connector.execute(statement)


    oracle_connector.close()
    mariadb_connector.close()





