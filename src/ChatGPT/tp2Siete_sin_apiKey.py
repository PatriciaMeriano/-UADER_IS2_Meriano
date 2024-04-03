import argparse
import openai

# Clave de API de OpenAI
api_key = 'sk-KjbMS6bUpm-------------------JMXkbp'

# Lista para almacenar las consultas y respuestas previas
consultas_respuestas_previas = []

def consultar_chatGPT(consulta):
    """
    Consulta el modelo de ChatGPT con la consulta proporcionada
    y devuelve la respuesta generada.
    """
    try:
        # Configura el cliente de OpenAI con la clave de API
        openai.api_key = api_key

        # Concatenar todas las consultas previas junto con la consulta actual
        consulta_completa = "\n".join([par[0] for par in consultas_respuestas_previas] + [consulta])
    
        # Llama a la API de OpenAI para obtener una respuesta de ChatGPT
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": consulta_completa}],
            max_tokens=500,
        )
        
        respuesta_chatGPT = respuesta.choices[0].message["content"]
        
        # Agregar la consulta y la respuesta al búfer de consultas y respuestas previas
        consultas_respuestas_previas.append((consulta, respuesta_chatGPT))
        
        return respuesta_chatGPT
    except Exception as e:
        print("Error al consultar ChatGPT:", e)
        return None

# La función principal del programa
def main():
    """
    Función principal del programa que maneja el modo de conversación
    con ChatGPT basado en los argumentos de línea de comandos proporcionados.
    """
    # Configurar el análisis de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Programa de conversación con ChatGPT")
    parser.add_argument("--convers", action="store_true", help="Modo de conversación con ChatGPT")
    args = parser.parse_args()

    # Verificar si se ha proporcionado el argumento --convers
    if args.convers:
        print("Modo de conversación activado. Para salir, escribe 'q'.")

        while True:
            try:
                # Leer la entrada del usuario
                entrada_usuario = input("You: ")

                # Salir del bucle si el usuario ingresa 'q'
                if entrada_usuario.lower() == 'q':
                    print("Saliendo del programa...")
                    break

                # Si se presiona la tecla "cursor Up", obtén la última consulta realizada
                if entrada_usuario == "\x1b[A":
                    if len(consultas_respuestas_previas) > 0:
                        consulta_anterior = consultas_respuestas_previas[-1][0]
                        print("Editando consulta anterior:", consulta_anterior)
                        entrada_usuario = input("You: ")
                    else:
                        print("No hay consultas anteriores para editar.")
                        continue

                # Almacenar la consulta actual en la lista de consultas previas
                if entrada_usuario.strip():  # Verificar si la consulta no está vacía
                    respuesta_chatGPT = consultar_chatGPT(entrada_usuario)
                    print("chatGPT:", respuesta_chatGPT)

                # Imprimir la consulta
                print("You:", entrada_usuario)

            except KeyboardInterrupt:
                print("\nSaliendo del programa...")
                break
            except Exception as e:
                print("Error en la ejecución del programa:", e)
    else:
        print("Modo de conversación no activado. Utiliza '--convers' para activarlo.")

if __name__ == "__main__":
    main()

