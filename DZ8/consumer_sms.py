import pika
import json
from time import sleep
from models import Contact

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue='email_queue', durable=True)


def send_email_stub(contact_id):
    # Функція-заглушка для надсилання емейлу
    print(f"Sending email to contact with ID: {contact_id}")
    sleep(1)  # Imitate sending email

    # Отримання контакту та встановлення is_message_sent в True
    contact = Contact.objects.get(id=contact_id)
    contact.is_message_sent = True
    contact.save()


# Функція, яка викликається при отриманні повідомлення з черги
def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']

    # Виклик функції-заглушки
    send_email_stub(contact_id)

    print(f" [x] Received message for contact with ID: {contact_id}")


# Вказуємо функцію обробки повідомлень
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
