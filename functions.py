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


# #inicializa o diretorio com uma chave de acesso para o dontpad
# def init(op,chave):
#     if(op=='-r'):
#         try:
#             #key=gera_chave(sys.argv[3])
#             criar_init(key)
#         except Exception as e :
#             print("erro: ",e)
#     else:
#         try:
#             criar_init(sys.argv[2])
#         except Exception as e:
#             print("erro: ",e)

def escreve(dados,file_name):
    f = open(file=file_name,mode='w')
    dados=dados.replace('\\n','\n')
    f.write(dados)
    f.close

def pull(file,key):
    data="ERRO"
    try:
        data=dontpad.get_data(page_name=file,key=key)
        # print(data)
        # return(data)
        escreve(dados=data,file_name=file)
        print("Sucesso")
    except Exception as e:
        print("erro",e)
def push(file_name,key):
    f=open(file=file_name,mode='r')
    data=f.read()
    f.close
    page_name=""
    if(key=="NONE"):
        page_name=file_name
    else:
        page_name=get_key()+"/"+file_name

    data=data.replace('\\n','\n')
    dontpad.post_data(page_name=page_name,content=data)
