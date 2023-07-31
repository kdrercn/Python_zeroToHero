import mysql.connector
from datetime import datetime
from connection import connection


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()     
   
    @staticmethod
    def updateStudent(id, name, surname):
        connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="schooldb")
        cursor = connection.cursor()

        sql = "Update student Set name= %s, surname= %s where id= %s"
        values = (name, surname, id)
        cursor.execute(sql, values)

        try:
                connection.commit()   
                print(f'{cursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
                print('hata:', err)
        finally:
                connection.close()
                print('database bağlantısı kapandı.')

Student.updateStudent(15,"Kadir","Ercen")

