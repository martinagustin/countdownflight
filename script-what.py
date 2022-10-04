#import pywhatkit
import time
from datetime import datetime
today = datetime.today()
#print(today)
fecha_hora_str = today.strftime('%d/%m/%Y %H:%M')
actual="enviado: "+fecha_hora_str
print(actual)
# Send a WhatsApp Message to a Contact at 1:30 PM
#pywhatkit.sendwhatmsg_instantly("+543487662839", "Hola")
#pywhatkit.sendwhatmsg_instantly("+543487347519", "hello", 5, False)
#pywhatkit.sendwhatmsg("+3487347519", "Enviado desde python a las ", 13, 30)
