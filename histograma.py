import json

archivo = open('histograms.txt','r')

contenido = archivo.read()
#print contenido

histograma = json.loads(contenido)

#print histograma['histograms']['v_error']['xs']
print histograma['histograms']['v_error']['ys']
