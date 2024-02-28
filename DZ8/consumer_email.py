import pika
import json
import logging
from smtplib import SMTPException
from time import sleep
from models import Contact

logging.basicConfig(level=logging.INFO)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги для SMS
channel.queue_declare(queue='sms_queue', durable=True)

def send_sms_stub(contact_id):
    try:
        # Функція-заглушка для надсилання SMS
        logging.info(f"Sending SMS to contact with ID: {contact_id}")
        sleep(1)  # Imitate sending SMS

        # Отримання контакту та встановлення is_message_sent в True
        contact = Contact.objects.get(id=contact_id)
        contact.is_message_sent = True
        contact.save()

    except Exception as e:
        logging.error(f"Error sending SMS to contact with ID {contact_id}: {e}")

# Функція, яка викликається при отриманні повідомлення з черги SMS
def callback_sms(ch, method, properties, body):
    try:
        message = json.loads(body)
        contact_id = message['contact_id']

        # Виклик функції-заглушки для SMS
        send_sms_stub(contact_id)

        logging.info(f" [x] Received SMS for contact with ID: {contact_id}")

    except Exception as e:
        logging.error(f"Error processing SMS message: {e}")

# Вказуємо функцію обробки повідомлень для SMS
channel.basic_consume(queue='sms_queue', on_message_callback=callback_sms, auto_ack=True)

logging.info(' [*] Waiting for SMS messages. To exit press CTRL+C')
channel.start_consuming()
