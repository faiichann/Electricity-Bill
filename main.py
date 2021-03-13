#Program Electricity Bill with python
import string
import os
import math

totalWatt = 0
totalUnit = 0 
pay = 0
day = 30
week = 4
month = 1

bulb = {
    "name": "Light bulb",
    "type": {
        "incandescent": 60,
        "fluorescent": 13,
        "small neon": 17,
        "short neon": 28,
        "long neon": 46,
    }
}

fan = {
    "name": "Fan",
    "type": {
        "small": 45,
        "medium": 60,
        "large": 75
    }
}

riceCooker = {
    "name": "riceCooker",
    "type": {
        "0.5L": 300,
        "1L": 450,
        "1.5L": 520,
        "2.5L": 1100,
        "4L": 1400
    }
}

TV = {
    "name": "TV",
    "type": {
        "14 inch": 60,
        "21 inch": 110,
        "30 inch": 200
    }
}

iron = {
    "name": "iron",
    "type": {
        "normal": 1000,
        "steam": 1700
    }
}

airCondition = {
    "name": "airCondition",
    "type": {
        "12000 BTU": 1000,
        "18000 BTU": 2000,
        "24000 BTU": 2500
    }
}

other = {
    "name": "Other",
    "type": {
        "hot pot": 3500,
        "refrigerator": 100,
        "water heater": 3500,
        "washing machine": 1000,
        "toaster": 850,
        "computer": 300,
        "DVD player": 40,
        "vacuum": 800,
        "microwave": 1000,
        "air fryer": 1200,
        "electric pan": 1000
    }
}

electrical_list = [bulb, fan, riceCooker, TV, iron, airCondition, other]

def printElectrical_list() :
    index = 0
    for e1 in electrical_list :
        if e1 is not None :
            if e1.get("name") is not "Other" :
                print("(" + str(index) + ") " + e1.get("name"))
            else :
                for e2 in e1.get("type").keys() :
                    print("(" + str(index) + ") " + e2)
                    index+=1
        index += 1

def getWattFunc (selector) :
    dataDict = electrical_list[int(selector)]
    print("Please select your electrical type")
    index = 0
    for e in dataDict.get("type").keys() :
        print("("+ str(index) + ") " + e)
        index+=1
    type_list = dataDict.get("type")
    selectType = int(input("electrical type : "))
    if selectType < len(type_list.keys()) and selectType >= 0:
        return type_list[list(type_list.keys())[selectType]]
    else :
        return "type error!"

def calc_Bill(totalUnit):
        if(totalUnit>0 and totalUnit<=15):
            pay = totalUnit*2.3488
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
      
        elif(totalUnit>15 and totalUnit<=25):
            pay = (15*2.3488)+(totalUnit-15)*2.9882
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
      
        elif(totalUnit>25 and totalUnit<=35):
            pay = (15*2.3488)+((25-15)*2.9882)+(totalUnit-25)*3.2405
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

        elif(totalUnit>35 and totalUnit<=100):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+(totalUnit-35)*3.6237
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

        elif(totalUnit>100 and totalUnit<=150):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+(totalUnit-100)*3.7171
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

        elif(totalUnit>150 and totalUnit<=400):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+((150-100)*3.7171)+(totalUnit-150)*4.2218
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
     
        elif(totalUnit>400):
            pay =(15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+((150-100)*3.7171)+(totalUnit-400)*4.4217
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
       
        else:
            print('------------------------------------------------------')
            print("Electricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

while True  :
    print('------------------------------------')
    print('************************************')
    selected = input('SELECT MENU FROM FOLLOWING OPTIONS: \nChoose Electrical appliances_______(E)  \nQuit_______________________________(Q) \n: ').lower()
    print('************************************')
    print('------------------------------------')
    print()
    valid_selected = ['e','q']
    selected = selected.lower()
    if selected == 'e':
        print('------------------------------------')
        print('************************************')
        print('SELECT ELECTRICAL FROM FOLLOWING OPTIONS:\n')
        printElectrical_list()
        Elec = int(input())
        print('************************************')
        print('------------------------------------')
        print()
        # valid_Elec = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','stop']
        # Elec = Elec.lower()

        while Elec != 'stop':
            if Elec < len(electrical_list) and Elec >= 0:
                watt = getWattFunc(Elec)
                while type(watt) == str :
                    watt = getWattFunc(Elec)
                print(str(watt) + " watt")
                time = int(input('Enter Amount of time spent : '))
                freq = input('Select Frequency used by following : \n(1).Day \n(2).Week \n(3).month \n:')
                if freq == '1':
                    allTime = time * day
                elif freq == '2':
                    allTime = time * week
                elif freq == '3':
                    allTime = time * month
                else:
                    print('TRY AGAIN !!!!')
                    print('------------------------------------') 
                    freq = input('Select Frequency used by following : \n(1).Day \n(2).Week \n(3).month')

                unit = (watt * allTime)*0.001
                print(unit)
                totalUnit += unit
            
                add = input('Add more electrical : \n(Y).Yes \n(N).No \n :').lower()
                print('************************************')
                if add == 'y':
                    print('************************************')
                    print('SELECT ELECTRICAL FROM FOLLOWING OPTIONS:\n')
                    printElectrical_list()
                    Elec = int(input())
                    print('************************************')
                elif add == 'n':
                    calc_Bill(totalUnit)
                    totalUnit = 0 
                    break
                else :
                    print('TRY AGAIN !!!!')
                    print('------------------------------------')
                    add = input('Add more electrical : \n(Y).Yes \n(N).No \n :').lower()
                    print('************************************')

            else :
                print('TRY AGAIN !!!!')
                print('------------------------------------')
                print('SELECT ELECTRICAL FROM FOLLOWING OPTIONS:\n')
                printElectrical_list()
                Elec = int(input())
                print('------------------------------------')
                print()
        
        if Elec == 'stop':
            calc_Bill(totalUnit)
            totalUnit = 0 

    elif selected == 'q':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')