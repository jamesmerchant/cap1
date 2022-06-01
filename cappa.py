from cgitb import text

import sqlite3

import pandas as pd

# from subprocess import call

import bcrypt

import csv

import datetime

import sys

















conn = sqlite3.connect('cap_database.db')

c = conn.cursor()







def export_to_csv():# Get data in batches

    # Open the file

    f = open('output.csv', 'w')



    data = pd.read_sql_query('SELECT * FROM Assessment_Results', conn)

    

    # We are done if there are no data

    if len(data) == 0:

        return

    # Let's write to the file

    else:

        data.to_csv('output.csv')



    # Clean up

    f.close()





#login#####



def login():

#store your password:

    email = input("Enter your email: \n")

    password = input("input password: \n")

   

    sql_query = c.execute("SELECT password FROM Users WHERE email =?", (email,)).fetchone()

    

    

    if sql_query[0] == 'password':

        print("ENter your password")

    elif sql_query[0] == bcrypt.hashpw(password.encode,bcrypt.gensalt()('utf-8'), sql_query[0]):

        print("login success")



# login()

 

   











'''Create Table in Database'''

c.execute('CREATE TABLE IF NOT EXISTS Users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT,phone INTEGER, email TEXT NOT NULL, password TEXT, active INTEGER, date_created TEXT, hire_date INTEGER, user_type TEXT)')

c.execute('CREATE TABLE IF NOT EXISTS Competencies(Competency_id INTEGER PRIMARY KEY,comp_name TEXT, date_created INTEGER,competency_scale INTEGER)')

c.execute('CREATE TABLE IF NOT EXISTS Assessments(assessment_id INTEGER PRIMARY KEY, date_created INTEGER,assessment_name TEXT)')

c.execute('CREATE TABLE IF NOT EXISTS Assessment_Results(user_id INTEGER,assessment_result_name TEXT, assessment_id INTEGER,assessment_result_id INTEGER, score INTEGER, date_taken INTEGER, manager TEXT,PRIMARY KEY (user_id, assessment_result_id),FOREIGN KEY (user_id) REFERENCES Users (user_id),FOREIGN KEY (assessment_id) REFERENCES Assessments (assessment_id)) ')



# CREATE TABLE IF NOT EXISTS Student_Cohort_Registrations (student_id INTEGER,cohort_id INTEGER,registration_date TEXT NOT NULL,completion_date TEXT,drop_date TEXT,active INTEGER DEFAULT 1,PRIMARY KEY (student_id, cohort_id),FOREIGN KEY (student_id) REFERENCES People (person_id),FOREIGN KEY (cohort_id) REFERENCES Cohorts (cohort_id))



'''Instert multiple rows of data into the table'''



conn.commit()

# conn.close()









'''Tracker file to modify and update the database: [table = 'str']'''

conn = sqlite3.connect('cap_database.db')

c = conn.cursor()





'''Function to Display all tables in relational database'''

def print_table(table):

    

    print('/-----------------------\\')

    print(table + '\n-------------')#prints table header

    for row in c.execute(f'SELECT * FROM {table}'):

        print(row)

    print('\-----------------------/')



'''Function to display add/edit menu 1'''

def add_edit_menu():

    print_table('USERS,COMPETENCIES,ASSESSMENTS,ASSESSMENT_RESULTS')

    print('\-----------------------/')

    print('e). Exit\n')



'''function to display menu 1'''

def menu_1():

    print('\nMenu')

    print('1). Add User')

    print('2). Edit User')

    print('3). Add Competency')

    print('4). Edit Competency')

    print('5). Add Assessment')

    print('6). Edit Assessment')

    print('7). Add Assessment Result')

    print('8). Edit Assessment Result')

    print('9). Export to CSV')

    print('e). Exit\n')



def add_user():

    #first_name, last_name, phone, email, password, active, date_created, hire_date, user_type

    

    first = input('Please enter first name')

    last = input('Please enter last name')

    email = input('Please enter email')

    password = input('Please enter password')

    active = input('enter 1 for active or 0 for inactive user')

    date_created = input('Please enter date created')

    date_hired = input('Please enter date hired')

    user_type = input('Please enter "normal" or "manager"')



    USERS = [first,last,email,password,int(active),date_created,date_hired,user_type]



    c.execute('INSERT INTO Users (first_name, last_name, email, password, active, date_created, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?)',USERS)



    conn.commit()





def edit_user():

    c.execute('UPDATE Users SET first_name = ? WHERE user_id = ',(value, user_id))



