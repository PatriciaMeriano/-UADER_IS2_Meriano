from abc import ABC, abstractmethod

#Definición de la interfaz IPing:
#clase abstracta que define un método abstracto llamado execute. 
#Las clases que implementen esta interfaz deben proporcionar una implementación concreta para este método.
#El método execute toma un argumento ip_address de tipo cadena y no devuelve ningún valor.


class IPing(ABC):
    @abstractmethod
    def execute(self, ip_address: str) -> None:
        pass

#Clase Ping:
#La clase Ping no hereda de ninguna otra clase, tiene dos métodos: execute y executefree.
#El método execute verifica si la dirección IP comienza con “192.” y, si es así, realiza 10 intentos de ping a esa dirección.
#El método executefree siempre realiza 10 intentos de ping a la dirección IP proporcionada, sin restricciones de dirección.

class Ping:
    def execute(self, ip_address: str) -> None:
        if ip_address.startswith("192."):
            for _ in range(10):
                # Realizar intento de ping a la dirección IP
                print(f"Pinging {ip_address}... (attempt {_ + 1})")
        else:
            print("Error: IP address must start with '192.'")

    def executefree(self, ip_address: str) -> None:
        for _ in range(10):
            # Realizar intento de ping sin restricciones de dirección
            print(f"Pinging {ip_address}... (attempt {_ + 1})")

# Ejemplo de uso
#Se crea una instancia de la clase Ping llamada ping_instance
ping_instance = Ping()
#Se llama al método execute de ping_instance con la dirección IP “192.168.0.1”, lo que debería funcionar correctamente.
ping_instance.execute("192.168.0.1")  # Funciona correctamente
#Luego, se llama al método executefree con la dirección IP “8.8.8.8”, que también funciona sin restricciones.
ping_instance.executefree("8.8.8.8")   # Funciona sin restricciones

class PingProxy(IPing):
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address: str) -> None:
        if ip_address == "192.168.0.254":
            # Realiza un ping a www.google.com usando el método executefree de Ping
            self.ping.execute("www.google.com")
        else:
            # Reenvía la solicitud a la clase Ping
            self.ping.execute(ip_address)
            
if __name__ == "__main__":
    ping_proxy = PingProxy()
    ping_proxy.execute("192.168.0.254")  # Realizará un ping a www.google.com
    ping_proxy.execute("192.168.1.1")    # Realizará pings a la dirección IP proporcionada
    ping_proxy.execute("10.0.0.1")       # No realizará pings (no comienza con "192.")

