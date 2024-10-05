from database import obtener_conexion

def agregar_propiedad(direccion, tipo, precio, disponible):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO propiedades (direccion, tipo, precio, disponible) VALUES (%s, %s, %s, %s)''', (direccion, tipo, precio, disponible))
    conn.commit()
    print("Propiedad agregada exitosamente.")
    cursor.close()
    conn.close()

def listar_propiedades():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM propiedades')
    propiedades = cursor.fetchall()
    
    for propiedad in propiedades:
        print(f"ID: {propiedad[0]}, Dirección: {propiedad[1]}, Tipo: {propiedad[2]}, Precio: {propiedad[3]}, Disponible: {propiedad[4]}")
    
    cursor.close()
    conn.close()

def actualizar_propiedad(id_propiedad, nueva_direccion, nuevo_tipo, nuevo_precio, nueva_disponibilidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''UPDATE propiedades SET direccion = %s, tipo = %s, precio = %s, disponible = %s WHERE id = %s''', (nueva_direccion, nuevo_tipo, nuevo_precio, nueva_disponibilidad, id_propiedad))
    conn.commit()
    print("Propiedad actualizada exitosamente.")
    cursor.close()
    conn.close()

def eliminar_propiedad(id_propiedad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM propiedades WHERE id = %s', (id_propiedad,))
    conn.commit()
    print("Propiedad eliminada exitosamente.")
    cursor.close()
    conn.close()