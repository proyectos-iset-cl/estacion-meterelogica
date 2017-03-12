#!/usr/bin/python
 

import serial
 
# Abrimos el puerto 9600
PuertoSerie = serial.Serial('/dev/ttyACM0', 9600)
# Creamos un buble sin fin
while True:
  # lectura
  sArduino = PuertoSerie.readline()
  sArduino = PuertoSerie.readline()
  print "Valor Arduino: " + sArduino.rstrip('\r\n')
  lista=sArduino.split(":")
  if len(lista) < 2:
   sArduino = PuertoSerie.readline()
   lista=sArduino.split(":")
   print "*******************Error*******************"
  print "Lista-> " + str(lista)
  Psensor=lista[0]
  Temp=lista[1]
  Pvalor=Temp.rstrip('\r\n')
  print "Sensor-> " + str(Psensor)
  print "Valor-> " + str(Pvalor)
  
