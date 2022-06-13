import random
#agregar el resto del abecedario

#volver el codigo infinite usando un while True
while True:
  base="abcde"
  passw=""
  base2="fghijklmnñopqrstuvwxyz"
#permite que el usuario seleccione la lomgitud de su password
x=int(input("pon la longitud de la password que quieras: "))
for passwords in range (x) :
  for i in range (15):
   passw=passw+random.choice(base)

print("password", passwords,passw)
passw=''
