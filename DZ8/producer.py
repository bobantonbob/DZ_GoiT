import pika
import json
from faker import Faker
from models import Contact

fake = Faker()

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги для SMS та email
channel.queue_declare(queue='sms_queue', durable=True)
channel.queue_declare(queue='email_queue', durable=True)

def generate_fake_contacts():
    fake_contacts = []
    for _ in range(5):  # Згенеруємо 5 контактів для прикладу
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
            phone_number=fake.phone_number()
        )
        contact.is_preferred_sms = fake.boolean()
        contact.is_preferred_email = fake.boolean()
        contact.save()
        fake_contacts.append(contact)
    return fake_contacts

def send_to_rabbitmq(contact, queue_name):
    message = {'contact_id': str(contact.id)}
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Зберігаємо повідомлення на диск
        )
    )

def main():
    fake_contacts = generate_fake_contacts()

    for contact in fake_contacts:
        if contact.is_preferred_sms:
            send_to_rabbitmq(contact, "sms_queue")
        if contact.is_preferred_email:
            send_to_rabbitmq(contact, "email_queue")

    print("Messages sent to the queues")

    # Закриття підключення
    connection.close()

if __name__ == '__main__':
    main()
