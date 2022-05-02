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
Se crea un archivo de Python `adquisicion.py`, para adquirir los datos del puerto serial de la computadora

```python
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import serial

arduinoSerial = serial.Serial('COM4', 9600)

x_data = []
y_data = []
 
figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')
 
def graph(frame):
    datos = arduinoSerial.readline()
    datos = float(datos)
    x_data.append(datetime.now())
    y_data.append(datos)
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,
 
animacion = FuncAnimation(figure, graph, interval=3000)
pyplot.show()
```
