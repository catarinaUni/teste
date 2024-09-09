import socket
def client(host = '10.0.3.103', port=8082): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = (host, port) 
    print ("Conectando em %s porta %s" % server_address) 
    sock.connect(server_address) 
    try: 
        message = input("Menssagem: ")
        print ("Enviando %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Recebido: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 

client()