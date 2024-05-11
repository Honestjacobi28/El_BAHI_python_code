from math import sqrt 

def somme(N1,N2,N3,N4,N5):
    S=N1+N2+N3+N4+N5
    return S

def moyenne(N1,N2,N3,N4,N5):
    S=N1+N2+N3+N4+N5
    M=S/5
    return M

def variance(N1,N2,N3,N4,N5):
    M=moyenne(N1,N2,N3,N4,N5)
    Var=(N1-M)**2+(N2-M)**2+(N3-M)**2+(N4-M)**2+(N5-M)**2
    return Var

def ecart_type(N1,N2,N3,N4,N5):
    Var=variance(N1,N2,N3,N4,N5)
    E=sqrt(Var)
    return E

def coefficient_variation(N1,N2,N3,N4,N5):
    E=ecart_type(N1,N2,N3,N4,N5)
    M=moyenne(N1,N2,N3,N4,N5)
    CV=(E/M)*100
    return CV