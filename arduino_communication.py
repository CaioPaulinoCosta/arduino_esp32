import serial
import time
 
# Substitua 'COM3' pela porta correta
arduino_port = 'COM3'  # Exemplo: COM3
baud_rate = 115200  # Ajuste para a taxa de transmissão usada no ESP32
 
# Conectar ao Arduino
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Aguarda a conexão ser estabelecida
 
try:
    print("Conectado ao ESP32!")
 
    while True:
        if ser.in_waiting > 0:  # Verifica se há dados disponíveis
            try:
                # Tentativa de decodificar usando 'utf-8'
                line = ser.readline().decode('utf-8').rstrip()
            except UnicodeDecodeError:
                # Se der erro, tenta com 'latin-1' ou ignora os erros
                line = ser.readline().decode('latin-1', errors='ignore').rstrip()
            # Verifica se a linha contém dados do sensor
            if "Valor do sensor:" in line:
                valor = line.split(":")[-1].strip()  # Extrai o valor do sensor
                print(f"Leitura do sensor HW-503: {valor}")
 
except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
 
finally:
    ser.close()  # Fecha a conexão