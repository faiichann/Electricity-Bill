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

class Electrical_dict:
    def __init__(self, name, typeDict):
        self.name = name
        self.typeDict = typeDict

    def __repr__(self):
        return str(self.name)

    def printTypeList(self) :
        for index, elec in enumerate(self.typeDict) :
            print(f"({index}) {elec}")
        print("(cancel) to stop")


class Electrical:
    def __init__(self, name, watt):
        self.name = name
        self.watt = watt

    def __repr__(self):
        return str(self.name)

    def getWatt(self):
        print(f"{self.name} has {self.watt} watts!")
        print('------------------------------------------------------')
        return self.watt

electrical_list = [
    Electrical_dict("Light bulb", [
        Electrical("incandescent", 60),
        Electrical("fluorescent", 13),
        Electrical("small neon", 17),
        Electrical("short neon", 28),
        Electrical("long neon", 46)
    ]),
    Electrical_dict("Fan", [
        Electrical("small", 45),
        Electrical("medium", 60),
        Electrical("large", 75)
    ]),
    Electrical_dict("Rice Cooker", [
        Electrical("0.5L", 300),
        Electrical("1L", 450),
        Electrical("1.5L", 520),
        Electrical("2.5L", 1100),
        Electrical("4L", 1400)
    ]),
    Electrical_dict("TV", [
        Electrical("14 inch", 60),
        Electrical("21 inch", 110),
        Electrical("30 inch", 200)
    ]),
    Electrical_dict("Iron", [
        Electrical("normal", 1000),
        Electrical("steam", 1700),
    ]),
    Electrical_dict("Air Condition", [
        Electrical("12000 BTU", 1000),
        Electrical("18000 BTU", 2000),
        Electrical("24000 BTU", 2500),
    ]),
    Electrical("hot pot", 3500),
    Electrical("refrigerator", 100),
    Electrical("water heater", 3500),
    Electrical("washing machine", 1000),
    Electrical("toaster", 850),
    Electrical("computer", 300),
    Electrical("DVD player", 40),
    Electrical("vacuum", 800),
    Electrical("microwave", 1000),
    Electrical("air fryer", 1200),
    Electrical("electric pan", 1000)
]

def print_Electrical_List() :
    for index, elec in enumerate(electrical_list) :
        print(f"({index}) {elec}")
    print("(cancel) to cancel all bill")
    print("(cal) to calculate all bill")

def inputOk(inputt) :
    try :
        int(inputt)
        return True
    except :
        return True if inputt == "cancel" or inputt == "cal" else False

def topicPrint(msg) :
    print('------------------------------------')
    print('************************************')
    print(msg)
    print('************************************')
    print('------------------------------------')

def inputTopicPrint(msg) :
    print('------------------------------------')
    print('************************************')
    keyboardInput = input(msg).lower()
    print('************************************')
    print('------------------------------------')
    return keyboardInput

def printBill(pay) :
    print('------------------------------------------------------')
    print("Electricity bill pay :[ %.2f ]" %pay ," Bath.")
    print('------------------------------------------------------')

def calc_Bill(totalUnit):
        if(totalUnit>0 and totalUnit<=15):
            pay = totalUnit*2.3488
            printBill(pay)
      
        elif(totalUnit>15 and totalUnit<=25):
            pay = (15*2.3488)+(totalUnit-15)*2.9882
            printBill(pay)
      
        elif(totalUnit>25 and totalUnit<=35):
            pay = (15*2.3488)+((25-15)*2.9882)+(totalUnit-25)*3.2405
            printBill(pay)

        elif(totalUnit>35 and totalUnit<=100):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+(totalUnit-35)*3.6237
            printBill(pay)

        elif(totalUnit>100 and totalUnit<=150):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+(totalUnit-100)*3.7171
            printBill(pay)

        elif(totalUnit>150 and totalUnit<=400):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+((150-100)*3.7171)+(totalUnit-150)*4.2218
            printBill(pay)
     
        elif(totalUnit>400):
            pay =(15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+((150-100)*3.7171)+(totalUnit-400)*4.4217
            printBill(pay)
       
        else:
            printBill(0)

while True  :
    selected = inputTopicPrint('SELECT MENU FROM FOLLOWING OPTIONS: \nChoose Electrical appliances_______(E)  \nQuit_______________________________(Q) \n: ')
    valid_selected = ['e','q']
    if selected == 'e':
        Elec = "temp"
        while Elec != "cancel":
            print('SELECT ELECTRICAL FROM FOLLOWING OPTIONS:\n')
            print_Electrical_List()
        
            Elec = inputTopicPrint("id : ")

            while not inputOk(Elec) :
                print('Valid input!')
                Elec = input("id : ")

            if Elec == "cancel" or  Elec == "cal":
                break

            Elec = int(Elec)
            if Elec < len(electrical_list) and Elec >= 0:
                electrical = electrical_list[Elec]
                watt = 0
                if type(electrical) is Electrical_dict :
                    print('SELECT ELECTRICAL TYPE FROM FOLLOWING OPTIONS:\n')

                    electrical.printTypeList()
                    selectedType = inputTopicPrint("id : ")

                    while not inputOk(selectedType) :
                        print('Valid input!')
                        selectedType = input("id : ")

                    if selectedType == "cancel" :
                        continue

                    selectedType = int(selectedType)
                    typeList = electrical.typeDict

                    while selectedType >= len(typeList) and selectedType < 0 :
                        print("This number does not match any Electrical!")
                        selectedType = int(input("id : "))

                    watt = typeList[selectedType].getWatt()

                elif type(electrical) is Electrical :
                    watt = electrical.getWatt()

                else :
                    print("This element is not a Electrical!")
                    continue

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
                    continue

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
                continue
        
        if Elec == 'cal':
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