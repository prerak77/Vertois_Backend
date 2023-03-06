import mysql.connector as mys


#                   To Create a Database
def create_database():
    try:
        myconn = mys.connect(host="sql12.freemysqlhosting.net",
                             user="sql12602665", passwd="FAUkhKG9WP", port="3306")
        mycur = myconn.cursor()
        query = "create database UserInfo"
        mycur.execute(query)
        myconn.commit()
        print("Database successfully created")

    except Exception as e:
        pass


#                   To create a table for CAR MODEL details
def create_table_user():
    try:
        myconn = mys.connect(host="sql12.freemysqlhosting.net",
                             user="sql12602665", passwd="FAUkhKG9WP", database="sql12602665", port="3306")
        mycur = myconn.cursor()
        query = "CREATE TABLE user_details (name VARCHAR(255), email VARCHAR(255),password VARCHAR(255),ID VARCHAR(255))"
        mycur.execute(query)
        myconn.commit()
        print("Table successfully created")

    except Exception as e:
        print(e)


def insert_table_user(details):
    try:
        KEYS = list(details["content"].keys())
        VALUES = list(details["content"].values())

        print(VALUES)
        myconn = mys.connect(host="sql12.freemysqlhosting.net", user="sql12602665",
                             passwd="FAUkhKG9WP", database="sql12602665")
        mycur = myconn.cursor()
        query = "insert into user_details values\
                                            ('{}','{}','{}','{}')".format(VALUES[0], VALUES[1], VALUES[2], '')
        mycur.execute(query)
        myconn.commit()
    except Exception as e:
        print(e)


def get_data(id):
    try:
        VALUES = list(id["content"].values())

        print(VALUES[0])
        myconn = mys.connect(host="sql12.freemysqlhosting.net", user="sql12602665",
                             passwd="FAUkhKG9WP", database="sql12602665")
        if myconn.is_connected():
            print("Succesfully connected")
        mycur = myconn.cursor()
        query = "SELECT * FROM user_details where user_details.email = '{}' and user_details.password = '{}' ".format(
            VALUES[0], VALUES[1])
        mycur.execute(query)
        rs = mycur.fetchall()
        print(rs[0])
        if len(rs[0]) != 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)


create_table_user()
