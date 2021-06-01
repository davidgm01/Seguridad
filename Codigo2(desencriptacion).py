# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:30:18 2020

@author: David
"""

txt = open("Seguridad Código 2 para desencripción.txt", 'r+', encoding='utf-8').read().lower() #Abrir, leer y poner el archivo en minúscula
abecedario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','á','é','í','ó','ú',' '] #Crear el abecedario incluyendo el CR
n=33 #Cantidad de caracteres del abecedario
for ainv in range(17986,35937):
    for j in range (1,pow(n,3)+1):
        if (j*ainv)%pow(n,3)==1:
            for b in range(17986,35937):
                txt2= open ("Archivo desencriptado {} - {}.txt".format(ainv,b), 'w', encoding='utf-8') #Crear un nuevo archivo para guardarlo con las modificaciones
                for i in range(0, len(txt),3):
                    for position, item in enumerate(abecedario):
                        if txt[i]==item:
                            pospriletra=position
                        if txt[i+1]==item:
                            possegletra=position
                        if txt[i+2]==item:
                            postreletra=position
                    encnum=((((pospriletra*pow(n,2))+(possegletra*n)+postreletra)-b)*ainv)%(n**3)
                    pospriletra=int(encnum/pow(n,2))
                    possegletra=int((encnum%pow(n,2))/n)
                    postreletra=encnum%n
                    desencripcion=abecedario[pospriletra] + abecedario[possegletra] + abecedario[postreletra]
                    txt2.write(desencripcion)
                txt2.close()
                txt2= open ("Archivo desencriptado {} - {}.txt".format(ainv,b), 'r', encoding='utf-8').read()
                for word in txt2.split():
                    prueba=" " + word + " "
                    if prueba==" de ":
                        print ("Archivo desencriptado {} - {}.txt".format(ainv,b))
#txt2.close() #Cerrar el archivo creado para las modificaciones
print('Finalizado') #Mostrar en pantalla que el proceso se finalizó