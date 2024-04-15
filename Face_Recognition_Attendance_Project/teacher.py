# Required Libraries
# For GUI
from tkinter import*
from tkinter import ttk
from PIL import  Image,ImageTk
from tkinter import messagebox
from tkcalendar import Calendar # For Date Of Birth To Open Calendar
from tkcalendar import DateEntry # For Duration To Customize The Selected Date
import re # To Match The Email
# For MongoDB
import pymongo
from pymongo import MongoClient
import cv2 # For Taking Image Samples
import os # For OS Operations
from time import strftime # For Time Stamp
# For Generating Invoice
import gtts
import playsound

# Main class
class Teacher_Details:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1560x820+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_teacherid = StringVar()
        self.var_teachername = StringVar()
        self.var_qualification = StringVar()
        self.var_dept = StringVar()
        self.var_duration = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_experince = StringVar()
        self.var_post = StringVar()
        self.var_search = StringVar()
        self.var_search_combo = StringVar()

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
        title_label = Label(self.root,text="TEACHER DETAILS",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=130,width=1530,height=45)

        # Back To Home Button At Label
        back_button = Button(self.root,cursor="hand2",command=self.back_to_home,text="Home",width=10,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        back_button.place(x=1400,y=136)

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
        img3 = img3.resize((1600,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=175,width=1600,height=710)

        # Main Frame For Data Entry And Search
        main_frame = Frame(bg_img,bd = 2,bg="white")
        main_frame.place(x=0,y=0,width=1600,height=600)

        # Left Frame For Data Entry
        teacher_info_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Details",font=("times new roman",12,"bold"))
        teacher_info_frame.place(x=10,y=5,width=765,height=587)

        # Images Of Left Frame
        img_left1 = Image.open(r"images\teacher\teacher1.jpg")
        img_left1 = img_left1.resize((370,150),Image.Resampling.LANCZOS)
        self.photoimg_left1 = ImageTk.PhotoImage(img_left1)
        f_lbl = Label(teacher_info_frame,image=self.photoimg_left1)
        f_lbl.place(x=7,y=0,width=370,height=150)

        img_left2 = Image.open(r"images\teacher\teacher2.jpg")
        img_left2 = img_left2.resize((365,150),Image.Resampling.LANCZOS)
        self.photoimg_left2 = ImageTk.PhotoImage(img_left2)
        f_lbl = Label(teacher_info_frame,image=self.photoimg_left2)
        f_lbl.place(x=383,y=0,width=365,height=150)

        # Teacher Information
        teacher_info_frame = LabelFrame(teacher_info_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Personal Information",font=("times new roman",12,"bold"))
        teacher_info_frame.place(x=10,y=155,width=740,height=400)

        # Teacher Id
        teacher_id_Label = Label(teacher_info_frame,text="Teacher ID :",font=("times new roman",12,"bold"),bg="white")
        teacher_id_Label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        def on_id_focus_in(event):
            if self.var_teacherid.get() == "Digits only":
                self.var_teacherid.set("")

        def on_id_focus_out(event):
            if not self.var_teacherid.get():
                self.var_teacherid.set("Digits only")

        def validate_id(action, value_if_allowed):
            if action == "0" or value_if_allowed.isdigit(): # Allow Deletion And Numbers
                return True
            return False

        teacher_id_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_teacherid,font=("times new roman",12),width=24,validate="key")
        self.var_teacherid.set("Digits only")
        teacher_id_entry.config(validate="key",validatecommand=(root.register(validate_id), "%d", "%P"))
        teacher_id_entry.bind("<FocusIn>", on_id_focus_in) # Set The Value On Focus
        teacher_id_entry.bind("<FocusOut>", on_id_focus_out) # Set The Value Off Focus
        teacher_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        def validate_text_input(P):
            return re.match("^[a-zA-Z]*$", P) is not None # Allow Only Letters (Text)
        teacher_name_Label = Label(teacher_info_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
        teacher_name_Label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_teachername,font=("times new roman",12),width=24,validate="key", validatecommand=(root.register(validate_text_input), "%P"))
        teacher_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Teacher Qualifacation
        qualifacation_Label = Label(teacher_info_frame,text="Qualifacation :",font=("times new roman",12,"bold"),bg="white")
        qualifacation_Label.grid(row=1,column=0,padx=10,sticky=W)

        qualifacation_combobox = ttk.Combobox(teacher_info_frame,textvariable=self.var_qualification,font=("times new roman",12),state="readonly",width=22)
        qualifacation_combobox["values"]=("Select Qualifacation","12th","Phd")
        qualifacation_combobox.current(0)
        qualifacation_combobox.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Teacher Department
        department_Label = Label(teacher_info_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        department_Label.grid(row=1,column=2,padx=10,sticky=W)

        department_combobox = ttk.Combobox(teacher_info_frame,textvariable=self.var_dept,font=("times new roman",12),state="readonly",width=22)
        department_combobox["values"]=("Select Department","Computer Science","Data Science")
        department_combobox.current(0)
        department_combobox.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Duration For Which Teacher Is Going To Be In College/School
        duration_Label = Label(teacher_info_frame,text="Duration :",font=("times new roman",12,"bold"),bg="white")
        duration_Label.grid(row=2,column=0,padx=10,sticky=W)

        def open_calendar_duration(event):
            def save_interval():
                start_date = start_cal.get_date()
                end_date = end_cal.get_date()

                self.var_duration.set(f"{start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')}")
                root._cal_win_duration.destroy()
                del root._cal_win_duration

            def on_closing():
                root._cal_win_duration.destroy()
                del root._cal_win_duration

            if self.var_duration.get() == " " or self.var_duration.get() == "MMYY - MMYY":
                self.var_duration.set("")
                if not hasattr(root, "_cal_win_duration"):  # Check If The Calendar Window Is Already Open
                    root._cal_win_duration = Toplevel(root)
                    root._cal_win_duration.title("Select Date")
                    root._cal_win_duration.geometry("140x150+100+200")

                    Label1 = Label(root._cal_win_duration,text="Start Date : ",font=("times new roman",12))
                    Label1.place(x=20,y=0)

                    start_cal = DateEntry(root._cal_win_duration, date_pattern="MM/dd/yyyy",takefocus=False)
                    start_cal.place(x=10,y=30)
                    Label2 = Label(root._cal_win_duration,text="End Date : ",font=("times new roman",12))
                    Label2.place(x=20,y=60)

                    end_cal = DateEntry(root._cal_win_duration, date_pattern="MM/dd/yyyy",takefocus=False)
                    end_cal.place(x=10,y=90)

                    save_button = ttk.Button(root._cal_win_duration, text="Save duration", command=save_interval)
                    save_button.place(x=20,y=120)
                    root._cal_win_duration.protocol("WM_DELETE_WINDOW", on_closing)

        duration_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_duration,font=("times new roman",12),width=24)
        duration_entry.insert(0, "MMYY - MMYY")  # Placeholder Text
        duration_entry.bind("<FocusIn>", open_calendar_duration)  # Open Calendar On Focus
        duration_entry.bind("<Button-1>", open_calendar_duration)  # Open Calendar On Click
        duration_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Teacher Gender
        gender_Label = Label(teacher_info_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_Label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        gender_combobox = ttk.Combobox(teacher_info_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=22)
        gender_combobox["values"]=("Select Gender","Male","Female","Other")
        gender_combobox.current(0)
        gender_combobox.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Teacher Date Of Birth
        date_of_birth_Label = Label(teacher_info_frame,text="Date Of Birth :",font=("times new roman",12,"bold"),bg="white")
        date_of_birth_Label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        def open_calendar(event):
            def set_selected_date():
                selected_date = cal.get_date()
                self.var_dob.set(selected_date)
                root._cal_win_dob.destroy()
                del root._cal_win_dob

            def on_closing():
                root._cal_win_dob.destroy()
                del root._cal_win_dob

            if self.var_dob.get() == " " or self.var_dob.get() == "MM/DD/YY":
                self.var_dob.set("")
                if not hasattr(root, "_cal_win_dob"):  # Check If The Calendar Window Is Already Open
                    root._cal_win_dob = Toplevel(root)
                    root._cal_win_dob.title("Select Date")
                    cal = Calendar(root._cal_win_dob, selectmode='day')
                    cal.pack()

                    select_button = Button(root._cal_win_dob, text="Select", command=set_selected_date)
                    select_button.pack()
                    root._cal_win_dob.protocol("WM_DELETE_WINDOW", on_closing)

        date_of_birth_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_dob,font=("times new roman",12),width=24)
        date_of_birth_entry.insert(0, "MM/DD/YY")  # Placeholder Text
        date_of_birth_entry.bind("<FocusIn>", open_calendar)  # Open Calendar On Focus
        date_of_birth_entry.bind("<Button-1>", open_calendar)  # Open Calendar On Click
        date_of_birth_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Teacher Email
        email_Label = Label(teacher_info_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        email_Label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        def validate_email(event):
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.var_email.get()):
                email_entry.config(foreground="black")  # Set Text Color To Black
            else:
                email_entry.config(foreground="red")  # Set Text Color To Red

        email_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_email,font=("times new roman",12),width=24)
        email_entry.bind("<KeyRelease>", validate_email)  # Check On Each Key Release
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Teacher Phone Number
        phone_number_Label = Label(teacher_info_frame,text="Phone Number :",font=("times new roman",12,"bold"),bg="white")
        phone_number_Label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        def on_phone_focus_in(event):
            if self.var_phone.get() == "10 Digits only":
                self.var_phone.set("")

        def on_phone_focus_out(event):
            if not self.var_phone.get():
                self.var_phone.set("10 Digits only")

        def validate_phone_number(action, value_if_allowed):
            if action == "0" or value_if_allowed.isdigit() and len(value_if_allowed) <= 10: # Allow deletion And Numbers, And Ensure Length Is 10
                return True
            return False

        phone_number_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_phone,font=("times new roman",12),width=24,validate="key")
        self.var_phone.set("10 Digits only")
        phone_number_entry.config(validate="key",validatecommand=(root.register(validate_phone_number), "%d", "%P"))
        phone_number_entry.bind("<FocusIn>", on_phone_focus_in) # Set The Value On Focus
        phone_number_entry.bind("<FocusOut>", on_phone_focus_out) # Set The Value Off Focus
        phone_number_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Address
        address_Label = Label(teacher_info_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_Label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(teacher_info_frame,textvariable=self.var_address,font=("times new roman",12),width=24)
        address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Teacher Experience
        experience_Label = Label(teacher_info_frame,text="Experience :",font=("times new roman",12,"bold"),bg="white")
        experience_Label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        experience_combobox = ttk.Combobox(teacher_info_frame,textvariable=self.var_experince,font=("times new roman",12),state="readonly",width=22)
        experience_combobox["values"]=("Select Experience","0","1 yr","2 yr","3 yr","4+ yr")
        experience_combobox.current(0)
        experience_combobox.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        # Teacher Post
        post_Label = Label(teacher_info_frame,text="Post :",font=("times new roman",12,"bold"),bg="white")
        post_Label.grid(row=5,column=2,padx=10,pady=5,sticky=W)

        post_combobox = ttk.Combobox(teacher_info_frame,textvariable=self.var_post,font=("times new roman",12),state="readonly",width=22)
        post_combobox["values"]=("Select Post","HOD","Faculty","Visiting Faculty")
        post_combobox.current(0)
        post_combobox.grid(row=5,column=3,padx=10,pady=5,sticky=W)

        # Radio Buttons For Take/Update Photo Sample
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(teacher_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.place(x=20,y=235)

        radiobtn2 = ttk.Radiobutton(teacher_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.place(x=170,y=235)

        # Button Frames For Operations
        btn_frame = Frame(teacher_info_frame,bd=2,relief=RIDGE,bg="white",border=0)
        btn_frame.place(x=8,y=280,width=720,height=35)

        save_button = Button(btn_frame,command=self.add_data,cursor="hand2",text="Save",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        save_button.grid(row=0,column=0,padx=9)

        update_button = Button(btn_frame,command=self.update_data,cursor="hand2",text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        update_button.grid(row=0,column=1,padx=9)

        delete_button = Button(btn_frame,command=self.delete_data,cursor="hand2",text="Delete",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        delete_button.grid(row=0,column=2,padx=9)

        reset_button = Button(btn_frame,cursor="hand2",command=self.reset_data,text="Reset",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        reset_button.grid(row=0,column=3,padx=9)

        # Button For Take/Update Photo Sample
        take_photo_sample_button = Button(teacher_info_frame,command=self.generate_dataset,cursor="hand2",text="Take/Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        take_photo_sample_button.place(x=210,y=330)


        # Right Frame For Display Teachers Data And Perform Search
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Details",font=("times new roman",12,"bold"))
        right_frame.place(x=785,y=5,width=740,height=587)

        # Images Of Right Frame
        img_right1 = Image.open(r"images\teacher\teacher3.jpg")
        img_right1 = img_right1.resize((375,130),Image.Resampling.LANCZOS)
        self.photoimg_right1 = ImageTk.PhotoImage(img_right1)
        f_lbl = Label(right_frame,image=self.photoimg_right1)
        f_lbl.place(x=7,y=0,width=365,height=130)

        img_right2 = Image.open(r"images\teacher\teacher4.jpg")
        img_right2 = img_right2.resize((360,130),Image.Resampling.LANCZOS)
        self.photoimg_right2 = ImageTk.PhotoImage(img_right2)
        f_lbl = Label(right_frame,image=self.photoimg_right2)
        f_lbl.place(x=379,y=0,width=350,height=130)

        #  ************** Search System Code *************
        # Search Combo Box (Search Parameter)
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=135,width=720,height=70)

        search_combobox = ttk.Combobox(search_frame,textvariable=self.var_search_combo,font=("times new roman",15,"bold"),state="readonly",width=15)
        search_combobox["values"]=("Select","Email","Phone No","Name")
        search_combobox.current(0)
        search_combobox.place(x=10,y=8)

        # Take Search Data
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",15))
        search_entry.place(x=200,y=8)

        # Search Button
        search_button = Button(search_frame,command=self.perform_search,cursor="hand2",text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        search_button.place(x=375,y=6)

        # Refresh Button To Refresh The Teacher Details Window
        refresh_button = Button(search_frame,command=self.fetch_data,cursor="hand2",text="Refresh",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        refresh_button.place(x=515,y=6)

        # Table Frame To Show Teachers Data
        table_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=215,width=720,height=345)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.teacher_table = ttk.Treeview(table_frame,columns=("id","name","qualification","dept","duration","gender","dob","email","phone","address","experience","post","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("id",text="TeacherID")
        self.teacher_table.heading("name",text="Name")
        self.teacher_table.heading("qualification",text="Qualification")
        self.teacher_table.heading("dept",text="Department")
        self.teacher_table.heading("duration",text="duration")
        self.teacher_table.heading("gender",text="Gender")
        self.teacher_table.heading("dob",text="Date Of Birth")
        self.teacher_table.heading("email",text="Email")
        self.teacher_table.heading("phone",text="Phone")
        self.teacher_table.heading("address",text="Address")
        self.teacher_table.heading("experience",text="Experience")
        self.teacher_table.heading("post",text="Post")
        self.teacher_table.heading("photo",text="Photo Sample Status")
        self.teacher_table["show"]="headings"

        self.teacher_table.column("id",width=100)
        self.teacher_table.column("name",width=100)
        self.teacher_table.column("qualification",width=100)
        self.teacher_table.column("dept",width=110)
        self.teacher_table.column("duration",width=100)
        self.teacher_table.column("gender",width=100)
        self.teacher_table.column("dob",width=100)
        self.teacher_table.column("email",width=100)
        self.teacher_table.column("phone",width=100)
        self.teacher_table.column("address",width=100)
        self.teacher_table.column("experience",width=100)
        self.teacher_table.column("post",width=100)
        self.teacher_table.column("photo",width=250)

        self.teacher_table.pack(fill=BOTH,expand=1)
        self.teacher_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#-------------------------------------------------- Function Declaration ---------------------------------------------------------

    # ******************* Validation On Data Feilds *******************
    def validate_fields(self):
        def validate_phone_number(phone_number):
            return len(phone_number) == 10 and phone_number.isdigit()
        def validate_email(email):
            return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) # Basic Email Validation Using Regular Expression
        if not validate_phone_number(self.var_phone.get()):
            messagebox.showerror("Error","Phone Number Must Be Of 10 Digits",parent=self.root) # Display An Error Message For Invalid Phone Number
            return 0
        if not validate_email(self.var_email.get()):
            messagebox.showerror("Error","Enter A Valid Email Address",parent=self.root) # Display An Error Message For Invalid Email
            return 0
        return 1


    # ******************* Add The Data To Database *******************
    def add_data(self):
        if self.var_teacherid.get() == "Digits only" or self.var_teachername.get() == "" or self.var_duration.get() == "MMYY - MMYY" or self.var_qualification.get() == "Select Qualifacation" or self.var_dept.get() == "Select Department" or self.var_experince.get() == "Select Experience" or self.var_post.get() == "Select Post" or self.var_gender.get() == "Select Gender" or self.var_dob.get() == "MM/DD/YY" or self.var_email.get() == "" or self.var_phone.get() == "10 Digits only" or self.var_address.get() == "" or self.var_radio1.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            if(self.validate_fields()):
                try:
                    client = MongoClient('mongodb://localhost:27017/')
                    collection = client['face_recognition_system']['teacher_details']
                    collection.create_index([("teacher_id", pymongo.ASCENDING)], unique=True) # Create a Unique Index On a Field
                    collection.insert_one({"teacher_id":self.var_teacherid.get(),"teacher_name":self.var_teachername.get(),"qualification":self.var_qualification.get(),"department":self.var_dept.get(),"duration":self.var_duration.get(),"gender":self.var_gender.get(),"date_of_birth":self.var_dob.get(),"email":self.var_email.get(),"phone_number":self.var_phone.get(),"address":self.var_address.get(),"experience":self.var_experince.get(),"post":self.var_post.get(),"photo_sample_status":self.var_radio1.get(),"attendance":"absent","status":"teacher"})
                    client.close()
                    # Invoice Code After Successfull Completion Of Operation
                    sound = gtts.gTTS("Teacher details has been added successfully",lang = "en")
                    sound.save(r"teacher.mp3")
                    playsound.playsound(r"teacher.mp3")
                    if os.path.exists("teacher.mp3"):
                        os.remove("teacher.mp3")
                    messagebox.showinfo("Success","Teacher Details Has Been Added Successfully",parent=self.root)
                    self.fetch_data()
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Fetch The Data From Database *******************
    def fetch_data(self):
        self.var_search.set("")
        self.var_search_combo.set("Select")
        client = MongoClient('mongodb://localhost:27017/')
        collection = client['face_recognition_system']['teacher_details']
        result = collection.find({},{'_id': 0})
        values_list = []
        self.teacher_table.delete(*self.teacher_table.get_children())
        for document in result:
            values_list.clear()
            for key in document:
                values_list.append(document[key])
            self.teacher_table.insert("",END,values=values_list)
        client.close()
        self.reset_data() # To Reset The Entry Fields

    # ******************* Search From The Table TreeView *******************
    def perform_search(self):
        search_text = self.var_search.get().lower()
        selected_criteria = self.var_search_combo.get()

        self.teacher_table.delete(*self.teacher_table.get_children())  # Clear The Treeview Before Inserting Data

        client = MongoClient('mongodb://localhost:27017/')
        collection = client['face_recognition_system']['teacher_details']
        records_found = False # Create A Flag To Track If Any Matching Records Were Found
        result = collection.find({}, {'_id': 0})  # Exclude The _id Field With The Help Of Projection

        for row in result:
            if selected_criteria == "Email":
                roll_no = row.get("email", "")
                if search_text == str(roll_no).lower():
                    self.teacher_table.insert("", END, values=list(row.values()))
                    records_found = True
            elif selected_criteria == "Phone No":
                phone_number = row.get("phone_number", "")
                if search_text == str(phone_number).lower():
                    self.teacher_table.insert("", END, values=list(row.values()))
                    records_found = True
            elif selected_criteria == "Name":
                student_name = row.get("teacher_name", "")
                if search_text == str(student_name).lower():
                    self.teacher_table.insert("", END, values=list(row.values()))
                    records_found = True
        client.close()

        # Check If No Matching Records Were Found
        if not records_found:
            self.teacher_table.insert("", END, values=("No records found", "", "", "", "", "", "", "", "", "", "", "", "", "", ""))


    # ******************* Fetch The Data From Table TreeView To The Input Fields *******************
    def get_cursor(self,event=""):
        cursor_focus = self.teacher_table.focus()
        content = self.teacher_table.item(cursor_focus)
        data = content["values"]
        self.var_teacherid.set(data[0])
        self.var_teachername.set(data[1])
        self.var_qualification.set(data[2])
        self.var_dept.set(data[3])
        self.var_duration.set(data[4])
        self.var_gender.set(data[5])
        self.var_dob.set(data[6])
        self.var_email.set(data[7])
        self.var_phone.set(data[8])
        self.var_address.set(data[9])
        self.var_experince.set(data[10])
        self.var_post.set(data[11])
        self.var_radio1.set(data[12])

    # ******************* Update The Selected Data *******************
    def update_data(self):
        if self.var_teacherid.get() == "Digits only" or self.var_teachername.get() == "" or self.var_duration.get() == "MMYY - MMYY" or self.var_qualification.get() == "Select Qualifacation" or self.var_dept.get() == "Select Department" or self.var_experince.get() == "Select Experience" or self.var_post.get() == "Select Post" or self.var_gender.get() == "Select Gender" or self.var_dob.get() == "MM/DD/YY" or self.var_email.get() == "" or self.var_phone.get() == "10 Digits only" or self.var_address.get() == "" or self.var_radio1.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            if(self.validate_fields()):
                try:
                    Update = messagebox.askyesno("Update","Do You Want To Update This Teacher Details",parent=self.root)
                    if Update > 0:
                        client = MongoClient('mongodb://localhost:27017/')
                        collection = client['face_recognition_system']['teacher_details']
                        collection.update_one({"teacher_id":self.var_teacherid.get()},{"$set": {"teacher_id":self.var_teacherid.get(),"teacher_name":self.var_teachername.get(),"qualification":self.var_qualification.get(),"department":self.var_dept.get(),"duration":self.var_duration.get(),"gender":self.var_gender.get(),"date_of_birth":self.var_dob.get(),"email":self.var_email.get(),"phone_number":self.var_phone.get(),"address":self.var_address.get(),"experience":self.var_experince.get(),"post":self.var_post.get(),"photo_sample_status":self.var_radio1.get(),"attendance":"absent","status":"teacher"}})
                        client.close()
                        # Invoice Code After Successfull Completion Of Operation
                        sound = gtts.gTTS("Teacher details has been updated successfully",lang = "en")
                        sound.save(r"teacher.mp3")
                        playsound.playsound(r"teacher.mp3")
                        if os.path.exists("teacher.mp3"):
                            os.remove("teacher.mp3")
                        messagebox.showinfo("Success","Teacher Details Has Been Updated Successfully",parent=self.root)
                    else:
                        if not Update:
                            return
                    self.fetch_data()
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Delete The Selected Data *******************
    def delete_data(self):
        if self.var_teacherid.get() == "Digits only":
            messagebox.showerror("Error","Teacher Id Must Be Required",parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Delete","Do You Want To Delete The Selected Teacher Details",parent=self.root)
                if Delete > 0:
                    client = MongoClient('mongodb://localhost:27017/')
                    collection = client['face_recognition_system']['teacher_details']
                    collection.delete_one({"teacher_id":self.var_teacherid.get()})
                    client.close()
                    # Invoice Code After Successfull Completion Of Operation
                    sound = gtts.gTTS("Teacher details has been deleted successfully",lang = "en")
                    sound.save(r"teacher.mp3")
                    playsound.playsound(r"teacher.mp3")
                    if os.path.exists("teacher.mp3"):
                        os.remove("teacher.mp3")
                    messagebox.showinfo("Success","Teacher Details Has Been Deleted Successfully",parent=self.root)
                else:
                    if not Delete:
                        return
                self.fetch_data()
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Reset All The Fields To Default Values *******************
    def reset_data(self):
        self.var_teacherid.set("Digits only")
        self.var_teachername.set("")
        self.var_qualification.set("Select Qualifacation")
        self.var_dept.set("Select Department")
        self.var_duration.set("MMYY - MMYY")
        self.var_gender.set("Select Gender")
        self.var_dob.set("MM/DD/YY")
        self.var_email.set("")
        self.var_phone.set("10 Digits only")
        self.var_address.set("")
        self.var_experince.set("Select Experience")
        self.var_post.set("Select Post")
        self.var_radio1.set("")
        self.var_search.set("")
        self.var_search_combo.set("Select")

    # ******************* Generate Dataset Or Take/Update Photo Sample *******************
    def generate_dataset(self):
        if self.var_teacherid.get() == "Digits only" or self.var_teachername.get() == "" or self.var_duration.get() == "MMYY - MMYY" or self.var_qualification.get() == "Select Qualifacation" or self.var_dept.get() == "Select Department" or self.var_experince.get() == "Select Experience" or self.var_post.get() == "Select Post" or self.var_gender.get() == "Select Gender" or self.var_dob.get() == "MM/DD/YY" or self.var_email.get() == "" or self.var_phone.get() == "10 Digits only" or self.var_address.get() == "" or self.var_radio1.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            if(self.validate_fields()):
                try:
                    client = MongoClient('mongodb://localhost:27017/')
                    collection = client['face_recognition_system']['teacher_details']
                    id = self.var_teacherid.get()
                    collection.update_one({"teacher_id":self.var_teacherid.get()},{"$set": {"teacher_id":self.var_teacherid.get(),"teacher_name":self.var_teachername.get(),"qualification":self.var_qualification.get(),"department":self.var_dept.get(),"duration":self.var_duration.get(),"gender":self.var_gender.get(),"date_of_birth":self.var_dob.get(),"email":self.var_email.get(),"phone_number":self.var_phone.get(),"address":self.var_address.get(),"experience":self.var_experince.get(),"post":self.var_post.get(),"photo_sample_status":self.var_radio1.get(),"attendance":"absent","status":"teacher"}})
                    client.close()
                    self.fetch_data()
                    self.reset_data()

                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # Load Predefined Data On Face Frontals From Opencv For Object Detection

                    def face_cropped(img): # Cropping The Image In Gray Scale / Resize The Image
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Converting The Img To Grey Scale
                        faces = face_classifier.detectMultiScale(gray,1.3,5) # Scaling Factor = 1.3(By Default) Minimum Neighbour = 5
                        for(x,y,w,h) in faces: # x = xaxis y = yaxis w = weight h = height of a rectangle
                            return img[y:y+h,x:x+w]

                    cap = cv2.VideoCapture(0) # Camera Captured
                    img_id = 0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face = cv2.resize(face_cropped(my_frame),(450,450))
                            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_path = "data/Teacher_userid_"+str(id)+"_photosample_"+str(img_id)+"_done.jpg"
                            cv2.imwrite(file_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
                            cv2.imshow("Cropped Face",face)
                        if cv2.waitKey(1) == 13 or int(img_id) == 100: # 13 Represents The User Has Hit The Enter Then The Capture Will Stop
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    # Invoice Code After Successfull Completion Of Operation
                    sound = gtts.gTTS("Generation of Data set is completed successfully",lang = "en")
                    sound.save(r"teacher.mp3")
                    playsound.playsound(r"teacher.mp3")
                    if os.path.exists("teacher.mp3"):
                        os.remove("teacher.mp3")
                    messagebox.showinfo("Success","Generation Of Data Set Is Completed Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Back To Home Function *******************
    def back_to_home(self):
        self.root.destroy()

# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Teacher_Details(root)
    root.mainloop()