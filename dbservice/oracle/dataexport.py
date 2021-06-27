
import csv
def get_data(connector, schema, table) -> object:
    statement = f"""select * from {schema}.{table}"""
    data = connector.execute(statement)
    return data

def write_to_file(data, path):

    with open(path,"w",newline="") as f:
        write = csv.writer(f)
        write.writerows(data)
    f.close()





