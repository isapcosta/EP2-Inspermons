import json
def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))

    return  

with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)
for i in range(3):
    print(mostra_ipmon(inspermons[i]))
    

insperdex=[]
listadeinspermons={"picaxu":inspermons[0],'xamando':inspermons[1],"pigijet":inspermons[2]}
inspermoninicial=input("Qual seu inspermon inicial da lista?")

i=0
while i==0:
    inicio=input("Você quer passear ou dormir?")
    if inicio=="dormir":
        print("Bom descanso")
        break
    elif inicio=="passear":	
        inimigo=random.choice(list(listadeinspermons.keys()))
        insperdex.append(inimigo)
    
        print("Você acabou de encontrar o:",inimigo)
        VidaJogador=listadeinspermons[inspermoninicial]["vida"]
        VidaOponente=listadeinspermons[inimigo]["vida"]
        PoderJogador=listadeinspermons[inspermoninicial]["poder"]
        PoderOponente=listadeinspermons[inimigo]["poder"]
        DefesaJogador=listadeinspermons[inspermoninicial]["defesa"]
        DefesaOponente=listadeinspermons[inimigo]["defesa"]
        batalha=input("Você quer batalhar ou tentar fugir?")
        opcoes=['escapou','semsorte']
        if batalha=="batalhar":
            while VidaJogador > 0 and VidaOponente > 0:
            
                
                VidaOponente = VidaOponente - ( PoderJogador - DefesaOponente ) 
                
                if VidaOponente <= 0:
                    print("Você derrotou o : {0}".format(inimigo))
                else:
                    VidaJogador = VidaJogador - ( PoderOponente - DefesaJogador )
                    
                if VidaJogador <= 0:        
                    print("Você perdeu! para o : {0}".format(inimigo))
                    
        if batalha=="fugir":
            escolha=random.choice(opcoes)
            if escolha=="escapou":
                print("Ufa,Você escapou")
                continue
            if escolha=="semsorte":
                print("Você perdeu sua vez de jogar")
                while VidaJogador > 0 and VidaOponente > 0:
                    VidaJogador = VidaJogador - ( PoderOponente - DefesaJogador )
                    if VidaJogador <= 0:        
                        print("Que pena,Você perdeu para o : {0}".format(inimigo))
                    
                    else:
                        VidaOponente = VidaOponente - ( PoderJogador - DefesaOponente ) 
                    
                    if VidaOponente <= 0:
                        print("Você derrotou o : {0}".format(inimigo))

print("Estes foram os inspermons que cruzaram sua jornada",set(insperdex))