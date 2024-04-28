import time
import tkinter
import tkinter as tk
from tkinter import filedialog
import subprocess

#create window
root=tkinter.Tk()
root.title("Uninstall")

#create label
labelButton=tkinter.Label(root,text="UNINSTALL",font=("Arial",20,"bold"),padx=10,pady=10)
labelFrame=tkinter.Frame(root,bg="")

def on_button_click_install_apk():
    dV = subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n", " ").replace("\t", " ").split(" ")
    dList = list(dV)
    devicesModelList = dList[4::14]
    filePath = filedialog.askopenfilename()
    while "" in devicesModelList:
        devicesModelList.remove("")  # Remove blank
    for i in range(len(devicesModelList)):
        device = devicesModelList[i]
        strDevice = str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "install"+" "+filePath)
        except subprocess.CalledProcessError:
            print("install qqmusic ing.......")
        else:
            print("install "+filePath+" DONE")


def on_button_click_uninstall_qqmusic():
    dV = subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n", " ").replace("\t", " ").split(" ")
    dList = list(dV)
    devicesModelList = dList[4::14]
    while "" in devicesModelList:
        devicesModelList.remove("")  # Remove blank
    for i in range(len(devicesModelList)):
        device = devicesModelList[i]
        strDevice = str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "uninstall com.tencent.qqmusic")
        except subprocess.CalledProcessError:
            print("Please install com.tencent.qqmusic first")
        else:
            print("Uninstall com.tencent.qqmusic ALL DONE!")

#button监听事件:karaoke
def on_button_click_uninstall_karaoke():
    dV = subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n", " ").replace("\t", " ").split(" ")
    dList = list(dV)
    devicesModelList = dList[4::14]
    while "" in devicesModelList:
        devicesModelList.remove("")  # Remove blank
    for i in range(len(devicesModelList)):
        device = devicesModelList[i]
        strDevice = str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "uninstall com.tencent.karaoke")
        except subprocess.CalledProcessError:
            print("Please install com.tencent.karaoke first")
        else:
            print("Uninstall com.tencent.karaoke ALL DONE!")

def on_button_click_start_karaoke():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesList=dList[4::14]
    while "" in devicesList:
        devicesList.remove("") #Remove blank
    for i in range(len(devicesList)):
        device=devicesList[i]
        strDevice=str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell am start com.tencent.karaoke/com.tencent.karaoke.module.splash.ui.SplashBaseActivity")
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell input keyevent 82")
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell input keyevent 82")
            time.sleep(1)
            subprocess.check_output("adb -s"+" "+strDevice+" "+"shell input text 78542435")
            time.sleep(0.5)
            subprocess.check_output("adb -s "+" "+strDevice+" "+"shell input keyevent 66")
        except subprocess.CalledProcessError:
            print("Please install com.tencent.karaoke first")
            print("********************************")
        else:
            print("Done")
            print("********************************")

def on_button_click_start_qqmusic():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesList=dList[4::14]
    while "" in devicesList:
        devicesList.remove("") #Remove blank
    for i in range(len(devicesList)):
        device=devicesList[i]
        strDevice=str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell am start com.tencent.qqmusic/.activity.AppStarterActivity")
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell input keyevent 82")
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell input keyevent 82")
            time.sleep(1)
            subprocess.check_output("adb -s"+" "+strDevice+" "+"shell input text 78542435")
            time.sleep(0.5)
            subprocess.check_output("adb -s "+" "+strDevice+" "+"shell input keyevent 66")
        except subprocess.CalledProcessError:
            print("Please install com.tencent.qqmusic first")
            print("********************************")
        else:
            print("Done")
            print("********************************")

def on_button_click_stop_qqmusic():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesList=dList[4::14]
    while "" in devicesList:
        devicesList.remove("") #Remove blank
    for i in range(len(devicesList)):
        device=devicesList[i]
        strDevice=str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell am force-stop com.tencent.qqmusic")
            #time.sleep(0.5)
            #subprocess.check_output("adb -s"+" "+strDevice+" "+"shell input keyevent 26") #休眠手机
        except subprocess.CalledProcessError:
            print("Please install com.tencent.karaoke first")
        else:
            print("Done")

def on_button_click_stop_karaoke():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesList=dList[4::14]
    while "" in devicesList:
        devicesList.remove("") #Remove blank
    for i in range(len(devicesList)):
        device=devicesList[i]
        strDevice=str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell am force-stop com.tencent.karaoke")
            #time.sleep(0.5)
            #subprocess.check_output("adb -s"+" "+strDevice+" "+"shell input keyevent 26") #休眠手机
        except subprocess.CalledProcessError:
            print("Please install com.tencent.karaoke first")
        else:
            print("Done")

def on_button_click_restart_adb():
    killServer=subprocess.check_output("adb kill-server")
    time.sleep(2)
    startServer=subprocess.check_output("adb start-server")
    print(str(killServer,'utf-8'))
    print(type(startServer))
    print("RESTART FINISH")



button1=tkinter.Button(root,text="Uninstall com.tencent.qqmusic")
button1.bind("<Button-1>",lambda event:on_button_click_uninstall_qqmusic()) #<Button-1>,鼠标左键点击事件
button1.grid(row=0,column=0,padx=10,pady=10)

button2=tkinter.Button(root,text="Uninstall com.tencent.karaoke")
button2.bind("<Button-1>",lambda event:on_button_click_uninstall_karaoke()) #<Button-1>,鼠标左键点击事件
button2.grid(row=1,column=0,padx=10,pady=10)

button3=tkinter.Button(root,text="START QQMUSIC")
button3.bind("<Button-1>",lambda event:on_button_click_start_qqmusic())
button3.grid(row=0,column=1,padx=10,pady=10)

button4=tkinter.Button(root,text="START KARAOKE")
button4.bind("<Button-1>",lambda event:on_button_click_start_karaoke())
button4.grid(row=1,column=1,padx=10,pady=10)

button5=tkinter.Button(root,text="STOP QQMUSIC")
button5.bind("<Button-1>",lambda event:on_button_click_stop_qqmusic())
button5.grid(row=0,column=2,padx=10,pady=10)

button6=tkinter.Button(root,text="STOP KARAOKE")
button6.bind("<Button-1>",lambda event:on_button_click_stop_karaoke())
button6.grid(row=1,column=2,padx=10,pady=10)

button7=tkinter.Button(root,text="RESTART ADB")
button7.bind("<Button-1>",lambda event:on_button_click_restart_adb())
button7.grid(row=1,column=3,padx=10,pady=10)

button8=tkinter.Button(root,text="INSTALL APK")
button8.bind("<Button-1>",lambda event:on_button_click_install_apk())
button8.grid(row=0,column=3,padx=10,pady=10)

button9=tkinter.Button(root,text="COPY FILES TO COMPUTER")
button9.grid(row=2,column=0,padx=10,pady=10)

root.mainloop()