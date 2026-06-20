#Ejercicio 2

num = 10

def sum_10_to():
    num += 10

def sum_10_to_global():
    global num
    num += 10

#sum_10_to() #-> cannot access local variable 'num' where it is not associated with a value
sum_10_to_global() #-> work perfectly because we specify the use of the global variable 
print(num) #-> 20


# Ejercicio 1

def try_to_get_the_variable():
    variable = "I'm trying to get this"

#print(variable) 