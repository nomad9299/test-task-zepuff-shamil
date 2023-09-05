#!/usr/bin/env python
import pika, sys, os

# def main():
#     credentials = pika.PlainCredentials('guest', 'guest')
#     parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
#     #parameters = pika.ConnectionParameters('localhost',15672,'/',credentials)
#     connection = pika.BlockingConnection(parameters)
#     #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=15672,credentials=credentials,heartbeat=30))
#     channel = connection.channel()

#     channel.queue_declare(queue='hello')

#     def callback(ch, method, properties, body):
#         print(f" [x] Received {body}")

#     channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)

parameters = pika.URLParameters('amqp://guest:guest@localhost:15672/%2F')
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.basic_publish('test_exchange',
                      'test_routing_key',
                      'message body value',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))

connection.close()
