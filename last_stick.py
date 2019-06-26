import random
import numpy as np

# --------------------------------------------------- GLOBAIS
LINHAS = 5
pyramid = None
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
    
# ---------------------------------------------------- MAIN
def main():
    global LINHAS
    global pyramid

    pyramid = init_pyramid(n=LINHAS)
    print(pyramid)
    h_easy(pyramid)
    print(pyramid)
    h_med(pyramid)
    print(pyramid)

if __name__ == '__main__':
    main()
