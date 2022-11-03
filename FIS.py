from MF import *

Purity = Height = Price = 0
PUisE = PUisH = PUisM = PUisL = HisT = HisM = HisL = PRisE = PRisH = PRisM =PRisL = 0
PriceArray={x: 0 for x in range(1500, 30001)}

def Fuzzyfication():
    global Purity, Height
    global PUisE, PUisH, PUisM, PUisL, HisT, HisM, HisL

    PUisE = mfPUisE(Purity)
    PUisH = mfPUisH(Purity)
    PUisM = mfPUisM(Purity)
    PUisL = mfPUisL(Purity)
    HisT = mfHisT(Height)
    HisM = mfHisM(Height)
    HisL = mfHisL(Height)

def FuzzyInference():
    global PUisE, PUisH, PUisM, PUisL, HisT, HisM, HisL, PRisE, PRisH, PRisM, PRisL

    PRisE = min(PUisE, HisT)
    PRisH = max(min(PUisE, HisM), min(PUisH, HisT))
    PRisM = max(min(PUisH, HisM), min(PUisH, HisL), min(PUisM, HisT))
    PRisL = max(PUisL, min(HisM, 1 - PUisE))


def Composition():
    global PRisE, PRisH, PRisM, PRisL
    global PriceArray
    for i in range(1500, 30001):
        PriceArray[i] = max(min(mfPRisE(i), PRisE),
                            min(mfPRisH(i), PRisH),
                            min(mfPRisM(i), PRisM),
                            min(mfPRisL(i), PRisL))


def Defuzzyfication():
    global Price
    global PriceArray

    X=list(PriceArray.keys())
    Y=list(PriceArray.values())

    Price = LastMax(X, Y)

def Run():
    Fuzzyfication()
    FuzzyInference()
    Composition()
    Defuzzyfication()

def Init():
    global Purity, Height
    
    Purity = float(input('Purity = '))
    Height = float(input('Height = '))

def Terminate():
    global Price

    print('Price = ', Price)

def Main():
    Init()
    Run()
    Terminate()

if __name__=='__main__':
    Main()






    












    
