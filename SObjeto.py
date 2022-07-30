import pickle

class vehiculo:
    def descripcion(self,puertas,ruedas):
        self.puertas = puertas
        self.ruedas = ruedas

Vehiculo = vehiculo()
Vehiculo.descripcion(4,4)
f = open('Vehiculo.bin', 'wb')
pickle.dump(Vehiculo, f)
f.close()

f = open('Vehiculo.bin', 'rb')
Vehiculo = pickle.load(f)
f.close()

print('Numero de puertas:',Vehiculo.puertas)
print('Numero de ruedas :',Vehiculo.ruedas)