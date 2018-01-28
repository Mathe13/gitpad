import sys
import functions

def main():
    if(len(sys.argv))<3:
        print("use python gitpad.py --op name")
        return
    if(sys.argv[1]=="--init"):
        if(sys.argv[2]=="-r" or sys.argv[2]=="-R"):
            if sys.argv[3].isdigit:
                functions.criar_init(functions.gera_chave(sys.argv[3]))
            else:
                print("voce deve especificar o tamanho da chave")
        else:
            functions.criar_init(sys.argv[2])
    elif(sys.argv[1]=="--pull"):
        if(sys.argv[2]=="-kl"):
            functions.pull(sys.argv[3],"NONE")
        else:
            functions.pull(sys.argv[2],functions.get_key())
    elif(sys.argv[1]=="--push"):
        if(sys.argv[2]=="-kl"):
            functions.push(sys.argv[3],"NONE")
        else:
            functions.push(sys.argv[2],functions.get_key)
    else:
        print("erro,opção invalida")


if (__name__=='__main__'):
    main()
else:
    print('execute este script diretamente')
