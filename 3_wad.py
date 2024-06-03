import subprocess
import argparse
import sys
parser=argparse.ArgumentParser()
parser.add_argument('-t','--target',help="indica la url \n(e.g https://ejemplo.com)")
parser=parser.parse_args()

def main():
    if parser.target:
        subprocess.call("wad -u "+parser.target+">"+"información.txt",shell=True)
    else:
        print('ingresa una url')

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()