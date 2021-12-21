
print("start code")




def restart():
    print("vuoi riprovare il codice?\n1)si \n2)no")
    codice_restart = int(input())
    if codice_restart == 1:
            calcolo_cibo()
    elif codice_restart == 2 :    
            print("buona giornata alla prossima")
    else :
            print("selezione non accettata")
            restart()






def calcolo_cibo():
    print("vorrei aiutarti a capire quanto\ncibo comprare nella tua fattoria\n quanti animali hai?\n\n\n")
    print("cavalli?")
    cavalli = int(input())
    print("mucche?")
    mucche_da_latte = int(input())
    print("pecore?")
    pecora = int(input())
    cibo_pecora = 45 * pecora
    cibo_mucche_da_latte = 40 * mucche_da_latte
    cibo_cavalli = cavalli*10
    cibo_totale = cibo_cavalli + cibo_mucche_da_latte + cibo_pecora
    
    print(f"nella fattoria ogni giorno hai bisogno di: {cibo_totale}kg")
    print(f"ed al mese di : {cibo_totale * 30}kg di cibo")

    
    restart()
    print("===============================================\n===============================================\n")


calcolo_cibo()





    



    


    

















