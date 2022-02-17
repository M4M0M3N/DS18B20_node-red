from w1thermsensor import W1ThermSensor

for i in range(0,5):                #leggo il sensore per massimo 5 volte, per evitare il blocco dello script
        sensor = W1ThermSensor()
        temp = sensor.get_temperature()
        
        if temp != "":              #se in una di queste 5 volte ricevo una temperatura valida esco dal cliclo
                break

print(temp)


