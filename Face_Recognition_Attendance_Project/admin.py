# Required Libraries
# For GUI
from tkinter import*
from tkinter import ttk
from PIL import  Image,ImageTk
from tkinter import messagebox
from tkcalendar import Calendar # For Date Of Birth To Open Calendar
import re  # To Match The Email
# For Date And Time Stamp
from time import strftime
from datetime import datetime
from pymongo import MongoClient # For MongoDB
import os # For OS Operations
# For Sending E-Mails
import smtplib
from email.message import EmailMessage
from twilio.rest import Client # For Sending Text SMS To The Phone Number
import shutil # For Moving File From One Directory To Another
import csv # For CSV File Opeartions
# For Generating Invoice
import gtts
import playsound
# For Including Other Project Windows
from main import Face_Recognition_System
from student_data import Student_Data
from teacher_data import Teacher_Data
from staff_data import Staff_Data

# Main class
class Admin:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1560x820+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_address = StringVar()
        self.var_sec_que = StringVar()
        self.var_sec_ans = StringVar()
        self.var_pass = StringVar()
        self.var_search = StringVar()
        self.var_search_combo = StringVar()
        self.var_department = StringVar()

        # Top Title Label
        title_label = Label(self.root,text="ADMIN PANEL",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1550,height=45)

        # Back To Login At Label
        back_button = Button(self.root,cursor="hand2",command=self.back_to_login,text="Logout",width=10,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        back_button.place(x=1400,y=5)

        # To Display Time At Label
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_label,font=("times new roman",12,"bold"),background='white',foreground='black')
        lbl.place(x=10,y=0,width=110,height=50)
        time()

        # Background Image Below Main Frame
        img3 = Image.open(r"images\background.jpg")
        img3 = img3.resize((1600,800),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=45,width=1600,height=800)
        main_frame = Frame(bg_img,bd = 2,bg="white")
        main_frame.place(x=0,y=0,width=1600,height=800)

        # Redirect To Home Button
        home_button = Button(main_frame,cursor="hand2",command=self.go_to_home,text="Home",width=15,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        home_button.place(x=1200,y=695)

        # Left Frame For Registered Users Details
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="User Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=470,height=670)

        # First Name
        fname_label = Label(left_frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname_label.grid(row=0,column=0,padx=10,sticky=W)
        def validate_text_input(P):
            return re.match("^[a-zA-Z]*$", P) is not None # Allow Only Letters (Text)

        fname_entry = ttk.Entry(left_frame,textvariable=self.var_fname,font=("times new roman",12),width=27,validate="key", validatecommand=(root.register(validate_text_input), "%P"))
        fname_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # Last Name
        lname_label = Label(left_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname_label.grid(row=1,column=0,padx=10,sticky=W)

        lname_entry = ttk.Entry(left_frame,textvariable=self.var_lname,font=("times new roman",12),width=27,validate="key", validatecommand=(root.register(validate_text_input), "%P"))
        lname_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # Contact Number
        contact_label = Label(left_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact_label.grid(row=2,column=0,padx=10,sticky=W)

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

        contact_entry = ttk.Entry(left_frame,textvariable=self.var_contact,font=("times new roman",12),width=27)
        self.var_contact.set("10 Digits only")
        contact_entry.config(validate="key",validatecommand=(root.register(validate_phone_number), "%d", "%P"))
        contact_entry.bind("<FocusIn>", on_phone_focus_in) # Set The Value On Focus
        contact_entry.bind("<FocusOut>", on_phone_focus_out) # Set The Value Off Focus
        contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # User Email
        email_label = Label(left_frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        def validate_email(event):
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.var_email.get()):
                email_entry.config(foreground="black")  # Set Text Color To Black
            else:
                email_entry.config(foreground="red")  # Set Text Color To Red

        email_entry = ttk.Entry(left_frame,textvariable=self.var_email,font=("times new roman",12),width=27)
        email_entry.bind("<KeyRelease>", validate_email)  # Check On Each Key Release
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        # User Gender
        gender_Label = Label(left_frame,text="Gender ",font=("times new roman",15,"bold"),bg="white")
        gender_Label.grid(row=4,column=0,padx=10,sticky=W)

        gender_combobox = ttk.Combobox(left_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=25)
        gender_combobox["values"]=("Select Gender","Male","Female","Other")
        gender_combobox.current(0)
        gender_combobox.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        # User Date Of Birth
        date_of_birth_Label = Label(left_frame,text="Date Of Birth ",font=("times new roman",12,"bold"),bg="white")
        date_of_birth_Label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

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
                if not hasattr(root, "_cal_win"):  # Check If The Calendar Window Is Already Open
                    root._cal_win = Toplevel(root)
                    root._cal_win.title("Select Date")

                    cal = Calendar(root._cal_win, selectmode='day')
                    cal.pack()

                    select_button = Button(root._cal_win, text="Select", command=set_selected_date)
                    select_button.pack()
                    root._cal_win.protocol("WM_DELETE_WINDOW", on_closing)

        date_of_birth_entry = ttk.Entry(left_frame,textvariable=self.var_dob,font=("times new roman",12),width=27)
        date_of_birth_entry.insert(0, "MM/DD/YY")  # Placeholder Text
        date_of_birth_entry.bind("<FocusIn>", open_calendar)  # Open Calendar On Focus
        date_of_birth_entry.bind("<Button-1>", open_calendar)  # Open Calendar On Click
        date_of_birth_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        # User Address
        address_Label = Label(left_frame,text="Address ",font=("times new roman",15,"bold"),bg="white")
        address_Label.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(left_frame,textvariable=self.var_address,font=("times new roman",12),width=27)
        address_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        # User Department
        department_Label = Label(left_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        department_Label.grid(row=7,column=0,padx=10,pady=5,sticky=W)

        department_combobox = ttk.Combobox(left_frame,textvariable=self.var_department,font=("times new roman",12),state="readonly",width=25)
        department_combobox["values"]=("Select Department","Computer Science","Data Science")
        department_combobox.current(0)
        department_combobox.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        # User Security Question
        sec_que_label = Label(left_frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        sec_que_label.grid(row=8,column=0,padx=10,pady=5,sticky=W)

        sec_que_combobox = ttk.Combobox(left_frame,textvariable=self.var_sec_que,font=("times new roman",12),state="readonly",width=25)
        sec_que_combobox["values"]=("Select Question","Your Birth Place","Your BestFriend Name","Your Pet Name")
        sec_que_combobox.current(0)
        sec_que_combobox.grid(row=8,column=1,padx=10,pady=10,sticky=W)

        # User Security Answer
        sec_ans_label = Label(left_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        sec_ans_label.grid(row=9,column=0,padx=10,pady=5,sticky=W)

        sec_ans_entry = ttk.Entry(left_frame,textvariable=self.var_sec_ans,font=("times new roman",12),width=27)
        sec_ans_entry.grid(row=9,column=1,padx=10,pady=10,sticky=W)

        # User Password
        pass_label = Label(left_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pass_label.grid(row=10,column=0,padx=10,pady=5,sticky=W)

        pass_entry = ttk.Entry(left_frame,textvariable=self.var_pass,font=("times new roman",12),width=27)
        pass_entry.grid(row=10,column=1,padx=10,pady=10,sticky=W)

        # Basic CRUD Operations On User Data
        save_button = Button(left_frame,cursor="hand2",command=self.add_data,text="Save",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        save_button.place(x=15,y=520)

        update_button = Button(left_frame,cursor="hand2",command=self.update_data,text="Update",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        update_button.place(x=220,y=520)

        delete_button = Button(left_frame,cursor="hand2",command=self.delete_data,text="Delete",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        delete_button.place(x=15,y=580)

        reset_button = Button(left_frame,cursor="hand2",command=self.reset_data,text="Reset",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        reset_button.place(x=220,y=580)

        # Display Full Data Buttons
        student_data = Button(main_frame,cursor="hand2",command=self.student_data,text="Student Data",width=15,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        student_data.place(x=300,y=695)

        teacher_data = Button(main_frame,cursor="hand2",command=self.teacher_data,text="Teacher Data",width=15,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        teacher_data.place(x=600,y=695)

        staff_data = Button(main_frame,cursor="hand2",command=self.staff_data,text="Staff Data",width=15,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        staff_data.place(x=900,y=695)


        # Right Frame For Display Users Data And Perform Search
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="User Data",font=("times new roman",12,"bold"))
        right_frame.place(x=490,y=10,width=1025,height=670)

        # ************** Search System Code *************
        # Search Combox (Search Parameter)
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=10,width=1000,height=70)

        search_combobox = ttk.Combobox(search_frame,textvariable=self.var_search_combo,font=("times new roman",15,"bold"),state="readonly",width=15)
        search_combobox["values"]=("Select","Email","Phone No","First Name")
        search_combobox.current(0)
        search_combobox.place(x=10,y=8)

        # Take Search Data
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",15))
        search_entry.place(x=200,y=8)

        # Search Button
        search_button = Button(search_frame,command=self.perform_search,cursor="hand2",text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        search_button.place(x=375,y=6)

        # Refresh Button To Refresh The User Details Window
        refresh_button = Button(search_frame,command=self.fetch_data,cursor="hand2",text="Refresh",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        refresh_button.place(x=515,y=6)

        # Send Email Button To Absent Individuals
        send_mail_button = Button(search_frame,command=self.send_absent_mail,cursor="hand2",text="Absent Message",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        send_mail_button.place(x=655,y=6)

        # Set All Individuals Attendance Fields To Absent And Save The CSV File In Other Directory And Create New CSV File In Same Directory
        reset_system_button = Button(search_frame,command=self.reset,cursor="hand2",text="Reset Data",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        reset_system_button.place(x=810,y=6)

        # Table Frame To Show Users Data
        table_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=100,width=1000,height=525)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.admin_table = ttk.Treeview(table_frame,columns=("First_Name","Last_Name","Contact_Number","Department","Gender","Date_Of_Birth","Email","Address","Security_Question","Security_Answer","Password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.admin_table.xview)
        scroll_y.config(command=self.admin_table.yview)

        self.admin_table.heading("First_Name",text="First_Name")
        self.admin_table.heading("Last_Name",text="Last_Name")
        self.admin_table.heading("Contact_Number",text="Contact_Number")
        self.admin_table.heading("Department",text="Department")
        self.admin_table.heading("Gender",text="Gender")
        self.admin_table.heading("Date_Of_Birth",text="Date_Of_Birth")
        self.admin_table.heading("Email",text="Email")
        self.admin_table.heading("Address",text="Address")
        self.admin_table.heading("Security_Question",text="Security_Question")
        self.admin_table.heading("Security_Answer",text="Security_Answer")
        self.admin_table.heading("Password",text="Password")
        self.admin_table["show"]="headings"

        self.admin_table.column("First_Name",width=110)
        self.admin_table.column("Last_Name",width=100)
        self.admin_table.column("Contact_Number",width=100)
        self.admin_table.column("Department",width=100)
        self.admin_table.column("Gender",width=100)
        self.admin_table.column("Date_Of_Birth",width=100)
        self.admin_table.column("Email",width=100)
        self.admin_table.column("Address",width=100)
        self.admin_table.column("Security_Question",width=100)
        self.admin_table.column("Security_Answer",width=100)
        self.admin_table.column("Password",width=100)

        self.admin_table.bind("<ButtonRelease>",self.get_cursor)
        self.admin_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

#-------------------------------------------------- Function Declaration ---------------------------------------------------------

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
    def add_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "10 Digits only" or self.var_email.get() == "" or self.var_sec_ans.get() == "" or self.var_sec_que.get() == "Select Question" or self.var_pass.get() == ""  or self.var_dob.get() == "MM/DD/YY" or self.var_gender.get() == "Select Gender" or self.var_address.get() == "" or self.var_department.get() == "Select Department":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            if(self.validate_fields()):
                try:
                    client = MongoClient('mongodb://localhost:27017/')
                    collection = client['face_recognition_system']['registration_details']
                    collection.insert_one({"first_name":self.var_fname.get(),"last_name":self.var_lname.get(),"contact_number":self.var_contact.get(),"department":self.var_department.get(),"gender":self.var_gender.get(),"date_of_birth":self.var_dob.get(),"email":self.var_email.get(),"address":self.var_address.get(),"security_question":self.var_sec_que.get(),"security_answer":self.var_sec_ans.get(),"password":self.var_pass.get()})
                    # Invoice Code After Successfull Completion Of Operation
                    sound = gtts.gTTS("User details has been added successfully",lang = "en")
                    sound.save(r"admin.mp3")
                    playsound.playsound(r"admin.mp3")
                    if os.path.exists("admin.mp3"):
                        os.remove("admin.mp3")
                    messagebox.showinfo("Success","User Details Has Been Added Successfully",parent=self.root)
                    self.fetch_data()
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Fetch The Data From Database *******************
    def fetch_data(self):
        self.var_search.set("")
        self.var_search_combo.set("Select")
        client = MongoClient('mongodb://localhost:27017/')
        collection = client['face_recognition_system']['registration_details']
        result = collection.find({},{'_id': 0})
        values_list = []
        self.admin_table.delete(*self.admin_table.get_children())
        for document in result:
            values_list.clear()
            for key in document:
                values_list.append(document[key])
            self.admin_table.insert("",END,values=values_list)
        client.close()
        self.reset_data()

    # ******************* Search From The Table TreeView *******************
    def perform_search(self):
        search_text = self.var_search.get().lower()
        selected_criteria = self.var_search_combo.get()

        self.admin_table.delete(*self.admin_table.get_children())  # Clear The Treeview Before Inserting Data
        client = MongoClient('mongodb://localhost:27017/')
        collection = client['face_recognition_system']['registration_details']
        records_found = False # Create A Flag To Track If Any Matching Records Were Found
        result = collection.find({}, {'_id': 0})  # Exclude The _id Field With The Help Of Projection

        for row in result:
            if selected_criteria == "Email":
                roll_no = row.get("email", "")
                if search_text == str(roll_no).lower():
                    self.admin_table.insert("", END, values=list(row.values()))
                    records_found = True
            elif selected_criteria == "Phone No":
                phone_number = row.get("contact_number", "")
                if search_text == str(phone_number).lower():
                    self.admin_table.insert("", END, values=list(row.values()))
                    records_found = True
            elif selected_criteria == "First Name":
                student_name = row.get("first_name", "")
                if search_text == str(student_name).lower():
                    self.admin_table.insert("", END, values=list(row.values()))
                    records_found = True
        client.close()

        # Check If No Matching Records Were Found
        if not records_found:
            self.admin_table.insert("", END, values=("No records found", "", "", "", "", "", "", "", "", "", "", "", "", "", ""))


    # ******************* Fetch The Data From Table TreeView To The Input Fields *******************
    def get_cursor(self,event=""):
        cursor_focus = self.admin_table.focus()
        content = self.admin_table.item(cursor_focus)
        data = content["values"]
        self.var_fname.set(data[0])
        self.var_lname.set(data[1])
        self.var_contact.set(data[2])
        self.var_department.set(data[3])
        self.var_gender.set(data[4])
        self.var_dob.set(data[5])
        self.var_email.set(data[6])
        self.var_address.set(data[7])
        self.var_sec_que.set(data[8])
        self.var_sec_ans.set(data[9])
        self.var_pass.set(data[10])

    # ******************* Update The Selected Data *******************
    def update_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "10 Digits only" or self.var_email.get() == "" or self.var_sec_ans.get() == "" or self.var_sec_que.get() == "Select Question" or self.var_pass.get() == ""  or self.var_dob.get() == "MM/DD/YY" or self.var_gender.get() == "Select Gender" or self.var_address.get() == "" or self.var_department.get() == "Select Department":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            if(self.validate_fields()):
                try:
                    Update = messagebox.askyesno("Update","Do You Want To Update This User Details",parent=self.root)
                    if Update > 0:
                        client = MongoClient('mongodb://localhost:27017/')
                        collection = client['face_recognition_system']['registration_details']
                        collection.update_one({"date_of_birth":self.var_dob.get()},{"$set": {"first_name":self.var_fname.get(),"last_name":self.var_lname.get(),"contact_number":self.var_contact.get(),"department":self.var_department.get(),"gender":self.var_gender.get(),"date_of_birth":self.var_dob.get(),"email":self.var_email.get(),"address":self.var_address.get(),"security_question":self.var_sec_que.get(),"security_answer":self.var_sec_ans.get(),"password":self.var_pass.get()}})
                        # Invoice Code After Successfull Completion Of Operation
                        sound = gtts.gTTS("User details has been updated successfully",lang = "en")
                        sound.save(r"admin.mp3")
                        playsound.playsound(r"admin.mp3")
                        if os.path.exists("admin.mp3"):
                            os.remove("admin.mp3")
                        messagebox.showinfo("Success","User Details Has Been Updated Successfully",parent=self.root)
                    else:
                        if not Update:
                            return
                    self.fetch_data()
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Delete The Selected Data *******************
    def delete_data(self):
        try:
            Delete = messagebox.askyesno("Delete","Do You Want To Delete The Selected User Details",parent=self.root)
            if Delete > 0:
                client = MongoClient('mongodb://localhost:27017/')
                collection = client['face_recognition_system']['registration_details']
                collection.delete_one({"date_of_birth":self.var_dob.get()})
                # Invoice Code After Successfull Completion Of Operation
                sound = gtts.gTTS("User details has been deleted successfully",lang = "en")
                sound.save(r"admin.mp3")
                playsound.playsound(r"admin.mp3")
                if os.path.exists("admin.mp3"):
                    os.remove("admin.mp3")
                messagebox.showinfo("Success","User Details Has Been Deleted Successfully",parent=self.root)
            else:
                if not Delete:
                    return
            self.fetch_data()
            self.reset_data()
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Reset All The Fields To Default Values *******************
    def reset_data(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("10 Digits only")
        self.var_email.set("")
        self.var_sec_que.set("Select Security Question")
        self.var_sec_ans.set("")
        self.var_pass.set("")
        self.var_address.set("")
        self.var_department.set("Select Department")
        self.var_gender.set("Select Gender")
        self.var_dob.set("MM/DD/YY")

    # ******************* Send Absent Mails To The Absent Individuals *******************
    def send_absent_mail(self):
        d1 = datetime.now().strftime("%d/%m/%Y") # Getting Current Date
        dt_string = datetime.now().strftime("%H:%M:%S") # Getting Current Time

        client = MongoClient('mongodb://localhost:27017/')

        student_collection = client['face_recognition_system']['student_details']
        teacher_collection = client['face_recognition_system']['teacher_details']
        staff_collection = client['face_recognition_system']['staff_details']

        absent_records = [] # Query Each Collection For Absent Records And Project Only Email And Phone Fields

        # Query And Project Data From student_collection
        results1 = student_collection.find({"attendance": "absent"}, {"_id": 0, "email": 1, "phone_number": 1,"student_name" : 1})
        absent_records += list(results1)
        for i in absent_records:
            self.send_mail(i['student_name']+" was absent at the time : "+dt_string+" on the day : "+d1,i['email'])
            self.send_msg(i['student_name']+" was absent at the time : "+dt_string+" on the day : "+d1,i['phone_number'])
        absent_records.clear()

        # Query And Project Data From teacher_collection
        results1 = teacher_collection.find({"attendance": "absent"}, {"_id": 0, "email": 1, "phone_number": 1,"teacher_name" : 1})
        absent_records += list(results1)
        for i in absent_records:
            self.send_mail(i['teacher_name']+" was absent at the time : "+dt_string+" on the day : "+d1,i['email'])
            self.send_msg(i['teacher_name']+" was absent at the time : "+dt_string+" on the day : "+d1,i['phone_number'])
        absent_records.clear()

        # Query And Project Data From staff_collection
        results1 = staff_collection.find({"attendance": "absent"}, {"_id": 0, "email": 1, "phone_number": 1,"staff_name" : 1})
        absent_records += list(results1)
        for i in absent_records:
            self.send_mail(i['staff_name']+" was absent at the time : "+dt_string+" on the day : "+d1,i['email'])
            self.send_msg(i['staff_name']+" was absent at the time : "+dt_string+" on the day : "+d1,i['phone_number'])

        client.close()
        # Invoice Code After Successfull Completion Of Operation
        sound = gtts.gTTS("Absent Confirmation Send Successfully",lang = "en")
        sound.save(r"admin.mp3")
        playsound.playsound(r"admin.mp3")
        if os.path.exists("admin.mp3"):
            os.remove("admin.mp3")
        messagebox.showinfo("Success","Absent Confirmation Send Successfully",parent=self.root)

    # ******************* Sendimg Emails *******************
    def send_mail(self,message,email):
        msg = EmailMessage()
        msg.set_content(message)
        msg['subject'] = "Attendance"
        msg['to'] = email
        msg['from'] = "Your_Email"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("Your_Email","Your_App_Password") # App Passwords
        server.send_message(msg)
        server.quit()

    # ******************* Sending Text SMS *******************
    def send_msg(self,message,phone):
        account_sid = 'Your_Twilio_Account_SID' # Twilio Account SID
        auth_token = 'Your_Twilio_Account_Authentication_Token' # Twilio Account Authentication Token

        client = Client(account_sid, auth_token)  # Create A Twilio Client
        twilio_phone_number = '+Your_Twilio_Phone_Number' # Your Twilio Phone Number (You Must Have Purchased This Number On Twilio)
        recipient_phone_number = f"+91{phone}" # Recipient's Phone Number (In E.164 Format, Including Country Code, e.g., +1234567890)
        client.messages.create(body = message, from_ = twilio_phone_number, to = recipient_phone_number) # Send The SMS

    # ******************* Reset The System For Next Day Attendance *******************
    def reset(self):
        if os.path.exists("attendance.csv"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Get The Timestamp As A String In The Format YYYYMMDD_HHMMSS
            base, ext = os.path.splitext(os.path.basename("attendance.csv")) # Split The Source CSV File Path Into Base And Extension
            shutil.move("attendance.csv", os.path.join("attendance/", f"{base}_{timestamp}{ext}")) # Move The Source CSV File To The Predefined Directory With The TimeStamp And Date

        with open("attendance.csv", 'w', newline='') as csv_file:  # Create A New CSV File In The Same Directory As We Have Moved The CSV File In Another Location
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["ID", "STATUS", "NAME", "DATE", "TIME", "ATTENDANCE"])  # Add The Header Row To The CSV File

        # Setting The Attendance Field Of All The Tables To 'Absent' For Next Day Attendance
        client = MongoClient('mongodb://localhost:27017/')

        student_collection = client['face_recognition_system']['student_details']
        teacher_collection = client['face_recognition_system']['teacher_details']
        staff_collection = client['face_recognition_system']['staff_details']

        student_collection.update_many({}, {"$set": {"attendance": "absent"}})
        teacher_collection.update_many({}, {"$set": {"attendance": "absent"}})
        staff_collection.update_many({}, {"$set": {"attendance": "absent"}})

        client.close()

        # Invoice Code After Successfull Completion Of Operation
        sound = gtts.gTTS("Reset done successfully",lang = "en")
        sound.save(r"admin.mp3")
        playsound.playsound(r"admin.mp3")
        if os.path.exists("admin.mp3"):
            os.remove("admin.mp3")
        messagebox.showinfo("Success","Reset Done Successfully",parent=self.root)

    # ******************* Back To Login Function *******************
    def back_to_login(self):
        self.root.destroy()

    # ******************* Redirect To Home Function *******************
    def go_to_home(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

    # ******************* Function For Navigating To Individuals Data Window *******************
    def student_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Student_Data(self.new_window)

    def staff_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Staff_Data(self.new_window)

    def teacher_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Teacher_Data(self.new_window)


# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()