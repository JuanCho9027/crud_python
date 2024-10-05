from crud import agregar_propiedad, listar_propiedades, actualizar_propiedad, eliminar_propiedad

# Agregar propiedades
agregar_propiedad('Calle 123, Ciudad', 'Apartamento', 250000, 1)
agregar_propiedad('Carrera 45, Ciudad', 'Casa', 500000, 0)

# Listar propiedades
print("Propiedades:")
listar_propiedades()

# Actualizar una propiedad
actualizar_propiedad(1, 'Calle 123, Ciudad', 'Apartamento de Lujo', 300000, 1)

# Listar de nuevo para ver el cambio
print("Propiedades después de actualizar:")
listar_propiedades()

# Eliminar una propiedad
eliminar_propiedad(2)

# Listar de nuevo para ver el cambio
print("Propiedades después de eliminar:")
listar_propiedades()
