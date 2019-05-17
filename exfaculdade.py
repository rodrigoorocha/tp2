import os
import time
import json
from pprint import pprint
import psutil

def obter_numero():
    try:
        num = int(input("digite seu numero: "))
    except ValueError as error:
        print("Numero errado")
        num = obter_numero()
    return num


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))
    
def get_appendix(appendix):
    if appendix == None:
        return 1

    return appendix + 1


def create_directory_folder(current_path, directory_name, appendix=None):
    # ver se ja existe
    available_name = directory_name
    if appendix:
        available_name = f"{directory_name} ({appendix})"

    fullpath = os.path.join(current_path, available_name)

    #criar
    try:
        os.mkdir(fullpath)
    except FileExistsError as error:
        # print(error)
        appendix = get_appendix(appendix)
        create_directory_folder(current_path, directory_name, appendix)


def questao_1():
    """
    Escreva um programa em Python que obtenha
    um número inteiro de um usuário e o imprima na tela.
    Caso o usuário não tenha digitado um número,
    indicar a seguinte mensagem “Programa abortado! Digite um número.”.
    """
    print('Questao 01')
    try:
        num = int(input("digite seu numero: "))
        print(num)
    except ValueError as error:
        print("Numero errado")
        time.sleep(2)
        questao_1()
    
def questao1_b():
    """
    Escreva um programa em Python que obtenha
    um número inteiro de um usuário e o imprima na tela.
    Caso o usuário não tenha digitado um número,
    indicar a seguinte mensagem “Programa abortado! Digite um número.”.
    """
    print('Questao1_b')
    #obter_numero()
    content = input('Digite um numero: ')
    if type(content) == int:
        print(content)
    else:
        print('Programa abortado!')
        questao1_b()


def questao1_c():
    """
    Escreva um programa em Python que obtenha
    um número inteiro de um usuário e o imprima na tela.
    Caso o usuário não tenha digitado um número,
    indicar a seguinte mensagem “Programa abortado! Digite um número.”.
    """
    print('Questao1_c')
    content = obter_numero()
    print(content)

        
def questao2():
    """
    Escreva um programa em Python que
    - obtenha um número inteiro de um usuário e
    - calcule sua potência de 2 (multiplique o número por ele mesmo).
    Faça com que seu programa só finalize quando o usuário digitar um valor válido.
    """
    
    print('Questao 02')
    num = obter_numero()
    potencia = num**2
    print(f"A potencia de {num} é: {potencia}")

def questao3():
    """Escreva um programa em Python que obtenha dois números A e B e calcule A*B.
       Trate o caso do usuário não digitar um número para A e B
       (letras ou outro conjunto de caracteres)."""
    num_A = obter_numero()
    num_B = obter_numero()
    resultado = num_A * num_B
    print(f" a multiplicacao de {num_A} * {num_B} é : {resultado}")
   
    
def questao4():
    """ Escreva um programa em Python que crie um diretório no diretório corrente de execução
        de seu programa. Capture os erros FileExistsError e FileNotFoundError e apresente
        uma mensagem sua para eles. Indique também uma mensagem de erro caso ocorra um
        erro não previsto. """
    dirname = 'dir3'
    cur_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cur_path, dirname)
    try:
        os.mkdir(path)
        print("Diretorio {path} criado com sucesso!")
    except FileExistsError as error:
        print(error)
    except FileNotFoundError as error:    
        print("Diretorio já criado")
    except Exception as error:
        print(error)
        
    filename = 'renan.txt'
    full_filename = os.path.join(path, filename)
    with open(full_filename, "w") as file:
        content = 'Conteudo escrito'
        file.write(content)

def questao4_bonus():
    """ 
    Escreva um programa em Python que crie um diretório no diretório corrente de execução
    de seu programa. Capture os erros FileExistsError e FileNotFoundError e apresente
    uma mensagem sua para eles. Indique também uma mensagem de erro caso ocorra um
    erro não previsto. 
    """

    directory_name = "Nova Pasta"
    current_path = get_current_path()
    create_directory_folder(current_path, directory_name)



def questao6():
   """
   Escreva uma função em Python que receba como parâmetro um diretório e gere uma lista com
   todos os arquivos existente nela.
   """          
   pastaAtual = get_current_path()
   print(criarListaArquivos(pastaAtual))
    

def criarListaArquivos(diretorio):
    arquivos = os.listdir(diretorio)
    return arquivos

def questao7():
    """Escreva um programa em Python que teste a função do item 6 com o seguinte parâmetro “./”
       e imprima a lista retornada por ela."""
    print(criarListaArquivos("./"))

def questao9():
    """Escreva um programa em Python que imprima a lista de processos em execução no computador.
       Esta lista deve conter o PID e nome do processo"""
    
    lista_tarefas = [] 
    #listaProcessos = psutil.Process
    for process in psutil.process_iter():
        
        lista_tarefas.append({"pid": process.pid,
                              "nome": process.name()})
    
    #print(lista_tarefas)
    pprint(lista_tarefas)
    
def questao9_b():
    #                                       | COMEÇA AQUI (Pelo for)
    pprint([p.as_dict(attrs=['name', 'pid', 'cpu_percent']) for p in psutil.process_iter()])

def questao10():
    """
    Escreva um programa em Python que
    - imprima a lista de processos em execução no computador
    que tenham percentual de CPU acima de 5%.
    Esta lista deve conter
    - o PID,
    - o nome do processo e
    - o percentual de uso de CPU.
    """
    #psutil.cpu_percent(interval=5)
    for process in psutil.process_iter():
        cpu_percent = process.cpu_percent(interval=1)
        if cpu_percent > .03:
            print(process.cpu_percent(interval=1), process.name())
    
def questao13():
    """
    Dada a lista: [(‘Azul’, 7, 3), (‘Vermelho’, 12, 1), (‘Amarelo’, 10, 2), (‘Verde’, 5, 1)].

    Escreva um programa que imprima:

    a lista ordenada crescentemente pela cor;
    a lista ordenada crescentemente pela quantidade;
    a lista ordenada decrescentemente pelo número de vizinhos.
    """
    lista_cores = [('Azul', 7, 3), ('Vermelho', 12, 1), ('Amarelo', 10, 2), ('Verde', 5, 1)]
    
    lista_cor= sorted(lista_cores)
    lista_quant = sorted(lista_cores, key = lambda item : item[1])
    lista_vizinhos = sorted(lista_cores, key=lambda item : item[2], reverse=True)
    
    
    print(f"A lista ordenada pela cor: {lista_cor}")
    print(f"A lista ordenada pela quantidade: {lista_quant}")
    print(f"A lista ordenada decrescentemente pelo numero de vizinhos: {lista_vizinhos}")
    
    
def questao18():
    """Escreva um programa em Python que gere um arquivo contendo o percentual de uso de memória e CPU em cada linha
    medidos a cada 1 segundo.O arquivo deve ter 20 linhas (isto é, serão 20 medidas)."""
    dir_atual = get_current_path()
    filename = os.path.join(dir_atual,"process.log")
    with open(filename, 'w') as output_file: 
        process_list = getProcess()
        output_file.write('\n'.join( process_list))
        
    
def getProcess():
    process_list = []
    for count, process in enumerate(psutil.process_iter()):
        process_list.append((f"Processo {process.cpu_percent(interval=1)} : {process.memory_percent()}"))
        if count > 20:
            break
    return process_list
        
    

def Main():
    #questao1_b()
    #questao1_c()
    #questao2()
    #questao3()
    #questao4()
    #questao9()
    #questao9_b()
    #questao13()
    questao18()
    
if __name__ == '__main__':
    Main()