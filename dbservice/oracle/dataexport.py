import os
import csv

def get_data(connector, schema, table) -> object:
    statement = f"""select * from {schema}.{table}"""

    data = connector.execute(statement)
    return data

def write_to_file(data, path):
    # f = open(path, "w+")
    # for row in data:
    #     f.write(str(row))
    # f.close()
    data = [list(i) for i in data]
    print(data)

    with open(path,"w",newline="") as f:
        write = csv.writer(f)
        write.writerows(data)
    f.close()





