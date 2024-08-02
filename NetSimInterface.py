import numpy as np
import matplotlib.pyplot as plt
import socket
import struct
import pandas as pd

port = 12349
server_address = (socket.gethostbyname(socket.gethostname()), port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print("Connected to the server")
a=1
while a:
	data = client_socket.recv(128)
	if(data):
		#extract values from netsim. Here mention the type specifiers such as I for int, d for double,c for char.
		unpacked_data = struct.unpack(">dd", data) # here dd implies two double values are received.

		print(f"Received values are",unpacked_data[0],unpacked_data[1])# Received values from NetSim

		a= 5
		b=10

		packed_data = struct.pack(">dd", a,b)# pass the processed results back to NetSim

		bytes = client_socket.send(packed_data)
	else:
		print("\nClosing connection")
		a=0