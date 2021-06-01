# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:01:38 2020

@author: David
"""

txt = open("Seguridad Código 2 para desencripción.txt", 'r+', encoding='utf-8').read().lower() #Abrir, leer y poner el archivo en minúscula
txt2= open ("Seguridad Código 2 para desencripción (encriptado).txt", 'w', encoding='utf-8') #Crear un nuevo archivo para guardarlo con las modificaciones
abecedario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','á','é','í','ó','ú',' '] #Crear el abecedario incluyendo el CR
a=31861 #Valor a la variable a, para la ecuación
b=35099 #Valor a la variable b, para la ecuación
n=33 #Cantidad de caracteres del abecedario
#Quitar los caracteres que no pertenecen al abecedario o diccionario
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
    txt2.write(encripcion)
txt2.close() #Cerrar el archivo creado para las modificaciones
print('Finalizado') #Mostrar en pantalla que el proceso se finalizó