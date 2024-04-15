# Required Libraries
# For GUI
from tkinter import *
from tkinter import ttk
from PIL import  Image,ImageTk
from tkinter import messagebox
from pymongo import MongoClient # For MongoDB
# For Generating Invoice
import gtts
import playsound
import re # For Strong Password Requirements
import os # For OS Operations
# For Including Other Project Windows
from registration import Register_Window
from main import Face_Recognition_System
from admin import Admin

message = [] # To Check The Password Requirements

# Main class
class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1560x820+0+0")
        self.root.title("Login")

        # Variables
        self.var_uname = StringVar()
        self.var_pass = StringVar()

        # First Top Image
        img = Image.open(r"images\main\img1.jpg")
        img = img.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        # Second Top Image
        img1 = Image.open(r"images\main\img2.jpg")
        img1 = img1.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        # Third Top Image
        img2 = Image.open(r"images\main\img3.png")
        img2 = img2.resize((520,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1050,y=0,width=520,height=130)

        # Top Title Label
        title_label = Label(self.root,text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=130,width=1530,height=45)

        # Background Image Below Login Frame
        self.bg = ImageTk.PhotoImage(file=r"images\login\background.jpg")
        lbl_bg =Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=175,relwidth=1,relheight=1)

        # Main Frame For Login Entries
        main_frame = Frame(self.root,bg="black")
        main_frame.place(x=610,y=250,width=340,height=380)

        # Login Frame Top Label
        get_strt_label = Label(main_frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_strt_label.place(x=95,y=40)

        # User UserName
        uname_label = Label(main_frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        uname_label.place(x=40,y=95)

        uname_entry = ttk.Entry(main_frame,textvariable=self.var_uname,width=20,font=("times new roman",12))
        uname_entry.place(x=40,y=125,width=270)

        # User Password
        pass_label = Label(main_frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pass_label.place(x=40,y=165)

        pass_entry = ttk.Entry(main_frame,textvariable=self.var_pass,width=20,font=("times new roman",12),show="*")
        pass_entry.place(x=40,y=195,width=270)

        # Login Button
        login_button = Button(main_frame,command=self.login,text="Login",cursor="hand2",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_button.place(x=110,y=240,width=120,height=35)

        # Registration Button
        register_button = Button(main_frame,command=self.registration_window,text="New User Register",cursor="hand2",font=("times new roman",11,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_button.place(x=18,y=290,width=160)

        # Forgot Password Button
        forgot_password_button = Button(main_frame,command=self.forgot_password,text="Forget Password",cursor="hand2",font=("times new roman",11,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgot_password_button.place(x=10,y=325,width=160)


#-------------------------------------------------- function declaration ---------------------------------------------------------

    # ******************* Login *******************
    def login(self):
        if self.var_uname.get() == "" or self.var_pass.get() == "" :
            messagebox.showerror("Error","Please Enter Username And Password",parent=self.root)
        elif self.var_uname.get() == "admin" or self.var_pass.get() == "admin" : # Admin Credentials
            # Invoice Code After Successfull Admin Login
            sound = gtts.gTTS("Welcome Admin",lang = "en")
            sound.save(r"login.mp3")
            playsound.playsound(r"login.mp3")
            if os.path.exists("login.mp3"):
                os.remove("login.mp3")
            self.admin_window()
        else:
            try:
                client = MongoClient('mongodb://localhost:27017/')
                collection = client['face_recognition_system']['registration_details']
                result = collection.find({"email":self.var_uname.get(),"password":self.var_pass.get()},{'_id': 0})
                if not list(result):
                    messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)
                else:
                    self.var_pass.set("")
                    self.var_uname.set("")
                    self.new_window = Toplevel(self.root)
                    self.new_window.app = Face_Recognition_System(self.new_window)
                client.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # ******************* Forgot Password *******************
    def forgot_password(self):
        if self.var_uname.get() == "":
            messagebox.showerror("Error","Please Enter Username To Reset Password",parent=self.root)
        else:
            try:
                client = MongoClient('mongodb://localhost:27017/')
                collection = client['face_recognition_system']['registration_details']
                result = collection.find({"email":self.var_uname.get()},{'_id': 0})
                if not list(result):
                    messagebox.showerror("Error","Please Enter Valid Username",parent=self.root)
                else:
                    client.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("360x500+610+170")

                    # Variables
                    self.var_sec_que = StringVar()
                    self.var_sec_ans = StringVar()
                    self.var_reset_pass = StringVar()

                    # Main Frame For Forgot Password Fields And Labels
                    main_frame = Frame(self.root2,bg="white")
                    main_frame.place(x=0,y=0,width=360,height=500)

                    # Top Title Label
                    l = Label(main_frame,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                    l.place(x=0,y=10,relwidth=1)

                    # Security Question
                    sec_que_label = Label(main_frame,text="Your Selected Security Question",font=("times new roman",15,"bold"),bg="white")
                    sec_que_label.place(x=50,y=80)

                    sec_que_combobox = ttk.Combobox(main_frame,textvariable=self.var_sec_que,font=("times new roman",12),state="readonly")
                    sec_que_combobox["values"]=("Select Question","Your Birth Place","Your BestFriend Name","Your Pet Name")
                    sec_que_combobox.current(0)
                    sec_que_combobox.place(x=50,y=110,width=250)

                    # Security Answer
                    sec_ans_label = Label(main_frame,text="Your Security Answer",font=("times new roman",15,"bold"),bg="white")
                    sec_ans_label.place(x=50,y=150)

                    sec_ans_entry = ttk.Entry(main_frame,textvariable=self.var_sec_ans,font=("times new roman",12))
                    sec_ans_entry.place(x=50,y=180,width=250)

                    # Reset Password
                    reset_pass_label = Label(main_frame,text="New Password",font=("times new roman",15,"bold"),bg="white")
                    reset_pass_label.place(x=50,y=220)

                    reset_pass_entry = ttk.Entry(main_frame,textvariable=self.var_reset_pass,font=("times new roman",12),show="*")
                    reset_pass_entry.place(x=50,y=250,width=250)
                    reset_pass_entry.bind("<KeyRelease>", lambda event: self.check_password_strength(pass_strength_label))
                    pass_strength_label = Label(main_frame, text="",bg="white")
                    pass_strength_label.place(x=50,y=280,width=250)

                    # Reset Button For Password Reset
                    reset_button = Button(main_frame,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green",activeforeground="white",activebackground="green")
                    reset_button.place(x=150,y=310)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Check Password Strength *******************
    def check_password_strength(self,pass_strength_label):
        password = self.var_reset_pass.get()
        message.clear()

        # Check The Complexity
        if len(password) < 8:
            message.append("Password should be at least 8 characters.")
        if not bool(re.search(r'[a-z]', password)): # Lowercase
            message.append("Password should contain at least one lowercase letter.")
        if not bool(re.search(r'[A-Z]', password)): # Uppercase
            message.append("Password should contain at least one uppercase letter.")
        if not bool(re.search(r'[0-9]', password)): # Digits
            message.append("Password should contain at least one digit.")
        if not bool(re.search(r'[!@#$%^&*()_+{}:;<>,.?~]', password)): # Special Characters
            message.append("Password should contain at least one special character.")

        # To Check Password Strength Dynamically
        if message:
            pass_strength_label.config(text="Weak", fg="red")
        elif len(password) < 12:
            pass_strength_label.config(text="Moderate", fg="orange")
        else:
            pass_strength_label.config(text="Strong", fg="green")

    # ******************* Reset Password *******************
    def reset_pass(self):
        if self.var_sec_que.get() == "Select Question" or self.var_sec_ans.get() == "" or self.var_reset_pass.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)
        else :
            client = MongoClient('mongodb://localhost:27017/')
            collection = client['face_recognition_system']['registration_details']
            result = collection.find({"email":self.var_uname.get(),"security_question":self.var_sec_que.get(),"security_answer":self.var_sec_ans.get()},{'_id': 0})
            if not list(result):
                messagebox.showerror("Error","Please Enter Valid Details",parent=self.root2)
            elif message:
                messagebox.showerror("Error", "\n".join(message),parent=self.root2)
            else:
                collection.update_one({"email":self.var_uname.get()},{"$set": {"password":self.var_reset_pass.get()}})
                # Invoice Code After Successfull Password Reset
                sound = gtts.gTTS("Password reset done successfully",lang = "en")
                sound.save(r"login.mp3")
                playsound.playsound(r"login.mp3")
                if os.path.exists("login.mp3"):
                    os.remove("login.mp3")
                messagebox.showinfo("Success","Password Reset Done Successfully",parent=self.root2)
                self.root2.destroy()
            client.close()

    # ******************* Open Register Window *******************
    def registration_window(self):
        self.new_window = Toplevel(self.root)
        self.app=Register_Window(self.new_window)

    # ******************* Open Admin Window *******************
    def admin_window(self):
        self.new_window = Toplevel(self.root)
        self.app=Admin(self.new_window)


# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()