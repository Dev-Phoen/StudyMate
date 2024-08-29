# imports my GUI frame wrk 
import customtkinter
from customtkinter import *
import subprocess
#Creats the GUI

#gives the name selection to the window 

# shows the text "subject" on the window 
# allows the text to be commited to the GUI 
# A function that show what the user has chosen from the combobox 


class selection():
    def __init__(self):
        self.app=customtkinter.CTk()
        self.app.title("selection")
        self.tittle=customtkinter.CTkLabel(self.app,text="Please choose a subject:",font=("defult",20))
        self.tittle.grid()
        self.combo=customtkinter.CTkComboBox(master=self.app,values=["History Russia","History Britain","Sociology"],)
        self.btn=customtkinter.CTkButton(self.app,text="Choose",command=self.option,fg_color="#3EB489",text_color="black")
        self.combo.grid(padx=20,pady=10,sticky="ew")
        self.btn.grid()

        


    
    def submit(self):
    #this retrives the data from the combobox 
        selected= self.combo.get()
        print("You have selected:",selected)



# a function that will open another Python file depending on what they chosen from the combo box 
    def option(self):
    # will retrive the data from the combo box 
        opt=self.combo.get()
    # will compare what user has selected
        if opt == "History Russia":
            subprocess.Popen(["python","Russia7.py"])
            self.app.quit()
            self.app.destroy()
        #will open another python file called "Russia_GUI.py" if user chose it 
        # with open("Russia_GUI.py") as f:
        #     # allows it to be opend if the user chose it 
        #     exec(f.read())
        elif opt == "History Britain":
            subprocess.Popen(["python","Brit76.py"])
            self.app.quit()
            self.app.destroy()
        # with open("Britain_GUI.py") as f:
        #     exec(f.read())
        #     app_path="C:\Users\BTEC09\Documents\OneDrive - Thomas Deacon Education Trust\Documents\sixthform\y13\computer science"
        #     subprocess.Popen(app_path)
        else:
            opt == "Sociology"
            subprocess.Popen(["python","Sociology7.py"])
            self.app.quit()
            self.app.destroy()
        # with open("Sociology_GUI.py") as f:
        #     exec(f.read())
    
    def run(self):
        self.app.mainloop()

subject=selection()
subject.run()
        


