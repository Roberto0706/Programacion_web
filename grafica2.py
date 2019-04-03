import json
import matplotlib.pyplot as plt
archivo = open('histograms.txt','r')

contenido = archivo.read()
#print contenido

histograma = json.loads(contenido)

#print histograma['histograms']['v_error']['xs']
#print histograma['histograms']['v_error']['ys']

v_error = histograma["histograms"]["v_error"]
t_error = histograma["histograms"]["t_error"]

plt.plot(v_error["xs"],v_error["ys"])
plt.plot(t_error["xs"],t_error["ys"])

plt.title("Representacion de histograma de errores ")
plt.xlabel("Iteraciones")
plt.ylabel("valor del error")
plt.legend(['error de validacion','error de entrenamiento '])
plt.show()
