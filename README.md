# DS18B20 in node-red
Aggiungere un sensore di temperatura digitale DS18B20 in nodered

In questo progetto ho aggiunto un sensore di temperatura digitale ad un raspberry. In questo modo posso leggere la temperatura diirettamente da lui, senza aggiungere un sensore esterno.

# Digitale vs Analogico
Ho usato un sensore digitale. Questo ha pro e contro.

# Digitale
Pro 
- Circuito molto semplice
- La libreria fa tutto, a noi basta 2 righe

Contro
- Pecca un po di precisione 

# Analogico
Pro
- Maggiore accuratezza

Contro
- Circuito piu' complicato
- Programma con un po di istruzioni

# Circuito
Abbiamo bisogno solo del sensore e di 1 resistenza da 50 Kohm

ATTENTI al verso del sensore!!

![circuito](https://farm5.staticflickr.com/4215/35139160190_cea3435a09_b_d.jpg)


# Software
Il DS18B20 e' un sensore digitale che comunica con un solo filo { 1-wire }.
Questo protocollo e' molto diffuso e il raspberry usa il pin GPIO 4.

Per abilitare il protocollo vi lascio la [guida](https://www.raspberrypi-spy.co.uk/2018/02/enable-1-wire-interface-raspberry-pi/). E' molto semplice e si puo fare in diversi modi


Scarichiamo la libreria con questo comando
> pip install w1thermsensory
Aspettiamo che si installi.

Una volta abilitata, creiamo il nostro file python

> nano nome_programma.py

Dentro ci scriviamo

```python
rom w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
print( sensor.get_temperature() )
```

Trovate il file anche nella repository.

Ora premiamo 
> ctrl+x

> y

> invio

In questo modo abbiamo creato il file. 
Se digitiamo

> python3 nome_file.py
Ci dovrebbe scrivere la temperatura.

# Aggiungerlo a nodered
Ora basta che prendiamo un nodo exec e come comando inseriamo
> python3 nome_programma.py



