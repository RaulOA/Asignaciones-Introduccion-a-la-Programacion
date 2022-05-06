from tkinter import *
from tkinter import ttk
import os
os.system("cls")
# Tamaño y fuente para los textos
font="Comic Sans MS"
size="15"
# tipo de rol
rol=""
# diccionario principal donde se guardan las secciones como clave y los datos de los estudiantes como valor
main_dicc={}
# aqui se guardan los nombres de seccion
section_list=[]
# aqui se guardan los campos asignados
spaces_list=[]
# aqui se guardan las cedulas
id_list=[]
#==============================================================
# contiene la ventana de ususarios o login
def ventana_login():
    global login
    login=Tk()
    login.title("Ventana Login")
    login.resizable(0,0)
    Label(login).pack()
    Label(login,text="Administración de Estudiantes",font=(font,size)).pack()
    Label(login).pack()
    Button(login,text="Administrador",font=(font,size),command=rol_1).pack()
    Label(login).pack()
    Button(login,text="Oficinista",font=(font,size),command=rol_2).pack()
    Label(login).pack()
    login.mainloop()
#==============================================================
# se activa si se presiona el boton -admin-, ademas cambia el rol
def rol_1():
    global rol
    rol="administrador"
    ventana_principal()
#==============================================================
# se activa si se presiona el boton -oficinista-, ademas cambia el rol
def rol_2():
    global rol
    rol="oficinista"
    ventana_principal()
#==============================================================
# contiene la pantalla principal, con su tabla que muestra las secciones y sus botones para sus diferentes funciones
def ventana_principal():
    login.destroy()
    global principal
    global table
    global count_1
    count_1=0
    principal=Tk()
    principal.title("Ventana Principal")
    principal.resizable(0,0)
    Label(principal).pack()
    Button(principal,text="<< Atras",font=(font,size),command=back).pack()
    Label(principal).pack()
    Label(principal,text="Lista de Secciones",font=(font,size)).pack()
    Label(principal).pack()
    table=ttk.Treeview(principal)
    table["columns"]=("Seccion","Espacios")
    table.column("#0",width=0,stretch=NO)
    table.column("Seccion",anchor=CENTER,width=200)
    table.column("Espacios",anchor=CENTER,width=100)
    table.heading("#0",text="",anchor=CENTER)
    table.heading("Seccion",text="Seccion",anchor=CENTER)
    table.heading("Espacios",text="Espacios",anchor=CENTER)
    table.pack()
    table.bind("<<TreeviewSelect>>",capturar_seleccion)
    Label(principal).pack()
    if rol=="administrador":
        Button(principal,text="<< Crear Secciones >>",font=(font,size),command=add_section).pack()
        Label(principal).pack()
    Button(principal,text="<< Añadir Alumno >>",font=(font,size),command=add_student).pack()
    Label(principal).pack()
    if len(section_list)>0:
        for p in section_list:
            m=spaces_list[count_1]
            table.insert(parent="",index="end",iid=count_1,text="",values=(p,m))
            count_1+=+1
    principal.mainloop()
#==============================================================
# funcion para regresar a la ventana de roles, se activa con el boton -atras-
def back():
    global rol
    rol=""
    principal.destroy()
    ventana_login()
#==============================================================
# ventana donde se añade las secciones, con un entry para poner el nombre de seccion y un spinbox para asignar campos.
def add_section():
    global section_entry
    global section_warning
    global campos
    section=Tk()
    section.title("Crear Seccion")
    section.resizable(0,0)
    Label(section).pack()
    Label(section,text="Nombre de Seccion:",font=(font,size)).pack()
    Label(section).pack()
    section_entry=Entry(section)
    section_entry.pack()
    Label(section).pack()
    Label(section,text="Campos Asignados:",font=(font,size)).pack()
    Label(section).pack()
    campos = Spinbox(section,from_=10, to=80,state="readonly")
    campos.pack()
    Label(section).pack()
    Button(section,text="Agregar Estudiante",font=(font,size),command=add_section_opp).pack()
    Label(section).pack()
    section_warning=Label(section,text="",font=(font,size))
    section_warning.pack()
    section=mainloop()
#==============================================================
# se activa al oprimir el boton -Agregar Estudiante-, se captura el nombre y los campos asignados,
# si hace falta el nombre dara un aviso, si la seccion ya existe en la lista dara aviso, si no, los datos 
# se agregaran a a tabla, y ademas se agregara la seccion y sus campos a sus respectivas listas
def add_section_opp():
    global count_1
    section_name=section_entry.get()
    space_in_class=campos.get()
    if section_name=="":
        section_warning.config(text="Falta el Nombre",fg="red")
    else:
        if section_name in section_list:
            section_warning.config(text=f"Esa Seccion Ya Existe",fg="red")
        else:
            table.insert(parent="",index="end",iid=count_1,text="",values=(section_name,space_in_class))
            save_section(section_name,space_in_class)
            section_warning.config(text=f"Grupo #{count_1} Añadido",fg="green")
            count_1+=1
