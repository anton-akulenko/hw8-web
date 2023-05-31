from connect import *
import time

from faker import Faker

from models import Contact


fake = Faker('uk-UA')
CONTACTS_NUMBER = 20


channel = connection_Rabbit.channel()
# Clean queue from data
# channel.queue_delete(queue='for_mail')
channel.queue_declare(queue='for_mail', durable=True)

def fill_db(CONTACTS_NUMBER):
    for _ in range(CONTACTS_NUMBER):
        contact = Contact(fullname=fake.name(), email=fake.email())
        contact.save()

def main():
    contacts = Contact.objects()
    for contact in contacts:
        message = str(contact.id).encode()
        channel.basic_publish(
            exchange='',
            routing_key='for_mail',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(f"Contact email: {contact.email} for contact {contact.fullname} was added to queue")
        # time.sleep(3)
    connection_Rabbit.close()


if __name__ == '__main__':
    # fill_db(CONTACTS_NUMBER)
    main()



