from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np

#-------------CREADORES PY----------#
#Autor: Cristofer Berganza
#Autor: Carlos Palma
#Seccion: "A"
#Curso: Algebra Lineal
#Tema: Matrices
#-----------------------------------#

#-------------VENTANA TKINTER-------#
global opciones
opciones = ["2X2","3X3","4X4"]
ventana = tk.Tk()
ventana.title("Solucion de Matrices")
ventana.geometry("650x90")
ventana.configure(background="#0E2C61")
#------------------------------------#
 

def inversa():

    def matrices(): 
        
        def proceso():
            
            numeros1 = numero1.get()
            numeros2 = numero2.get()
            numeros3 = numero3.get()
            numeros4 = numero4.get()
            
            m = np.array([[numeros1,numeros2],[numeros3,numeros4]],dtype=np.int16)
            
            mostrar = np.linalg.inv(m)
            
            mos = tk.Label(pestana, text=mostrar)
            mos.place(relx=0.40,rely=0.45)
        
        operacion = listado.get()
        if operacion == "2X2":
            numero1 = tk.Entry(pestana)
            numero1.place(relx= 0.40,rely=0.30)
            numero1.config(width=10)
            
            numero2 = tk.Entry(pestana)
            numero2.place(relx= 0.50,rely=0.30)
            numero2.config(width=10)
            
            numero3 = tk.Entry(pestana)
            numero3.place(relx= 0.40,rely=0.35)
            numero3.config(width=10)
            
            numero4 = tk.Entry(pestana)
            numero4.grid(column=0)
            numero4.place(relx= 0.50,rely=0.35)
            numero4.config(width=10)
            
            boton = tk.Button(pestana, 
                              text="Generar", 
                              command=proceso,
                              background="deepskyblue",
                              border = 3)
            
            boton.place(relx=0.45,rely=0.40)
            boton.config(width=8) 
            
        
        if(operacion == "3X3"):
            def proceso():
                numeros1 = numero1.get()
                numeros2 = numero2.get()
                numeros3 = numero3.get()
                numeros4 = numero4.get()
                numeros5 = numero5.get()
                numeros6 = numero6.get()
                numeros7 = numero7.get()
                numeros8 = numero8.get()
                numeros9 = numero9.get()
                    
            
                m = np.array([[numeros1,numeros2,numeros3],[numeros4,numeros5,numeros6],[numeros7,numeros8,numeros9]],dtype=np.int16)
            
                mostrar = np.linalg.inv(m)
            
                mos = tk.Label(pestana, text=mostrar)
                mos.place(relx=0.35, rely=0.70)
        
            numero1 = tk.Entry(pestana, border=3)
            numero1.place(relx= 0.30,rely=0.30)
            numero1.config(width=10)
            
            numero2 = tk.Entry(pestana, border=3)
            numero2.place(relx= 0.45,rely=0.30)
            numero2.config(width=10)
            
            numero3 = tk.Entry(pestana, border=3)
            numero3.place(relx= 0.60,rely=0.30)
            numero3.config(width=10)
            
            numero4 = tk.Entry(pestana, border=3)
            numero4.place(relx= 0.30,rely=0.40)
            numero4.config(width=10)
                    
            numero5 = tk.Entry(pestana, border=3)
            numero5.place(relx= 0.45,rely=0.40)
            numero5.config(width=10)
                    
            numero6 = tk.Entry(pestana, border=3)
            numero6.place(relx= 0.60,rely=0.40)
            numero6.config(width=10)
                    
            numero7 = tk.Entry(pestana, border=3)
            numero7.place(relx= 0.30,rely=0.50)
            numero7.config(width=10)
                    
            numero8 = tk.Entry(pestana, border=3)
            numero8.place(relx= 0.45,rely=0.50)
            numero8.config(width=10)
                    
            numero9 = tk.Entry(pestana, border=3)
            numero9.place(relx= 0.60,rely=0.50)
            numero9.config(width=10)
            
            boton = tk.Button(pestana, 
                              text="Generar", 
                              command=proceso,
                              background="deepskyblue",
                              border = 3)
            
            boton.place(relx=0.45,rely=0.60)
            boton.config(width=8)
                    
            
        if(operacion == "4X4"):
            def proceso():
                numeros1 = numero1.get()
                numeros2 = numero2.get()
                numeros3 = numero3.get()
                numeros4 = numero4.get()
                numeros5 = numero5.get()
                numeros6 = numero6.get()
                numeros7 = numero7.get()
                numeros8 = numero8.get()
                numeros9 = numero9.get()
                numeros10 = numero10.get()
                numeros11 = numero11.get()
                numeros12 = numero12.get()
                numeros13 = numero13.get()
                numeros14 = numero14.get()
                numeros15 = numero15.get()
                numeros16 = numero16.get()
                    
            
                m = np.array([[numeros1,numeros2,numeros3,numeros4],[numeros5,numeros6,numeros7,numeros8],[numeros9,numeros10,numeros11,numeros12],[numeros13,numeros14,numeros15,numeros16]],dtype=np.int16)
            
                mostrar = np.linalg.inv(m)
            
                mos = tk.Label(pestana, text=mostrar)
                mos.place(relx=0.32, rely=0.55)
                
                m = 0
                
            #FILA1        
            numero1 = tk.Entry(pestana, border=3)
            numero1.place(relx= 0.30,rely=0.30)
            numero1.config(width="10")
            
            numero2 = tk.Entry(pestana, border=3)
            numero2.place(relx= 0.40,rely=0.30)
            numero2.config(width="10")
            
            numero3 = tk.Entry(pestana, border=3)
            numero3.place(relx= 0.50,rely=0.30)
            numero3.config(width="10")
            
            numero4 = tk.Entry(pestana, border=3)
            numero4.place(relx= 0.60,rely=0.30)
            numero4.config(width="10")
            #FILA2        
            numero5 = tk.Entry(pestana, border=3)
            numero5.place(relx= 0.30,rely=0.35)
            numero5.config(width="10")
                    
            numero6 = tk.Entry(pestana, border=3)
            numero6.place(relx= 0.40,rely=0.35)
            numero6.config(width="10")
                    
            numero7 = tk.Entry(pestana, border=3)
            numero7.place(relx= 0.50,rely=0.35)
            numero7.config(width="10")
                    
            numero8 = tk.Entry(pestana, border=3)
            numero8.place(relx= 0.60,rely=0.35)
            numero8.config(width="10")
            #FILA3        
            numero9 = tk.Entry(pestana, border=3)
            numero9.place(relx= 0.30,rely=0.40)
            numero9.config(width="10")
            
            numero10 = tk.Entry(pestana, border=3)
            numero10.place(relx= 0.40,rely=0.40)
            numero10.config(width="10")
            
            numero11 = tk.Entry(pestana, border=3)
            numero11.place(relx= 0.50,rely=0.40)
            numero11.config(width="10")
            
            numero12 = tk.Entry(pestana, border=3)
            numero12.place(relx= 0.60,rely=0.40)
            numero12.config(width="10")
            #FILA4
            numero13 = tk.Entry(pestana, border=3)
            numero13.place(relx= 0.60,rely=0.45)
            numero13.config(width="10")
            
            numero14 = tk.Entry(pestana, border=3)
            numero14.place(relx= 0.30,rely=0.45)
            numero14.config(width="10")
            
            numero15 = tk.Entry(pestana, border=3)
            numero15.place(relx= 0.40,rely=0.45)
            numero15.config(width="10")
            
            numero16 = tk.Entry(pestana, border=3)
            numero16.place(relx= 0.50,rely=0.45)
            numero16.config(width="10")
            
            boton = tk.Button(pestana, text="Generar", command=proceso)
            boton.place(relx=0.45,rely=0.50)
            boton.config(width=8)
            
    pestana = Toplevel()
    pestana.geometry("650x500") 
    pestana.configure(background="#0E2C61")
                    
    texto1 = tk.Label(pestana,text="Seleccione la siguiente opcion:")
    texto1.place(relx=0.40)

    listado = ttk.Combobox(pestana, width=17)
    listado.place(relx=0.35, rely=0.10)
    
    listado['values']=opciones
    
    obtener = tk.Button(pestana, 
                        text="Siguiente", 
                        command=matrices,
                        background="deepskyblue",
                        border = 3)
    
    obtener.place(relx=0.55, rely=0.09)  
    
