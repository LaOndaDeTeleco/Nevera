import sqlite3

dbase = sqlite3.connect("onda.db")
cursor = dbase.cursor()

print("Bienvenido, quien eres? (numero id). Si no te has unido aun, pulsa enter.")
user = input()

print("¿Qué quieres hacer?\n     1) Comprar\n     2) Ingresar dinero\n     3) Añadir productos\n     4) Añadir usuario")
accion = input()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Si el valor dado es 1 la accion es la de comprar un producto
if accion == 1:
    cursor.execute("SELECT * FROM productos")
    products = cursor.fetchall()
    for tup in products:
        print("{0}. {1}   --->    Precio: {2}  Cantidad: {3}".format(tup[0], tup[1], tup[2], tup[3]))
    print("¿Que quieres comprar?")
    producto = input()
    tup = products[int(producto) - 1]
    cursor.execute(
        "UPDATE productos SET cantidad = {0} WHERE id = {1}".format(tup[3] - 1, tup[0]))
    cursor.execute("SELECT saldo FROM usuarios WHERE id = {0};".format(str(user)))
    prev = cursor.fetchone()[0]
    cursor.execute("UPDATE usuarios SET saldo = {0} WHERE id = {1};".format(prev - tup[2], str(user)))

# Si el valor dado es 2 la accion es la de ingresar dinero
elif accion == 2:
    print("¿Cuánto dinero quieres ingresar")
    din = float(input())
    cursor.execute("SELECT saldo FROM usuarios WHERE id = {0};".format(user))
    prev = cursor.fetchone()[0]
    cursor.execute("UPDATE usuarios SET saldo = {0} WHERE id = {1};".format(din + prev,user))
    print("Su saldo actual es: " + str(din + prev))

# Si el valor dado es 3 la accion es la añadir productos
elif accion == 3:
    cursor.execute("SELECT * FROM productos")
    products = cursor.fetchall()
    for tup in products:
        print("{0}. {1}   --->    Precio: {2}  Cantidad: {3}".format(tup[0], tup[1], tup[2], tup[3]))
    print("¿Qué producto vas a ingresar? Si es un producto nuevo, indicalo con -1")
    prod = int(input())
    n = input("Con que nombre guardo al producto?   ")
    p = input("A que precio lo cobro?     ")
    c = input("Que cantidad total quedara?    ")
    if prod == -1:
        cursor.execute("SELECT * FROM productos;")
        las = cursor.fetchall()[-1]
        n_id = las[0] + 1
        cursor.execute(
            "INSERT INTO productos (id, nombre, precio, cantidad) VALUES ({0}, '{1}', {2}, {3});".format(str(n_id), n,
                                                                                                         p, c))
    else:
        cursor.execute(
            "UPDATE productos SET nombre = '{0}', precio = {1}, cantidad = {2} WHERE id = {3}".format(n, p, c, prod))

# Si el valor dado es 4 la accion es la de añadir usuario
elif accion == 4:
    print("Quien es el nuevo usuario? (nombre)")
    n = input()
    cursor.execute("SELECT * FROM usuarios;")
    las = cursor.fetchall()[-1]
    n_id = las[0] + 1
    cursor.execute("INSERT INTO usuarios (id, nombre, saldo) VALUES ({0}, '{1}', 0);".format(str(n_id), n))
    print("Su id es: " + str(n_id))

# Como no hay mas acciones, cualquier otra indicacion es un error
else:
    print("No es una opción disponible\nTerminando el programa, pulse enter")
    input()

dbase.commit()
dbase.close()

input("Para terminar pulsa enter...")