import mysql.connector


class DBManager:
    def __init__(self, password, database='people', host="db", user="root"):
        self.connection = mysql.connector.connect(user=user, host=f"{host}", password=password,
                                                  database=database)

    def create_table(self):
        # with self.connection.cursor()
        create_query = ("\n"
                        "            create table if not exists info (\n"
                        "            name text not null,\n"
                        "            age integer\n"
                        "            );\n"
                        "        ")
        with self.connection.cursor() as cursor:
            cursor.execute(create_query)

    def select_all(self):
        with self.connection.cursor() as cursor:
            result = []
            cursor.execute("SELECT * FROM info")
            for record in cursor:
                result.append(record)
            return result

    def put_data(self, name: str, age: int):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO info VALUES (%s, %s)", (name, age))
            self.connection.commit()

    def close(self):
        self.connection.close()
