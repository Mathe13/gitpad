import sys
import functions
# from time import sleep


class gitpad():
    # def __init__(**kwargs):
    #     pass

    @staticmethod
    def usage():
        print("use python gitpad.py --op name")

    @staticmethod
    def repo_init(comands):
        if(comands[1] == "-r" or comands[1] == "-R"):
            if comands[2].isdigit:
                functions.criar_init(functions.gera_chave(comands[2]))
            else:
                print("voce deve especificar o tamanho da chave")
        else:
            functions.criar_init(sys.argv[2])

    @staticmethod
    def repo_pull(comands):
        if(comands[1] == "-kl"):
            functions.pull(comands[2], "NONE")
        else:
            functions.pull(comands[1], functions.get_key())

    @staticmethod
    def repo_push(comands):
        if(comands[1] == "-kl"):
            functions.push(comands[2], "NONE")
        else:
            functions.push(comands[1], functions.get_key)

    @staticmethod
    def repo_syn_up(comands):
        if len(comands) < 2:
            while True:
                print("synchronizing...")
                functions.push(comands[1], comands[2])
                print("done")
        else:
            while True:
                print("synchronizing...")
                functions.push(comands[1], "NONE")
                print("done")


def main():
    comands = sys.argv[1:]
    if(len(sys.argv)) < 3:
        gitpad.usage()
    if(sys.argv[1] == "--init"):
        gitpad.repo_init(comands=comands)
    elif(sys.argv[1] == "--pull"):
        gitpad.repo_pull(comands)
    elif(sys.argv[1] == "--push"):
        gitpad.repo_push(comands)
    elif(sys.argv[1] == "--sync_up"):
        gitpad.repo_syn_up(comands)
    else:
        print("erro,opção invalida")


if (__name__ == '__main__'):
    main()
else:
    print('execute este script diretamente')
