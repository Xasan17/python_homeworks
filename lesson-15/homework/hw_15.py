#1 
import sqlite3 
with sqlite3.connect("test.db") as conn:
    point = conn.cursor()
    create = """create table Roster (Name text, Species text, Age int)"""
    point.execute(create)
    conn.commit()
#2
with sqlite3.connect("test.db") as conn:
    point = conn.cursor()
    insert = """insert into Roster values ('Benjamin Sisko','Human', 40), ('Jadzia Dax','Trill',300),('Kira Nerys', 'Bajoran',29)"""
    point.execute(insert)
    conn.commit()
#3
with sqlite3.connect("test.db") as conn:
    point = conn.cursor()
    insert = """update Roster set Name='Ezri Dax' where Name='Jadzia Dax'"""
    point.execute(insert)
    conn.commit()
#4
with sqlite3.connect("test.db") as conn:
    select = """select name, age from Roster  where Species = 'Bajoran'"""
    cursor = conn.cursor()
    a=cursor.execute(select)
    print(a.fetchall())
    conn.commit()
