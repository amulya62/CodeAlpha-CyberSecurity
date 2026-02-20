import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and port
server.bind(("localhost", 9999))

# Listen for connection
server.listen(1)
print("Server is waiting for connection...")

# Accept client
client_socket, addr = server.accept()
print("Connected to:", addr)

# Receive message
message = client_socket.recv(1024).decode()
print("Client says:", message)

# Send reply
client_socket.send("Hello from Server!".encode())

# Close connection
client_socket.close()