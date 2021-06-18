from dbservice.oracle.oracleconnector import OracleConnector
from dbservice.mariadb.mariadbconnector import MariadbConnector
from dbservice.mariadb.loaddata import load_data
from dbservice.oracle.dataexport import get_data, write_to_file
from datetime import datetime
import os



#staging_path = f'staging_data\table\{datetime.now().date().__str__()}.csv' # a file path where you want to store ur csv file

staging_path = rf'C:\Users\Chun\Desktop\MyFiles\sem9\fyp\app\dbservice\staging_data\table\{datetime.now().date().__str__()}.csv' # a file path where you want to store ur csv file

#list tables name
# list_tables_query = """SELECT u.schema, u.table_name
#      FROM USER_ALL_TABLES u
#      WHERE u.nested='NO'
#      AND (u.iot_type is null or u.iot_type='IOT')"""

list_tables_query = """select table_name from tabs"""


oracle_connector = OracleConnector()
mariadb_connector = MariadbConnector()

for row in oracle_connector.execute(list_tables_query):
    # get data
    # schema = row[0]
    # table = row[1]
    table = str(row[0])
    data = get_data(oracle_connector,"admin",table) # only 1 schema is used, multiple schema migration still in process


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










