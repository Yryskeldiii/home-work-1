x=3
san1= int(input("1 sandy engiz: "))
amal=input("amaldy engiz(+ - * / ): ")
san2= int(input("2 sandy engiz: "))

def qosu (birinchi_san, ekinchi_san):
    nat = birinchi_san + ekinchi_san
    print("ekis sannyn qosundysy: ", nat)

def azaitu (birinchi_san, ekinchi_san):
    nat = birinchi_san - ekinchi_san
    print("ekis sannyn aiyrmasy: ", nat)

def kobeitu(birinchi_san, ekinchi_san):
    nat = birinchi_san* ekinchi_san
    print("ekis sannyn kobeitindisi: ", nat)

def bolu (birinchi_san, ekinchi_san):
    nat = birinchi_san/ ekinchi_san
    print("ekis sannyn bolindisi: ", nat)

while x==3:
    san1 = int(input("1 sandy engiz: "))
    amal = input("amaldy engiz(+ - * / ): ")
    san2 = int(input("2 sandy engiz: "))



if(amal=="+"):
    qosu(san1, san2)
if(amal=="-"):
    azaitu(san1, san2)
if(amal=="*"):
    kobeitu(san1, san2)
if(amal=="/"):
    bolu(san1, san2)

