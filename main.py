import requests

def dish_fetch(num):
    """
    Busca un plato típico en tiempo real usando la API de Colombia.
    Devuelve un diccionario con la información del plato o None si no existe.
    """
    
    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
    
    try:
        
        response = requests.get(url)
        
        
        if response.status_code == 200:
            
            dish_data = response.json()
            return dish_data
        else:
          
            return None
            
    except requests.exceptions.RequestException:
        
        print("\n[Error de conexión con la API]")
        return None


def main():
    print("¡Bienvenido al Menú en Vivo de Platos Típicos de Colombia!")
    print("==========================================================")
    print("Consulta en tiempo real los platos típicos de Colombia.")
    print("==========================================================")
    while True:
        try:
            user_choice = int(input("Introduce el ID del plato que deseas consultar (ej: 1, 2, 5): "))
            
            
            dish_info = dish_fetch(user_choice)
            
            if dish_info:
                print("\n--- Detalles Obtenidos de la API ---")
                
                print(f"Nombre:      {dish_info.get('name')}")
                print(f"Descripción: {dish_info.get('description')}")
            else:
                print("\nNo se encontró ningún plato con ese ID o hubo un problema en la red.")
        except ValueError:
            print("\nPor favor, introduce un número entero válido.")


if __name__ == "__main__":
    main()