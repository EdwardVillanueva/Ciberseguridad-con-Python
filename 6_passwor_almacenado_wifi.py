import subprocess

def mostrar_cred():
    perfiles=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    nombre_perfiles=[]
    for i in perfiles:
        if "Perfil de todos los usuarios" in i:
            i=i.split(":")
            nombre_perfiles.append(i[1].strip())
         
    contraseña_perfiles=[]
    for nombre_perfil in nombre_perfiles:
        try:
            contraseñas=subprocess.check_output(['netsh', 'wlan', 'show', 'profile',nombre_perfil, 'key=clear']).decode('ISO-8859-1').split('\n')
            for linea in contraseñas:
                if "Contenido de la clave" in linea:
                    print(f"SSID: {nombre_perfil}, Contraseña: {linea.split(':')[1].strip()}")
        except subprocess.CalledProcessError as e:
            print(f"Error al obtener la contraseña del perfil {nombre_perfil}: {e.output.decode('utf-8')}")
        except Exception as e:
            print(f"Ocurrió un error inesperado con el perfil {nombre_perfil}: {str(e)}")
    
mostrar_cred()