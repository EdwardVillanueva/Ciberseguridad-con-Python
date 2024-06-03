import hashlib
import sys
import argparse

def md5(palabraa_encriptada,texto_plano):
    for lista in texto_plano:
        cifrado=lista.encode('utf-8')
        encrypted=hashlib.md5(cifrado)
        if encrypted.hexdigest()==palabraa_encriptada:
            print(lista)
def sha1(palabraa_encriptada,texto_plano):
    for lista in texto_plano:
        cifrado=lista.encode('utf-8')
        encrypted=hashlib.sha1(cifrado)
        if encrypted.hexdigest()==palabraa_encriptada:
            print(lista)
def sha256(palabraa_encriptada,texto_plano):
    for lista in texto_plano:
        cifrado=lista.encode('utf-8')
        encrypted=hashlib.sha256(cifrado)
        if encrypted.hexdigest()==palabraa_encriptada:
            print(lista)
def sha512(palabraa_encriptada,texto_plano):
    for lista in texto_plano:
        cifrado=lista.encode('utf-8')
        encrypted=hashlib.sha512(cifrado)
        if encrypted.hexdigest()==palabraa_encriptada:
            print(lista)
    
def main():
    print(". :RAINBOW TABLE ATTACK")
    print(". Este programa soporta md5,sha1,sha256,sha512")
    file=open("diccionario.txt","r")
    # parser sirve para obtener el valor de lo que vas a poner en el bash
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target',help='Indicar le hash')
    parser=parser.parse_args()
    palabra_encriptada=parser.target
    texto_plano=file.read().split('\n')
    if len(palabra_encriptada)==32:
        print("la encriptacion es md5")
        md5(palabra_encriptada,texto_plano)
    elif len(palabra_encriptada)==40:
        print("la encriptacion es sha1")
        sha1(palabra_encriptada,texto_plano)

    elif len(palabra_encriptada)==64:
        print("la encriptacion es sha256")
        sha256(palabra_encriptada,texto_plano)

    elif len(palabra_encriptada)==128:
        print("la encriptacion es sha512")
        sha512(palabra_encriptada,texto_plano)   

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
#md5:20901f355b103728d009ff1d0d1a7a64
#sha1:e4fe3bcf0f5dd4f8a2d09c756135a37a00855da1
#sha256:2cc8248a5f2e849dc188b1117e6f2efb8c4e27a9ddc6a50d8a41e0e104bea40a
#sha512:66fd16912136a29ec549fc1f561034375c1ed961ca4b35062b0a38122d773bdf0f8977f2e40cf6b46593e3cd371d2c71a8c43df3fc38d144470f8b2e8c13fbbe   