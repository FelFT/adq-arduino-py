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