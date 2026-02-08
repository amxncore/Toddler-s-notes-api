import socket

HOST = "127.0.0.1"
PORT = 9090

notes = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"server running on http://{HOST}:{PORT}")

while True:
    client, addr = server.accept()
    request = client.recv(4096).decode()

    print("----- REQUEST -----")
    print(request)

    try:
        if request.startswith("GET /notes"):
            response_body = str(notes)

        elif request.startswith("POST /notes"):
            body = request.split("\r\n\r\n", 1)[1]
            notes.append(body)
            response_body = '{"message":"note saved"}'

        else:
            response_body = "hi batman"

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "\r\n"
            + response_body
        )

        client.sendall(response.encode())

    except Exception as e:
        print("ERROR:", e)

    finally:
        client.close()
