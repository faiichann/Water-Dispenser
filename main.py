#Program Water dispenser with python
import string
import os
import math

#defind
Sbottle = 0.33
Mbottle = 0.6
Lbottle = 1.5

#Selected Menu
while True:
    print('-------------------------------')
    print('*******************************')
    selectMenu = input('SELECT MENU FROM FOLLOWING OPTIONS: \nInput Money_______(M) \nInput Bottle______(B) \nInput Water_______(W) \nQuit______________(Q) \n: ').lower()
    print('*******************************')
    print('-------------------------------')
    print()
    valid_selectMenu = ['m', 'b', 'w' , 'q']
    selectMenu = selectMenu.lower()

    if selectMenu == 'm':
        money = int(input('Enter your Money(Bath): '))
        print('*******************************')
        print('-------------------------------')
        print()

        water = money
        small = (water//Sbottle) + (water%Sbottle > 0)
        meduim = (water//Mbottle) + (water%Mbottle > 0)
        large = (water//Lbottle) + (water%Lbottle > 0)

        print('You have ',money,' bath. \nYou can get ',water,' liter of water.' )
        print('************************')
        print('LIST TYPE OF BOTTLE : \nSmall size 0.33 L :  ',small,' Bottle \nMeduim size 0.6 L : ',meduim,' Bottle \nLarge size 1.5 L : ',large,' Bottle')
        print('************************')
        print()
        

        program = input('Are you sure to make a list? : \nConfirm____(1) \nCancle_____(0) \n')
        if program == '1':
            print('------------------------------------------------------------------')
            print('YOU HAVE TO PAY [',money, '] BATH. For [',water,'] liter of water.')
            print('------------------------------------------------------------------')
            print()

            pay = int(input('Input your payment : '))
            paid = money - pay 
            while paid > 0 :
                    print('You have the amount paid ',paid, 'Bath.')
                    pays = int(input('Input your payment : '))
                    print('*******************************')
                    paid = paid-pays

                    if paid == 0 :
                        print('SUCCESSFULL !!!!')
                        print('Thank you for using our service')
                        print('*******************************')
                        print('-------------------------------')
                        print()  
                        break

                    elif paid < 0 :
                        print('You get change :',math.fabs(paid),' Bath.')
                        print('*******************************')
                        print('SUCCESSFULL !!!!')
                        print('Thank you for using our service')
                        print('*******************************')
                        print('-------------------------------')
                        print()  
                        break      
            if pay == money :
                print('SUCCESSFULL !!!!')
                print('Thank you for using our service')
                print('*******************************')
                print('-------------------------------')
                print()
            
            elif pay > money :
                print('You get change :',math.fabs(paid),' Bath.')
                print('*******************************')
                print('SUCCESSFULL !!!!')
                print('Thank you for using our service')
                print('*******************************')
                print('-------------------------------')
                print()                

        elif program == '0':
            print('Thank you for using our service')
            print('*******************************')
            print('-------------------------------')
            print()
        else :
            print('Input was invalid')
            print('*******************************')
            print('-------------------------------')
            print()
    
    elif selectMenu == 'b':
        print('SELECT BOTTLE SIZE FROM FOLLOWING OPTIONS :')
        sizeSelect = input('Small Size 0.33 L. ______(S) \nMeduim Size 0.6 L. ______(M) \nLarge Size 1.5 L. ______(L) \nStop Choosing___________(OK)\n:').lower()
        print('*******************************')
        print('-------------------------------')
        print()
        valid_sizeSelect =['s','m','l','ok']
        sizeSelect = sizeSelect.lower()
        sAmount = 0
        mAmount = 0
        lAmount = 0

        while sizeSelect != 'ok':
                if sizeSelect == 's' :
                    print('YOU CHOOSE SMALL SIZE 0.33 L.')
                    sAmount = int(input('Enter Number of bottles :'))
                    print('---------------------------------')
                    print('Would you like to add more?')
                    sizeSelect = input('Small Size 0.33 L. ______(S) \nMeduim Size 0.6 L. ______(M) \nLarge Size 1.5 L. ______(L) \nStop Choosing___________(OK)\n:').lower()
                    print('---------------------------------')

                elif sizeSelect == 'm' :
                    print('YOU CHOOSE MEDUIM SIZE 0.6 L.')
                    mAmount = int(input('Enter Number of bottles :'))
                    print('---------------------------------')
                    print('Would you like to add more?')
                    sizeSelect = input('Small Size 0.33 L. ______(S) \nMeduim Size 0.6 L. ______(M) \nLarge Size 1.5 L. ______(L) \nStop Choosing___________(OK)\n:').lower()
                    print('---------------------------------')

                elif sizeSelect == 'l' :
                    print('YOU CHOOSE LARGE SIZE 1.5 L.')
                    lAmount = int(input('Enter Number of bottles :'))
                    print('---------------------------------')
                    print('Would you like to add more?')
                    sizeSelect = input('Small Size 0.33 L. ______(S) \nMeduim Size 0.6 L. ______(M) \nLarge Size 1.5 L. ______(L) \nStop Choosing___________(OK)\n:').lower()
                    print('---------------------------------')

                else :
                    print('TRY AGAIN !!!!')
                    print('---------------------------------')
                    sizeSelect = input('Small Size 0.33 L. ______(S) \nMeduim Size 0.6 L. ______(M) \nLarge Size 1.5 L. ______(L) \nStop Choosing___________(OK)\n:').lower()
                    print('---------------------------------')

        if sizeSelect == 'ok' :
            print()
            print('THIS IS ALL YOUR LIST SIZE OF BOTTLES :')
            print('Small Size 0.33 L. You enter[',sAmount,'] Bottle. \nMeduim Size 0.6 L. You enter[',mAmount,'] Bottle. \nLarge Size 1.5 L. You enter[',lAmount,'] Bottle.')
            print('---------------------------------')
            total = (Sbottle * sAmount) + (Mbottle * mAmount ) + (Lbottle * lAmount)
            money = math.ceil(total)
            print('The total amount of water [',total,'] Liter of water.')
            print('The total amount of money [',money,'] Bath.')
            print('*******************************************')
            print('-------------------------------------------')
            print()

        program = input('Are you sure to make a list? : \nConfirm____(1) \nCancle_____(0) \n')
        if program == '1':
            print('------------------------------------------------------------------')
            print('YOU HAVE TO PAY [',money, '] BATH. For [',total,'] liter of water.')
            print('------------------------------------------------------------------')
            print()

            pay = int(input('Input your payment : '))
            paid = money - pay 
            while paid > 0 :
                    print('You have the amount paid ',paid, 'Bath.')
                    pays = int(input('Input your payment : '))
                    print('*******************************')
                    paid = paid-pays

                    if paid == 0 :
                        print('SUCCESSFULL !!!!')
                        print('Thank you for using our service')
                        print('*******************************')
                        print('-------------------------------')
                        print()  
                        break

                    elif paid < 0 :
                        print('You get change :',math.fabs(paid),' Bath.')
                        print('*******************************')
                        print('SUCCESSFULL !!!!')
                        print('Thank you for using our service')
                        print('*******************************')
                        print('-------------------------------')
                        print()  
                        break      
            if pay == money :
                print('SUCCESSFULL !!!!')
                print('Thank you for using our service')
                print('*******************************')
                print('-------------------------------')
                print()
            
            elif pay > money :
                print('You get change :',math.fabs(paid),' Bath.')
                print('*******************************')
                print('SUCCESSFULL !!!!')
                print('Thank you for using our service')
                print('*******************************')
                print('-------------------------------')
                print()                

        elif program == '0':
            print('Thank you for using our service')
            print('*******************************')
            print('-------------------------------')
            print()
        else :
            print('Input was invalid')
            print('*******************************')
            print('-------------------------------')
            print()

    elif selectMenu == 'w':
        water = int(input('Enter amount of water (liter) : '))
        print('*************************************')
        print('-------------------------------------')
        print()

        money = water
        small = (water//Sbottle) + (water%Sbottle > 0)
        meduim = (water//Mbottle) + (water%Mbottle > 0)
        large = (water//Lbottle) + (water%Lbottle > 0)

        print('You have [',water,'] liter of water.')
        print('************************************')
        print('LIST TYPE OF BOTTLE : \nSmall size 0.33 L :  ',small,' Bottle \nMeduim size 0.6 L : ',meduim,' Bottle \nLarge size 1.5 L : ',large,' Bottle')
        print('******************************')
        print() 

        program = input('Are you sure to make a list? : \nConfirm____(1) \nCancle_____(0) \n')
        if program == '1':
            print('------------------------------------------------------------------')
            print('YOU HAVE TO PAY [',money, '] BATH. For [',water,'] liter of water.')
            print('------------------------------------------------------------------')
            print()

            pay = int(input('Input your payment : '))
            paid = money - pay 
            while paid > 0 :
                    print('You have the amount paid ',paid, 'Bath.')
                    pays = int(input('Input your payment : '))
                    print('*******************************')
                    paid = paid-pays

                    if paid == 0 :
                        print('SUCCESSFULL !!!!')
                        print('Thank you for using our service')
                        print('*******************************')
                        print('-------------------------------')
                        print()  
                        break

                    elif paid < 0 :
                        print('You get change :',math.fabs(paid),' Bath.')
                        print('*******************************')
                        print('SUCCESSFULL !!!!')
                        print('Thank you for using our service')
                        print('*******************************')
                        print('-------------------------------')
                        print()  
                        break      
            if pay == money :
                print('SUCCESSFULL !!!!')
                print('Thank you for using our service')
                print('*******************************')
                print('-------------------------------')
                print()
            
            elif pay > money :
                print('You get change :',math.fabs(paid),' Bath.')
                print('*******************************')
                print('SUCCESSFULL !!!!')
                print('Thank you for using our service')
                print('*******************************')
                print('-------------------------------')
                print()                

        elif program == '0':
            print('Thank you for using our service')
            print('*******************************')
            print('-------------------------------')
            print()
        else :
            print('Input was invalid')
            print('*******************************')
            print('-------------------------------')
            print()

    elif selectMenu == 'q':
        exit()

    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')