import sys
import requests
from random import choice
from string import ascii_lowercase
import dontpad
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
    except Exception as e:
        print("erro: ",e)
def get_key():
    try:
        f = open('init.txt','r')
        chave=f.read()
        return(chave)
        f.close()
    except Exception as e:
        print("erro: ",e)


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

def escreve(dados,file_name):
    f = open(file=file_name,mode='w')
    dados=dados.replace('\\n','\n')
    f.write(dados)
    f.close
def pull(file):
    chave=get_key()
    data="ERRO"
    try:
        data=dontpad.get_data(page_name=file,key=chave)
        # print(data)
        # return(data)
        escreve(dados=data,file_name=file)
        print("Sucesso")
    except Exception as e:
        print("erro",e)
def push(file_name):
    f=open(file=file_name,mode='r')
    data=f.read()
    f.close

    data=data.replace('\\n','\n')
    page_name=get_key()+"/"+file_name
    dontpad.post_data(page_name=page_name,content=data)

def main():
    if(len(sys.argv))<3:
        print("use python gitpad.py --op name")
        return
    if(sys.argv[1]=="--init" or sys.argv[1]=='--init-r'):
        init(sys.argv[1])
    elif(sys.argv[1]=="--pull"):
        pull(sys.argv[2])
    elif(sys.argv[1]=="--push"):
        push(sys.argv[2])
    else:
        print("erro,opção invalida")


if (__name__=='__main__'):
    main()
else:
    print('execute este script diretamente')
