import sys
import csv
import os
sys.path.append("..")
from src.DBManager import DBManager


def get_data(filename: str) -> list:
    with open(filename, "r") as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        data = [(row[0], int(row[1])) for row in reader]
        return data


if __name__ == '__main__':
    conn = DBManager(password=os.environ['MARIADB_ROOT_PASSWORD'])
    try:
        conn.create_table()
        data = get_data("/src/filler/data.csv")
        for name, age in data:
            conn.put_data(name, age)
        result_db_contents = conn.select_all()
        print("Result table content after filling:\nname, age")
        for el in result_db_contents:
            print(el)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
# conn.create_table()
