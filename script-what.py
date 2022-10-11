import pywhatkit
from datetime import datetime
#print(today)
fecha_actual = datetime.today()
fecha_hora_str = fecha_actual.strftime('%y/%m/%d')
hoy= datetime.now().strftime('%Y-%m-%d')
#navidad
navidad = datetime.strptime("2022-12-25", "%Y-%m-%d")
restanteNavidad=navidad-fecha_actual
#anio nuevo
anioNuevo = datetime.strptime("2022-12-31", "%Y-%m-%d")
restanteAnioNuevo=anioNuevo-fecha_actual
#Viaje
viaje = datetime.strptime("2023-03-02", "%Y-%m-%d")
restanteviaje=viaje-fecha_actual
#creamos lista con los numeros a enviar el mensaje
listaNumeros=["+54xxxxxxxxxx","+54xxxxxxxxxx"]

#aca esta el mensaje definitivo dentro de un string
mensaje='---Faltan---\n-\t{} dias para navidad\n-\t{} dias para anionuevo\n-\t{} dias para el viaje'.format(restanteNavidad.days, restanteAnioNuevo.days,restanteviaje.days)
print(mensaje)
#creamos bucle for para que envie ambos mensajes 

for i in range(2):
    pywhatkit.sendwhatmsg_instantly(listaNumeros[i], mensaje, 10)
    print('mensaje enviado a {}'.format(listaNumeros[i]))