def add_competency():

    Assessment = input('please enter Assessment')

    date_created = input('please enter date created')

    competency_scale = input('please enter competency value')

    

    COMPETENCIES = [Assessment,date_created,competency_scale]



    c.execute('INSERT INTO Competencies (Assessment, date_created, competency_scale) VALUES (?,?,?)',COMPETENCIES)

    

    conn.commit()



def edit_Competency():

    c.execute('UPDATE Competencies SET comp_name = ? WHERE Competency_id = ',(comp_value, Competency_id))



def add_Assessment():

    assessment_name = input('please enter Assessment Name: ')

    date_created = input('Please enter date created: ')

    

    assessment_info = [assessment_name, date_created]



    c.execute('INSERT INTO Assessments (assessment_name, date_created) VALUES (?,?)', assessment_info)

    

    conn.commit()



def edit_Assessment():

    c.execute('UPDATE Assessments SET assessment_name = ? WHERE assessment_id =?',(ass_value, assessment_id))



def add_assessment_result():

    

    user = input('please enter user')

    assessment_result_name = input(' Please name your assessment result')

    assessment = input('please enter assessment')

    score = input('Please enter the score')

    date_taken = input('Please enter the date taken')

    manager = input('please enter manager')





    ASSESSMENT_RESULTS = [user, assessment_result_name, assessment,score,date_taken, manager]

    

    c.execute('INSERT INTO Assessment_Results (user_id, assessment_result_name, assessment_id, score, date_taken, manager) VALUES (?,?,?,?,?,?)', ASSESSMENT_RESULTS)

    conn.commit()



def edit_Assessment_Result():

    c.execute('UPDATE Assessment_Results SET assessment_results_name = ? WHERE assessment_result_id =?',(asr_value,assessment_result_id))







def feedback(text):

    c.execute('SELECT User,first_name FROM Users WHERE user_id = ?')

    data = c.fetchone()



    print(f'{data[0]} user has been changed to{data[1]}')







def feedbackcomp():

    data =  c.execute('SELECT Competencies,comp_name FROM Competencies WHERE Competency_id = ?').fetchone()



    print(f'{data[0]} Competency has been changed to{data[1]}')

    print(current_date_time)



def feedbackass():

    c.execute('SELECT Assessment,assessment_name FROM Assessments WHERE assessment_id = ? ')

    data = c.fetchone()



    print(f'{data[0]} Assessment has been changed to{data[1]}')



def feedbackasr():

    c.execute('SELECT * FROM Assessment_Results WHERE assessment_result_id = ?')

    data = c.fetchone()



    print(f'{data[0]} Assement Result has been changed to{data[1]}')





while True:

    print_table('USERS,COMPETENCIES,ASSESSMENTS,ASSESSMENT_RESULTS')

    menu_1()

    choice =input("How can I help you today?")

    if choice == '1':

        

        add_edit_menu()

        # response = input('Which User?:')

        # if response == 'e':

            

        #     sys.exit()

        # else:

        add_user()

        

        print("User added")



    elif choice == '2':

        

        add_edit_menu()

        user_id = input('Which User?:')

        value = input('Please provide a new value for this User:')

        edit_user(value,user_id)

        

        feedback(user_id)



    elif choice == '3':

        

        add_edit_menu()

        add_competency()

        

        feedbackcomp()



    elif choice =='4':

        

        add_edit_menu()

        Competency_id = input('Which Competency?:')

        comp_value = input('Please provide a new value for this Competency:')

        edit_Competency(comp_value,Competency_id)

        

        feedbackcomp(Competency_id)



    elif choice =='5':

        

        # add_edit_menu()

        # response = input('Which Assessment?:')

        add_Assessment()

        

        # feedbackass(response)



    elif choice =='6':

        

        add_edit_menu()

        assessment_id = input('Which Assessment?:')

        ass_value = input('Please provide a new value for this Assessment:')

        edit_Assessment(ass_value,assessment_id)

        

        feedbackass(assessment_id)

        

    elif choice == '7':

    

        add_edit_menu()

        add_assessment_result()



        print('Assessment result added')



    elif choice == '8':

        

        add_edit_menu()

        assessment_result_id = input('Which Assessment Results?:')

        asr_value = input('Please provide a new value for this Assessment Result:')

        edit_Assessment_Result(asr_value,assessment_result_id)

        

        feedbackasr(assessment_result_id)

    elif choice == '9':

        export_to_csv()



    elif choice == 'e':

        break









