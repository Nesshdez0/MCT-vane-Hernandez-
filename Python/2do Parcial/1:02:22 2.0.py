import datetime

dia= datetime.date.today()

print(dia)

w=dia.weekday()+1

if (w==0):
  print("feliz domingo")

elif (w==2):
  print("yay es martes")

else:
  print("yahoo, es sabado")

if (w==0):
  print('feliz lunes')

elif (w==3):
  print("yay es jueves")

else:
  print("wuhu, ya casi es miercoles")

if (w==0):
  print("se aproxima viernes")