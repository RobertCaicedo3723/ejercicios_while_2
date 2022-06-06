print("-------------------------------------------------------")
print("--------Calcular la rata de una población--------------")
print("-------------------------------------------------------")



#Procesing


a = 3.5 
b = 5.0
n = 1980  

while a<b:
    a = a+0.07*a 
    b = b+0.05*b 
    n = n+1 

#Output 

print("El crecimiento de la rata A es mayor que la rata B en el año: " + str(n))



