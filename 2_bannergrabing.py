import socket
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='Indicar la ip de la victima')
parser=parser.parse_args()
def banner(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print(str(s.recv(1024)))
    except socket.error as e:
        print(f"No se pudo conectar a {ip}:{port}. Error: {e}")
    finally:
        s.close()
def main():
    if parser.target:
        ip=parser.target
        port=21
        banner(ip,port)

    else:
        print('(-) ingresa una ip')

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()