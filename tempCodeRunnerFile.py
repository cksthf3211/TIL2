import socket

server_ip = '192.168.0.11'  # 서버 IP
# server_ip = '192.168.0.198'  # 서버 IP

server_port = 4004  # 서버 포트번호
server_port = 81

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

try:
    while True:
        msg = input('msg:')
        client_socket.sendall(msg.encode(encoding='utf-8'))

        # 서버가 에코로 되돌려 보낸 메시지를 클라이언트가 받음
        data = client_socket.recv(100)
        msg = data.decode()  # 읽은 데이터 디코딩
        print('echo msg:', msg)

        # 만약 메시지가 '+++'이면 클라이언트 종료
        if msg == '+++':
            print("클라이언트 종료")
            break

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    client_socket.close()
