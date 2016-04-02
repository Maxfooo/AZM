'''
Created on Mar 30, 2016

@author: Max Ruiz
'''
from ResTempLUT import getTempDict
import serial
import time
import datetime

""" Thermistor Vars/ Constants"""

nominalTemp = 25 # Celsius
nominalRes = 10,000
r1 = 10,000
vdd = 3.3
sampleTime = 0.5
resTempLUT = getTempDict()

""" Pyserial Vars / Constants"""

comPort = 'COM4'
baud = 9600
tout = 1

""" Other Global Vars / Constants"""

fname = "TempData_{}".format(datetime.date.today()).replace("-", "_")

def findClosestTemp(resistance):
    if resistance == -1:
        return -1
    else:
        closestTemp = resTempLUT[min(resTempLUT, key=lambda x:abs(x-resistance))]
        return closestTemp

"""Serial connection and reading from Arduino/ChipKIT"""

# example reading:
# ser = serial.Serial(comPort, baud, timeout=tout, parity = serial.PARITY_NONE,
# stopbits = serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
# print(ser.readline()) # This will read a line in the serial port terminated by \n
# print(ser.read(4)) # This will read 4 bytes sent through the serial port

def readSerPort():
    ser = serial.Serial(comPort, baud, timeout=tout, parity = serial.PARITY_NONE,
                        stopbits = serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
    # Currently I am getting some garbage when reading serial data from
    # my arduino duemillinova, my solution would be to use a second
    # serial port on a better arduino and connect it via an RS232 to USB switch
    try:
        print("Try")
        val = ser.readline()
        print("Value: ", val)
        if val is None or val == '':
            time.sleep(sampleTime * 2)
            print("Value was none or ''")
            return -1, val
        else:
            time.sleep(sampleTime)
            return val, -1
    except:
        print("except")
        time.sleep(sampleTime * 2)
        print("Failed to read.")
        return -1, -1

def valToRes(val):
    if val == -1:
        return -1
    else:
        volt = val * vdd / 1024
        res = volt * r1 / (vdd - volt)
        return res

def writeTemp(t, temp):
    try:
        f = open(fname, 'a')
    except:
        f = open(fname, 'w')
    f.write("{},{}\n".format(str(t), str(temp)))
    f.close()

if __name__ == '__main__':
    sampleCount = 0
    while 1:
        val, val2 = readSerPort()
        print(val2, type(val2))
        res = valToRes(val)
        temp = findClosestTemp(res)
        timeStamp = sampleCount * sampleTime
        writeTemp(timeStamp, temp)
        sampleCount += 1
        print(timeStamp, temp, val2)