#----------------------------------------------------------------------

def multiplicacion():
#---------------------------MATRIZ 2---------------------
    def matriz2():
        pestana4 = Toplevel()
        pestana4.geometry("650x500") 
        pestana4.configure(background="#0E2C61")
    
        def proceso1():
                 
            numeros1 = numero1.get()
            numeros2 = numero2.get()
            numeros3 = numero3.get()
            numeros4 = numero4.get()
            
            global m2
            m2 = np.array([[numeros1,numeros2],[numeros3,numeros4]],dtype=np.int16)
            
        operacion = listado.get()
        if operacion == "2X2":
            numero1 = tk.Entry(pestana4)
            numero1.place(relx= 0.40,rely=0.30)
            numero1.config(width=10)
            
            numero2 = tk.Entry(pestana4)
            numero2.place(relx= 0.50,rely=0.30)
            numero2.config(width=10)
            
            numero3 = tk.Entry(pestana4)
            numero3.place(relx= 0.40,rely=0.35)
            numero3.config(width=10)
            
            numero4 = tk.Entry(pestana4)
            numero4.grid(column=0)
            numero4.place(relx= 0.50,rely=0.35)
            numero4.config(width=10)
            
            boton = tk.Button(pestana4, 
                              text="Generar", 
                              command=proceso1,
                              background="deepskyblue",
                              border = 3)
            
            boton.place(relx=0.45,rely=0.40)
            boton.config(width=8) 
            
        
        if(operacion == "3X3"):
            def proceso():
                numeros1 = numero1.get()
                numeros2 = numero2.get()
                numeros3 = numero3.get()
                numeros4 = numero4.get()
                numeros5 = numero5.get()
                numeros6 = numero6.get()
                numeros7 = numero7.get()
                numeros8 = numero8.get()
                numeros9 = numero9.get()
                    
                global m2
                m2 = np.array([[numeros1,numeros2,numeros3],[numeros4,numeros5,numeros6],[numeros7,numeros8,numeros9]],dtype=np.int16)
            
            
            numero1 = tk.Entry(pestana4, border=3)
            numero1.place(relx= 0.30,rely=0.30)
            numero1.config(width=10)
            
            numero2 = tk.Entry(pestana4, border=3)
            numero2.place(relx= 0.45,rely=0.30)
            numero2.config(width=10)
            
            numero3 = tk.Entry(pestana4, border=3)
            numero3.place(relx= 0.60,rely=0.30)
            numero3.config(width=10)
            
            numero4 = tk.Entry(pestana4, border=3)
            numero4.place(relx= 0.30,rely=0.40)
            numero4.config(width=10)
                    
            numero5 = tk.Entry(pestana4, border=3)
            numero5.place(relx= 0.45,rely=0.40)
            numero5.config(width=10)
                    
            numero6 = tk.Entry(pestana4, border=3)
            numero6.place(relx= 0.60,rely=0.40)
            numero6.config(width=10)
                    
            numero7 = tk.Entry(pestana4, border=3)
            numero7.place(relx= 0.30,rely=0.50)
            numero7.config(width=10)
                    
            numero8 = tk.Entry(pestana4, border=3)
            numero8.place(relx= 0.45,rely=0.50)
            numero8.config(width=10)
                    
            numero9 = tk.Entry(pestana4, border=3)
            numero9.place(relx= 0.60,rely=0.50)
            numero9.config(width=10)
            
            boton = tk.Button(pestana4, 
                              text="Generar", 
                              command=proceso,
                              background="deepskyblue",
                              border = 3)
            
            boton.place(relx=0.45,rely=0.60)
            boton.config(width=8)
                    
            
        if(operacion == "4X4"):
            def proceso():
                numeros1 = numero1.get()
                numeros2 = numero2.get()
                numeros3 = numero3.get()
                numeros4 = numero4.get()
                numeros5 = numero5.get()
                numeros6 = numero6.get()
                numeros7 = numero7.get()
                numeros8 = numero8.get()
                numeros9 = numero9.get()
                numeros10 = numero10.get()
                numeros11 = numero11.get()
                numeros12 = numero12.get()
                numeros13 = numero13.get()
                numeros14 = numero14.get()
                numeros15 = numero15.get()
                numeros16 = numero16.get()
                    
                global m2
                m2 = np.array([[numeros1,numeros2,numeros3,numeros4],[numeros5,numeros6,numeros7,numeros8],[numeros9,numeros10,numeros11,numeros12],[numeros13,numeros14,numeros15,numeros16]],dtype=np.int16)
                  
            #FILA1        
            numero1 = tk.Entry(pestana4, border=3)
            numero1.place(relx= 0.30,rely=0.30)
            numero1.config(width="10")
            
            numero2 = tk.Entry(pestana4, border=3)
            numero2.place(relx= 0.40,rely=0.30)
            numero2.config(width="10")
            
            numero3 = tk.Entry(pestana4, border=3)
            numero3.place(relx= 0.50,rely=0.30)
            numero3.config(width="10")
            
            numero4 = tk.Entry(pestana4, border=3)
            numero4.place(relx= 0.60,rely=0.30)
            numero4.config(width="10")
            #FILA2        
            numero5 = tk.Entry(pestana4, border=3)
            numero5.place(relx= 0.30,rely=0.35)
            numero5.config(width="10")
                    
            numero6 = tk.Entry(pestana4, border=3)
            numero6.place(relx= 0.40,rely=0.35)
            numero6.config(width="10")
                    
            numero7 = tk.Entry(pestana4, border=3)
            numero7.place(relx= 0.50,rely=0.35)
            numero7.config(width="10")
                    
            numero8 = tk.Entry(pestana4, border=3)
            numero8.place(relx= 0.60,rely=0.35)
            numero8.config(width="10")
            #FILA3        
            numero9 = tk.Entry(pestana4, border=3)
            numero9.place(relx= 0.30,rely=0.40)
            numero9.config(width="10")
            
            numero10 = tk.Entry(pestana4, border=3)
            numero10.place(relx= 0.40,rely=0.40)
            numero10.config(width="10")
            
            numero11 = tk.Entry(pestana4, border=3)
            numero11.place(relx= 0.50,rely=0.40)
            numero11.config(width="10")
            
            numero12 = tk.Entry(pestana4, border=3)
            numero12.place(relx= 0.60,rely=0.40)
            numero12.config(width="10")
            #FILA4
            numero13 = tk.Entry(pestana4, border=3)
            numero13.place(relx= 0.60,rely=0.45)
            numero13.config(width="10")
            
            numero14 = tk.Entry(pestana4, border=3)
            numero14.place(relx= 0.30,rely=0.45)
            numero14.config(width="10")
            
            numero15 = tk.Entry(pestana4, border=3)
            numero15.place(relx= 0.40,rely=0.45)
            numero15.config(width="10")
            
            numero16 = tk.Entry(pestana4, border=3)
            numero16.place(relx= 0.50,rely=0.45)
            numero16.config(width="10")
            
            boton = tk.Button(pestana4, text="Generar", command=proceso)
            boton.place(relx=0.45,rely=0.50)
            boton.config(width=8)
    
