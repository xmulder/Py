import subprocess

def adbDevices():
    dV=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").replace("\t"," ").split(" ")
    dList=list(dV)
    devicesModelList=dList[15::14]
    while "" in devicesModelList:
        devicesModelList.remove("") #Remove blank
    for i in range(len(devicesModelList)):
        device=devicesModelList[i]
        strDevice=str(device)
        print(strDevice)
        try:
            subprocess.check_output("adb -s" + " " + strDevice + " " + "uninstall com.tencent.karaoke")
        except subprocess.CalledProcessError:
            print("Please install com.tencent.karaoke first")
        else:
            print("Uninstall com.tencent.karaoke ALL DONE!")

if __name__=='__main__':
    adbDevices()