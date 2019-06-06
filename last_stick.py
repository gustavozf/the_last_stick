import random
import numpy as np

# --------------------------------------------------- GLOBAIS
LINHAS = 5
piramid = None
# --------------------------------------------------- FUNCS
def init_piramid(n=4):
    return np.arange(1, n+1)

def get_total(piramid):
    return piramid.sum()
# --------------------------------------------------- HEURISTICAS
def h_easy():
    global piramid
    
    # pega todos os argumentos nao nulos
    valid_lines = np.argwhere(piramid > 0)[:,0]
    # escolhe um aleatorio
    l = random.choice(valid_lines)
    # remove um valor entre 1 e TOTAL
    p = random.randint(1, piramid[l])
    piramid[l] -= p

    print('l: {} / p: {}'.format(l, p))

# ---------------------------------------------------- MAIN
def main():
    global LINHAS
    global piramid

    piramid = init_piramid(n=LINHAS)
    print(piramid)
    h_easy()
    print(piramid)

if __name__ == '__main__':
    main()