#-------------------------MATRIZ #1--------------------------    
    def matriz1():
        pestana3 = Toplevel()
        pestana3.geometry("650x500") 
        pestana3.configure(background="#0E2C61")
       
        
        def proceso1():
                 
            numeros1 = numero1.get()
            numeros2 = numero2.get()
            numeros3 = numero3.get()
            numeros4 = numero4.get()
            
            global m
            m = np.array([[numeros1,numeros2],[numeros3,numeros4]],dtype=np.int16)
            
        operacion = listado.get()
        if operacion == "2X2":
            numero1 = tk.Entry(pestana3)
            numero1.place(relx= 0.40,rely=0.30)
            numero1.config(width=10)
            
            numero2 = tk.Entry(pestana3)
            numero2.place(relx= 0.50,rely=0.30)
            numero2.config(width=10)
            
            numero3 = tk.Entry(pestana3)
            numero3.place(relx= 0.40,rely=0.35)
            numero3.config(width=10)
            
            numero4 = tk.Entry(pestana3)
            numero4.grid(column=0)
            numero4.place(relx= 0.50,rely=0.35)
            numero4.config(width=10)
            
            boton = tk.Button(pestana3, 
                              text="Generar", 
                              command=proceso1,
                              background="deepskyblue",
                              border = 3)
            
            boton.place(relx=0.45,rely=0.40)
            boton.config(width=8) 
            
        
        if(operacion == "3X3"):
            def proceso():
                numeros1 = numero1.get()
                numeros2 = numero2.get()
                numeros3 = numero3.get()
                numeros4 = numero4.get()
                numeros5 = numero5.get()
                numeros6 = numero6.get()
                numeros7 = numero7.get()
                numeros8 = numero8.get()
                numeros9 = numero9.get()
                    
                global m
                m = np.array([[numeros1,numeros2,numeros3],[numeros4,numeros5,numeros6],[numeros7,numeros8,numeros9]],dtype=np.int16)
            
            
            numero1 = tk.Entry(pestana3, border=3)
            numero1.place(relx= 0.30,rely=0.30)
            numero1.config(width=10)
            
            numero2 = tk.Entry(pestana3, border=3)
            numero2.place(relx= 0.45,rely=0.30)
            numero2.config(width=10)
            
            numero3 = tk.Entry(pestana3, border=3)
            numero3.place(relx= 0.60,rely=0.30)
            numero3.config(width=10)
            
            numero4 = tk.Entry(pestana3, border=3)
            numero4.place(relx= 0.30,rely=0.40)
            numero4.config(width=10)
                    
            numero5 = tk.Entry(pestana3, border=3)
            numero5.place(relx= 0.45,rely=0.40)
            numero5.config(width=10)
                    
            numero6 = tk.Entry(pestana3, border=3)
            numero6.place(relx= 0.60,rely=0.40)
            numero6.config(width=10)
                    
            numero7 = tk.Entry(pestana3, border=3)
            numero7.place(relx= 0.30,rely=0.50)
            numero7.config(width=10)
                    
            numero8 = tk.Entry(pestana3, border=3)
            numero8.place(relx= 0.45,rely=0.50)
            numero8.config(width=10)
                    
            numero9 = tk.Entry(pestana3, border=3)
            numero9.place(relx= 0.60,rely=0.50)
            numero9.config(width=10)
            
            boton = tk.Button(pestana3, 
                              text="Generar", 
                              command=proceso,
                              background="deepskyblue",
                              border = 3)
            
            boton.place(relx=0.45,rely=0.60)
            boton.config(width=8)
                    
            
        if(operacion == "4X4"):
            def proceso():
                numeros1 = numero1.get()
                numeros2 = numero2.get()
                numeros3 = numero3.get()
                numeros4 = numero4.get()
                numeros5 = numero5.get()
                numeros6 = numero6.get()
                numeros7 = numero7.get()
                numeros8 = numero8.get()
                numeros9 = numero9.get()
                numeros10 = numero10.get()
                numeros11 = numero11.get()
                numeros12 = numero12.get()
                numeros13 = numero13.get()
                numeros14 = numero14.get()
                numeros15 = numero15.get()
                numeros16 = numero16.get()
                    
                global m
                m = np.array([[numeros1,numeros2,numeros3,numeros4],[numeros5,numeros6,numeros7,numeros8],[numeros9,numeros10,numeros11,numeros12],[numeros13,numeros14,numeros15,numeros16]],dtype=np.int16)
                  
            #FILA1        
            numero1 = tk.Entry(pestana3, border=3)
            numero1.place(relx= 0.30,rely=0.30)
            numero1.config(width="10")
            
            numero2 = tk.Entry(pestana3, border=3)
            numero2.place(relx= 0.40,rely=0.30)
            numero2.config(width="10")
            
            numero3 = tk.Entry(pestana3, border=3)
            numero3.place(relx= 0.50,rely=0.30)
            numero3.config(width="10")
            
            numero4 = tk.Entry(pestana3, border=3)
            numero4.place(relx= 0.60,rely=0.30)
            numero4.config(width="10")
            #FILA2        
            numero5 = tk.Entry(pestana3, border=3)
            numero5.place(relx= 0.30,rely=0.35)
            numero5.config(width="10")
                    
            numero6 = tk.Entry(pestana3, border=3)
            numero6.place(relx= 0.40,rely=0.35)
            numero6.config(width="10")
                    
            numero7 = tk.Entry(pestana3, border=3)
            numero7.place(relx= 0.50,rely=0.35)
            numero7.config(width="10")
                    
            numero8 = tk.Entry(pestana3, border=3)
            numero8.place(relx= 0.60,rely=0.35)
            numero8.config(width="10")
            #FILA3        
            numero9 = tk.Entry(pestana3, border=3)
            numero9.place(relx= 0.30,rely=0.40)
            numero9.config(width="10")
            
            numero10 = tk.Entry(pestana3, border=3)
            numero10.place(relx= 0.40,rely=0.40)
            numero10.config(width="10")
            
            numero11 = tk.Entry(pestana3, border=3)
            numero11.place(relx= 0.50,rely=0.40)
            numero11.config(width="10")
            
            numero12 = tk.Entry(pestana3, border=3)
            numero12.place(relx= 0.60,rely=0.40)
            numero12.config(width="10")
            #FILA4
            numero13 = tk.Entry(pestana3, border=3)
            numero13.place(relx= 0.60,rely=0.45)
            numero13.config(width="10")
            
            numero14 = tk.Entry(pestana3, border=3)
            numero14.place(relx= 0.30,rely=0.45)
            numero14.config(width="10")
            
            numero15 = tk.Entry(pestana3, border=3)
            numero15.place(relx= 0.40,rely=0.45)
            numero15.config(width="10")
            
            numero16 = tk.Entry(pestana3, border=3)
            numero16.place(relx= 0.50,rely=0.45)
            numero16.config(width="10")
            
            boton = tk.Button(pestana3, text="Generar", command=proceso)
            boton.place(relx=0.45,rely=0.50)
            boton.config(width=8)
            
    def matriz_final():
        mf = np.dot(m,m2)
            
        mos = tk.Label(pestana2, text=mf)
        mos.place(relx=0.45,rely=0.45)
        
        
        
         

    pestana2 = Toplevel()
    pestana2.geometry("650x500") 
    pestana2.configure(background="#0E2C61")
     
    texto1 = tk.Label(pestana2,text="Seleccione tipo matriz #1:")
    texto1.place(relx=0.40)

    listado = ttk.Combobox(pestana2, width=17)
    listado.place(relx=0.35, rely=0.10)
    
    listado['values']=opciones

    obtener = tk.Button(pestana2, 
                        text="Siguiente", 
                        command=matriz1,
                        background="deepskyblue",
                        border = 3)
    
    obtener.place(relx=0.55, rely=0.09)
    
    texto1 = tk.Label(pestana2,text="Seleccione tipo matriz #2:")
    texto1.place(relx=0.40, rely=0.17)

    listado2 = ttk.Combobox(pestana2, width=17)
    listado2.place(relx=0.35, rely=0.25)
    
    listado2['values']=opciones

    obtener = tk.Button(pestana2, 
                        text="Siguiente", 
                        command=matriz2,
                        background="deepskyblue",
                        border = 3)
    
    obtener.place(relx=0.55, rely=0.25)
    
    obtener = tk.Button(pestana2, 
                        text="Generar Matriz", 
                        command=matriz_final,
                        background="deepskyblue",
                        border = 3)
    
    obtener.place(relx=0.45, rely=0.35)
    
