# 2 types of conversion Implicit(automatic), Explicit(forece)

#implicit
joey=99
chandler=float(joey)
print(type(chandler))

#explicit
a=99.11
b=int(a)
print(b)

'''if we want to convert a list into string

a=['joey','is','foodie']
s=' '.join(map(str,a))
print(s)
'''


# we cant change str to int or float
