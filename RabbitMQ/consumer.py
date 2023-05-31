import time

from connect import *

from models import Contact

def send_email(status, message_id):
    time.sleep(1)
    print(f"Contact id {message_id} has status {status}")

def main():
    channel = connection_Rabbit.channel()

    channel.queue_declare(queue='for_mail', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        object_id = body.decode()
        contact = Contact.objects(id=object_id)[0]
        status = contact.status
        message_id = contact.id

        print(f" [x] Received task for sending e-mail for {contact.fullname} with e-mail: {contact.email}")
        send_email(status, message_id)
        contact.status = True
        contact.save()
        print(f" [x] Done: {method.delivery_tag}")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='for_mail', on_message_callback=callback)
    channel.start_consuming()

if __name__ == "__main__":
    main()
