import serial
import time
import csv
import struct

ser=serial.Serial("COM5",9600)
lista=[]
def registrar_valor():
    n=0
    data=[]
    while n<20:
        value = ser.readline().decode().strip()
        lista.append(value)
        data.append(lista)
        print(value)

        with open("Valores.csv","w",newline="") as file:
            writer=csv.writer(file,delimiter=";")
            writer.writerow(["Valores"]) 
            writer.writerows(data)
        time.sleep(1)     
        n=n+1
    maximo=max(lista)
    minimo=min(lista)
    return maximo,minimo

def mostrar_valor():
    print("\nEsta es la funcion de mostrar pacientes")
    import csv

    with open("Valores.csv","r") as file:
        reader= csv.reader(file, delimiter=";")
        next(reader)
        for row in reader:
            print("\nValores:",row[0])
            print("\n")
            

def mostrar_max_y_min(maxi,mini):
    print("Maximo:",maxi)
    print("Minimo:",mini)
    max_min=[]
    lista1=[maxi,mini]
    max_min.append(lista1)
    with open("Max_Min.csv","w",newline="") as file:
            writer=csv.writer(file,delimiter=';')
            writer.writerow(["Maximo","Minimo"]) 
            writer.writerows(max_min)

def led(maximo,minimo):
    maxi=int(maximo)
    mini=int(minimo)
    #pendiente
    rango=maxi-mini
    n=0
    while n<20:
        value = ser.readline().decode().strip()
        time.sleep(0.6)
        print("Valor:",value)

        if int(value)>rango:
            print("EL valor es mas grande que el rango.")
        else:
            arduino=int(int(value)/rango*255) 
            print(arduino)
            ser.write(struct.pack(">B",arduino))
        n=n+1

def salir():
    print("\nGracias por usar nuestra aplicacion")


def menu():
    sel=0
    while sel!=5:
        print("Bienvinidos a la aplicacion")
        print("elige una de las opciones:")
        print("1. Registrar valores")
        print("2. Mostrar valores")
        print("3. Mostrar Maximo y minimo" )
        print("4. Mandar valores al Led")
        print("5. Salir")
        sel=int(input("Elige una opcion: "))
        if sel==1:
            maximo,minimo=registrar_valor()
        if sel==2:
            mostrar_valor()
        if sel==3:
            mostrar_max_y_min(maximo,minimo)
        if sel==4:
            led(maximo,minimo)
        if sel==5:
            salir()
menu()
