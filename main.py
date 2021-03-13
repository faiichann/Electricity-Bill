#Program Electricity Bill with python
import string
import os
import math

totalWatt = 0
unit = 0 
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
            print('------------------------------------------------------')
            print("\nElectricity bill pay :[ %.2f ]" %pay ," Bath.");
            print('------------------------------------------------------')
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

