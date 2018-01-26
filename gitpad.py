import sys
import requests
from random import choice
from string import ascii_lowercase
#python dntpd.py --init/--init-r/--push/--pull

def gera_chave(tamanho):
    caractere=list(ascii_lowercase);
    caractere=caractere+['0','1','2','3','4','5','6','7','8','9']
    chave=''
    for i in range(0,int(tamanho)):
        chave=chave+choice(caractere)
    #print(chave)
    return chave

def criar_init(chave):
    try:
        f = open('init.txt','w')
        f.write(chave)
        f.close()
        pass
    except Exception as e:
        print("erro: ",e)
        pass

#inicializa o diretorio com uma chave de acesso para o dontpad
def init(op):
    if(op=='--init-r'):
        try:
            key=gera_chave(sys.argv[2])
            criar_init(key)
        except Exception as e :
            print("erro: ",e)
    elif(op=='--init'):
        try:
            criar_init(sys.argv[2])
        except Exception as e:
            print("erro: ",e)
def post(filename):
    pass

def main():
    init(sys.argv[1])

if (__name__=='__main__'):
    main()
else:
    print('execute este script diretamente')