#==============================================================
# añadir nombre de seccion y campos asignados a sus respectivas listas
def save_section(nombre_seccion,espacios_en_clase):
    section_list.append(nombre_seccion)
    spaces_list.append(int(espacios_en_clase))
#==============================================================
# captura los valores de la seccion seleccionada en la tabla
def capturar_seleccion(arg):
    for a in table.selection():
        valores=table.item(a)
        registros=valores["values"]
        student_list(registros)
#==============================================================
# se dispara una vez que se hace clik en alguna seccion de la tabla, 
# itera el diccionario para poder mostrar a los estudiantes de esa seccion como una lista de texto.
def student_list(valores):
    global selected
    selected=valores[0]
    students=Toplevel()
    students.title("Estudiantes")
    students.resizable(0,0)
    Label(students).pack()
    Label(students,text=f"Seccion {selected}",font=(font,size)).pack()
    Label(students).pack()
    Label(students,text="Cedula -- Nombre -- Apellido",font=(font,size)).pack()
    Label(students).pack()
    for f in main_dicc[selected]:
                for g,h in f.items():
                    ced=g
                    nom=h[0]
                    ape=h[1]
                    Label(students,text=f"{ced} -- {nom} -- {ape}",font=(font,size)).pack()
                    Label(students).pack()
    students.mainloop()
#==============================================================
# ventana para matricular estudiantes, contiene entrys y un combobox que toma los datos de la lista 
# de secciones como valores para mostrar
def add_student():
    global cedula
    global nombre
    global apellido
    global combobox_secciones
    global student_data_warning
    student_data=Tk()
    student_data.title("Crear Seccion")
    student_data.resizable(0,0)
    Label(student_data).pack()
    Label(student_data,text="Cedula del Estudiante",font=(font,size)).pack()
    Label(student_data).pack()
    cedula=Entry(student_data,font=(font,size),validate="key",validatecommand=(student_data.register(validate_entry), "%S"))
    cedula.pack()
    Label(student_data).pack()
    Label(student_data,text="Nombre del Estudiante",font=(font,size)).pack()
    nombre=Entry(student_data,font=(font,size))
    nombre.pack()
    Label(student_data,text="Apellidos del Estudiante",font=(font,size)).pack()
    apellido=Entry(student_data,font=(font,size))
    apellido.pack()
    Label(student_data).pack()
    combobox_secciones=ttk.Combobox(student_data,font=("Comic Sans MS",12),values=section_list,state="readonly")
    combobox_secciones.pack()
    Label(student_data).pack()
    Button(student_data,text="Añadir",font=(font,size),command=add_student_opp).pack()
    Label(student_data).pack()
    student_data_warning=Label(student_data,text="",font=(font,size))
    student_data_warning.pack()
    student_data=mainloop()
    #==============================================================
# verificar si el argumento es un numero, devuelve Falso o Verdadero
def validate_entry(text):
    return text.isnumeric()
#==============================================================
# agrega los valores al diccionario principal, toma de argumentos el diccionario principal, 
# el nombre de la seccion y los datos del estudiante
def append_value(Diccionario, Clave, Valor):
    if Clave in Diccionario:
        if not isinstance(Diccionario[Clave], list):
            Diccionario[Clave]=[Diccionario[Clave]]
        Diccionario[Clave].append(Valor)
    else:
        Diccionario[Clave]=Valor
#==============================================================
# verifica si se han llenado todos los datos necesarios para agregar el estudiante, si no es asi mostrara un mensaje,
# una vez completados llenados todos los datos la funcion verifica que la cedula no se repita, si no es asi, la cedula 
# nueva se agrega a la lista, y se dispara la funcion que agrega los datos al diccionario principal.
def add_student_opp():
    if cedula.get()=="" or nombre.get()=="" or apellido.get()=="" or combobox_secciones.get()=="":
        student_data_warning.config(text="Faltan Datos",fg="red")
    else:
        if cedula.get() in id_list:
            student_data_warning.config(text="Cedula Existente",fg="red")
        else:
            id_list.append(cedula.get())
            
            append_value(main_dicc,combobox_secciones.get(), 
            {cedula.get():[nombre.get().title(),apellido.get().title()]})

            student_data_warning.config(text="Estudiante Añadido",fg="green")
#==============================================================
ventana_login()