# Required Libraries
# For GUI
from tkinter import*
from PIL import  Image,ImageTk
from pymongo import MongoClient # For MongoDB
# For Date And Time Stamp
from time import strftime
from datetime import datetime
import cv2 # For Face Recognition
import os # For OS Operations
# For Sending E-Mails
import smtplib
from email.message import EmailMessage
from twilio.rest import Client # For Sending Text SMS To The Phone Number
# For Generating Invoice
import gtts
import playsound

# Main class
class Face_Recognition:
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
        title_label = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
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

        # Left Image
        img_left = Image.open(r"images\face_recognition\img1.png")
        img_left = img_left.resize((700,640),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=175,width=700,height=640)

        # Right Image
        img_right = Image.open(r"images\face_recognition\img2.jpg")
        img_right = img_right.resize((850,640),Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=700,y=175,width=850,height=640)

        # Recognition Button
        b1_1 = Button(self.root,text="Recognize",cursor="hand2",command = self.face_recog,font=("times new roman",15,"bold"),bg="darkgreen",fg="white",activebackground="darkgreen",activeforeground="white")
        b1_1.place(x=1030,y=740,width=200,height=40)

#-------------------------------------------------- Function Declaration ---------------------------------------------------------

    # ******************* Mark Attendance To CSV And Send Confirmation Message *******************
    def mark_attendance(self,sid,status,name,email,phone):
        with open("attendance.csv","r+",newline="\n") as f:  # Create File Manually For 1st Time
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry = line.split(",")
                name_list.append(entry[0])
            if((sid not in name_list) and (status not in name_list) and (name not in name_list)):
                d1 = datetime.now().strftime("%d/%m/%Y")
                dt_string = datetime.now().strftime("%H:%M:%S")
                f.writelines(f"{sid},{status},{name},{d1},{dt_string},Present\n")
                message = name+" was present at the time : "+dt_string+" on the day : "+d1
                self.send_mail(message,email)
                self.send_msg(message,phone)
                sound = gtts.gTTS(name+" marked Present",lang = "en")
                sound.save(r"recognize.mp3")
                playsound.playsound(r"recognize.mp3")
                if os.path.exists("recognize.mp3"):
                    os.remove("recognize.mp3")

    # ******************* Send E-Mail Confirmation Message *******************
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

    # ******************* Send SMS Confirmation Message *******************
    def send_msg(self,message,phone):
        account_sid = 'Your_Twilio_Account_SID' # Twilio Account SID
        auth_token = 'Your_Twilio_Account_Authentication_Token' # Twilio Account Authentication Token
        client = Client(account_sid, auth_token)  # Create A Twilio Client
        twilio_phone_number = '+Your_Twilio_Phone_Number' # Your Twilio Phone Number (You Must Have Purchased This Number On Twilio)
        recipient_phone_number = f"+91{phone}" # Recipient's Phone Number (In E.164 Format, Including Country Code, e.g., +1234567890)
        client.messages.create(body = message, from_ = twilio_phone_number, to = recipient_phone_number) # Send The SMS

    # ******************* Face Recognition Function *******************
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
            coordinates = []
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                client = MongoClient('mongodb://localhost:27017/')
                db = client['face_recognition_system']

                name = ""  # Default Values
                status = ""
                individual_id = ""
                email = ""
                phone = ""
                duration = ""

                collection = db['student_details']
                data = collection.find({"student_id": str(id)}, {"student_name": 1, "student_id": 1, "status": 1, "email": 1, "phone_number": 1,"duration" : 1, "_id": 0})
                data_list = list(data) # Convert The Cursor To A List Of Documents
                if data_list:
                    c = 1
                    student_data = data_list[0]
                    name = student_data.get("student_name", "")
                    status = student_data.get("status", "")
                    individual_id = student_data.get("student_id", "")
                    email = student_data.get("email", "")
                    phone = student_data.get("phone_number", "")
                    duration = student_data.get("duration","")

                collection = db['teacher_details']
                data = collection.find({"teacher_id":str(id)},{"teacher_name": 1, "teacher_id": 1, "status": 1, "email": 1, "email": 1, "phone_number": 1,"duration" : 1,"_id": 0})
                data_list.clear()
                data_list = list(data) # Convert The Cursor To A List Of Documents
                if data_list:
                    c = 2
                    teacher_data = data_list[0]
                    name = teacher_data.get("teacher_name", "")
                    status = teacher_data.get("status", "")
                    individual_id = teacher_data.get("teacher_id", "")
                    email = teacher_data.get("email", "")
                    phone = teacher_data.get("phone_number", "")
                    duration = teacher_data.get("duration", "")

                collection = db['staff_details']
                data = collection.find({"staff_id":str(id)},{"staff_name": 1, "staff_id": 1, "status": 1, "email": 1, "email": 1,"phone_number": 1,"duration" : 1, "_id": 0})
                data_list.clear()
                data_list = list(data) # Convert The Cursor To A List Of Documents
                if data_list:
                    c = 3
                    staff_data = data_list[0]
                    name = staff_data.get("staff_name", "")
                    status = staff_data.get("status", "")
                    individual_id = staff_data.get("staff_id", "")
                    email = staff_data.get("email", "")
                    phone = staff_data.get("phone_number", "")
                    duration = staff_data.get("duration", "")

                # Parse The Duration String Into Start And End Months And Years
                start_month, start_year, _, end_month, end_year = duration.split()
                start_date = datetime(int(start_year), datetime.strptime(start_month, "%b").month, 1).date()
                end_date = datetime(int(end_year), datetime.strptime(end_month, "%b").month, 1).date()
                current_date = datetime.now().date() # Get The Current Date

                if confidence > 77 and start_date <= current_date <= end_date:
                    cv2.putText(img,f"Status : {status}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(100,100,0),3)
                    cv2.putText(img,f"Id : {individual_id}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    cv2.putText(img,f"Name : {name}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    if c == 1:
                        collection = db['student_details']
                        collection.update_one({"student_id":individual_id},{"$set":{"attendance":"present"}})
                    elif c == 2:
                        collection = db['teacher_details']
                        collection.update_one({"teacher_id":individual_id},{"$set":{"attendance":"present"}})
                    elif c == 3:
                        collection = db['staff_details']
                        collection.update_one({"staff_id":individual_id},{"$set":{"attendance":"present"}})
                    self.mark_attendance(individual_id,status,name,email,phone)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face Detected",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    # Invoice Code After Successfull Completion Of Operation
                    sound = gtts.gTTS("Unknown Face Detected",lang = "en")
                    sound.save(r"recognize.mp3")
                    playsound.playsound(r"recognize.mp3")
                    if os.path.exists("recognize.mp3"):
                        os.remove("recognize.mp3")
                coordinates = [x,y,w,h]
                client.close()
            return coordinates

        def recognize(img,clf,faceCascade):
            coordinates = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        # Recognizing Individual
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    # ******************* Back To Home Function *******************
    def back_to_home(self):
        self.root.destroy()

# --------------------------------- Main Class Calling ---------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()