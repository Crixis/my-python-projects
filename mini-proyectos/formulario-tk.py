""" Formulario de productos
Crear un programa que tenga:
-ventana
-tamaño fijo
-no redimensionable
-un menu (inicio, añadir, info, salir)
-diferentes pantallas
-formulario de añadir productos
-guardar datos temporalmente
-mostrar datos listados en la pantalla home
-opcion de salir
"""

from tkinter import *

from colorama import Style

#definir ventana
ventana= Tk()
#ventana.geometry("400x400")
ventana.minsize(400, 400)
ventana.title("Proyecto tkinter")
ventana.resizable(0, 0)

#pantallas
def home():
    #montar pantalla
    
    home_label.config(
        fg="white",
        bg="black",
        font=("arial", 30),
        padx=160,
        pady=30
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=1)

    #listar productos
    for product in products:
        if len(product)==3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------------------").grid()

    #ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    
    add_label.config(
        fg="white",
        bg="black",
        font=("arial", 30),
        padx=60,
        pady=30
    )
    add_label.grid(row=0, column=0, columnspan=5)

    #campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("consolas", 12),
        padx=15,
        pady=15
    )

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        bg="black",
        fg="white",
        padx=15
    )

    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

    return True

def info():
    
    info_label.config(
        fg="white",
        bg="black",
        font=("arial", 30),
        padx=100,
        pady=30
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    
    home()

#variables importantes
products=[]
name_data=StringVar()
price_data=StringVar()

#definir campos de pantallas
home_label=Label(ventana, text="Inicio")
products_box=Frame(ventana, width=250)

add_label=Label(ventana, text="Añadir producto")

info_label=Label(ventana, text="Información")

data_label=Label(ventana, text="Creado por Cristian Vargas - 2022")

#campos del formulario
add_frame=Frame(ventana)

add_name_label=Label(add_frame, text="Nombre: ")
add_name_entry=Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame, text="Precio: ")
add_price_entry=Entry(add_frame, textvariable=price_data)

add_description_label=Label(add_frame, text="Descripcion: ")
add_description_entry=Text(add_frame)

boton= Button(add_frame, text="Guardar", command=add_product)

#cargar pantalla inicio
home()

#menu
el_menu=Menu(ventana)
el_menu.add_command(label="Inicio", command=home)
el_menu.add_command(label="Añadir", command=add)
el_menu.add_command(label="Info", command=info)
el_menu.add_command(label="Salir", command=ventana.quit)

#cargar menu
ventana.config(menu=el_menu)

#cargar ventana
ventana.mainloop()