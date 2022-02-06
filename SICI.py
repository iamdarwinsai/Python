# # Simple intrest

# # si=p*t*r/100

p=int(input("enter the principal amount :"))
t=int(input("enter the time :"))
r=int(input("enter the rate :"))
s_i=(p*t*r)/100
print(s_i)

# compund intrest
'''
amount=p*(1+r/100)**t
ci=amount - p

'''

p=int(input("Enter the value : "))
rate=float(input("Enter the value : "))
t=int(input("Enter the value : "))

amount=p*pow((1+rate/100),t)
ci=amount - p

print(ci)
