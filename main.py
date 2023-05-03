from menu import Menu
import os

if __name__ == '__main__':
    listaViaj = []
    xMenu = Menu()
    bandera = False
    while not bandera:
        xMenu.mostrarMenu()
        op = int(input('Su opcion: '))
        xMenu.opcion (op, listaViaj)
        os.system('pause')
        if op == 0:
            bandera = True
    os.system('exit')