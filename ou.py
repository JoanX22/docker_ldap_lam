def genera_contenido_ldif_multiples_unidades_organizativas(filename, lista_ou_name, base_dn):
    """Genera un archivo LDIF con múltiples unidades organizativas."""
    
    ldif_content = ""
    
    for ou_name in lista_ou_name:
        ldif_content += f"""
# Organisational unit for {ou_name}
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""
    
    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}.ldif' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}.ldif': {e}")


# Lista de unidades organizativas
lista_ou_name = [
    "directores", "profesores", "alumnos", "personalnodocente",
    "eso1", "eso2", "eso3", "eso4", "bach1ciencias", "bach1humanidades",
    "bach2ciencias", "bach2humanidades", "profesoreseso", "profesoresbach",
    "profesoreseso1", "profesoreseso2", "profesoreseso3", "profesoreseso4",
    "profesoresbach1ciencias", "profesoresbach1humanidades",
    "profesoresbach2ciencias", "profesoresbach2humanidades"
]

# Parámetros de configuración
filename = "instituto"
base_dn = "dc=villena,dc=org"  # Reemplaza con tu dominio real

# Generar el archivo LDIF
genera_contenido_ldif_multiples_unidades_organizativas(filename, lista_ou_name, base_dn)

