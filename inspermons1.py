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
import 

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
    
        print("O seu inimigo de batalha é:",inimigo)
        VidaJogador=listadeinspermons[inspermoninicial]["vida"]
        VidaOponente=listadeinspermons[inimigo]["vida"]
        PoderJogador=listadeinspermons[inspermoninicial]["poder"]
        PoderOponente=listadeinspermons[inimigo]["poder"]
        DefesaJogador=listadeinspermons[inspermoninicial]["defesa"]
        DefesaOponente=listadeinspermons[inimigo]["defesa"]
        while VidaJogador > 0 and VidaOponente > 0:
            VidaOponente = VidaOponente - ( PoderJogador - DefesaOponente ) 
            if VidaOponente <= 0:
                print("Você ganhou a batalha!")
            else:
                VidaJogador = VidaJogador - ( PoderOponente - DefesaJogador )
                
            if VidaJogador <= 0:        
                print("Voce perdeu")
                

            
        
        
        
        
        
