# Required Libraries
# For GUI
from tkinter import*
from PIL import  Image,ImageTk
from tkinter import messagebox
import cv2 # For Training Model With Photo Samples
from time import strftime # For Time Stamp
import os # For OS Operations
# For Generating Invoice
import gtts
import playsound
import numpy as np # It Gives The Performance Of More Than 88% While Converting In Array

# Main class
class Train:
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

        # Top Title Label
        title_label = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=130,width=1550,height=45)

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

        # Background Image
        img_top = Image.open(r"images\train\img1.jpg")
        img_top = img_top.resize((1550,650),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=175,width=1550,height=650)

        # Button For Train Data
        b1_1 = Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white")
        b1_1.place(x=700,y=650,width=200,height=60)


#-------------------------------------------------- Function Declaration ---------------------------------------------------------

    # ******************* Train The Classifier *******************
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir) ]
        faces=[]
        ids=[]
        for image in path:
            img = Image.open(image).convert('L') # Convert Into Grayscale
            image_np = np.array(img,'uint8') # uint8 Is Data Type
            id = int(os.path.split(image)[1].split('_')[2])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train The Classifier And Save The Data
        classifier = cv2.face.LBPHFaceRecognizer_create() # For This Error Try This Command  'pip install opencv-contrib-python' And if Open CV Is Not There Try 'pip install opencv-python'
        classifier.train(faces,ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        # Invoice Code After Successfull Completion Of Operation
        sound = gtts.gTTS("Training Data set completed successfully",lang = "en")
        sound.save(r"train.mp3")
        playsound.playsound(r"train.mp3")
        if os.path.exists("train.mp3"):
            os.remove("train.mp3")
        messagebox.showinfo("Result","Training Data set completed successfully",parent=self.root)

    # ******************* Back To Home Function *******************
    def back_to_home(self):
        self.root.destroy()

# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()