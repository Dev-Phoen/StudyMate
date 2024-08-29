# CREATE TABLE Questions(
#      QuestionID INT AUTO_INCREMENT NOT NULL, 
#      Qt INT,
#      Questions Varchar(255), 
#      CAnswers Varchar(255), 
#      WAnswer1 Varchar(255), 
#      WAnswer2 Varchar(255), 
#      WAnswer3 Varchar(255), 
#      PRIMARY KEY(QuestionID);
import tkinter
import customtkinter
#https://www.youtube.com/watch?feature=shared&v=3vsC05rxZ8c
#followed youtube video as tuttorial on how to implement sql into mython using my sql on 4/9/23
import mysql.connector
import datetime
from datetime import *
from numpy import random
import matplotlib.pyplot as prog
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk )
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import math
import subprocess

#connects the already existing Studymate db to this file 
#
#https://www.geeksforgeeks.org/python-mysql-create-database/
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="//IhateThis128",
    database="StudyMate",
    )
#allows to curse through the database
mcr=db.cursor(buffered=True)
# class that asks the user how many questions they wish to anser

class Number_of_questions():
    """initialises so any method can use this"""
    def Only_numb(self,text):
        #https://pythonassets.com/posts/textbox-entry-validation-in-tk-tkinter/
        #followed above tutorial to ensure that the user can only enter a number 11/12/23
        #only allows for a number to be inputted 
        return text.isdecimal()
    
    def __init__(self,Username,access):
        #whatever user logged in will be used here 
        self.current_user=Username
        Cuser=Username
        self.acess=access
        self.user_data=access
        print("self.user_data------>",self.user_data)
        self.user_id=(self.user_data[1])
        print("user_id--->",self.user_id)
        # sets up the gui window so any method can alter the gui 
        #followed the tutorial in the link above to create the GUI on 4/09/23
        #https://customtkinter.tomschimansky.com/tutorial/grid-system
        self.app=customtkinter.CTk()
        self.app.title("Amount of questions to be asked")
        #validates the entry field so that the user has to enter a number only 
        self.userinput=customtkinter.CTkEntry(self.app,
                                              validate="key",
                                              #%s formats to a string
                                              validatecommand=(self.app.register(self.Only_numb),"%S")
                                              )
        self.tittle=customtkinter.CTkLabel(self.app,text=f"Hello {Cuser} Enter the Number of questions you wish to answer max questions max 24 ")
        self.subbtn=customtkinter.CTkButton(self.app,text="submit",command=self.get_input,fg_color="#3EB489",text_color="Black")
        self.progressbtn=customtkinter.CTkButton(self.app,text="Show progress",fg_color="#3EB489",text_color="Black",command=self.gets_progress)
        self.logoff=customtkinter.CTkButton(self.app,text="Log out",fg_color="#3EB489",text_color="Black",command=self.sign_out)
        self.change_subbtn=customtkinter.CTkButton(self.app,text="Change subject",fg_color="#3EB489",text_color="Black",command=self.change_subject)
        #places the wigets 
        self.tittle.grid()
        self.userinput.grid()
        self.subbtn.grid()
        self.progressbtn.grid()
        self.logoff.grid()
        self.change_subbtn.grid()
        
    
    
    
        
        
        
    """the method/command for the  submit button"""

    def get_input(self):
        #gets what the user had inputted 
        num_questions=self.userinput.get()

        #validates it so there is input
        if num_questions and int(num_questions)>0:
            self.app.destroy()
            #creats the object assign_get_ques which calls the get questions class which is called with the variable num questions 
            #calls get_questions with the value the user has entered
            assign_get_ques=Get_Data(num_questions,self.current_user,self.acess)
            #calls the display class with what the user has entred
            assign_disp=Display(num_questions,self.current_user,self.user_id,self.acess)
            # assign_check=check(num_questions)
            #calls the nrun method from the display
            assign_disp.nrun()
        else:
            self.tittle.configure(text="Cannot be empty or 0")
            
        

        
    
    def gets_progress(self):
        self.app.destroy()
        self.proggress=progress(self.current_user,self.user_id,self.acess)
        self.proggress.retrivesdata()
        self.proggress.show_graph()
        
        
        
    
    def sign_out(self):
        self.app.destroy()
        login=loginpage()
        login.execute()
    
    def change_subject(self):
        self.app.destroy()
        subprocess.Popen(["python","selection_subjects2.py"])
        
        
        
        
        #object is used used in the retrivefromdb method
    def run(self):
        #allows the gui to be seen and be interacted with
        self.app.mainloop()
    

