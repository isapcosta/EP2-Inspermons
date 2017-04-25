import json
def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}".format(ipmon["defesa"]))
    
    return  


with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)


    
insperdex=[]
Store={'Guitarra':70,'Bateria':40,'Violino':50,'Violao':20}

listadeinspermons={"Rocko":inspermons[0],'Reggae':inspermons[1],"Eletro":inspermons[2],"Classico":inspermons[3]}
Jogador=[{"nome" : "Compositor","timbre de voz" : 15,"espectro sonoro":20, "vida" : 90, "defesa" : 20},
         {"nome" : "Musico","timbre de voz" : 25,"espectro sonoro":30,"vida" : 150,"defesa" : 25},
         {"nome" : "Maestro","timbre de voz" :35,"espectro sonoro":40,"vida" : 200,"defesa" : 30}]
Notasmusicais=0
<<<<<<< HEAD
Coins=0 

=======
Coins=0
<<<<<<< HEAD

=======
# with open(salvos.pickle) 
# salvos=pickle.dump() 
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
Nome_do_Jogador=input("Qual é o seu Nickname?")
>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
inspermoninicial=Jogador[0]   
print("Welcome ! Você inicia o jogo sendo {0} e tem {1} de vida,a força da sua defesa é {2} e seus ataques: timbre de voz tem {3} de poder e o espectro sonoro {4} de poder. Ao longo da sua jornada encontrará inspermons que você pode batalhar".format(inspermoninicial["nome"],inspermoninicial["vida"],inspermoninicial["defesa"],inspermoninicial["timbre de voz"],inspermoninicial["espectro sonoro"]))   
i=0
while i==0:
    import random
    inicio=int(input("Olá ! Você quer passear(1) ou dormir(2) ou ir a loja (3)?"))
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
            item=input("Escolha o item que quer comprar")
            if Store[item]<=Coins:
                compra=int(input("{0} pode ser seu/sua , deseja comprar(1), escolher outro item (2) ou sair(3)".format(item)))
                if compra==3:
                    break
                elif compra==2:
                    continue
                elif compra==1:
                    Coins=Coins-Store[item]
                    print("Parabens! Você adquiriu: {0}".format(item))
                    print("Você tem agora:{0} coins".format(Coins))
                    if item=='Violao':
                        inspermoninicial["vida"]=inspermoninicial["vida"] + 5
                        inspermoninicial["defesa"]=inspermoninicial["defesa"] + 5
                        inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+5
                        inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+5
                        print("Sua vida, defesa e ataques foram aumentados em 5!")
                    elif item=='Bateriia':
                        inspermoninicial["vida"]=inspermoninicial["vida"] + 10
                        inspermoninicial["defesa"]=inspermoninicial["defesa"] + 10
                        inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+10
                        inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+10
                        print("Sua vida, defesa e ataques foram aumentados em 10!")
                    elif item=='Violino':
                        inspermoninicial["vida"]=inspermoninicial["vida"] + 20
                        inspermoninicial["defesa"]=inspermoninicial["defesa"] + 20
                        inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+20
                        inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+20
                        print("Sua vida, defesa e ataques foram aumentados em 20!")                
                    elif item=='Guitarra':
                        inspermoninicial["vida"]=inspermoninicial["vida"] + 40
                        inspermoninicial["defesa"]=inspermoninicial["defesa"] + 40
                        inspermoninicial["timbre de voz"]=inspermoninicial["timbre de voz"]+40
                        inspermoninicial["espectro sonoro"]=inspermoninicial["espectro sonoro"]+40
                        print("Sua vida, defesa e ataques foram aumentados em 40!") 
                    cont2=int(input("Sair(1) ou continuar comprando(2)"))
                    if cont2==1:
                        break
                    elif cont2==2:
                        continue
            else:
                prox=int(input("Voce nao tem coins suficientes, volte depois(1) ou escolha outro item(2)"))
                if prox==1:
                    break
                elif prox==2:
                    continue
                
    if inicio==2:
        print("Bom descanso")
        break
    elif inicio==1:	
        
        
        inimigo=random.choice(list(listadeinspermons.keys()))
        insperdex.append(listadeinspermons[inimigo]["nome"])
    
        print("Você acabou de encontrar o:",inimigo)
        print(mostra_ipmon(listadeinspermons[inimigo]))
        
        VidaJogador=inspermoninicial["vida"]
        VidaOponente=listadeinspermons[inimigo]["vida"]
        DefesaJogador=inspermoninicial["defesa"]
        DefesaOponente=listadeinspermons[inimigo]["defesa"]
        Poder1Jogador=inspermoninicial["timbre de voz"]
        Poder2Jogador=inspermoninicial["espectro sonoro"]
        PoderOponente=listadeinspermons[inimigo]["poder"]
        
        batalha=int(input("Você quer batalhar(1) ou tentar fugir(2)?"))
