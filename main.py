import click
from dbservice.mariadb.mariadbconnector import MariadbConnector
from dbservice.migratedata import migrate_data
from dbservice.migrateschema import migrate_schema
@click.command()
@click.option(
    "--pre_data_load_sql_stmt",
    required=False,
    help="Optional argument for alter table statement before loading table"
    "Example: ALTER TABLE enrolment MODIFY student_id BIGINT,ALTER TABLE student MODIFY name VARCHAR",
    type=str,
)
@click.option(
    "--post_data_load_sql_stmt",
    required=False,
    help="Optional argument for alter table statement after loading table"
    "Example: ALTER TABLE t1 MODIFY a BIGINT,ALTER TABLE t1 MODIFY a BIGINT",
    type=str,
)
@click.option(
    "--table_names",
    required=False,
    help="For specify tables",
    type=str,
)

def print_menu():
    click.echo()

    return

def main(sql_stmt,table_names):

    migrate_schema(table_names)
    if sql_stmt:
        for sql in sql_stmt.split(","):
            conn = MariadbConnector
            conn.execute(sql)
            conn.close()

    migrate_data(table_names)
    if sql_stmt:
        for sql in sql_stmt.split(","):
            conn = MariadbConnector
            conn.execute(sql)
            conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_menu()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
