# Required Libraries
# For GUI
from tkinter import*
from tkinter import ttk
from PIL import  Image,ImageTk
from tkinter import messagebox
from time import strftime # For Time Stamp
import os # For OS Operations
import re # To Restrict Name Input To Aplhabates Only
import csv # To CSV Operations
from tkinter import filedialog # Window For Selecting Files
# For Generating Invoice
import gtts
import playsound

my_data=[] # Load Data From The CSV File Into Memory

# Main class
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1560x820+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_attendance_id = StringVar()
        self.var_attendance_individual_status = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_status = StringVar()

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
        title_label = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=130,width=1530,height=45)

        # Back To Home Button At Label
        back_button = Button(self.root,cursor="hand2",command=self.back_to_home,text="Home",width=10,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        back_button.place(x=1400,y=136)

        # To Display Time At Label
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_label,font=("times new roman",14,"bold"),background='white',foreground='black')
        lbl.place(x=50,y=0,width=110,height=50)
        time()

        # Background Image Below Main Frame
        img3 = Image.open(r"images\background.jpg")
        img3 = img3.resize((1600,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=175,width=1600,height=710)

        # Main Frame For Attendance Record Operations And Viewing Attendance Records
        main_frame = Frame(bg_img,bd = 2,bg="white")
        main_frame.place(x=0,y=0,width=1600,height=600)

        # Left Frame For Attendance Record Operations
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=400,height=580)

        # Attendance Id
        attendance_id_Label = Label(left_frame,text="Attendance ID :",font=("comicsansns",12,"bold"),bg="white")
        attendance_id_Label.grid(row=0,column=0,pady=10,padx=10)
        def on_id_focus_in(event):
            if self.var_attendance_id.get() == "Digits only":
                self.var_attendance_id.set("")

        def on_id_focus_out(event):
            if not self.var_attendance_id.get():
                self.var_attendance_id.set("Digits only")

        def validate_id(action, value_if_allowed):
            if action == "0" or value_if_allowed.isdigit(): # Allow Deletion And Numbers
                return True
            return False

        attendance_id_entry = ttk.Entry(left_frame,textvariable=self.var_attendance_id,width=22,font=("comicsansns",12),validate="key")
        self.var_attendance_id.set("Digits only")
        attendance_id_entry.config(validate="key",validatecommand=(root.register(validate_id), "%d", "%P"))
        attendance_id_entry.bind("<FocusIn>", on_id_focus_in) # Set The Value On Focus
        attendance_id_entry.bind("<FocusOut>", on_id_focus_out) # Set The Value Off Focus
        attendance_id_entry.grid(row=0,column=1,pady=10,padx=10)

        # Individual Status
        status_label = Label(left_frame,text="Select Status :",font=("comicsansns",12,"bold"),bg="white")
        status_label.grid(row=1,column=0,pady=10,padx=10)

        status_entry = ttk.Combobox(left_frame,textvariable=self.var_attendance_individual_status,font=("comicsansns",12),state="readonly",width=20)
        status_entry["values"]=("Status","Student","Teacher","Staff")
        status_entry.current(0)
        status_entry.grid(row=1,column=1,pady=10,padx=10)

        # Individual Name
        name_Label = Label(left_frame,text="Name :",font=("comicsansns",12,"bold"),bg="white")
        name_Label.grid(row=2,column=0,pady=10,padx=10)
        def validate_text_input(P):
            return re.match("^[a-zA-Z]*$", P) is not None # Allow Only Letters (Text)

        name_entry = ttk.Entry(left_frame,textvariable=self.var_attendance_name,width=22,font=("comicsansns",12),validate="key", validatecommand=(root.register(validate_text_input), "%P"))
        name_entry.grid(row=2,column=1,pady=10,padx=10)

        # Attendance Date
        time_Label = Label(left_frame,text="Date :",font=("comicsansns",12,"bold"),bg="white")
        time_Label.grid(row=3,column=0,pady=10,padx=10)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_attendance_time,width=22,font=("comicsansns",12))
        time_entry.grid(row=3,column=1,pady=10,padx=10)

        # Attendance Time
        date_Label = Label(left_frame,text="Time :",font=("comicsansns",12,"bold"),bg="white")
        date_Label.grid(row=4,column=0,pady=10,padx=10)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_attendance_date,width=22,font=("comicsansns",12))
        date_entry.grid(row=4,column=1,pady=10,padx=10)

        # Attendance Status
        attendance_Label = Label(left_frame,text="Attendance :",font=("comicsansns",12,"bold"),bg="white")
        attendance_Label.grid(row=5,column=0,pady=10,padx=10)

        attendance_status = ttk.Combobox(left_frame,textvariable=self.var_attendance_status,font=("comicsansns",12),state="readonly",width=20)
        attendance_status["values"]=("Select Status","Present","Absent")
        attendance_status.current(0)
        attendance_status.grid(row=5,column=1,pady=10,padx=10)

        # Buttons For Operations
        import_csv_button = Button(left_frame,cursor="hand2",text="Import CSV",command=self.import_csv,width=17,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        import_csv_button.place(x=70,y=300)

        export_csv_button = Button(left_frame,cursor="hand2",text="Export CSV",command=self.export_csv,width=17,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        export_csv_button.place(x=70,y=360)

        update_button = Button(left_frame,cursor="hand2",text="Update",command=self.update_csv,width=17,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        update_button.place(x=70,y=420)

        reset_button = Button(left_frame,cursor="hand2",text="Reset",command=self.reset_data,width=17,font=("times new roman",14,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        reset_button.place(x=70,y=480)


        # Right Frame For Viewing Attendance Records
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Attendance Details ",font=("times new roman",12,"bold"))
        right_frame.place(x=430,y=10,width=1085,height=580)

        # Table Frame To Show Attendance Records
        table_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=5,width=1055,height=548)
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.Attendance_Report_table = ttk.Treeview(table_frame,columns=("id","status","name","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_Report_table.xview)
        scroll_y.config(command=self.Attendance_Report_table.yview)

        self.Attendance_Report_table.heading("id",text="Attendance ID")
        self.Attendance_Report_table.heading("status",text="Status")
        self.Attendance_Report_table.heading("name",text="Name")
        self.Attendance_Report_table.heading("date",text="Date")
        self.Attendance_Report_table.heading("time",text="Time")
        self.Attendance_Report_table.heading("attendance",text="Attendance")
        self.Attendance_Report_table["show"]="headings"

        self.Attendance_Report_table.column("id",width=100)
        self.Attendance_Report_table.column("status",width=100)
        self.Attendance_Report_table.column("name",width=100)
        self.Attendance_Report_table.column("time",width=100)
        self.Attendance_Report_table.column("date",width=100)
        self.Attendance_Report_table.column("attendance",width=100)

        self.Attendance_Report_table.pack(fill=BOTH,expand=1)
        self.Attendance_Report_table.bind("<ButtonRelease>",self.get_cursor)

#-------------------------------------------------- Function Declaration ---------------------------------------------------------

    # ******************* Fetching Data From CSV File *******************
    def fetch_data(self,rows):
        self.Attendance_Report_table.delete(*self.Attendance_Report_table.get_children())
        for i in rows:
            self.Attendance_Report_table.insert("",END,values=i)

    # ******************* Importing CSV File *******************
    def import_csv(self):
        global my_data , file_name
        my_data.clear()
        file_name  = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csv_read = csv.reader(myfile,delimiter=",")
            headers = next(csv_read)  # Skip The First Row
            for i in csv_read:
                my_data.append(i)
            self.fetch_data(my_data)

    # ******************* Exporting CSV File *******************
    def export_csv(self):
        try:
            if(len(my_data)) < 1:
                messagebox.showerror("Error","No Data Found To Export",parent = self.root)
                return False
            export_file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(export_file_name,mode="w",newline="") as myfile:
                export_write = csv.writer(myfile,delimiter=",")
                for i in my_data:
                    export_write.writerow(i)
                messagebox.showinfo("Success",f"Data Exported To File **{self.export_file_name}** Successfully",parent= self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ******************* Updating CSV File *******************
    def update_csv(self):
        if self.var_attendance_date.get() == "" or self.var_attendance_status.get() == "Select Status" or self.var_attendance_individual_status.get() == "Select Status" or self.var_attendance_name.get() == "" or self.var_attendance_name.get() == "" or self.var_attendance_id.get() == "" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else :
            Update = messagebox.askyesno("Update","Do You Want To Update This Attendance Record",parent=self.root)
            if Update > 0:
                selected_item = self.Attendance_Report_table.selection()
                if selected_item:
                    selected_item = selected_item[0]
                    selected_id = self.Attendance_Report_table.item(selected_item, "values")[0]
                    data = [] # Load data from the CSV file into memory
                    with open(file_name, 'r') as csvfile: # Add The CSV Data To Data List
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            data.append(row)

                    for row in data: # Update The Data List W.R.T Id Field
                        if row['ID'] == selected_id:
                            row['STATUS'] = self.var_attendance_individual_status.get()
                            row['NAME'] = self.var_attendance_name.get()
                            row['DATE'] = self.var_attendance_date.get()
                            row['TIME'] = self.var_attendance_time.get()
                            row['ATTENDANCE'] = self.var_attendance_status.get()

                    with open(file_name, 'w', newline='') as csvfile: # Save the updated data back to the CSV file, including the 'ID' column
                        fieldnames = ['ID','STATUS', 'NAME', 'DATE','TIME','ATTENDANCE']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(data)

                    # Invoice Code After Successfull Completion Of Operation
                    sound = gtts.gTTS("Attendance Record Has Been Updated Successfully",lang = "en")
                    sound.save(r"attendance.mp3")
                    playsound.playsound(r"attendance.mp3")
                    if os.path.exists("attendance.mp3"):
                        os.remove("attendance.mp3")
                    messagebox.showinfo("Success","Attendance Record Has Been Updated Successfully",parent=self.root)

                    # Populate The Treeview With Updated CSV File
                    my_data.clear()
                    with open(file_name) as myfile:
                        csv_read = csv.reader(myfile,delimiter=",")
                        headers = next(csv_read)  # Skip the first row
                        for i in csv_read:
                            my_data.append(i)
                        self.fetch_data(my_data)
            else:
                if not Update:
                    return

    # ******************* Reset All The Fields To Default Values *******************
    def reset_data(self):
        self.var_attendance_status.set("Select Status")
        self.var_attendance_id.set("Digits only")
        self.var_attendance_date.set("")
        self.var_attendance_name.set("")
        self.var_attendance_name.set("")
        self.var_attendance_individual_status.set("Select Status")

    # ******************* Fetch The Data From Table TreeView To The Input Fields *******************
    def get_cursor(self,event=""):
        cursor_focus = self.Attendance_Report_table.focus()
        content = self.Attendance_Report_table.item(cursor_focus)
        data = content["values"]

        self.var_attendance_id.set(data[0])
        self.var_attendance_individual_status.set(data[1])
        self.var_attendance_name.set(data[2])
        self.var_attendance_date.set(data[3])
        self.var_attendance_time.set(data[4])
        self.var_attendance_status.set(data[5])

    # ******************* Back To Home Function *******************
    def back_to_home(self):
        self.root.destroy()


# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()