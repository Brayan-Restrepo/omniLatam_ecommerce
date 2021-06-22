# pylint: disable=C0111
'''
Archivo para el envio de Email
'''
import asyncio
import time
loop = asyncio.get_event_loop()

# -- coding: utf-8 --
from django.core.mail import EmailMessage
from rest_framework.exceptions import ValidationError


def async_send_mail(subject, user, to_email):
    #   arguments = []
  print('init run_in_executor')
  loop.run_in_executor(None, send_mail, subject, user, to_email)
  print('fin run_in_executor')
  
def send_mail(subject, user, to_email):
    try:
        time.sleep(15)
        print('Enviando........')
        mail_body = f'''<body style='font-family:Tahoma; font-size:13px;'>
            Buen día,<br><br>
            <br><strong>Señor:</strong> {user.first_name} {user.last_name}
            <br><br><p>Tu compra ha sido completada, tu pedido llegará muy pronto</p>
            <br><br><em>Este correo es generado automáticamente, por favor no responder.</em>
            <br><br><strong"OmniLatam</strong>'''
        email = EmailMessage(subject, mail_body, to=[to_email], from_email= 'pruebaomnilatam@gmail.com',)
        email.content_subtype = 'html'
        email.send()
        print('Fin........')
    except Exception as error:
        raise ValidationError(error)