class Get_Data():
    #the value that the user entred is assigned to the class 
    # takes the value that was retrived in num_questions and passes through the constructor, allows the value to passed and used in the class
    def __init__(self,num_questions,Username,acess):
        #allows the value from num_questions to be used in the class 
        self.value_num_questions=num_questions
        self.current_user=Username
        self.acess=acess
        
    def recive_questions(self):
        #https://stackoverflow.com/questions/10195139/how-to-retrieve-sql-result-column-value-using-column-name-in-python
        #used as an example and followed how to do it om 10/09/23 used the above link to assist with most methods using sql
        #selects a random question from the questions table with the question ID 
        #qt is the question type and qt 3 will mean questions on AQA Sociology will be asked
        #https://stackoverflow.com/questions/12867140/python-mysqldb-get-the-result-of-fetchall-in-a-list
        #link used to help form the sql query 
        #https://www.geeksforgeeks.org/sql-select-random/ used to help get the random sql results om 10/09/23
        get_from_db = f"SELECT QuestionID,Questions FROM questions WHERE Qt=3 ORDER BY RAND() LIMIT {self.value_num_questions} "
        run_sql=mcr.execute(get_from_db)
        run_sql
        #fetches all the data 
        qst=mcr.fetchall()
        #puts the data in a list 
        self.qs_list=[questions for questions in qst]
        print(f"Questions= {self.qs_list}")
        #takes the first item in the list to use for another query 
        self.qid=[qst[0] for qst in qst ]
        print("Qid =",self.qid)
    #method to retrive all the data in the dataset 
    def getall(self,num_questions):
        entred=int(num_questions)
        print("-->entred",entred)
        getall = f"SELECT QuestionID FROM questions WHERE Qt=3 "
        run_sql=mcr.execute(getall)
        #fetches all the data 
        fall=mcr.fetchall()
        #puts the data in a list 
        self.allist=[questions for questions in fall]
        print("fall--->",int(len(self.allist)))
        self.max=int(len(self.allist))

    
           
    def get_answeres(self):
        self.getall(self.value_num_questions)
        # sets Id to an interger to be used in a loop
        if int(self.value_num_questions) <= int(len(self.allist)):
            id=int(self.value_num_questions)
            #creates an empty array to put the questions that was fetched from the database 
            self.CAnsweres_list=[]
            #loop to retrive questions from the datase used the Qid to select the certain bits of data 
            for self.id in range(1,id+1):
                #Query to get the correct anserws 
                Selects_correct=f"SELECT QuestionID, CAnswers FROM questions WHERE QuestionID = {self.qid[self.id-1]}"
                #exxecutes the SQL 
                exe_CAns=mcr.execute(Selects_correct)
                fetch_correct=mcr.fetchall()
                #takes the fetched items and puts them into the empty list
                self.CAnsweres_list.append(fetch_correct)
            print(self.CAnsweres_list)
        else:
            print("invalid")
            re=Number_of_questions(self.current_user,self.acess)
            re.tittle.configure(text=f"Invalid please enter a number below {int(len(self.allist))} and above one")
            re.run()
        

    #method to retrive the wrongs answer method assisted throught gpt on 
    def gets_wrong1(self):
        #creates the empty list
        self.wrong1_list=[]
        #a loop that will select the wrong anserers based on qid 
        for self.id in range(1,self.id+1):
            get_wrong1=f"SELECT QuestionID,WAnswer1 FROM questions WHERE QuestionID = {self.qid[self.id-1]}"
            wrong_exe=mcr.execute(get_wrong1)
            wrong1fetch=mcr.fetchall()
            #puts the fetched items into the list 
            self.wrong1_list.append(wrong1fetch)
        print("self.wrong list=",self.wrong1_list)

    def gets_wrong2(self):
        self.wrong2_list =[]
        for self.id in range(1,self.id+1):
            get_wrong2=f"SELECT QuestionID,WAnswer2 FROM questions WHERE QuestionID = {self.qid[self.id-1]}"
            wrong_exe2=mcr.execute(get_wrong2)
            wrong2fetch=mcr.fetchall()
            self.wrong2_list.append(wrong2fetch)
        print("WrongAnswer2:", self.wrong2_list)
    
    def gets_wrong3(self):
        self.wrong3_list=[]
        for self.id in range(1,self.id+1):
            get_wrong3=f"SELECT QuestionID,WAnswer3 FROM questions WHERE QuestionID = {self.qid[self.id-1]}"
            wrong_exe3=mcr.execute(get_wrong3)
            wrong3fetch=mcr.fetchall()
            self.wrong3_list.append(wrong3fetch)
        print(f"WrongAnswers3:", self.wrong3_list)

