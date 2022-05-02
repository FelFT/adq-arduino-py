# adq-arduino-py

## Requisitos
- [Tarjeta Arduino UNO]()
- Potenciómetro 
- [Visual Studio Code]()
  - Extensión Arduino
  - Extensión Python
 
 ## Conexiones del circuito
Se conecta un potenciómetro a la alimentación de 5 V y a GND. La salida analógica se conecta al pin A0. El circuito se muestra a continuación.

![Circuito](https://github.com/FelFT/adq-arduino-py/blob/main/img/circuit.png)

## Programación en Arduino
Se crea un archivo de Arduino `send.ino`, para definir la adquisición de los datos y enviarlos por el puerto serial

```c
#define POT A0

float voltage = 0;

void setup()
{
  pinMode(POT, INPUT);
  Serial.begin(9600);
}

void loop()
{
  voltage = analogRead(POT);
  Serial.println(voltage);
  delay(100);
}
```
## Programación en Python

