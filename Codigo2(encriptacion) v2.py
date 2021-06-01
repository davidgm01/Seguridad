#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:40:35 2020

@author: David
"""

import os
import filecmp
txt = open("Seguridad Código 2 para desencripción (para encriptar).txt", 'r+', encoding='utf-8').read().lower() #Abrir, leer y poner el archivo en minúscula
abecedario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','á','é','í','ó','ú',' '] #Crear el abecedario incluyendo el CR
n=33 #Cantidad de caracteres del abecedario
pospriletra=0
possegletra=0
postreletra=0
for a in range(26071,26076):
    for j in range (1,pow(n,3)+1):
        if (j*a)%pow(n,3)==1:
            for b in range(31331,31336):
                txt3= open ("Seguridad Código 2 para desencripción {} - {}.txt".format(a,b), 'w', encoding='utf-8') #Crear un nuevo archivo para guardarlo con las modificaciones
                for i in txt:
                    if i in abecedario:
                        txt = txt
                    elif i=='\n':
                        txt=txt.replace(i,' ')
                    else:
                        txt=txt.replace(i,'')
                #Si la cantidad de caracteres que tiene el archivo no es múltiplo de 2 se le agregan espacios hasta que este lo sea
                if len(txt)%3!=0:
                    while len(txt)%3!=0:
                        txt=txt+' '
                #Se realiza la encriptación de AFIN x2, mediante la utilización de la ecuación y se guarda en el archivo encriptado
                for i in range(0, len(txt),3):
                    for position, item in enumerate(abecedario):
                        if txt[i]==item:
                            pospriletra=position
                        if txt[i+1]==item:
                            possegletra=position
                        if txt[i+2]==item:
                            postreletra=position
                    encnum=(a*(pospriletra*(n**2)+possegletra*n+postreletra)+b)%(n**3)
                    pospriletra=int(encnum/(n**2))
                    possegletra=int((encnum%(n**2))/n)
                    postreletra=encnum%n
                    encripcion=abecedario[pospriletra] + abecedario[possegletra] + abecedario[postreletra]
                    txt3.write(encripcion)
                if filecmp.cmp("Seguridad Código 2 para desencripción.txt", "Seguridad Código 2 para desencripción {} - {}.txt".format(a,b))==True:
                    print("a= ", a, " y b= ", b)
                if os.path.exists("Seguridad Código 2 para desencripción {} - {}.txt".format(a,b)):
                    os.remove("Seguridad Código 2 para desencripción {} - {}.txt".format(a,b))
#txt3.close() #Cerrar el archivo creado para las modificaciones
print('Finalizado') #Mostrar en pantalla que el proceso se finalizó