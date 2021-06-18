import cx_Oracle
from os import getenv


class OracleConnector:
    def __init__(self):
        self.hostname = getenv('HOSTNAME')
        self.sid = getenv('ORACLE_SID')
        self.pid = getenv('ORACLE_PID')
        self.user = getenv('ORACLE_USER')
        self.pwd = getenv('ORACLE_PWD')

        self.dsn_tns = cx_Oracle.makedsn(self.hostname, "1521", self.sid, self.pid)  # need to mask credentials
        self.connection = cx_Oracle.connect(
            user=self.user, password=self.pwd, dsn=self.dsn_tns, encoding="UTF-8"
        )

    def execute(self, statement):
        cursor = self.connection.cursor()
        cursor.callproc(
            "DBMS_METADATA.SET_TRANSFORM_PARAM", ["-1", "STORAGE", False]
        )
        cursor.callproc(
            "DBMS_METADATA.SET_TRANSFORM_PARAM", ["-1", "TABLESPACE", False]
        )
        cursor.callproc(
            "DBMS_METADATA.SET_TRANSFORM_PARAM", ["-1", "SEGMENT_ATTRIBUTES", False]
        )
        cursor.callproc(
            "DBMS_METADATA.SET_TRANSFORM_PARAM", ["-1", "EMIT_SCHEMA", False]
        )
        cursor.callproc(
            "DBMS_METADATA.SET_TRANSFORM_PARAM", ["-1", "SQLTERMINATOR", True]
        )



        cursor.execute(statement)


        records = [row for row in cursor]

        # self.connection.commit()
        # self.connection.close()

        return records

    def close(self):
        self.connection.commit()
        self.connection.close()
        return

    def describe(self, statement):

        cursor = self.connection.cursor()
        cursor.execute(statement)
        return cursor.description










