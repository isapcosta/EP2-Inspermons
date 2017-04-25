import json
import random
import pickle


def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("level : {0}".format(ipmon["level"]))
    print("volume = {0}".format(ipmon["volume"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("Barreira Sonora = {0}".format(ipmon["Barreira Sonora"]))
    
    return  


with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)


    
insperdex=[]
Store={'Guitarra':70,'Bateria':40,'Violino':50,'Violao':20}

listadeinspermons={"Rocko":inspermons[0],'Reggae':inspermons[1],"Eletro":inspermons[2],"Classico":inspermons[3]}
Jogador=[{"nome" : "Compositor","level" : 1 ,"timbre de voz" : 15,"espectro sonoro":20, "vida" : 90, "Barreira Sonora" : 20},
         {"nome" : "Musico","level" : 2 ,"timbre de voz" : 25,"espectro sonoro":35,"vida" : 150,"Barreira Sonora" : 25},
         {"nome" : "Maestro","level" : 3 ,"timbre de voz" :35,"espectro sonoro":40,"vida" : 200,"Barreira Sonora" : 30}]
Notasmusicais=0
Coins=0

Nome_do_Jogador=input("Qual é o seu Nickname?")
inspermoninicial=Jogador[0]   
print("Bem vindo {0} ! Você inicia o jogo sendo {1} e tem {2} de vida,a força da sua Barreira Sonora é {3} e seus ataques: timbre de voz tem {4} de poder e o espectro sonoro {5} de poder. Ao longo da sua jornada encontrará inspermons que você pode batalhar".format(Nome_do_Jogador,inspermoninicial["nome"],inspermoninicial["vida"],inspermoninicial["Barreira Sonora"],inspermoninicial["timbre de voz"],inspermoninicial["espectro sonoro"]))   
i=0
while i==0:
    
    inicio=int(input("Olá ! Você quer passear(1), dormir(2), ir a loja (3), Salvar o Jogo (4) ou carregar o jogo anterior (5)?"))
    if Notasmusicais==20:
        print("Voce evoluiu de Compositor para Musico!")
        inspermoninicial=Jogador[1]
    if Notasmusicais==40:
        print("Voce evoluiu de Musico para Maestro!")
        inspermoninicial=Jogador[2]
        
    if inicio==3:
        x=0
        while x==0:
            print("Esses são os itens disponiveis:",Store)
            print("Suas coins",Coins)
            item=input("Qual deles voce deseja comprar? ")
            item=item.lower().title()
            if item not in Store:
                print("Esse Item nao consta no inventario da loja, escolha outro item!")
                continue
            else:
                if Store[item]<=Coins:
                        compra=int(input("{0} pode ser seu/sua , deseja comprar(1), escolher outro item (2) ou sair(3)? ".format(item)))
                        if compra==3:
                            break
                        elif compra==2:
                            continue
                        elif compra==1:
                            Coins=Coins-Store[item]
                            print("Parabens! Você adquiriu: {0}".format(item))
                            print("Você tem agora:{0} coins. ".format(Coins))
                            if item=='Violao':
                                inspermoninicial["vida"]=inspermoninicial["vida"] + 5
                                inspermoninicial["Barreira Sonora"]=inspermoninicial["Barreira Sonora"] + 5
                                inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+5
                                inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+5
                                print("Sua vida, Barreira Sonora e ataques foram aumentados em 5!")
                            elif item=='Bateriia':
                                inspermoninicial["vida"]=inspermoninicial["vida"] + 15
                                inspermoninicial["Barreira Sonora"]=inspermoninicial["Barreira Sonora"] + 15
                                inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+15
                                inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+15
                                print("Sua vida, Barreira Sonora e ataques foram aumentados em 15!")
                            elif item=='Violino':
                                inspermoninicial["vida"]=inspermoninicial["vida"] + 20
                                inspermoninicial["Barreira Sonora"]=inspermoninicial["Barreira Sonora"] + 20
                                inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+20
                                inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+20
                                print("Sua vida, Barreira Sonora e ataques foram aumentados em 20!")                
                            elif item=='Guitarra':
                                inspermoninicial["vida"]=inspermoninicial["vida"] + 40
                                inspermoninicial["Barreira Sonora"]=inspermoninicial["Barreira Sonora"] + 40
                                inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+40
                                inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+40
                                print("Sua vida, Barreira Sonora e ataques foram aumentados em 40!") 
                            cont2=int(input("Sair(1) ou continuar comprando(2)? "))
                            if cont2==1:
                                break
                            elif cont2==2:
                                continue
                else:
                    prox=int(input("Voce nao tem coins suficientes, volte depois(1) ou escolha outro item(2)! "))
                    if prox==1:
                        break
                    elif prox==2:
                        continue
    elif inicio==2:
        print("Bom descanso!")
        break
    elif inicio==1:	
        
        
        inimigo=random.choice(list(listadeinspermons.keys()))
        insperdex.append(listadeinspermons[inimigo]["nome"])
    
        print("Você acabou de encontrar o:",inimigo)
        print(mostra_ipmon(listadeinspermons[inimigo]))

        LevelJogador=inspermoninicial["level"]
        LevelOponente=listadeinspermons[inimigo]["level"]
        VidaJogador=inspermoninicial["vida"]
        VidaOponente=listadeinspermons[inimigo]["vida"]
        DefesaJogador=inspermoninicial["Barreira Sonora"]
        DefesaOponente=listadeinspermons[inimigo]["Barreira Sonora"]
        Poder1Jogador=inspermoninicial["timbre de voz"]
        Poder2Jogador=inspermoninicial["espectro sonoro"]
        PoderOponente=listadeinspermons[inimigo]["volume"]
        
        batalha=int(input("Você quer batalhar(1) ou tentar fugir(2)?"))

        opcoes=["com","com","sem"]
        opcoes2=["sem","com"]
        opcoes3=["sem","sem","com"]
        evasiva=[0,0,0,0,0,0,0,1,2]
        if batalha==1:
            
            while VidaJogador > 0 and VidaOponente > 0:

                ataque=int(input("Escolha seu ataque: Timbre de voz (1) ou Espectro Sonoro(2)"))
                if ataque==1:
                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("O inimigo desviou do seu golpe.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                        DAJ=Poder1Jogador - DefesaOponente
                        if DAJ<=0:
                            print("Seu golpe nao surtiu efeito no inimigo.")
                            DAJ=0
                        VidaOponente = VidaOponente - DAJ
                        
                        
                        if VidaOponente <= 0:
                            print("Você derrotou o : {0}".format(inimigo))
                            Notasmusicais=Notasmusicais+10
                            Coins=Coins+20
                            print("coins",Coins)
                            print("notas",Notasmusicais)
                        
                    else:
                            print("Voce deu um ataque critico!")
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                            DAJ=Poder1Jogador + 15 - DefesaOponente
                            if DAJ<=0:
                                print("Seu golpe nao surtiu efeito no inimigo.")
                                DAJ=0
                            VidaOponente = VidaOponente - DAJ
                            
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
                                print("coins",Coins)
                                print("notas",Notasmusicais)
                            

                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("Voce desviou do golpe do inimigo.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                        DAOP=PoderOponente - DefesaJogador
                        if DAOP<=0:
                            print("Golpe do inimigo nao surtiu efeito em voce.")
                            DAOP=0
                        VidaJogador = VidaJogador - DAOP
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
                    else:
                        print("O oponente lhe deu um ataque critico!")
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                        DAOP=PoderOponente + 15 - DefesaJogador
                        if DAOP<=0:
                            print("Golpe do inimigo nao surtiu efeito em voce.")
                            DAOP=0
                        VidaJogador = VidaJogador - DAOP
                        
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
                        
                    
                elif ataque==2:
                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("O inimigo desviou do seu golpe.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                        DAJ2=Poder2Jogador - DefesaOponente
                        if DAJ2<=0:
                            print("Seu golpe nao surtiu efeito no inimigo.")
                            DAJ2=0
                        VidaOponente = VidaOponente - DAJ2
                        
                        if VidaOponente <= 0:
                            print("Você derrotou o : {0}".format(inimigo))
                            Notasmusicais=Notasmusicais+10
                            Coins=Coins+20
                            print("coins:",Coins)
                            print("notas",Notasmusicais)
                        
                    else:
                            print("Voce deu um ataque critico!")
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                            DAJ2=Poder2Jogador + 15 - DefesaOponente
                            if DAJ2<=0:
                                print("Seu golpe nao surtiu efeito no inimigo.")
                                DAJ2=0
                            VidaOponente = VidaOponente - DAJ2
                              
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
                                print("coins:",Coins)
                                print("notas",Notasmusicais)
                             

                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("Voce desviou do golpe do inimigo.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                        DAOP2=PoderOponente - DefesaJogador
                        if DAOP2<=0:
                            print("Golpe do inimigo nao surtiu efeito em voce.")
                            DAOP2=0
                        VidaJogador = VidaJogador - DAOP2

                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
                    else:
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                        print("O oponente lhe deu um ataque critico!")
                        DAOP2=PoderOponente + 15 - DefesaJogador
                        if DAOP2<=0:
                            print("Golpe do inimigo nao surtiu efeito em voce.")
                            DAOP2=0
                        VidaJogador = VidaJogador - DAOP2
                        
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
                        
                    
                    
        if batalha==2:

            if LevelOponente < LevelJogador:
                escolha=random.choice(opcoes)
            elif LevelOponente == LevelJogador:
                escolha=random.choice(opcoes2)
            elif LevelOponente>LevelJogador:
                escolha=random.choice(opcoes3)
            
            if escolha=="com":
                print("Ufa,Você escapou")
                continue
            else:
                print("Você perdeu sua vez de jogar")
                while VidaJogador > 0 and VidaOponente > 0:
                    
                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("Voce desviou do golpe do inimigo.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                        DAOP=PoderOponente - DefesaJogador
                        if DAOP<=0:
                            print("Golpe do inimigo nao surtiu efeito em voce.")
                            DAOP=0
                        VidaJogador = VidaJogador - DAOP
                        
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                    else:
                        print("O oponente lhe deu um ataque critico!")
                        DAOP=PoderOponente + 15 - DefesaJogador
                        if DAOP<=0:
                            print("Golpe do inimigo nao surtiu efeito em voce.")
                            DAOP=0
                        VidaJogador = VidaJogador - DAOP
                        
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                           
                    ataque=int(input("Escolha seu ataque: Timbre de voz (1) ou Espectro Sonoro(2)"))
                    if ataque==1:
                        escolha2=random.choice(evasiva)
                        if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                            print("O inimigo desviou do seu golpe.")
                            continue
                        elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                            DAJ=Poder1Jogador - DefesaOponente
                            if DAJ<=0:
                                print("Seu golpe nao surtiu efeito no inimigo.")
                                DAJ=0
                            VidaOponente = VidaOponente - DAJ
                            
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
                                print("coins",Coins)
                                print("notas",Notasmusicais)
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                        else:
                            print("Voce deu um ataque critico!")
                            DAJ=Poder1Jogador + 15 - DefesaOponente
                            if DAJ<=0:
                                print("Seu golpe nao surtiu efeito no inimigo.")
                                DAJ=0
                            VidaOponente = VidaOponente - DAJ
                            
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
                                print("coins",Coins)
                                print("notas",Notasmusicais)
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                   
                    elif ataque==2:
                        escolha2=random.choice(evasiva)
                        if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                            print("O inimigo desviou do seu golpe.")
                            continue
                        elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
                            DAJ2=Poder2Jogador - DefesaOponente
                            if DAJ2<=0:
                                print("Seu golpe nao surtiu efeito no inimigo.")
                                DAJ2=0
                            VidaOponente = VidaOponente - DAJ2
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
                                print("coins:",Coins)
                                print("notas",Notasmusicais)
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                        else:
                            print("Voce deu um ataque critico!")
                            DAJ2=Poder2Jogador + 15 - DefesaOponente

                            if DAJ2<=0:
                                print("Seu golpe nao surtiu efeito no inimigo.")
                                DAJ2=0
                            VidaOponente = VidaOponente - DAJ2  
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
                                print("coins:",Coins)
                                print("notas",Notasmusicais)
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador) 
    
    elif inicio == 4:
        salvos = open("salvos.txt", "r")
        lines=salvos.read()
        print("Essa é a lista de arquivos salvos:")
        print(lines)
        salvos = open("salvos.txt", "a")
        arqsave=input("Qual o nome do seu arquivo?"+"\n")
        arqsave=arqsave.upper()
        salvos.write(arqsave+"\n")
        # salvar
        with open(arqsave+".py", 'wb') as f:
            pickle.dump([Nome_do_Jogador, Notasmusicais, Coins, insperdex], f, protocol=2)
            print("O jogo foi salvo com sucesso!")
    elif inicio == 5:
        salvos = open("salvos.txt", "r")
        lines=salvos.read()
        print("Essa é a lista de arquivos que você pode carregar:")
        print(lines)
        arqload=input("Qual o arquivo voce deseja carreggar?")
        arqload=arqload.upper()
        # carregar
        with open(arqload+".py", 'rb') as f:
            Nome_do_Jogador, Notasmusicais, Coins, insperdex = pickle.load(f)
            print("O jogo foi carregado com sucesso!")                            
insperdex=set(insperdex)
insperdex=",".join(insperdex)
print("Estes foram os inspermons que cruzaram sua jornada:",insperdex)