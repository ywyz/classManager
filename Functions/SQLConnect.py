import pymysql


class SQLConnect:
    def __init__(self, user, password):
        self.host = "sh-cynosdbmysql-grp-lhkebs8k.sql.tencentcdb.com"
        self.user = user
        self.password = password
        self.db = user
        self.port = 21651

    def connect(self):
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              port=self.port,
                                              db=self.db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
            return True

        except pymysql.MySQLError as e:
            print(f"Failed to connect to database: {e}")
            return False

    def close(self):
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
