# FUNÇOES C/ CINEMATICA
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# vi veloc inicial - Vf velocidade final
def velocidade_media(vi,vf):
    v = vf-vi
    return v

# t - tempo medio / tf - tempo final / ti - tempo inicial
def tempo_medio(tf,ti):
    t = tf-ti
    return t

# v - velocidade media / t tempo medio
def aceleracao_media(v, t):
    am = v/t
    return am

# Movimento Retilíneo Uniforme (MRU)
# corpo se desloca em linha reta com velocidade constante, ou seja, sem aceleração
def mru(si, v, t):
    s = si+v*t


