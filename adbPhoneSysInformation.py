import subprocess

def adbDevices():

    dModel=subprocess.check_output("adb devices -l").decode('UTF-8').replace("\r\n"," ").split(" ")
    dModelList=dModel[15::14]
    dSerialList=dModel[4::14]
    for i,j in zip(dModelList,dSerialList):
        devicesM=i
        devicesS = j
        print(devicesM+"\n"+"SerialNo:"+devicesS)
        strScreen = subprocess.check_output("adb -s" + " " + devicesS + " " + "shell wm size").decode('UTF-8').replace(
            "\r\n", " ")
        print(strScreen)
        print("++++++++++++++++++++++++++++")


if __name__=='__main__':
    adbDevices()