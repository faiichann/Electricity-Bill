#Program Electricity Bill with python
import string
import os
import math

totalWatt = 0
u1 =25
u2 =30
u3 =10
u4 =5
u5 =1
totalUnit = 0 
pay = 0
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
        Elec = input('SELECT ELECTRICAL FROM FOLLOWING OPTIONS:\nLight bulb_____________(A)\nFan____________________(B)\nCeiling fan____________(C)\nRice cooker____________(D)\nTelevision_____________(E)\nIron___________________(F)\nHot pot________________(G)\nWater heater___________(H)\nRefrigerator___________(I)\nAir conditioner________(J)\nWashing machine________(K)\nToaster________________(L)\nComputer_______________(M)\nVideo Player___________(N)\nVacuum cleaner_________(O)\nMicrowave______________(P)\nOil free fryer_________(Q)\nElectric pan___________(R)\nStop choosing_______(STOP)\n:').lower()
        print('************************************')
        print('------------------------------------')
        print()
        valid_Elec = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','stop']
        Elec = Elec.lower()

        while Elec != 'stop':
            if Elec == 'a':
                print('A')
                print('A')

            elif Elec == 'b':
                print('B')
            else :
                print('TRY AGAIN !!!!')
                print('------------------------------------')
                Elec = input('SELECT ELECTRICAL FROM FOLLOWING OPTIONS:\nLight bulb_____________(A)\nFan____________________(B)\nCeiling fan____________(C)\nRice cooker____________(D)\nTelevision_____________(E)\nIron___________________(F)\nHot pot________________(G)\nWater heater___________(H)\nRefrigerator___________(I)\nAir conditioner________(J)\nWashing machine________(K)\nToaster________________(L)\nComputer_______________(M)\nVideo Player___________(N)\nVacuum cleaner_________(O)\nMicrowave______________(P)\nOil free fryer_________(Q)\nElectric pan___________(R)\nStop choosing_______(STOP)\n:').lower()
                print('------------------------------------')
                print()
        if Elec == 'stop':
            
            totalUnit = u1+u2+u3+u4+u5
            calc_Bill(totalUnit)
            
        else:
            print('------------------')
            print('******************')
            print('RESPONSE NOT VALID')
            print('******************')
            print('------------------')

    elif selected == 'q':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')

    def calc_Bill(totalUnit):
        if(totalUnit>0 and totalUnit<=15):
            pay = totalUnit*2.3488
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
      
        elif(totalUnit>15 and totalUnit<=25):
            pay = (15*2.3488)+(totalUnit-15)*2.9882
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
      
        elif(totalUnit>25 and totalUnit<=35):
            pay = (15*2.3488)+((25-15)*2.9882)+(totalUnit-25)*3.2405
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

        elif(totalUnit>35 and totalUnit<=100):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+(totalUnit-35)*3.6237
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

        elif(totalUnit>100 and totalUnit<=150):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+(totalUnit-100)*3.7171
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')

        elif(totalUnit>150 and totalUnit<=400):
            pay = (15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+((150-100)*3.7171)+(totalUnit-150)*4.2218
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
     
        elif(totalUnit>400):
            pay =(15*2.3488)+((25-15)*2.9882)+((35-25)*3.2405)+((100-35)*3.6237)+((150-100)*3.7171)+(totalUnit-400)*4.4217
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
       
        else:
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')