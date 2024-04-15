#Required Libraries
from tkinter import *
from tkinter import ttk
from PIL import  Image,ImageTk
from tkinter import messagebox
from pymongo import MongoClient # For MongoDB
import re # To Match Password Requirements
import os # For OS Operations
from tkcalendar import Calendar # For Date Of Birth
# For Generating Invoice
import gtts
import playsound

message = []  # to check the password requiriments

# Main class
class Register_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1660x900+0+0")
        self.root.title("Register")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_department = StringVar()
        self.var_address = StringVar()
        self.var_sec_que = StringVar()
        self.var_sec_ans = StringVar()
        self.var_pass = StringVar()
        self.var_confirm_pass = StringVar()
        self.var_check_btn = IntVar()

        # Background Image
        img3 = Image.open(r"images\registration\bg2.jpg")
        img3 = img3.resize((1550,800),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1550,height=800)

        # Left Image
        self.bg1 = Image.open(r"images\registration\registration.png")
        self.bg1 = self.bg1.resize((650,700),Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(self.bg1)
        f_lbl = Label(self.root,image=self.photobg1)
        f_lbl.place(x=100,y=50,width=650,height=700)

        # Main Frame For Registration Form
        main_frame = Frame(self.root,bg="white")
        main_frame.place(x=750,y=50,width=700,height=700)

        # Registration Label
        register_label = Label(main_frame,text="USER REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green")
        register_label.place(x=20,y=20)

        # Back To Home Button At Label
        back_button = Button(main_frame,cursor="hand2",command=self.return_login,text="Back",width=10,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        back_button.place(x=570,y=20)

        # First Name
        fname_label = Label(main_frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname_label.place(x=50,y=100)
        def validate_text_input(P):
            return re.match("^[a-zA-Z]*$", P) is not None # Allow Only Letters (Text)

        fname_entry = ttk.Entry(main_frame,textvariable=self.var_fname,font=("times new roman",12),validate="key", validatecommand=(root.register(validate_text_input), "%P"))
        fname_entry.place(x=50,y=130,width=250)

        # Last Name
        lname_label = Label(main_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname_label.place(x=370,y=100)

        lname_entry = ttk.Entry(main_frame,textvariable=self.var_lname,font=("times new roman",12),validate="key", validatecommand=(root.register(validate_text_input), "%P"))
        lname_entry.place(x=370,y=130,width=250)

        # Contact Number
        contact_label = Label(main_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact_label.place(x=50,y=170)

        def on_phone_focus_in(event):
            if self.var_contact.get() == "10 Digits only":
                self.var_contact.set("")

        def on_phone_focus_out(event):
            if not self.var_contact.get():
                self.var_contact.set("10 Digits only")

        def validate_phone_number(action, value_if_allowed):
            if action == "0" or value_if_allowed.isdigit() and len(value_if_allowed) <= 10: # Allow Deletion And Numbers, And Ensure Length Is 10
                return True
            return False

        contact_entry = ttk.Entry(main_frame,textvariable=self.var_contact,font=("times new roman",12))
        self.var_contact.set("10 Digits only")
        contact_entry.config(validate="key",validatecommand=(root.register(validate_phone_number), "%d", "%P"))
        contact_entry.bind("<FocusIn>", on_phone_focus_in)
        contact_entry.bind("<FocusOut>", on_phone_focus_out)
        contact_entry.place(x=50,y=200,width=250)

        # Email
        email_label = Label(main_frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email_label.place(x=370,y=170)

        def validate_email(event):
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.var_email.get()):
                email_entry.config(foreground="black")  # Set Text Color To Black
            else:
                email_entry.config(foreground="red")  # Set Text Color To Red

        email_entry = ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman",12))
        email_entry.bind("<KeyRelease>", validate_email)  # Check On Each Key Release
        email_entry.place(x=370,y=200,width=250)

        # Gender
        gender_Label = Label(main_frame,text="Gender ",font=("times new roman",15,"bold"),bg="white")
        gender_Label.place(x=50,y=240)

        gender_combobox = ttk.Combobox(main_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=18)
        gender_combobox["values"]=("Select Gender","Male","Female","Other")
        gender_combobox.current(0)
        gender_combobox.place(x=50,y=270,width=250)

        # Date Of Birth
        date_of_birth_Label = Label(main_frame,text="Date Of Birth ",font=("times new roman",15,"bold"),bg="white")
        date_of_birth_Label.place(x=370,y=240)

        def open_calendar(event):
            def set_selected_date():
                selected_date = cal.get_date()
                self.var_dob.set(selected_date)
                root._cal_win.destroy()
                del root._cal_win

            def on_closing():
                root._cal_win.destroy()
                del root._cal_win

            if self.var_dob.get() == " " or self.var_dob.get() == "MM/DD/YY":
                self.var_dob.set("")
                if not hasattr(root, "_cal_win"):  # Check if the calendar window is already open
                    root._cal_win = Toplevel(root)
                    root._cal_win.title("Select Date")
                    root._cal_win.geometry("260x220+1000+200")

                    cal = Calendar(root._cal_win, selectmode='day')
                    cal.pack()

                    select_button = Button(root._cal_win, text="Select", command=set_selected_date)
                    select_button.place(x=110,y=190)
                    root._cal_win.protocol("WM_DELETE_WINDOW", on_closing)

        date_of_birth_entry = ttk.Entry(main_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        date_of_birth_entry.insert(0, "MM/DD/YY")  # Placeholder text
        date_of_birth_entry.bind("<FocusIn>", open_calendar)  # Open calendar on focus
        date_of_birth_entry.bind("<Button-1>", open_calendar)  # Open calendar on click
        date_of_birth_entry.place(x=370,y=270,width=250)

        # Department
        department_Label = Label(main_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        department_Label.place(x=50,y=310)

        department_combobox = ttk.Combobox(main_frame,textvariable=self.var_department,font=("times new roman",12),state="readonly",width=20)
        department_combobox["values"]=("Select Department","Computer Science","Data Science")
        department_combobox.current(0)
        department_combobox.place(x=50,y=340,width=250)

        # Address
        address_Label = Label(main_frame,text="Address ",font=("times new roman",15,"bold"),bg="white")
        address_Label.place(x=370,y=310)

        address_entry = ttk.Entry(main_frame,textvariable=self.var_address,width=20,font=("times new roman",12))
        address_entry.place(x=370,y=340,width=250)

        # Security Question
        sec_que_label = Label(main_frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        sec_que_label.place(x=50,y=380)

        sec_que_combobox = ttk.Combobox(main_frame,textvariable=self.var_sec_que,font=("times new roman",12),state="readonly")
        sec_que_combobox["values"]=("Select Question","Your Birth Place","Your BestFriend Name","Your Pet Name")
        sec_que_combobox.current(0)
        sec_que_combobox.place(x=50,y=410,width=250)

        # Security Answer
        sec_ans_label = Label(main_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        sec_ans_label.place(x=370,y=380)

        sec_ans_entry = ttk.Entry(main_frame,textvariable=self.var_sec_ans,font=("times new roman",12))
        sec_ans_entry.place(x=370,y=410,width=250)

        # Password
        pass_label = Label(main_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pass_label.place(x=50,y=450)

        pass_entry = ttk.Entry(main_frame,textvariable=self.var_pass,font=("times new roman",12),show="*")
        pass_entry.place(x=50,y=480,width=250)
        pass_entry.bind("<KeyRelease>", lambda event: self.check_password_strength(pass_strength_label))
        pass_strength_label = Label(main_frame, text="",bg="white")
        pass_strength_label.place(x=50,y=515,width=250)

        # Confirm Password
        confirm_pass_label = Label(main_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pass_label.place(x=370,y=450)

        confirm_pass_entry = ttk.Entry(main_frame,textvariable=self.var_confirm_pass,font=("times new roman",12),show="*")
        confirm_pass_entry.place(x=370,y=480,width=250)

        # Terms And Policy Check Button
        check_button = Checkbutton(main_frame,variable=self.var_check_btn,text="I Agree To The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",activebackground="white",onvalue=1,offvalue=0)
        check_button.place(x=50,y=550)

        # Register Button
        register_btn = Button(main_frame,cursor="hand2",command=self.register_data,text="Register",width=10,font=("times new roman",12,"bold"),bg="Blue",fg="white",activebackground="Blue",activeforeground="white")
        register_btn.place(x=150,y=600,width=150,height=40)

        # Login Button
        login_btn = Button(main_frame,cursor="hand2",command=self.return_login,text="Login",width=10,font=("times new roman",12,"bold"),bg="Blue",fg="white",activebackground="Blue",activeforeground="white")
        login_btn.place(x=380,y=600,width=150,height=40)

#-------------------------------------------------- Function Declaration ---------------------------------------------------------

    # ******************* Check Password Strength *******************
    def check_password_strength(self,pass_strength_label):
        password = self.var_pass.get()
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

    # ******************* Validation On Data Feilds *******************
    def validate_fields(self):
        def validate_phone_number(phone_number):
            return len(phone_number) == 10 and phone_number.isdigit()
        def validate_email(email):
            return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) # Basic Email Validation Using Regular Expression
        if not validate_phone_number(self.var_contact.get()):
            messagebox.showerror("Error","Phone Number Must Be Of 10 Digits",parent=self.root) # Display An Error Message For Invalid Phone Number
            return 0
        if not validate_email(self.var_email.get()):
            messagebox.showerror("Error","Enter A Valid Email Address",parent=self.root) # Display An Error Message For Invalid Email
            return 0
        return 1

    # ******************* Add The Data To Database *******************
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "10 Digits only" or self.var_email.get() == "" or self.var_sec_ans.get() == "" or self.var_sec_que.get() == "Select Question" or self.var_pass.get() == "" or self.var_confirm_pass.get() == "" or self.var_dob.get() == "MM/DD/YY" or self.var_gender.get() == "Select Gender" or self.var_address.get() == "" or self.var_department.get() == "Select Department":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.var_pass.get() != self.var_confirm_pass.get():
            messagebox.showerror("Error","Password And Confirm Password Must Be Same!",parent=self.root)
        elif  self.var_check_btn.get() == 0 :
            messagebox.showerror("Error","Please Agree Our Terms And Conditions",parent=self.root)
        elif message:
                messagebox.showerror("Error", "\n".join(message),parent=self.root)
        else:
            if(self.validate_fields()):
                try:
                    client = MongoClient('mongodb://localhost:27017/')
                    db = client['face_recognition_system']
                    collection = db['registration_details']
                    result = collection.find({"email":self.var_email.get()},{'_id': 0})
                    if not result:
                        messagebox.showerror("Error","Other User Is Already Registered With The Provided Email",parent=self.root)
                    else:
                        collection.insert_one({"first_name":self.var_fname.get(),"last_name":self.var_lname.get(),"contact_number":self.var_contact.get(),"department":self.var_department.get(),"gender":self.var_gender.get(),"date_of_birth":self.var_dob.get(),"email":self.var_email.get(),"address":self.var_address.get(),"security_question":self.var_sec_que.get(),"security_answer":self.var_sec_ans.get(),"password":self.var_pass.get()})
                        self.var_fname.set("")
                        self.var_lname.set("")
                        self.var_contact.set("10 Digits only")
                        self.var_email.set("")
                        self.var_sec_que.set("Select Security Question")
                        self.var_sec_ans.set("")
                        self.var_pass.set("")
                        self.var_confirm_pass.set("")
                        self.var_address.set("")
                        self.var_department.set("Select Department")
                        self.var_gender.set("Select Gender")
                        self.var_dob.set("MM/DD/YY")
                        self.var_check_btn.set(0)
                        # Invoice Code After Successfull User Registration
                        sound = gtts.gTTS("User Registration Completed successfully",lang = "en")
                        sound.save(r"registration.mp3")
                        playsound.playsound(r"registration.mp3")
                        if os.path.exists("registration.mp3"):
                            os.remove("registration.mp3")
                        messagebox.showinfo("Success","User Registration Completed successfully",parent=self.root)
                    client.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Return To Login Button *******************
    def return_login(self):
        self.root.destroy()


# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Register_Window(root)
    root.mainloop()