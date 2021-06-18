import os
from os import getenv
from dbservice.oracle.oracleconnector import OracleConnector
from dbservice.mariadb.mariadbconnector import MariadbConnector


oracle_connector = OracleConnector()

for row in oracle_connector.describe("select * from EMPLOYEES"):
    row = list(row)
    temp = str(row[1])
    temp = temp.replace('<cx_Oracle.DbType DB_TYPE_','')
    temp = temp.replace('>', '')
    row[1] = temp
    print(row)

constraint_query = """SELECT *
from user_constraints natural join user_cons_columns
where table_name = 'EMPLOYEES'"""
for row in oracle_connector.execute(constraint_query):
    print(row)


mariadb_connector = MariadbConnector()
mariadb_connector.execute("""set global foreign_key_checks=1""")
mariadb_connector.execute("""set foreign_key_checks=1""")
# print(mariadb_connector.execute("""SELECT VARIABLE_NAME, SESSION_VALUE, GLOBAL_VALUE FROM
#   INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE
#   VARIABLE_NAME LIKE 'foreign_key_checks'"""))


variables = """SELECT VARIABLE_NAME, SESSION_VALUE, GLOBAL_VALUE FROM
  INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE
  VARIABLE_NAME LIKE 'foreign_key_checks'"""

for row in mariadb_connector.execute(variables):
    print(row)

mariadb_connector.close();




