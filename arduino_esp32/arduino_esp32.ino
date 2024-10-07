int sensorPin = 34;  // Pino analógico onde o sensor está conectado
 
void setup() {
  Serial.begin(115200);  // Inicializa a comunicação serial
  Serial.println("ESP32 está funcionando!");  // Mensagem de teste
}
 
void loop() {
  int valorSensor = analogRead(sensorPin);  // Lê o valor do sensor
  Serial.print("Valor do sensor: "); 
  Serial.println(valorSensor);  // Envia o valor pela porta serial
  delay(1000);  // Atraso de 1 segundo
}