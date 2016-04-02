'''
Created on Mar 30, 2016

@author: Max Ruiz
'''
# product: https://www.adafruit.com/products/372
# Table: https://www.adafruit.com/datasheets/103_3950_lookuptable.pdf




def getTempDict():
    resTempLUT = {}
    f = open("thermDataTable.txt", "r")
    for line in f:
        dataStr = line.split(" ")
        for i in range(1,len(dataStr)):
            if i % 2 == 1:
                resTempLUT[float(dataStr[i])*1000] = int(dataStr[i - 1])
            i += 1

    f.close()
    return resTempLUT

