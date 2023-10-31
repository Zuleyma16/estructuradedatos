from queue import Queue

class RegistroNumeros:
    def __init__(self):
        self.cola = Queue()
        self.pila = []

    def agregar_numero(self, numero):
        if numero not in self.pila:
            self.pila.append(numero)
            self.cola.put(numero)
            print(f"Número {numero} agregado correctamente.")
        else:
            print(f"El número {numero} ya está en la lista, no se permite duplicados.")

    def mostrar_numeros(self):
        print("Números en la cola:")
        while not self.cola.empty():
            print(self.cola.get(), end=" ")
        print("\nNúmeros en la pila:")
        print(self.pila)

# Ejemplo de uso
registro = RegistroNumeros()
registro.agregar_numero(5)
registro.agregar_numero(3)
registro.agregar_numero(5)  # Este número ya está en la lista y no se permiten duplicados
registro.agregar_numero(8)
registro.mostrar_numeros()