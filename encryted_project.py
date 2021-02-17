from tkinter import*
from tkinter import filedialog
root = Tk()
root.title("THE ENCRYPTION & DECRYPTION PROJECT")
root.minsize(1000,500)
def encrypted_image():
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    file_name = file1.name
    key = entry1.get()
    fi = open(file_name,'rb')
    image = fi.read()
    fi.close()
    image = bytearray(image)
    for index,values in enumerate(image):
        image[index] = values^int(key)
    fi1 = open(file_name,'wb')
    fi1.write(image)
    fi1.close()
def new_file():
    tp = Toplevel()
    tp.minsize(1300,1200)
    text11 = """'''::->Description About the App<-::'''"""
    label11 = Label(tp,text=text11,bd=15,font=("arial",20,"bold","underline"),justify="center")
    label11.place(x=460,y=0)
    text5 = """'''1->This is very Interactive small Software used for Encryption
    and Decryption of image (in the format of all jpg) .'''"""
    label4 = Label(tp,text=text5,justify="center",font=("arial",30,"bold"),bd=12,fg="purple")
    label4.place(x=0,y=60)
    text6 = """'''2-> If you want to send the image to anyone there is some 
    cyberattacks during the transmission of the data (image)
    due to this ,it can encrypt the data (image) in some different form
    for which the data (image) remains save as it is ..'''"""
    label6 = Label(tp,text =text6 ,justify="left",font=("arial",30,"bold"),bd=12,fg="purple")
    label6.place(x=0,y=230)
    text7 = """'''3->If you want to send the data in Encrypted form please download
    this app on both the desktop i.e. (userside & receiverside)
     for encryption and Decryption.''' """
    label7 = Label(tp,text=text7,justify="left",font=("arial",30,"bold"),bd=12,fg="purple")
    label7.place(x=0,y=460)

text1 = """'''If you want to encrypt the image so kindly choose any password,        
it must be in integer values such as 1,2,3,..,255 '''   """
label2 = Label(root,text=text1,bd=12,bg="slateblue",fg="black",font=("arial",20,"bold"))
label2.place(x=0,y=40)
label = Label(root,text ="""'''Enter the Password for Encryption & Decryption of Image''' """,bd=15,bg="slateblue",fg="black",font=("arial",24,"bold"))
label.place(x=0,y=140)
entry1 = Entry(root,bd=20,font=("arial",24,"bold"),width=51,justify="center")
entry1.place(x=0,y=220)
text2 = """'''If you want to Encrypt & Decrypt the image, so kindly press the           
Encryption and Decryption button which are given below'''"""
label3 = Label(root,text=text2,bd=12,bg="slateblue",fg="black",font=("arial",20,"bold"))
label3.place(x=0,y=300)
button = Button(root,text="Click for Encryption and Decryption",bd="20",fg="black",bg="cyan",font=("arial",20,"bold"),command=encrypted_image)
button.place(x=0,y=400)
button2 = Button(root,text = "About",font=("arial",20,"bold"),bd=20,bg="slateblue",fg="black",width=16,command=new_file)
button2.place(x=650,y=400)
root.resizable()
root.mainloop()