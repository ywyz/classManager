import pymysql
import os


class SQLConnect:
    def __init__(self, user, password):
        self.host = "sh-cynosdbmysql-grp-lhkebs8k.sql.tencentcdb.com"
        self.user = user
        self.password = password
        self.db = user
        self.port = 21651
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          port=self.port,
                                          db=self.db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.connection = None  # Database connection object
        self.cursor = None



    def connect(self):
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              port=self.port,
                                              db=self.db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()


            return True

        except pymysql.MySQLError as e:
            print(f"Failed to connect to database: {e}")
            return False

    def setAccount(self):
        os.environ['MYSQL_USER'] = self.user
        os.environ['MYSQL_PASSWORD'] = self.password
        os.environ['MYSQL_HOST'] = self.host
        os.environ['MYSQL_PORT'] = str(self.port)
        os.environ['MYSQL_DB'] = self.db

    def close(self):
        self.connection.close()

        os.environ.pop('MYSQL_USER')
        os.environ.pop('MYSQL_PASSWORD')
        os.environ.pop('MYSQL_HOST')
        os.environ.pop('MYSQL_PORT')
        os.environ.pop('MYSQL_DB')
        os.environ.pop('MYSQL_DB')

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        if self.connection:
            self.connection.commit()

    def rollback(self):
        if self.connection:
            self.connection.rollback()
    def clearAccount(self):
        os.environ.pop('MYSQL_USER')
        os.environ.pop('MYSQL_PASSWORD')
        os.environ.pop('MYSQL_HOST')
        os.environ.pop('MYSQL_PORT')
        os.environ.pop('MYSQL_DB')

    def uploadStudentData(self, data):
        self.cursor.execute("INSERT INTO StudentData (stu_id, stu_name, stu_sex, stu_birthday, stu_idcard, stu_address, \
        stu_moname,stu_moid, stu_faname, stu_faid, stu_mophone, stu_faphone, stu_liveaddress) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)

        try:
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False

    def uploadTeacherData(self, data):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO TeacherData (date, class_name, teacher_name, content_name, goal, content, \
                       evaluation_analysis, support_strategy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", data)

        try:
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False
    def uploadThingsData(self, data):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO ThingsData (date, class_name, device_id, device_name, address, is_repaired) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)", data)

        try:
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False
    def uploadHealthyData(self, data):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO StudentHealthy (date,class_name, stu_id, stu_name, stu_height, stu_weight,\
        stu_visionleft, stu_visionright, stu_hmoglobin,) VALUES (%s, %s, %s, %s, %s, %s, %s)", data)

        try:
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False

    def uploadDailuAttendData(self, data):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO StudentDailyAttend (date, class_name, stu_id, stu_name, is_attend, \
                       reason, is_gotohospital) VALUES (%s, %s, %s, %s, %s, %s, %s)", data)

        try:
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False
