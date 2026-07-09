
planes = []
inscripciones = []

planes = {
 "F001": ["Plan basico", "Mensual",1, False, False, "libre"],
 "F002": ["Plan full", "mensual", 1, True, True, "libre"],
 "F003": ["Plan estudiante", "Trimestral", 3, False, True,"Tarde"],
 "F004": ["Plan Senior", "TRIMESTRAL", 3, True, False, "Mañana"],
 "F005": ["Plan anual pro", "anual", 12, True, True, "Libre"],
 "F006": ["plan nocturno", "mensual", 1, False, 1, False, True, "Noche"],
}

inscripciones = {
     "F001": [14990, 30],
     "F002": [22990, 10],
     "F003": [39990, 0],
     "F004": [35990, 6],
     "F005": [159990, 2],
     "F006": [18990, 15],
}

def menu():
    while True:
        print("Menu Principal")
        print("1. Cupos por tipo de plan")
        print("2. Busqueda de planes")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar Plan")
        print("6. Salir")

def leer_opcion():
    while True:
        try:
            op = int(input("ingrese una opcion"))
            if 1 <= opcion <= 6:
                return op
        except:
            print("debe seleccionar una opcion valida")

def validar_cupo(cupo):
    return cupo.stript() != ""

def  cupos_tipos(tipo):
    tipo = input("ingrese el tipo de plan a consultar").strip
    if tipo == "":
        print("el texto no puede estar vacio")
        return None
    


def busqueda_precio(p_min, p_max):
    p_min = input("ponga el precio minimo: ")
    p_max = input("ponga su precio maximo: ")

    p_min 
    

   
    
def buscar_codigo(codigo):
    codigo = input("ingrese el codigo de plan: ")
    if codigo in [planes][" "]:
        return True
    else:
        return False


def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    if codigo(codigo) and nombre(nombre) and tipo(tipo) and duracion(duracion) and acceso_piscina(acceso_piscina) and incluye_clases(incluye_clases) and horario(horario) and precio(precio) and cupos(cupos):
        planes [1] = datos [codigo]

        print("plan registrado")
    else:
        print("plan no registrado")


def eliminar_plan(codigo):
    codigo = input("ingresa el nombre del codigo a eliminar")  
    if codigo != buscar_codigo:
        if codigo != -1:
            codigo.pop(codigo)
            print("registro eliminado")
        else:
            print("no encontrado")


lista = []

while True:
    menu()

    opcion = leer_opcion
    if opcion == 6:
        print("programa finalizado")












