import subprocess
import time


def adbDevices():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesList=dList[4::14]
    while "" in devicesList:
        devicesList.remove("") #Remove blank
    for i in range(len(devicesList)):
        device=devicesList[i]
        strDevice=str(device)
        print(strDevice)
        subprocess.check_output("adb -s" + " " + strDevice + " " + "shell screenrecord --verbose /sdcard/download/1.mp4")
        print("IF RECORD FINISH,PLEASE PRESS CTRL+C")


if __name__=='__main__':
    adbDevices()