<<<<<<< HEAD
        opcoes=['escapou','semsorte']
=======

        opcoes=["com","com","sem"]
        opcoes2=["sem","com"]
        opcoes3=["sem","sem","com"]
<<<<<<< HEAD
        evasiva=[0,0,0,0,0,0,0,1,2]
=======
        evasiva=[0,0,0,0,0,0,0,1]
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
        if batalha==1:
            
            while VidaJogador > 0 and VidaOponente > 0:
                ataque=int(input("Escolha seu ataque: Timbre de voz (1) ou Espectro Sonoro(2)"))
                if ataque==1:
<<<<<<< HEAD
                    VidaOponente = VidaOponente - ( Poder1Jogador - DefesaOponente ) 
                    print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                    print("Sua vida:",VidaJogador)
                    
                    if VidaOponente <= 0:
                        print("Você derrotou o : {0}".format(inimigo))
                        Notasmusicais=Notasmusicais+10
                        Coins=Coins+20
                        print("coins",Coins)
                        print("notas",Notasmusicais)
                    else:
                        VidaJogador = VidaJogador - ( PoderOponente - DefesaJogador )
                        
                         
=======
                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("O inimigo desviou do seu golpe.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
<<<<<<< HEAD
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
=======
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                        DAJ=Poder1Jogador - DefesaOponente
                        if DAJ<=0:
                            print("Seu golpe nao surtiu efeito no inimigo.")
                            DAJ=0
                        VidaOponente = VidaOponente - DAJ
<<<<<<< HEAD
                        
=======
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                        
                        if VidaOponente <= 0:
                            print("Você derrotou o : {0}".format(inimigo))
                            Notasmusicais=Notasmusicais+10
                            Coins=Coins+20
                            print("coins",Coins)
                            print("notas",Notasmusicais)
<<<<<<< HEAD
                        
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
                            

=======
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
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
>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
<<<<<<< HEAD
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
                        
=======
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                    
                elif ataque==2:
<<<<<<< HEAD
                    VidaOponente = VidaOponente - ( Poder2Jogador - DefesaOponente )
                    
                    
                    if VidaOponente <= 0:
                        print("Você derrotou o : {0}".format(inimigo))
                        Notasmusicais=Notasmusicais+10
                        Coins=Coins+20
                        print("coins:",Coins)
                        print("notas",Notasmusicais)
                    else:
                        VidaJogador = VidaJogador - ( PoderOponente - DefesaJogador )
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)     
                
=======
                    escolha2=random.choice(evasiva)
                    if escolha2==1 and VidaOponente>0 and VidaJogador>0:
                        print("O inimigo desviou do seu golpe.")
                        continue
                    elif escolha2==0 and VidaOponente>0 and VidaJogador>0:
<<<<<<< HEAD
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
=======
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                        DAJ2=Poder2Jogador - DefesaOponente
                        if DAJ2<=0:
                            print("Seu golpe nao surtiu efeito no inimigo.")
                            DAJ2=0
                        VidaOponente = VidaOponente - DAJ2
