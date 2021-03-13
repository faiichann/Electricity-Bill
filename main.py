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
            print("\nElectricity bill pay : %.2f [" %pay ,"] Bath.");
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


# //Electricity Bill Program
# m = int(input("Enter current meter number: "))
# bill = 0.0
# if( m == 1234):
# print("1-Agricultural")
# print("2-Residential")
# print("3-Commercial")
# c = int ( input ( "Choose Category: " ))
# if (c == 1):
# s = 20;
# u = int(input("Enter number of units consumed: "))
# if (u > 0 and u < 50):
# bill = (u * 0.25) + s;
# elif ( u > = 50 and u < 150):
# bill = (u * 0.55) + s
# elif (u >= 150 and u < 300):
# bill = (u * 0.80) + s
# elif (u >= 300 and u <500):
# bill = (u * 1) + s
# elif (u >= 500 and u<1000 ):
# bill = (u * 2) + s
# else:
# print("Invalid Units")
# print("Current meter number: ",m)
# print("Number of units consumed: ",u)
# print("Selected Category: ",c)
# print("Your bill amount: %.2f"%bill)
# elif (c == 2):
# s = 35;
# u = int(input("Enter number of units consumed: "))
# if (u > 0 and u < 50):
# bill = (u * 1.35) + s;
# elif (u >= 50 and u < 150):
# bill = (u * 2.15) + s
# elif (u >= 150 and u < 300):
# bill = (u * 3) + s
# elif (u >= 300 and u < 500):
# bill = (u * 3.5) + s
# elif (u >= 500 and u<1000):
# bill = (u * 6) + s
# else:
# print("Invalid Units")
# print("Current meter number: ", m)
# print("Number of units consumed: ", u)
# print("Selected Category: ", c
# print("Your bill amount: %.2f" % bill)
# elif(c== 3):
# s = 65;
# u = int(input("Enter number of units consumed: "))
# if (u > 0 and u < 50):
# bill = (u * 3) + s;
# elif (u >= 50 and u < 150):
# bill = (u * 4.5) + s
# elif (u >= 150 and u < 300):
# bill = (u * 5.5) + s
# elif (u >= 300 and u <500):
# bill = (u * 6.8) + s
# elif (u >= 500 and u<1000 ):
# bill = (u * 9) + s
# else:
# print("invalid Units")
# print("Current meter number: ", m)
# print("Number of units consumed: ", u)
# print("Selected Category: ", c)
# print("Your bill amount: %.2f" % bill)
# else:
# print("Wrong choice")
# else:
# print("Wrong pin number")

# units=int(input("Number of unit consumed: "))

# def calc_Bill(units): #function definition

#     if(units>0 and units<=100):
#         print("Electricity bill pay%.2f: " %units*1.5)
      
#     elif(units>100 and units<=200):
#         print("Electricity bill pay=%.2f: " %(100*1.5)+(units-100)*2.5)
      
#     elif(units>200 and units<=300):
#        print("Electricity bill pay%.2f: " %(100*1.5)+(200-100)*2.5+(units-200)*4)
     
#     elif(units>300):
#         print("Electricity bill pay%.2f: " %2500);#fixed rate
       
#     else:
#         print(0);

# calc_Bill(units) #call the function with argument

#program for calculating electricity bill in Python
# units=int(input("Number of unit consumed: "))
# if(units>0 and units<=100):
#     payAmount=units*1.5
#     fixedcharge=25.00
# elif(units>100 and units<=200):
#     payAmount=(100*1.5)+(units-100)*2.5
#     fixedcharge=50.00
# elif(units>200 and units<=300):
#     payAmount=(100*1.5)+(200-100)*2.5+(units-200)*4
#     fixedcharge=50.00
# elif(units>300):
#     payAmount=2500;#fixed rate
#     fixedcharge=75.00
# else:
#     payAmount=0;
    
# Total= payAmount+fixedcharge
# print("\nElectricity bill pay : %.2f: " %Total);