class Display():
    def __init__(self,num_questions,user,uid,acess):
        self.on_table=num_questions
        self.user=user
        self.uid=uid
        self.acess=acess
        self.question=Get_Data(self.on_table,self.user,self.acess)
        self.question.recive_questions()
        self.question.get_answeres()
        self.question.gets_wrong1()
        self.question.gets_wrong2()
        self.question.gets_wrong3()
        print("self.on_table =",self.on_table)
        self.napp=customtkinter.CTk()
        self.napp.title("StudyMate-Sociology")
        self.ntittle=customtkinter.CTkLabel(self.napp,text=f"Hello {self.user} Please answere: {self.on_table} questions",justify="center")
        self.score=0
        self.show_score=customtkinter.CTkLabel(self.napp,text=f"Score: {self.score}",justify="right")
        self.new=customtkinter.CTkButton(self.napp,text="New Quiz",fg_color="#3EB489",text_color="Black",command=self.redo)
        self.ends_btn=customtkinter.CTkButton(self.napp,text="End quiz and quit",fg_color="#3EB489",text_color="Black",command=self.Ends)
        self.homebtn=customtkinter.CTkButton(self.napp,text="Back to main menue",fg_color="#3EB489",text_color="Black",command=self.backtomenue)
        self.ntittle.grid()
        self.show_score.grid()
        self.new.grid()
        self.ends_btn.grid()
        self.homebtn.grid()
        self.num_of_buttons=int(self.on_table)
        self.num_of_buttons=int(self.num_of_buttons)
    

    #takes the question index selected answer from the button clicked in the lambda function in the button and is passed into the function
        """"""
        #was assisted through chatgpt 12.12.23
    def IsCorrect(self, question_index, selected):
        #correct ans is determined by going through the coorect answers list using the question index
        correct = self.question.CAnsweres_list[question_index - 1]
        if selected == correct:
            print(f"Question {question_index}: Correct")
            self.score += 1
            self.show_score.configure(text=f"Score: {self.score}")            
            #calls method to disable the buttons 
            self.DisableButton(question_index)
            self.shows_right(question_index)
        else:
            print(f"Question {question_index}: Incorrect, try again")
            self.napp.configure(text="Wrong")
            print(f"Incorrect answer for Question {question_index}: Your answer: {selected}, Correct answer: {correct}")
        #calls the disbled method to disable the button
            self.DisableButton(question_index)
            self.shows_wrong(question_index)

    
    #method to disable the button uses the button index to disable the button when clicked and all buttons in the row
    """the disble button method was assisted through chatgpt on the 12.12.23 i used if for the whole method for assistance 
        https://chat.openai.com/c/d188cf59-5535-4b61-ab47-a6524960286d"""
    def DisableButton(self, button_index):
        #the buttons index given by id=i is passed into the BtnDict the buttons are than stored in the dictionary 
        Btns = self.Dict_QA[button_index]
        #the index of the button stored in the button dictionary is than used to disabled the button that is clicked
        Btns['ans_btn'].configure(state='disabled')
        Btns['wr1_dict'].configure(state='disabled')
        Btns['wr2_dict'].configure(state='disabled')
        Btns['wr3_dict'].configure(state='disabled')
    
    def shows_right(self,button_index):
        qs=self.Dict_QA[button_index]
        qs["qs"].configure(text_color="green")
        qs["ans_btn"].configure(text_color_disabled="green")
        qs['wr3_dict'].configure(text_color_disabled="Red")
        qs['wr2_dict'].configure(text_color_disabled="Red")
        qs['wr1_dict'].configure(text_color_disabled="Red")
    
    def shows_wrong(self,button_index):
        qs=self.Dict_QA[button_index]
        qs["qs"].configure(text_color="red")
        qs["ans_btn"].configure(text_color_disabled="green")
        qs["ans_btn"].configure(text_color_disabled="green")
        qs['wr3_dict'].configure(text_color_disabled="Red")
        qs['wr2_dict'].configure(text_color_disabled="Red")
        qs['wr1_dict'].configure(text_color_disabled="Red")
    
    def redo(self):
        today=datetime.today()
        print(today)
        string_today=str(today)
        #destroys the questions window
        outof=f"{self.score}/{self.on_table}"
        print(outof)
        mcr.execute("INSERT INTO progress (name_user,UsersID,Date_last_score,Last_score,outof,Subject) VALUES(%s,%s,%s,%s,%s,%s)",(self.user,self.uid,string_today,self.score,self.on_table,"Sociology"))
        db.commit()
        self.napp.destroy()
        new=Number_of_questions(self.user,self.acess)
        new.run()
        #calls the Number_of_questions window so can get new questions or redo quiz with different question
        ##calls the run method to open the number of questions window
        #calls the method so new questions can be retrived 
        
    
    def Ends(self):
        #https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python used this website to help with datetime on 6/02/24
        today=datetime.today()
        print(today)
        string_today=str(today)
        print("user id is--->",self.uid)
        print(f"You got {self.score} out of {self.on_table}")
        outof=f"{self.score}/{self.on_table}"
        print(outof)
        mcr.execute("INSERT INTO progress (name_user,UsersID,Date_last_score,Last_score,outof,Subject) VALUES(%s,%s,%s,%s,%s,%s)",(self.user,self.uid,string_today,self.score,self.on_table,"Sociology"))
        db.commit()
        self.napp.destroy()
    
    def backtomenue(self):
        self.napp.destroy()
        new=Number_of_questions(self.user,self.acess)
        new.run()
    
    def create_buttons(self):
        """assisted through chatgpt on the 12.12.23 i used it to help create the lambda commands and i used it to help make the variables for the text of the buttons  
        https://chat.openai.com/c/d188cf59-5535-4b61-ab47-a6524960286d"""
        #creating button dictionary was assisted through chat gpt on 12.12.23
        self.Dict_QA = {}
        scroll=customtkinter.CTkScrollableFrame(self.napp,width=750,height=500)
        
        scroll.grid(row=20, column=0, padx=20, pady=20, sticky="ew")
        for i in range(1, self.num_of_buttons + 1):
            #creates the buttons and puts them into a dictionary 
            #variables to get the text for the buttons will loop through the list of retrived data 
            """https://chat.openai.com/c/d188cf59-5535-4b61-ab47-a6524960286d chatGPT/Open Ai was used on 12.12.23 to help make the veriables below for the text to go in the buttons """
            Questiontext = self.question.qs_list[i - 1]
            CAns = self.question.CAnsweres_list[i - 1]
            WAns1 = self.question.wrong1_list[i - 1]
            WAns2 = self.question.wrong2_list[i - 1]
            WAns3 = self.question.wrong3_list[i - 1]
            #creates the buttons 
            qs = customtkinter.CTkLabel(scroll, text=Questiontext)
            
            # uses the labda function to get the selected answer and put it into the list 
            """ the buttons fuction was helped 4/12/23 through the website 
                https://www.tutorialspoint.com/how-to-get-the-value-of-a-button-in-the-entry-widget-using-tkinter
                https://chat.openai.com/c/d188cf59-5535-4b61-ab47-a6524960286d chatGPT/Open Ai was used on 12.12.23 to help make the 
                lambda function/command"""
            
            ans_btn = customtkinter.CTkButton(scroll, text=CAns,fg_color="#3EB489",text_color="Black", border_color="black",
                                                    #command which gets the text from the button clicked and assigns the button with an id
                                                    #passes the id and the ans variable in the finction IsCorrect
                                                command=lambda id=i, select=CAns: self.IsCorrect(id,select))
            wr1_btn = customtkinter.CTkButton(scroll, text=WAns1,fg_color="#3EB489",text_color="Black", border_color="black",
                                                command=lambda id=i, select=WAns1: self.IsCorrect(id, select))
            wr2_btn = customtkinter.CTkButton(scroll, text=WAns2,fg_color="#3EB489",text_color="Black", border_color="black",
                                                command=lambda id=i, select=WAns2: self.IsCorrect(id, select))
            wr3_btn = customtkinter.CTkButton(scroll, text=WAns3,fg_color="#3EB489",text_color="Black", border_color="black",
                                                command=lambda id=i, select=WAns3: self.IsCorrect(id, select))
            #buttons are stored in the dictionary where i is used as the index/key and the buttons/text in buttsons are values
            #dictionaries work by key:value key is used as the index and duplicates
            #https://chat.openai.com/c/d188cf59-5535-4b61-ab47-a6524960286d chatGPT/Open Ai was used on 12.12.23 to help make the dictionary
            self.Dict_QA[i] = {"qs":qs,'ans_btn': ans_btn, 'wr1_dict': wr1_btn, 'wr2_dict': wr2_btn, 'wr3_dict': wr3_btn}

            rng=random.randint(1,4)
            print("rng------>",rng)

            
            

            #puts it on the interfacew using rng to place the order
            """"https://www.w3schools.com/python/numpy/trypython.asp?filename=demo_numpy_random_array
            used the above link to help makw the random number generator which will put the buttons in a certain order based on rng"""
            if rng==1:
                qs.grid()
                ans_btn.grid()
                wr1_btn.grid()
                wr2_btn.grid()
                wr3_btn.grid()
            elif rng==2:
                qs.grid()
                wr1_btn.grid()
                ans_btn.grid()
                wr2_btn.grid()
                wr3_btn.grid()
            elif rng==3:
                qs.grid()
                wr1_btn.grid()
                wr2_btn.grid()
                ans_btn.grid()
                wr3_btn.grid()
            else:
                qs.grid()
                wr1_btn.grid()
                wr2_btn.grid()
                wr3_btn.grid()
                ans_btn.grid()
                
            

        
    
        
   
    def nrun(self):
        self.create_buttons()
        self.napp.mainloop()
    
    


