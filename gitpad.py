import sys
import functions
# from time import sleep


class gitpad(functions):
    @staticmethod
    def usage(self):
        print("use python gitpad.py --op name")

    @staticmethod
    def repo_init(self, comands):
        if(comands[1] == "-r" or comands[1] == "-R"):
            if comands[2].isdigit:
                self.criar_init(functions.gera_chave(comands[2]))
            else:
                print("voce deve especificar o tamanho da chave")
        else:
            self.criar_init(sys.argv[2])

def main():
    if(len(sys.argv)) < 3:
        gitpad.usage()
        return
    if(sys.argv[1] == "--init"):
        gitpad.repo_init(sys.argv[2:])
    elif(sys.argv[1] == "--pull"):
        if(sys.argv[2] == "-kl"):
            functions.pull(sys.argv[3], "NONE")
        else:
            functions.pull(sys.argv[2], functions.get_key())
    elif(sys.argv[1] == "--push"):
        if(sys.argv[2] == "-kl"):
            functions.push(sys.argv[3], "NONE")
        else:
            functions.push(sys.argv[2], functions.get_key)
    elif(sys.argv[1] == "--sync_up"):
        if len(sys.argv) < 3:
            while True:
                print("synchronizing...")
                functions.push(sys.argv[2], sys.argv[3])
                print("done")
        else:
            while True:
                print("synchronizing...")
                functions.push(sys.argv[2], "NONE")
                print("done")

    else:
        print("erro,opção invalida")


if (__name__ == '__main__'):
    main()
else:
    print('execute este script diretamente')
