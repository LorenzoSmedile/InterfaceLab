def stampaDizionario(diz):
    for key,value in diz.items():
        print("la chiave è ......"+key)
        print("il valore è ......"+str (value))
        
def stampaSomma(diz2):
    somma=0
    for key,value in diz2.items():
        somma=somma+value
    print("la somma è ......"+str (somma))

def stampaInsegnanti(diz3):
    conta=0
    for key,value in dizionario.items():
        if value==18:
            conta=conta+1
    print("i insegnanti con tutte le ore sono ......"+str (conta))

dizionario ={"rossi":18,"bianchi":16,"verdi":6}
def prof(dizionario,key,value):
    if key in dizionario:
        dizionario[key]=value

def professori (dizionario,key,value):
    totaleOre=18
    if key in dizionario:
        totaleOre= totaleOre-value
    

prof(dizionario,"rossi",12)
prof(dizionario,"bianchi",15)
prof(dizionario,"verdi",18)
print((dizionario))

professori(dizionario)
print((dizionario))
    


#inserire un elemento dentro il dizionario
dizionario["viola"]=14
#modificare una coppia chiave valore
dizionario["bianchi"]=18
#itarare sul dizionario
#for key,value in dizionario.items():
#    print("la chiave è ......"+key)
#    print("il valore è ......"+str (value))

stampaDizionario(dizionario)
stampaSomma(dizionario)
stampaInsegnanti(dizionario)