class create_user():
    def __init__(self):
        #creates wigets
        self.create_page=customtkinter.CTk()
        self.create_page_tittle=customtkinter.CTkLabel(self.create_page,text="Create account",justify="center",anchor="center",font=("default",20))
        sign_in=customtkinter.CTkButton(self.create_page,text="sign in",fg_color="#3EB489",text_color="black",command=self.sign_in)
        self.create_username=customtkinter.CTkEntry(self.create_page,placeholder_text="create username")
        self.first_name=customtkinter.CTkEntry(self.create_page,placeholder_text="First name")
        self.LName=customtkinter.CTkEntry(self.create_page,placeholder_text="Last name")
        self.create_password=customtkinter.CTkEntry(self.create_page,placeholder_text="create password",show="*")
        create_account_btn=customtkinter.CTkButton(self.create_page,text="create account",fg_color="#3EB489",text_color="black",command=self.creates_account)
        #places wigets
        self.create_page_tittle.grid()
        self.first_name.grid()
        self.LName.grid()
        self.create_username.grid()
        self.create_password.grid()
        create_account_btn.grid(row=5,column=0)
        sign_in.grid(row=5,column=1)
    
    def sign_in(self):
        self.create_page.destroy()
        log_in_command=loginpage()
        log_in_command.execute()
    
    
    def creates_account(self):
        FName=self.first_name.get()
        LName=self.LName.get()
        new_user=self.create_username.get()
        new_pass=self.create_password.get()
        list_of_users=[]
        selects_users="SELECT Username FROM log_in"
        executes_sql=mcr.execute(selects_users)
        #all_users=mcr.fetchall()
        #https://stackoverflow.com/questions/41897027/python-removing-brackets-from-a-list-of-results used on 11/02/23 to help make the for loop
        for i in mcr.fetchall():
            list_of_users.extend(i)
        print("list_of_users--->",list_of_users)
        print(len(list_of_users))
        new_UID=len(list_of_users)+1
        print(len(new_user))
        print("new_UI--->",new_UID)
        if FName and LName:
            print("Lname -->",FName)
            print("Fname--->",LName)
           # mcr.execute("INSERT INTO users (FName,LName) VALUES(%s,%s)",(FName,LName))
            if new_user and new_pass:
                if new_user in list_of_users:
                    self.create_page_tittle.configure(text="User already exist")
                    print("User already exist")
                else:
                    print(new_user,"\n",new_pass)
                    self.create_page_tittle.configure(text=f"welcome {new_user}")
                    mcr.execute("INSERT INTO users (FName,LName) VALUES(%s,%s)",(FName,LName))
                    db.commit()
                    mcr.execute("SELECT usersID FROM users where fName=%s and LName=%s",(FName,LName))
                    list_uid=[]
                    for i in mcr.fetchall():
                        list_uid.extend(i)

                    print("list_uid--->",list_uid)
                    struid=str(list_uid)
                    
                    mcr.execute("INSERT INTO log_in (UsersID,Username,Pass) VALUES(%s,%s,%s)",(new_UID,str(new_user),new_pass))
                    db.commit()
                    self.create_page.destroy()
                    login=loginpage()
                    login.execute()

                
            else:
                self.create_page_tittle.configure(text="username or password can not be enpty")
                print("username or password cannot be enpty")
        else:
            self.create_page_tittle.configure(text="Lname and Fname Can not be empty")



    def run(self):
        self.create_page.mainloop()
        

