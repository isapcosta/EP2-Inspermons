# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:36:35 2017

@author: isadora
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:30:16 2017

@author: isadora
"""

import random
picaxu={"nome" : "picaxu",
"poder" : 20,
"vida" : 200,
"defesa" : 12}
	
xamando={"nome" : "xamando",
"poder" : 25,
"vida" : 100,
"defesa" : 10}
	
pidijet={"nome" : "pidijet",
"poder" : 15,
"vida" : 300,
"defesa" : 10}

insperdex=[]
listadeinspermons={"picaxu":picaxu,'xamando':xamando,"pigijet":pidijet}
print(listadeinspermons)
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