<<<<<<< HEAD
=======
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                        
                        if VidaOponente <= 0:
                            print("Você derrotou o : {0}".format(inimigo))
                            Notasmusicais=Notasmusicais+10
                            Coins=Coins+20
                            print("coins:",Coins)
                            print("notas",Notasmusicais)
<<<<<<< HEAD
                        
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
                             

=======
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
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

>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
<<<<<<< HEAD
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
                        
                    
=======
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                    
        if batalha==2:
            escolha=random.choice(opcoes)
            if escolha=="escapou":
                print("Ufa,Você escapou")
                continue
            if escolha=="semsorte":
                print("Você perdeu sua vez de jogar")
                while VidaJogador > 0 and VidaOponente > 0:
                    
<<<<<<< HEAD
                    VidaJogador = VidaJogador - ( PoderOponente - DefesaJogador )
                    
                    if VidaJogador <= 0:        
                        print("Que pena,Você perdeu para o : {0}".format(inimigo))
                    
                    else:
                        ataque=int(input("Escolha seu ataque: Timbre de voz (1) ou Espectro Sonoro(2)"))
                        if ataque==1:
                            VidaOponente = VidaOponente - ( Poder1Jogador - DefesaOponente )
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
=======
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
<<<<<<< HEAD
                        
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
=======
                        print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                        print("Sua vida:",VidaJogador)
                        if VidaJogador <= 0:        
                            print("Você perdeu! para o : {0}".format(inimigo))
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                           
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
<<<<<<< HEAD
                            
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
=======
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                        
                        if VidaOponente <= 0:
                            print("Você derrotou o : {0}".format(inimigo))
                            Notasmusicais=Notasmusicais+10
                            Coins=Coins+20
                            print("coins",Coins)
                            print("notas",Notasmusicais)
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
                   
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
<<<<<<< HEAD
>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
<<<<<<< HEAD
                                print("Coins:",Coins)
                                print("Notas:",Notasmusicais)
                                
                        elif ataque==2:
                            VidaOponente = VidaOponente - ( Poder2Jogador - DefesaOponente )
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
=======
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
=======
                            print("Vida do {0} : {1}".format(inimigo,VidaOponente))
                            print("Sua vida:",VidaJogador)
                            
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
                            if VidaOponente <= 0:
                                print("Você derrotou o : {0}".format(inimigo))
                                Notasmusicais=Notasmusicais+10
                                Coins=Coins+20
<<<<<<< HEAD
                                print("Coins:",Coins)
                                print("Notas:",Notasmusicais)

=======
                                print("coins:",Coins)
                                print("notas",Notasmusicais)
<<<<<<< HEAD
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
=======
    
    elif inicio == 4:
        # arqsave=input("Qual o nome do seu arquivo?")
        # arqsave=arqsave.lower()
        # salvos.append(arqsave)
        # salvar
        with open("salvo.py", 'wb') as f:
            pickle.dump([Nome_do_Jogador, Notasmusicais, Coins, insperdex], f, protocol=2)
            print("O jogo foi salvo com sucesso!")
    elif inicio == 5:
        # print(salvos, " ")
        # arqload=input("Qual o arquivo voce deseja carreggar?")
        # arqload=arqload.lower()
        # carregar
        with open("salvo.py", 'rb') as f:
>>>>>>> bcab75686cc139f60b900d1ae5aa71739d7a1286
            Nome_do_Jogador, Notasmusicais, Coins, insperdex = pickle.load(f)
            print("O jogo foi carregado com sucesso!")                            
>>>>>>> 8407ee3beb1f94ae4e902cde7de7502ee8553bff
insperdex=set(insperdex)
insperdex=",".join(insperdex)
print("Estes foram os inspermons que cruzaram sua jornada:",insperdex)