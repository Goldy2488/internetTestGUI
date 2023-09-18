from tkinter import *
import speedtest

# Function to get the internet speed
def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps" # bit per second ko mbps me change kiya
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_download.config(text=down)
    lab_upload.config(text=up)

# Create a Tkinter window
sp = Tk()
sp.title("🌐 Internet Speed Test 🌐")
sp.geometry("500x600")
sp.config(bg="blue")

# Create a label to display the internet speed
lab = Label(sp, text="Click below to test your internet speed!", font=("Times New Roman", 20, "bold"),bg="blue",fg="white")
lab.place(x=20,y=30,height=50,width=460)


lab = Label(sp, text="Download Speed", font=("Times New Roman", 20, "bold"),fg="black")
lab.place(x=60,y=120,height=50,width=380)

lab_download = Label(sp, text="00", font=("Times New Roman", 20, "bold"),fg="black")
lab_download.place(x=60,y=210,height=50,width=380)

lab = Label(sp, text="Upload Speed", font=("Times New Roman", 20, "bold"),fg="black")
lab.place(x=60,y=300,height=50,width=380)

lab_upload = Label(sp, text="00", font=("Times New Roman", 20, "bold"),fg="black")
lab_upload.place(x=60,y=390,height=50,width=380)

btn= Button(sp,text="🌐 Internet Test 🌐",font=("Time New Roman",20,"bold")
                     ,relief=RAISED,cursor="plus",bg="black",fg="white",command=speedcheck)
btn.place(x=120,y=480,height=50,width=270)
sp.mainloop()
