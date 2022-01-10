from time import time, sleep


def velocidade(func):
    def internaVeloc(*args, **kwargs):
        start = time()
        resulti = func(*args, **kwargs)
        end = time()
        tempo = (end - start) * 10000
        print(f'{tempo:.3f}')
        return resulti
    return internaVeloc


@velocidade
def demora():
    for i in range(5):
        sleep(1)

