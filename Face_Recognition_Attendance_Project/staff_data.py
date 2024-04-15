# Required Libraries
# For GUI
from tkinter import*
from tkinter import ttk
from time import strftime # For Time Stamp
from pymongo import MongoClient # For MongoDB

# Main class
class Staff_Data:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1560x820+0+0")
        self.root.title("Face Recognition System")

        # Top Title Label
        title_label = Label(self.root,text="STAFF DATA",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1550,height=45)

        # Back To Home Button At Label
        back_button = Button(self.root,cursor="hand2",command=self.back_to_admin,text="Back",width=10,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="darkgreen",activeforeground="white")
        back_button.place(x=1400,y=5)

        # To Display Time At Label
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_label,font=("times new roman",12,"bold"),background='white',foreground='black')
        lbl.place(x=10,y=0,width=110,height=50)
        time()

        # Main Frame For Staff Details Table
        main_frame = Frame(self.root,bd = 2,bg="white")
        main_frame.place(x=0,y=45,width=1600,height=800)

        # Table Frame For Staff Details
        table_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=0,width=1520,height=740)
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.staff_table = ttk.Treeview(table_frame,columns=("id","name","qualification","dept","duration","gender","dob","email","phone","address","experience","post","photo","attendance","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)

        self.staff_table.heading("id",text="TeacherID")
        self.staff_table.heading("name",text="Name")
        self.staff_table.heading("qualification",text="Qualification")
        self.staff_table.heading("dept",text="Department")
        self.staff_table.heading("duration",text="duration")
        self.staff_table.heading("gender",text="Gender")
        self.staff_table.heading("dob",text="Date Of Birth")
        self.staff_table.heading("email",text="Email")
        self.staff_table.heading("phone",text="Phone")
        self.staff_table.heading("address",text="Address")
        self.staff_table.heading("experience",text="Experience")
        self.staff_table.heading("post",text="Post")
        self.staff_table.heading("photo",text="Photo Sample Status")
        self.staff_table.heading("attendance",text="Attendance")
        self.staff_table.heading("status",text="Status")
        self.staff_table["show"]="headings"

        self.staff_table.column("id",width=100)
        self.staff_table.column("name",width=100)
        self.staff_table.column("qualification",width=100)
        self.staff_table.column("dept",width=110)
        self.staff_table.column("duration",width=100)
        self.staff_table.column("gender",width=100)
        self.staff_table.column("dob",width=100)
        self.staff_table.column("email",width=100)
        self.staff_table.column("phone",width=100)
        self.staff_table.column("address",width=100)
        self.staff_table.column("experience",width=100)
        self.staff_table.column("post",width=100)
        self.staff_table.column("photo",width=250)

        self.staff_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

#-------------------------------------------------- function declaration ---------------------------------------------------------

    # ******************* Fetch The Data From Database *******************
    def fetch_data(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['face_recognition_system']
        collection = db['staff_details']
        result = collection.find({},{'_id': 0})
        values_list = []
        self.staff_table.delete(*self.staff_table.get_children())
        for document in result:
            values_list.clear()
            for key in document:
                values_list.append(document[key])
            self.staff_table.insert("",END,values=values_list)
        client.close()

    # ******************* Back To Admin Function *******************
    def back_to_admin(self):
            self.root.destroy()

# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Staff_Data(root)
    root.mainloop()