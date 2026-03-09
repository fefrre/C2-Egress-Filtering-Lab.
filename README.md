
# Prueba de Concepto (PoC): Desarrollo de RAT y Auditoría de Red (Blue Team)

> ** AVISO LEGAL Y ÉTICO:** > Este repositorio contiene una Prueba de Concepto (PoC) desarrollada con fines estrictamente académicos y educativos. Todo el código fue ejecutado en un entorno de laboratorio aislado y controlado (VirtualBox - Red Interna). El objetivo de este proyecto no es el desarrollo de armamento digital (weaponization), sino la comprensión de tácticas ofensivas para el diseño de mitigaciones y reglas de seguridad efectivas a nivel de sistema operativo. 

##  Resumen del Proyecto
Auditoría técnica de un ecosistema de red que simula la infección y comunicación de un Troyano de Acceso Remoto (RAT). El laboratorio documenta el ciclo de vida completo: desde la exfiltración inicial de datos y establecimiento del canal C2 (Command & Control), hasta la cacería de amenazas (Threat Hunting) y la mitigación final mediante filtrado de salida.

##  Fase 1: Ofensiva (Red Team)
Desarrollo de scripts en Python con capacidades de recolección de inteligencia y control remoto:
* **Recolección de Datos:** Extracción de metadatos del sistema (OS, Hostname, User).
* **Keylogging:** Interceptación de pulsaciones de teclado a nivel de sistema.
* **Reverse Shell:** Apertura de un socket TCP (Puerto 4444) interactivo utilizando módulos nativos (`socket`, `subprocess`).

##  Fase 2: Defensa y Threat Hunting (Blue Team)
En lugar de depender de soluciones EDR comerciales, la detección se realizó comprendiendo las bases del sistema operativo y los protocolos de red:
1. **Auditoría de Tráfico (Wireshark):** Detección de exfiltración de credenciales viajando en texto plano por la red (Falta de cifrado en el canal C2).
2. **Análisis de Procesos Anómalos:** Uso de herramientas nativas de Windows (`PowerShell`, `netstat -abno | Select-String`) para identificar binarios ilegítimos (`python.exe`) estableciendo conexiones de red salientes no estandarizadas.
[/img/shell](https://github.com/fefrre/C2-Egress-Filtering-Lab./blob/main/img/shell.jpeg)

##  Fase 3: Mitigación (Zero Trust & Egress Filtering)
Para neutralizar la amenaza, se aplicó una arquitectura de filtrado de salida (Egress Filtering), corrigiendo el error común de dejar las conexiones salientes sin auditar.
* **Regla de Firewall:** Creación de una directiva estricta en Windows Defender Firewall bloqueando el tráfico TCP saliente en el puerto 4444.
* **Resultado:** Asfixia del binario malicioso de forma local (`[WinError 10013]`), impidiendo el establecimiento de la sesión de control remoto.

[/img/error](https://github.com/fefrre/C2-Egress-Filtering-Lab./blob/main/img/error.jpeg)
##  Tecnologías y Herramientas Utilizadas
* **Lenguajes:** Python, PowerShell.
* **Redes:** Wireshark, TCP/IP, Sockets.
* **Sistemas Operativos:** Kali Linux (Atacante), Windows 10/11 (Víctima).
* **Seguridad:** Windows Defender Firewall con Seguridad Avanzada.
