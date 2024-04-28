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
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "shell am force-stop com.tencent.qqmusic")
            time.sleep(0.5)
            subprocess.check_output("adb -s"+" "+strDevice+" "+"shell input keyevent 26")
        except subprocess.CalledProcessError:
            print("Please install com.tencent.karaoke first")
        else:
            print("Done")

if __name__=='__main__':
    adbDevices()