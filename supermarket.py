enter=str(input("Press Enter to continue :"))

print('''


                ----BILL GENRATOR----


''')
cname=str(input("Enter your name : \n"))
cadd=str(input("Enter your Address : \n"))
cphone=int(input("Enter your Phone No : \n"))
dict={}
k=0


print('''

     OPTIONS

    1.BUY ITEM
    2.EXIT  

''')
options=int(input("Enter your options : \n"))

while True:   
    if options == 1:
        print('''

    GROCERY LISTS :

    S.NO                PRODUCT              QUANTITY             PRICE
    1.                  MILK                   1L                 250 
    2.                  CORN FLAKES            1KG                130   
    3.                  WHEAT                  1KG                100                   
    4.                  TEA POWDER             1KG                150  
    5.                  COFFE POWDER           1KG                500
    
    CLICK THE OPTIONS:
    1.ADD PRODUCT
    2.CART LIST
    3.GENERATE BILL
    ''')
    
        a=int(input("Enter Your Options : \n"))
        
        if a == 1:
            while True:
                product=str(input("Enter the  product name you want to add :\n"))
                quantity=int(input("Enter the quantity : \n"))
                price=int(input("Enter the price of the product: \n"))
                k =k+1
                dict[k]=[product,quantity,price]
                print('''
                            1.Add Product
                            2.Main Menu
                    
                    
                ''')
                q=int(input("Enter your options"))
                if q == 2:
                    break
                   
                
                            

        elif a ==2:
            while True:
                print(dict)
                break
            
        elif a ==3:
            print(cname)
            print(cadd)
            print(cphone)
            print('''
            
            
            --------------------BILL--------------------
            
            ''')
            print("{:10}{:10}{:10}".format('NAME','QUANTITY','PRICE'))
            for j in dict.values():
                product,quantity,price=j
                print("{:10}{:10}{:10}".format(j[0],j[1],j[2]))   
            break
        elif a > 3:
            print("Enter right Option")
            break

    

    elif options == 2 :
        print('''
    

    -----THANKYOU VISIT AGAIN-----

    
    ''')
        break

    else :
        print("INVALID OPTION ENTERED")