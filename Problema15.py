""" 
Respuesta a las preguntas:
- ¿Qué estructura de datos permite manejar prioridades?
Una cola de prioridad (Priority Queue) es la estructura adecuada para manejar prioridades. 
En este caso, los pedidos urgentes deben tener mayor prioridad que los normales, y la cola 
de prioridad permite manejar este tipo de requerimientos, donde los elementos con mayor prioridad son atendidos primero.

- ¿Cómo se podría organizar la cola para que los pedidos urgentes sean atendidos primero?
Los pedidos urgentes pueden tener una prioridad mayor que los pedidos normales en la cola de prioridad. 
Esto se puede lograr asignando un valor de prioridad más alto a los pedidos urgentes. 
Por ejemplo, se podría asignar un valor de prioridad bajo (como 0) para los pedidos normales y un valor de prioridad alto (como 1) para los pedidos urgentes. 
De esta forma, los pedidos urgentes serán atendidos antes que los normales.

- ¿Cómo se asignan pedidos a los repartidores de manera eficiente?
Los repartidores pueden estar representados como una lista de recursos (repartidores) que tienen disponibilidad o no. 
Una vez que un pedido es atendido (es decir, asignado a un repartidor), el repartidor se marca como ocupado. 
Esto se puede hacer de manera eficiente utilizando una cola de prioridad donde los repartidores disponibles (que están libres) 
tienen una alta prioridad para ser asignados a los nuevos pedidos.
"""
import heapq  # Heapq para implementar una cola de prioridad

class Pedido:
    """
    Representa un pedido de cliente.
    
    Atributos:
        id (int): Identificador único del pedido.
        descripcion (str): Descripción del pedido.
        urgente (bool): Indica si el pedido es urgente (True) o normal (False).
    """
    def __init__(self, id, descripcion, urgente=False):
        self.id = id
        self.descripcion = descripcion
        self.urgente = urgente
    
    def __lt__(self, other):
        # La prioridad se determina por el atributo 'urgente': los pedidos urgentes tienen mayor prioridad
        return self.urgente > other.urgente  # True si 'self' es más urgente que 'other'

class Repartidor:
    """
    Representa un repartidor.
    
    Atributos:
        id (int): Identificador único del repartidor.
        ocupado (bool): Indica si el repartidor está ocupado (True) o libre (False).
    """
    def __init__(self, id):
        self.id = id
        self.ocupado = False
    
    def __str__(self):
        return f"Repartidor {self.id} {'(Ocupado)' if self.ocupado else '(Libre)'}"

class SistemaDeEntrega:
    """
    Sistema de gestión de pedidos y asignación de repartidores.
    
    Atributos:
        pedidos (list): Cola de prioridad para los pedidos.
        repartidores (list): Lista de repartidores.
    """
    def __init__(self):
        self.pedidos = []  # Cola de prioridad
        self.repartidores = []
    
    def agregar_pedido(self, id, descripcion, urgente=False):
        """
        Agrega un nuevo pedido al sistema.
        
        Argumentos:
            id (int): Identificador del pedido.
            descripcion (str): Descripción del pedido.
            urgente (bool): Si el pedido es urgente.
        """
        pedido = Pedido(id, descripcion, urgente)
        heapq.heappush(self.pedidos, pedido)  # Agregar pedido a la cola de prioridad
        print(f"Pedido {id} agregado: {descripcion}. {'Urgente' if urgente else 'Normal'}")

    def asignar_pedido(self):
        """
        Asigna el siguiente pedido disponible a un repartidor.
        """
        # Buscar el siguiente repartidor libre
        for repartidor in self.repartidores:
            if not repartidor.ocupado:
                # Buscar el siguiente pedido
                if self.pedidos:
                    pedido = heapq.heappop(self.pedidos)
                    repartidor.ocupado = True
                    print(f"Pedido {pedido.id} asignado al Repartidor {repartidor.id}: {pedido.descripcion}")
                    return
        print("No hay repartidores disponibles en este momento.")

    def mostrar_pedidos_pendientes(self):
        """
        Muestra los pedidos pendientes en la cola de prioridad.
        """
        if not self.pedidos:
            print("No hay pedidos pendientes.")
        else:
            print("Pedidos pendientes:")
            for pedido in self.pedidos:
                print(f"ID: {pedido.id}, Descripción: {pedido.descripcion}, {'Urgente' if pedido.urgente else 'Normal'}")

    def agregar_repartidor(self, id):
        """
        Agrega un nuevo repartidor al sistema.
        
        Argumento:
            id (int): Identificador del repartidor.
        """
        repartidor = Repartidor(id)
        self.repartidores.append(repartidor)
        print(f"Repartidor {id} agregado.")

def main():
    sistema = SistemaDeEntrega()
    
    # Agregar repartidores
    sistema.agregar_repartidor(1)
    sistema.agregar_repartidor(2)
    
    # Agregar pedidos
    sistema.agregar_pedido(101, "Pedido normal 1", urgente=False)
    sistema.agregar_pedido(102, "Pedido urgente 1", urgente=True)
    sistema.agregar_pedido(103, "Pedido normal 2", urgente=False)
    
    # Mostrar los pedidos pendientes
    sistema.mostrar_pedidos_pendientes()
    
    # Asignar pedidos a los repartidores
    sistema.asignar_pedido()  # El pedido urgente debe ser atendido primero
    sistema.asignar_pedido()  # El siguiente pedido normal
    
    # Mostrar los pedidos restantes
    sistema.mostrar_pedidos_pendientes()

if __name__ == "__main__":
    main()