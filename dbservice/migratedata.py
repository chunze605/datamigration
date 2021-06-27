from dbservice.oracle.oracleconnector import OracleConnector
from dbservice.mariadb.mariadbconnector import MariadbConnector
from dbservice.mariadb.loaddata import load_data
from dbservice.oracle.dataexport import get_data, write_to_file
from datetime import datetime
import os



def migrate_data():
    staging_path = rf'{os.path.abspath(os.getcwd())}\dbservice\staging_data\{datetime.now().date().__str__()}.csv' # a file path where you want to store ur csv file
    list_tables_query = """select table_name from tabs"""
    oracle_connector = OracleConnector()
    mariadb_connector = MariadbConnector()

    for row in oracle_connector.execute(list_tables_query):
        # get data
        # schema = row[0]
        # table = row[1]
        table = str(row[0])
        data = get_data(oracle_connector,"admin",table) # only 1 schema is used, multiple schema migration still in progress


        # write to staging file
        write_to_file(data,staging_path)

        # load data
        mariadb_connector.execute("""set foreign_key_checks=0""")
        load_data(mariadb_connector, table, staging_path)
        mariadb_connector.execute("""set foreign_key_checks=1""")

        # clear/delete folder
        os.remove(staging_path)
        # break

        # rmtree(staging_path)


    mariadb_connector.close()
    oracle_connector.close()










