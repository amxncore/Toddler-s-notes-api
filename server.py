import socket

HOST = "127.0.0.1"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"server running on http://{HOST}:{PORT}")

while True:
    client, addr = server.accept()
    request = client.recv(1024).decode()

    response_body = "hi batman"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        + response_body
    )

    client.sendall(response.encode())
    client.close()
