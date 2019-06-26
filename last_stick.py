import random
import numpy as np

# --------------------------------------------------- GLOBAIS
LINHAS = 5
pyramid = None

plays = {
    str([0, 2, 3]) : [0, 2, 2],
    str([1, 1, 3]) : [1, 1, 1],
    str([1, 0, 3]) : [1, 0, 0],
    str([1, 2, 2]) : [0, 2, 2],
    str([1, 2, 1]) : [1, 1, 1],
    str([1, 2, 0]) : [1, 0, 0]
}
# --------------------------------------------------- FUNCS
def init_pyramid(n=4):
    return np.arange(1, n+1)

def get_total(pyramid):
    return pyramid.sum()

def get_valid_lines(pyramid):
    return np.argwhere(pyramid > 0)[:,0]
# --------------------------------------------------- HEURISTICAS
def h_easy(pyramid):
    
    # pega todos os argumentos nao nulos
    valid_lines = get_valid_lines(pyramid)
    # escolhe um aleatorio
    l = random.choice(valid_lines)
    # remove um valor entre 1 e TOTAL
    p = random.randint(1, pyramid[l])
    pyramid[l] -= p
    
    return pyramid

def h_med(pyramid):
    valid_lines = get_valid_lines(pyramid)
    l = np.argmax(pyramid)

    # se for impar e se o num de palitos for maior que um
    if (len(valid_lines) & 1) and (pyramid[l] > 1):
        # pega o maior e tira o total -1
        pyramid[l] = 1
    else:
        # pega o maior e tira todos os palitos
        pyramid[l] = 0
        
    return pyramid

def h_hard(pyramid):
    global plays
    valid_lines = get_valid_lines(pyramid)

    if len(valid_lines) > 3:
        return h_med(pyramid)
    else:
        play_key = str(list(pyramid[:3]))
        if play_key in plays.keys():
            pyramid[:3] = plays[play_key]
            return pyramid
        else:
            return h_easy(pyramid)
    
# ---------------------------------------------------- MAIN
def main():
    global LINHAS
    global pyramid

    pyramid = init_pyramid(n=LINHAS)

    print("Inicio de jogo!")
    while get_total(pyramid) > 1:
        print("\nTabuleiro: " + str(pyramid))
        linha = int(input("Linha: "))
        valor = int(input("Valor: "))
        pyramid[linha] -= valor


        print("Tabuleiro: " + str(pyramid))
        print("Vez da IA!")
        h_hard(pyramid)

    print("Fim de jogo!")

if __name__ == '__main__':
    main()
