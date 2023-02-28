# chisla
# int - celye chisla 

4 = 5 
print (type(a))  #<class 'int'>

b = '5'

print (type(b))  #<class 'str'>

c = int('10')
print(type(c)) #<class 'int'>
#int('5a')
#value Error: invalid litersl for int ()with baser 10 '5a'

#float - chisla s plavaushei tochkoi (drobnye)

a = 10.5
print (type(a)) # <class 'float'>

b = float ('15.3') 
print (type(b)) # <class 'float'>

c = float (11)
print (c) # 11.0

print(0.1+0.1+0+0.1+0.1+0.1)
# 0.999999

#decimal - tochnoe drobnoe chislo 

# to use have to import
from decimal import Decimmal 
a=demical (0.1)#my uje peredali ne tochnoe chislo 

print (a+a+a+a+a+a)
# 1.000000555523443

b = decimal ('0.1')
print (b+b+b+b+b+b+b+b+b)

#1.0
#bin  binarn chislo 

a = bin- (10)
print (a) # '0b1010'

b= int (a,2)# - eto oznachaet chto my doljny zakinut v desyatichnuju sistemu 

print (b)#10

#complex  kompleksnye chisla (3i+5j-7k)
a = complex (10,3)
print (a)(10+3j)

# operacii kot my mojem delat 
5+7 # slojenie 
10-5# vychit 
2*6 # umnoj
10/#5delenie 2.0
10//5# celochislennoe delenie 2
5%2 # ostatok ot delenia 1
2**3#vozvedenie v stepen (8=2*2*2*2)
25**0.5 #nachojdenie kvadratnogo kornya ot chisla (5)

# luboe otrisatelnoe stanovitsya polojitelnym 
abs(-5)#5
abs(10)#10

# pow
# 1. vozvodit v stepen 
#2. nachodit ostatok ot delenia na chislo 3 

pow(2,3) # 8 = 2*2*2 =2**3
pow (2,3,4) # 0 =(2*2*2) % 4

# divmod (5.2)
print(res)#(2,1)
# 2 =5//2 celochislennoe delenie 
# 1= 5%2  ostatok ot delenia 

divmod (17, 3) #(5,2) vozvrash nazad 2 chisla (delenie  i ostatok)
#5 =17//3
#2= 17%3

#sqrt nahojdenie kvadratnogo kornya 
from math import sqrt
sqrt (25)#5 
sqrt(9)#3
sqrt(3) #1.7320580356346356