class loginpage():
    #https://www.youtube.com/watch?v=98qE8VQNuL0
    #used the video as a tutorial on how to make the log in class on 3/02/24 in which i used a similar format for the SQL statement and followed the video to make the validation if the username or password is correct
    def __init__(self):
        self.login=customtkinter.CTk()
        self.login.title("Login")
        #https://customtkinter.tomschimansky.com/documentation/widgets/label/
        #followed the tutorial in the link above to create the GUI on 4/09/23

        #creates the wigets 
        self.ltittle=customtkinter.CTkLabel(self.login,text="please log in",justify="center",anchor="center")
        self.username=customtkinter.CTkEntry(self.login,placeholder_text="Username")
        self.passwd=customtkinter.CTkEntry(self.login,placeholder_text="password",show="*")
        self.loginbtn=customtkinter.CTkButton(self.login,text="login",fg_color="#3EB489",text_color="black",command=self.GetLogin)
        self.quitbtn=customtkinter.CTkButton(self.login,text="Quit",fg_color="#3EB489",text_color="black",command=self.Quit)
        self.reset_pass=customtkinter.CTkButton(self.login,text="Reset login",fg_color="#3EB489",text_color="black",command=self.reset_login_page)
        self.create_account=customtkinter.CTkButton(self.login,text="create account",fg_color="#3EB489",text_color="black",command=self.new_acc)

        #places the wigets 
        self.ltittle.grid(column=0,row=0,sticky="ew")
        self.username.grid(row=1,sticky="ew",columnspan=2)
        self.passwd.grid(row=2,sticky="ew",columnspan=2)
        self.loginbtn.grid(row=3,column=0,padx=20,pady=20,sticky="ew")
        self.quitbtn.grid(row=3,column=1)
        self.reset_pass.grid()
        self.create_account.grid(row=4,column=1)
    
    def GetLogin(self):
        Uname=self.username.get()
        Pass=self.passwd.get()
        selects_details="SELECT * FROM log_in WHERE Username = %s and Pass = %s "
        values=(Uname,Pass)
        executestP=mcr.execute(selects_details,values)
        access=mcr.fetchone()
        print("acesss--->",access)
        if access is not None:
            print("Welcome")
            self.login.destroy()
            quiz=Number_of_questions(Uname,access)
            quiz.run()
            list_of_user_data=access
            progress(Uname,access,list_of_user_data)
        
        else:
            self.ltittle.configure(text="Username or Pass word does not match")
            self.username.delete(0,"end")
            self.passwd.delete(0,"end")
    
    def Quit(self):
        #https://www.youtube.com/watch?v=IFcIVl6da5o
        #used the video to help make the clear button
        self.login.quit()
        self.login.destroy()
        
        
    def execute(self):
        self.login.mainloop()
    
    def reset_login_page(self):
        self.login.destroy()
        self.Rapp=customtkinter.CTk()
        """used the link 08/2/24 to help build the geometry of the window
        https://customtkinter.tomschimansky.com/documentation/windows/window"""
        #Rapp.geometry("200x250")
        self.Rapp.title("Reset Password page")
        self.Rlabel=customtkinter.CTkLabel(self.Rapp,text="Reset Password",justify="center",font=("default",20))
        self.accountname=customtkinter.CTkEntry(self.Rapp,placeholder_text="Enter username")
        self.newpass=customtkinter.CTkEntry(self.Rapp,placeholder_text="new password",show="*")
        self.confirm=customtkinter.CTkEntry(self.Rapp,placeholder_text="confirm password",show="*")
        subbtn=customtkinter.CTkButton(self.Rapp,text="submit",fg_color="#3EB489",text_color="black",command=self.resets)
        cancel=customtkinter.CTkButton(self.Rapp,text="cancel",fg_color="#3EB489",text_color="black",command=self.quits)
        self.Rlabel.grid()
        self.accountname.grid(row=1,sticky="ew",columnspan=2)
        self.newpass.grid(row=2,sticky="ew",columnspan=2)
        self.confirm.grid(row=3,sticky="ew",columnspan=2)
        subbtn.grid(row=4,column=0,padx=20,pady=20,sticky="ew")#,columnspan=2,anchor="center")
        cancel.grid(row=4,column=1)#,columnspan=2,anchor="center")
        self.Rapp.mainloop()

    
    def resets(self):
        users_list=[]
        selects_users="SELECT Username FROM log_in"
        executes_sql=mcr.execute(selects_users)
        #all_users=mcr.fetchall()
        #https://stackoverflow.com/questions/41897027/python-removing-brackets-from-a-list-of-results used on 11/02/23 to help make the for loop
        for i in mcr.fetchall():
            users_list.extend(i)

        account=self.accountname.get()
        newpass=self.newpass.get()
        confirm=self.confirm.get()
        print("account------->",account)
        print("newpass------->",newpass)
        print("confirm------->",confirm)
        """https://stackoverflow.com/questions/1307378/python-mysql-update-statement/1307400 used on 9/2/24 to help create the 
        update command for the method"""
        if account in users_list:
            if newpass==confirm:
                mcr.execute("""UPDATE log_in SET Pass=%s WHERE Username=%s """,(confirm,account))
                db.commit()
                self.Rapp.destroy()
                again=loginpage()
                again.execute()
            else:
                self.Rlabel.configure(text="Passwords do not match")
                self.newpass.delete(0,"end")
                self.confirm.delete(0,"end")
        else:
            self.Rlabel.configure(text="Username doesnt exist")
        
    
    def quits(self):
        self.Rapp.destroy()
        again=loginpage()
        again.execute()
        
    
    def new_acc(self):
        self.login.destroy()
        create=create_user()
        create.run()


