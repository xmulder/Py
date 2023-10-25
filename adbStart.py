import subprocess
import time


def adbDevices():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesList=dList[15::14]
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

if __name__=='__main__':
    adbDevices()