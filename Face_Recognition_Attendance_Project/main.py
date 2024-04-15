# Required Libraries
# For GUI
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image,ImageTk
import os # For OS Operations
from time import strftime # For Time Stamp
# For Including Other Project Windows
from student import Student
from teacher import Teacher_Details
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from staff import Staff_Details

# r Is Used To Convert Back Slash To Forward Slash As In Python We Need To Convert It While Giving Path

# Main class
class Face_Recognition_System :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1560x820+0+0")
        self.root.title("Face Recognition System")

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

        # Background Image
        img3 = Image.open(r"images\background.jpg")
        img3 = img3.resize((1550,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=710)

        # Top Title Label
        title_label = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1550,height=45)

        # To Display Time At Label
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_label,font=("times new roman",12,"bold"),background='white',foreground='black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # Student Button
        img4 = Image.open(r"images\main\student.png")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Teacher Button
        img7 = Image.open(r"images\main\teacher.png")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.teacher_details)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Teacher Details",cursor="hand2",command=self.teacher_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Staff Button
        img10 = Image.open(r"images\main\staff.png")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.staff_details)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Staff Details",cursor="hand2",command=self.staff_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Train Data Button
        img8 = Image.open(r"images\main\train.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # Detect Face Button
        img5 = Image.open(r"images\main\detect.jpg")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        # Attendance Button
        img6 = Image.open(r"images\main\attendance.png")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command = self.attendance_data)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command = self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        # Photos Button
        img9 = Image.open(r"images\main\photos.png")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        # Exit Button
        img11 = Image.open(r"images\main\exit.jpg")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white",activebackground="darkblue",activeforeground="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

#-------------------------------------------------- Function Declaration ---------------------------------------------------------

    # ******************* Student Details Function *******************
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    # ******************* Train Data Function *******************
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    # ******************* Face Recognition Function *******************
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    # ******************* Attendance Record Function *******************
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    # ******************* Staff Details Function *******************
    def staff_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Staff_Details(self.new_window)

    # ******************* Teacher Details Function *******************
    def teacher_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Teacher_Details(self.new_window)

    # ******************* Exit From The System Function *******************
    def exit(self):
        self.exit = messagebox.askyesno("Face Recognition","Are you sure",parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    # ******************* Function To Open 'Data' Folder *******************
    def open_img(self):
        os.startfile("data")


# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()