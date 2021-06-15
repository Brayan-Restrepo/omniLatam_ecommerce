# pylint: disable=C0111
'''
Archivo para el envio de Email para la gestion de
'''
# -- coding: utf-8 --
from django.core.mail import EmailMessage
from rest_framework.exceptions import ValidationError
   
def send_mail(subject, user, to_email):
    try:
        mail_body = f'''<body style='font-family:Tahoma; font-size:13px;'>
            Buen día,<br><br>
            <br><strong>Señor:</strong> {user.first_name} {user.last_name}
            <br><br><p>Tu compra ha sido completada, tu pedido llegará muy pronto</p>
            <br><br><em>Este correo es generado automáticamente, por favor no responder.</em>
            <br><br><strong"OmniLatam</strong>'''
        email = EmailMessage(subject, mail_body, to=[to_email], from_email= 'pruebaomnilatam@gmail.com',)
        email.content_subtype = 'html'
        return email.send()
    except Exception as error:
        raise ValidationError(error)