class progress():
    def __init__(self,name,details,acess):
        self.name=name
        self.details=details
        self.acess=acess
        print("self.acess line 651--->",self.acess)
        self.graph=customtkinter.CTk()
        
        # self.graph.state("zoomed")
        self.graph.title("Progress of Sociology from")
        quits=customtkinter.CTkButton(master=self.graph,text="Close",command=self.quits)
        quits.pack(side=tkinter.BOTTOM)
    
    def retrivesdata(self):
        lst_score=[]
        lst_out_of=[]
        #https://stackoverflow.com/questions/14279849/how-to-remove-time-from-datetime taken on 11/03/24
        mcr.execute("""SELECT Last_score FROM progress WHERE Subject=%s AND name_user=%s AND UsersID=%s ORDER BY outof ASC, Last_score ASC, ProgressID ASC""",("Sociology",self.name,self.details))
        for score in mcr.fetchall():
            lst_score.extend(score)
        print("lst_score-->",lst_score)
        mcr.execute("""SELECT outof FROM progress WHERE Subject=%s AND name_user=%s AND UsersID=%s ORDER BY outof ASC, Last_score ASC, ProgressID ASC""",("Sociology",self.name,self.details))
        for outof in mcr.fetchall():
            lst_out_of.extend(outof)
        print("lst_out_of-->",lst_out_of)
        #https://stackoverflow.com/questions/14279849/how-to-remove-time-from-datetime taken on 26/03/24
        #sql statment assistance
        mcr.execute("""SELECT MAX(DATE_FORMAT(Date_last_score,'%d/%m/%Y')) FROM progress""")
        most_recent=[]
        for date in mcr.fetchall():
            most_recent.extend(date)
        earliest=[]
        mcr.execute("""SELECT MIN(DATE_FORMAT(Date_last_score,'%d/%m/%Y')) FROM progress""")
        for early in mcr.fetchall():
            earliest.extend(early)
        

        prog.title("Progress of Sociology")

        prog.ylabel('Score')
        prog.xlabel("Out Of")
        biggest_score=max(lst_score)
        biggest_out_of=max(lst_out_of)
        prog.ylim(0,int(biggest_score+1))
        prog.xlim(1,int(biggest_out_of+1))
        #https://github.com/TomSchimansky/CustomTkinter/issues/93 was used to help create the below code in 23/03/24
        #followed as a tutorial sections were used 
        #creates the figure the graph will fit in the window 
        #dpi will determine how big the graph is
        fig=Figure(figsize=(5,4),dpi=100)
        ax=fig.add_subplot()
        #https://stackoverflow.com/questions/69597448/embedding-matplotlib-graph-on-tkinter-gui used on 23/03/24 to help label the graph
        ax.plot(lst_out_of,lst_score,'-ro',label="Score/Out of")
        ax.set_ylabel('score')
        ax.set_xlabel('outof')
        ax.set_title(f"Progress of Sociology for {self.name} from {earliest} to {most_recent}")
        
        plots=FigureCanvasTkAgg(fig,master=self.graph)
        plots.draw()
        plots.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        tools=NavigationToolbar2Tk(plots,self.graph)
        tools.update()
        plots.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        # prog.plot(lst_out_of,lst_score,'-ro',label="Score/Out of")
        # prog.legend()
        # prog.show()

    def show_graph(self):
        self.graph.mainloop()
    
    def quits(self):
        self.graph.quit()
        self.graph.destroy()
        str(self.details)
        numq=Number_of_questions(self.name,self.acess)
        print("self.acess--->",self.acess)
        numq.run()

        
        
        




if __name__ =='__main__':
    start=loginpage()
    start.execute()
    print(__name__)
                