#----------------------------------------------------------------
#----------------------------------------------------------------
def sistem_ecuaciones():
    
    def gauss_jordan():
        def procesamiento():
            def proceso():
                
                numeros1 = float(numero1.get())
                numeros2 = float(numero2.get())
                numeros3 = float(numero3.get())
                numeros4 = float(numero4.get())           
                
                m1 = np.array([[numeros1,numeros2],[numeros3,numeros4]])
                    
                mostrar = np.linalg.det(m1)
                    
                mos = tk.Label(pestana5, text=mostrar)
                mos.place(relx=0.45, rely=0.65)
            
            operacion = listado.get()
            if operacion == "2X2":
                numero1 = tk.Entry(pestana5)
                numero1.place(relx= 0.40,rely=0.30)
                numero1.config(width=10)
                
                numero2 = tk.Entry(pestana5)
                numero2.place(relx= 0.50,rely=0.30)
                numero2.config(width=10)
                    
                numero3 = tk.Entry(pestana5)
                numero3.place(relx= 0.40,rely=0.35)
                numero3.config(width="10")
                    
                numero4 = tk.Entry(pestana5)
                numero4.place(relx= 0.50,rely=0.35)
                numero4.config(width="10")
                
                vec1 = tk.Entry(pestana5, border=3)
                vec1.place(relx= 0.40,rely=0.45)
                vec1.config(width="10")
                    
                vec2 = tk.Entry(pestana5, border=3)
                vec2.place(relx= 0.50,rely=0.45)
                vec2.config(width="10")
                    
                boton1 = tk.Button(pestana5, 
                                text="Generar", 
                                command=proceso,
                                background="deepskyblue",
                                border = 3)
                    
                boton1.place(relx=0.45,rely=0.50)
                boton1.config(width=8) 
                    
                
            if(operacion == "3X3"):
                def proceso():
                    numeros1 = float(numero1.get())
                    numeros2 = float(numero2.get())
                    numeros3 = float(numero3.get())
                    numeros4 = float(numero4.get())
                    numeros5 = float(numero5.get())
                    numeros6 = float(numero6.get())
                    numeros7 = float(numero7.get())
                    numeros8 = float(numero8.get())
                    numeros9 = float(numero9.get())
                                                              
                    m1 = np.array([[numeros1,numeros2,numeros3],[numeros4,numeros5,numeros6],[numeros7,numeros8,numeros9]])                 
                    mostrar = np.linalg.det(m1)
                    
                    mos = tk.Label(pestana5, text=mostrar)
                    mos.place(relx=0.45, rely=0.75)
                
                numero1 = tk.Entry(pestana5, border=3)
                numero1.place(relx= 0.30,rely=0.30)
                numero1.config(width=10)
                    
                numero2 = tk.Entry(pestana5, border=3)
                numero2.place(relx= 0.45,rely=0.30)
                numero2.config(width=10)
                    
                numero3 = tk.Entry(pestana5, border=3)
                numero3.place(relx= 0.60,rely=0.30)
                numero3.config(width=10)
                    
                numero4 = tk.Entry(pestana5, border=3)
                numero4.place(relx= 0.30,rely=0.40)
                numero4.config(width=10)
                            
                numero5 = tk.Entry(pestana5, border=3)
                numero5.place(relx= 0.45,rely=0.40)
                numero5.config(width=10)
                            
                numero6 = tk.Entry(pestana5, border=3)
                numero6.place(relx= 0.60,rely=0.40)
                numero6.config(width=10)
                            
                numero7 = tk.Entry(pestana5, border=3)
                numero7.place(relx= 0.30,rely=0.50)
                numero7.config(width=10)
                            
                numero8 = tk.Entry(pestana5, border=3)
                numero8.place(relx= 0.45,rely=0.50)
                numero8.config(width=10)
                            
                numero9 = tk.Entry(pestana5, border=3)
                numero9.place(relx= 0.60,rely=0.50)
                numero9.config(width=10)
                    
                boton = tk.Button(pestana5, 
                                text="Generar", 
                                command=proceso,
                                background="deepskyblue",
                                border = 3)
                    
                boton.place(relx=0.45,rely=0.65)
                boton.config(width=8)
                            
                    
            if(operacion == "4X4"):
                def proceso():
                    numeros1 = float(numero1.get())
                    numeros2 = float(numero2.get())
                    numeros3 = float(numero3.get())
                    numeros4 = float(numero4.get())
                    numeros5 = float(numero5.get())
                    numeros6 = float(numero6.get())
                    numeros7 = float(numero7.get())
                    numeros8 = float(numero8.get())
                    numeros9 = float(numero9.get())
                    numeros10 = float(numero10.get())
                    numeros11 = float(numero11.get())
                    numeros12 = float(numero12.get())
                    numeros13 = float(numero13.get())
                    numeros14 = float(numero14.get())
                    numeros15 = float(numero15.get())
                    numeros16 = float(numero16.get())
                                     
                            
                    m1 = np.array([[numeros1,numeros2,numeros3,numeros4],[numeros5,numeros6,numeros7,numeros8],[numeros9,numeros10,numeros11,numeros12],[numeros13,numeros14,numeros15,numeros16]])
                    
                    
                    mostrar = np.linalg.det(m1)
                    
                    mos = tk.Label(pestana5, text=mostrar)
                    mos.place(relx=0.50, rely=0.65)
                        
                    #FILA1        
                numero1 = tk.Entry(pestana5, border=3)
                numero1.place(relx= 0.30,rely=0.30)
                numero1.config(width="10")
                    
                numero2 = tk.Entry(pestana5, border=3)
                numero2.place(relx= 0.40,rely=0.30)
                numero2.config(width="10")
                    
                numero3 = tk.Entry(pestana5, border=3)
                numero3.place(relx= 0.50,rely=0.30)
                numero3.config(width="10")
                    
                numero4 = tk.Entry(pestana5, border=3)  
                numero4.place(relx= 0.60,rely=0.30)
                numero4.config(width="10")
                    #FILA2        
                numero5 = tk.Entry(pestana5, border=3)
                numero5.place(relx= 0.30,rely=0.35)
                numero5.config(width="10")
                            
                numero6 = tk.Entry(pestana5, border=3)
                numero6.place(relx= 0.40,rely=0.35)
                numero6.config(width="10")
                            
                numero7 = tk.Entry(pestana5, border=3)
                numero7.place(relx= 0.50,rely=0.35)
                numero7.config(width="10")
                            
                numero8 = tk.Entry(pestana5, border=3)
                numero8.place(relx= 0.60,rely=0.35)
                numero8.config(width="10")
                    #FILA3        
                numero9 = tk.Entry(pestana5, border=3)
                numero9.place(relx= 0.30,rely=0.40)
                numero9.config(width="10")
                    
                numero10 = tk.Entry(pestana5, border=3)
                numero10.place(relx= 0.40,rely=0.40)
                numero10.config(width="10")
                    
                numero11 = tk.Entry(pestana5, border=3)
                numero11.place(relx= 0.50,rely=0.40)
                numero11.config(width="10")
                    
                numero12 = tk.Entry(pestana5, border=3)
                numero12.place(relx= 0.60,rely=0.40)
                numero12.config(width="10")
                    #FILA4
                numero13 = tk.Entry(pestana5, border=3)
                numero13.place(relx= 0.60,rely=0.45)
                numero13.config(width="10")
                    
                numero14 = tk.Entry(pestana5, border=3)
                numero14.place(relx= 0.30,rely=0.45)
                numero14.config(width="10")
                    
                numero15 = tk.Entry(pestana5, border=3)
                numero15.place(relx= 0.40,rely=0.45)
                numero15.config(width="10")
                    
                numero16 = tk.Entry(pestana5, border=3)
                numero16.place(relx= 0.50,rely=0.45)
                numero16.config(width="10")
                    
                
                obtener = tk.Button(pestana5, 
                        text="Siguiente", 
                        command=proceso,
                        background="deepskyblue",
                        border = 3)
    
                obtener.place(relx=0.45, rely=0.60)
                       
        texto1 = tk.Label(pestana5,text="Seleccione la siguiente opcion:")
        texto1.place(relx=0.38, rely=0.11)
        
        listado = ttk.Combobox(pestana5, width=17)
        listado.place(relx=0.35, rely=0.16)
    
        listado['values']=opciones
    
        obtener = tk.Button(pestana5, 
                        text="Siguiente", 
                        command=procesamiento,
                        background="deepskyblue",
                        border = 3)
    
        obtener.place(relx=0.55, rely=0.16)
        
    def krammer():
        def procesamiento():
            def proceso():
                
                numeros1 = float(numero1.get())
                numeros2 = float(numero2.get())
                numeros3 = float(numero3.get())
                numeros4 = float(numero4.get())
                
                vector1 = float(vec1.get())
                vector2 = float(vec2.get())
                
                m1 = np.array([[numeros1,numeros2],[numeros3,numeros4]])
                vc = [[vector1],[vector2]]
                    
                mostrar = np.linalg.solve(m1,vc)
                    
                mos = tk.Label(pestana5, text=mostrar)
                mos.place(relx=0.45, rely=0.65)
            
            operacion = listado.get()
            if operacion == "2X2":
                numero1 = tk.Entry(pestana5)
                numero1.place(relx= 0.40,rely=0.30)
                numero1.config(width=10)
                
                numero2 = tk.Entry(pestana5)
                numero2.place(relx= 0.50,rely=0.30)
                numero2.config(width=10)
                    
                numero3 = tk.Entry(pestana5)
                numero3.place(relx= 0.40,rely=0.35)
                numero3.config(width="10")
                    
                numero4 = tk.Entry(pestana5)
                numero4.place(relx= 0.50,rely=0.35)
                numero4.config(width="10")
                
                vec1 = tk.Entry(pestana5, border=3)
                vec1.place(relx= 0.40,rely=0.45)
                vec1.config(width="10")
                    
                vec2 = tk.Entry(pestana5, border=3)
                vec2.place(relx= 0.50,rely=0.45)
                vec2.config(width="10")
                    
                boton1 = tk.Button(pestana5, 
                                text="Generar", 
                                command=proceso,
                                background="deepskyblue",
                                border = 3)
                    
                boton1.place(relx=0.45,rely=0.50)
                boton1.config(width=8) 
                    
                
            if(operacion == "3X3"):
                def proceso():
                    numeros1 = float(numero1.get())
                    numeros2 = float(numero2.get())
                    numeros3 = float(numero3.get())
                    numeros4 = float(numero4.get())
                    numeros5 = float(numero5.get())
                    numeros6 = float(numero6.get())
                    numeros7 = float(numero7.get())
                    numeros8 = float(numero8.get())
                    numeros9 = float(numero9.get())
                    
                    vector1 = float(vec1.get())
                    vector2 = float(vec2.get())
                    vector3 = float(vec3.get())
                            
                    
                    m1 = np.array([[numeros1,numeros2,numeros3],[numeros4,numeros5,numeros6],[numeros7,numeros8,numeros9]])
                    vc = [[vector1], [vector2],[vector3]]
                    
                    mostrar = np.linalg.solve(m1,vc)
                    
                    mos = tk.Label(pestana5, text=mostrar)
                    mos.place(relx=0.45, rely=0.75)
                
                numero1 = tk.Entry(pestana5, border=3)
                numero1.place(relx= 0.30,rely=0.30)
                numero1.config(width=10)
                    
                numero2 = tk.Entry(pestana5, border=3)
                numero2.place(relx= 0.45,rely=0.30)
                numero2.config(width=10)
                    
                numero3 = tk.Entry(pestana5, border=3)
                numero3.place(relx= 0.60,rely=0.30)
                numero3.config(width=10)
                    
                numero4 = tk.Entry(pestana5, border=3)
                numero4.place(relx= 0.30,rely=0.40)
                numero4.config(width=10)
                            
                numero5 = tk.Entry(pestana5, border=3)
                numero5.place(relx= 0.45,rely=0.40)
                numero5.config(width=10)
                            
                numero6 = tk.Entry(pestana5, border=3)
                numero6.place(relx= 0.60,rely=0.40)
                numero6.config(width=10)
                            
                numero7 = tk.Entry(pestana5, border=3)
                numero7.place(relx= 0.30,rely=0.50)
                numero7.config(width=10)
                            
                numero8 = tk.Entry(pestana5, border=3)
                numero8.place(relx= 0.45,rely=0.50)
                numero8.config(width=10)
                            
                numero9 = tk.Entry(pestana5, border=3)
                numero9.place(relx= 0.60,rely=0.50)
                numero9.config(width=10)
                
                vec1 = tk.Entry(pestana5, border=3)
                vec1.place(relx= 0.30,rely=0.60)
                vec1.config(width="10")
                    
                vec2 = tk.Entry(pestana5, border=3)
                vec2.place(relx= 0.45,rely=0.60)
                vec2.config(width="10")
                    
                vec3 = tk.Entry(pestana5, border=3)
                vec3.place(relx= 0.60,rely=0.60)
                vec3.config(width="10")
                    
                boton = tk.Button(pestana5, 
                                text="Generar", 
                                command=proceso,
                                background="deepskyblue",
                                border = 3)
                    
                boton.place(relx=0.45,rely=0.65)
                boton.config(width=8)
                            
                    
            if(operacion == "4X4"):
                def proceso():
                    numeros1 = float(numero1.get())
                    numeros2 = float(numero2.get())
                    numeros3 = float(numero3.get())
                    numeros4 = float(numero4.get())
                    numeros5 = float(numero5.get())
                    numeros6 = float(numero6.get())
                    numeros7 = float(numero7.get())
                    numeros8 = float(numero8.get())
                    numeros9 = float(numero9.get())
                    numeros10 = float(numero10.get())
                    numeros11 = float(numero11.get())
                    numeros12 = float(numero12.get())
                    numeros13 = float(numero13.get())
                    numeros14 = float(numero14.get())
                    numeros15 = float(numero15.get())
                    numeros16 = float(numero16.get())
                    
                    vector1 = float(vec1.get())
                    vector2 = float(vec2.get())
                    vector3 = float(vec3.get())
                    vector4 = float(vec4.get())
                    
                        
                            
                    m1 = np.array([[numeros1,numeros2,numeros3,numeros4],[numeros5,numeros6,numeros7,numeros8],[numeros9,numeros10,numeros11,numeros12],[numeros13,numeros14,numeros15,numeros16]], dtype=np.int16)
                    vc = [[vector1], [vector2],[vector3], [vector4]]
                    
                    mostrar = np.linalg.solve(m1,vc)
                    
                    mos = tk.Label(pestana5, text=mostrar)
                    mos.place(relx=0.50, rely=0.65)
                        
                    #FILA1        
                numero1 = tk.Entry(pestana5, border=3)
                numero1.place(relx= 0.30,rely=0.30)
                numero1.config(width="10")
                    
                numero2 = tk.Entry(pestana5, border=3)
                numero2.place(relx= 0.40,rely=0.30)
                numero2.config(width="10")
                    
                numero3 = tk.Entry(pestana5, border=3)
                numero3.place(relx= 0.50,rely=0.30)
                numero3.config(width="10")
                    
                numero4 = tk.Entry(pestana5, border=3)  
                numero4.place(relx= 0.60,rely=0.30)
                numero4.config(width="10")
                    #FILA2        
                numero5 = tk.Entry(pestana5, border=3)
                numero5.place(relx= 0.30,rely=0.35)
                numero5.config(width="10")
                            
                numero6 = tk.Entry(pestana5, border=3)
                numero6.place(relx= 0.40,rely=0.35)
                numero6.config(width="10")
                            
                numero7 = tk.Entry(pestana5, border=3)
                numero7.place(relx= 0.50,rely=0.35)
                numero7.config(width="10")
                            
                numero8 = tk.Entry(pestana5, border=3)
                numero8.place(relx= 0.60,rely=0.35)
                numero8.config(width="10")
                    #FILA3        
                numero9 = tk.Entry(pestana5, border=3)
                numero9.place(relx= 0.30,rely=0.40)
                numero9.config(width="10")
                    
                numero10 = tk.Entry(pestana5, border=3)
                numero10.place(relx= 0.40,rely=0.40)
                numero10.config(width="10")
                    
                numero11 = tk.Entry(pestana5, border=3)
                numero11.place(relx= 0.50,rely=0.40)
                numero11.config(width="10")
                    
                numero12 = tk.Entry(pestana5, border=3)
                numero12.place(relx= 0.60,rely=0.40)
                numero12.config(width="10")
                    #FILA4
                numero13 = tk.Entry(pestana5, border=3)
                numero13.place(relx= 0.60,rely=0.45)
                numero13.config(width="10")
                    
                numero14 = tk.Entry(pestana5, border=3)
                numero14.place(relx= 0.30,rely=0.45)
                numero14.config(width="10")
                    
                numero15 = tk.Entry(pestana5, border=3)
                numero15.place(relx= 0.40,rely=0.45)
                numero15.config(width="10")
                    
                numero16 = tk.Entry(pestana5, border=3)
                numero16.place(relx= 0.50,rely=0.45)
                numero16.config(width="10")
                    
                    
                vec1 = tk.Entry(pestana5, border=3)
                vec1.place(relx= 0.30,rely=0.53)
                vec1.config(width="10")
                    
                vec2 = tk.Entry(pestana5, border=3)
                vec2.place(relx= 0.40,rely=0.53)
                vec2.config(width="10")
                    
                vec3 = tk.Entry(pestana5, border=3)
                vec3.place(relx= 0.50,rely=0.53)
                vec3.config(width="10")
                    
                vec4 = tk.Entry(pestana5, border=3)
                vec4.place(relx= 0.60,rely=0.53)
                vec4.config(width="10")
                
                obtener = tk.Button(pestana5, 
                        text="Siguiente", 
                        command=proceso,
                        background="deepskyblue",
                        border = 3)
    
                obtener.place(relx=0.45, rely=0.60)
                       
        texto1 = tk.Label(pestana5,text="Seleccione la siguiente opcion:")
        texto1.place(relx=0.38, rely=0.11)
        
        listado = ttk.Combobox(pestana5, width=17)
        listado.place(relx=0.35, rely=0.16)
    
        listado['values']=opciones
    
        obtener = tk.Button(pestana5, 
                        text="Siguiente", 
                        command=procesamiento,
                        background="deepskyblue",
                        border = 3)
    
        obtener.place(relx=0.55, rely=0.16) 
    
    pestana5 = Toplevel()
    pestana5.geometry("650x500") 
    pestana5.configure(background="#0E2C61")

    boton1 = tk.Button(pestana5, 
                   text="Gauss Jordan",
                   background="deepskyblue",
                   border = 3, command=gauss_jordan).pack()
    
    boton2 = tk.Button(pestana5, 
                   text="Krammer",
                   background="deepskyblue",
                   border = 3, command=krammer).pack()
    
    
    
    
texto = tk.Label(text="Eliga la opcion")

boton1 = tk.Button(ventana, 
                   text="Sistema de ecuaciones",
                   background="deepskyblue",
                   border = 3, command=sistem_ecuaciones).pack()



boton2 = tk.Button(ventana, 
                   text="Multiplicacion de matrices", 
                   command=multiplicacion,
                   background="deepskyblue",
                   border = 3).pack()



boton3 = tk.Button(
    ventana, 
    text="Matriz Inversa", 
    command=inversa,
    background="deepskyblue",
    border = 3
    ).pack()



boton4 = tk.Button(ventana, text="Reset")

ventana.mainloop()
