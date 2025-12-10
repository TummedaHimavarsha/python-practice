import pymysql
try:
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pinkychinnu200"
    )
    print("Connection Successful")
except Exception as e:
    print("Connection Failed",e)
cursor=conn.cursor()
try:
    cursor.execute("create database if not exists 66r")
    print("database created successfully")
except Exception as e:
    print("database creation failed",e)
def create_table():
    try:
        cursor.execute("use 66r")
        cursor.execute("""create table if not exists student
        (id int primary key auto_increment,
        name varchar(20),age int,
        gender varchar(10))""")
        print("table created successfully")
    except Exception as e:
        print("table creation failed",e)
def insert_data():
    try:
        cursor.execute("USE 66r")
        cursor.execute("""
            INSERT INTO student (name, age, gender) VALUES
            ('chinnu',22,'male'),
            ('pinky',21,'female'),
            ('prasanna',23,'female'),
            ('jyothika',24,'female')
        """)
        # conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Data insertion failed:", e)
def men():
    print("1.create table\n2.insert data\n3.view data\n4.update data\n5.delete data\n6.exit")
    ip=int(input("enter your choice:"))
    if ip==1:
        create_table()
    elif ip==2:
        insert_data()
men()

        
