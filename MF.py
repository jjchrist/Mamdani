from BasicFuncs import *

def mfPUisE(x):
    return SmoothS(x, 80, 90)

def mfPUisH(x):
    return SmoothTrap(x, 50, 75, 90, 100)

def mfPUisM(x):
    return SmoothTrap(x, 35, 45, 75, 90)

def mfPUisL(x):
    return SmoothZ(x, 45, 50)

def mfHisT(x):
    return SmoothS(x, 140, 160)

def mfHisM(x):
    return SmoothTrap(x, 120, 140, 160, 180)

def mfHisL(x):
    return SmoothZ(x, 140, 160)

def mfPRisE(x):
    return SmoothS(x, 20000, 24000)

def mfPRisH(x):
    return SmoothTrap(x, 12000, 16500, 24000, 30000)

def mfPRisM(x):
    return SmoothTrap(x, 1500, 4500, 16500, 18000)

def mfPRisL(x):
    return SmoothZ(x, 4500, 9000)
