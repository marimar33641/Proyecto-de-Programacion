import json
import os
import sys
import webbrowser

def main():
    with open("datosAvion.json","a") as archivo:
        archivo.close()
    menu()
    
def menu():
    opcion=3
    while opcion!=0:
        print("1. Registrar vuelo\n2. Crear un resumen\n3. Ver video\n0. Cerrar el programa")
        opcion=int(input(">> "))
        filas=30
        columnas=30
        matriz=crearMatriz(filas,columnas,"-")
        if opcion==1:
            matriz=preguntarDatos(matriz)
        elif opcion==2:
            modeloAvion=input("Digite la placa del avion: ")
            tiempo=input("Digite el dia del vuelo: ")
            with open("datosAvion.json","r") as archivo:
                if os.stat("datosAvion.json").st_size==0:
                    print("No hay datos registrados")
                    break
                else:
                    datos=json.load(archivo)
                    for verificar in datos:
                        if verificar==tiempo:
                            for revision in datos[verificar]:
                                if revision==modeloAvion:
                                    resumen=open("datosAvion.txt","w")
                                    resumen.write(str(datos[verificar][revision]))
                                    resumen.close()
                                    print("Se ha creado en resumen en datosAvion.txt")
                                    pregunta=int(input("1.Ver el radar\n2.No ver el radar\n>> "))
                                    if pregunta==1:
                                        llenarMatriz(matriz,datos[verificar][revision]['Posiciones'])
                                    resultado=True
                                else:
                                    resultado="El avion digitado no existe dentro de los archivos"
                    if resultado!=True:
                        print(resultado)
                    archivo.close()
        elif opcion==3:
            webbrowser.open("https://www.youtube.com/watch?v=lRPOpcUrknY")

    webbrowser.open("https://www.youtube.com/watch?v=b8PxzPxI8Os")   
    print("Gracias por usar nuestro programa :D")

def llenarMatriz(matriz,XY):
    for p in XY:
        x=p[0]-1
        y=p[1]-1
        matriz[x][y]="X"
    acomodar(matriz)

def crearMatriz(filas,columnas,valor): 
    print("                           RADAR BELLO                       ")
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(valor)
    acomodar(matriz)
    return matriz

def acomodar(matriz):
    print()
    for fila in matriz:
        print("[", end= " ")
        for x in fila:
            print("{:}".format(x), end= " ")
        print("]")
    print()
    return matriz

def preguntarDatos(matriz):
        lista=[]
        dias=1
        contador=-1
        key=False
        horasTotales=0
        while key!=True:
            dias= int(input("Digite el dia: "))
            HoraDeVuelo= int(input("Digite la hora de entrada: "))
            if 100>HoraDeVuelo or HoraDeVuelo>2459 or 0>dias or dias>5:
                print("EL TIEMPO DIGITADO NO ES VALIDO")    
            else:
                dias=str(dias)
                key=True
        placaAvion= input("Digite la placa del avion: ")
        modeloAvion= int(input("Digite el modelo del avion: "))
        marcaAvion= input("Digite la marca del avion: ")
        aereolineaAvion= input("Digite la aereolinea del avion: ")
        if os.stat("datosAvion.json").st_size!=0:
            archivo=open("datosAvion.json")
            lista=json.load(archivo)
            for listado in lista:
                key=False
                if (listado==dias):
                    for fin in lista[listado]:
                        if fin==placaAvion:    
                            print("NO SE PUEDE REGISTRAR EL VUELO")
                            menu()
                            sys.exit()
        posicion=[]
        contador=-1
        while True:
            x=int(input(f"Digite la cordenada en x en el dia {dias}: "))
            y=int(input(f"Digite la cordenada en y en el dia {dias}: "))
            if (x!=1 and y!=1) and (y!=30 and x!=30):
                print("ESTAS POSICIONES NO PUEDEN SER REGISTRADAS COMO POSICIONES INICIALES")
            else:
                break
        posicionx=x
        posiciony=y
        suma1 = posicionx
        suma2 = posiciony
        resta1= posicionx
        resta2= posiciony
        try:
            if os.stat("datosAvion.json").st_size!=0:
                archivo=open("datosAvion.json","r+")
                datos=json.load(archivo)
                datos=datos[dias]
                sebastianPendejo = None
            else:
                sebastianPendejo=False
        except KeyError:
            sebastianPendejo = False
       
        while 100 <= HoraDeVuelo <= 2460: 
            sebastianEsMasPendejo= False    
            if ((x == suma1 and y == suma2)) or ((x == resta1 and y == resta2)) or (x==posicionx and y==posiciony) or ((x == suma1 and y == resta2)) or ((x == resta1 and y == suma2 )) or (x==suma1 and y==posiciony)or (x==posicionx and y==suma2) or (x==resta1 and y==posiciony) or (x==posicionx and y==resta2):
                contador+=1
                chequeo=False
                x=x
                y=y
                if sebastianPendejo == None:
                    for info in datos:
                        cont=0
                        for posicionA in datos[info]['Posiciones']:
                            if (cont+datos[info]['HoraDeVuelo'])==((contador*5)+HoraDeVuelo) and (posicionA==[x,y]):
                                chequeo=True
                                break
                            cont+=5
                if chequeo==False:
                    posicion.append([x,y])
                    matriz[x-1][y-1]="X"
                    posicionx=x
                    posiciony=y
                    suma1 = posicionx+1
                    suma2 = posiciony+1
                    resta1= posicionx-1
                    resta2= posiciony-1 
                    if x==30 or y==30:
                        print("SE ACABO")
                        contador= contador*5
                        horasTotales= HoraDeVuelo+contador
                        print(f"La hora que empezo su viaje fue a las: {HoraDeVuelo} y el vuelo termino a las {horasTotales}, por lo que su viaje duro {contador} minutos")
                        key= False
                        break
                else:
                    print("ESTA POSICION SE CRUZA CON OTRA A LA MISMA HORA")
                    sebastianEsMasPendejo= True
                    x=int(input(f"Digite la cordenada en x en el dia {dias}: "))
                    y=int(input(f"Digite la cordenada en y en el dia {dias}: "))
                    contador-=1
                    posicionx=x
                    posiciony=y
                    suma1 = posicionx
                    suma2 = posiciony
                    resta1= posicionx
                    resta2= posiciony
            else:
                print("Digito mal las posiciones ")       
            if sebastianEsMasPendejo!=True:                     
                x=int(input(f"Digite la cordenada en x en el dia {dias}: "))
                y=int(input(f"Digite la cordenada en y en el dia {dias}: "))
        lista={}
        lista[placaAvion]={'modeloAvion':modeloAvion,'marcaAvion':marcaAvion,'aereolineaAvion':aereolineaAvion,'HoraDeVuelo':HoraDeVuelo,'Posiciones':posicion}
        if os.stat("datosAvion.json").st_size==0:
            datos={}
            datos[dias]=lista
        else:
            archivo= open("datosAvion.json","r")
            datos=json.load(archivo)
            try:
                datos[dias]=lista
            except KeyError:
                datos[dias]=lista
            archivo.close()
        with open("datosAvion.json","w") as archivo:
            json.dump(datos,archivo,indent=4)
            archivo.close()
        pregunta=int(input("1.Ver el radar\n2.No ver el radar\n>> "))
        if pregunta==1:
            acomodar(matriz)
        return matriz
main()