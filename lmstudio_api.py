import requests
import json

# URL de la API en localhost
api_url = "http://127.0.0.1:1234"  # Cambia el puerto si es necesario

# Payload con el prompt
data = {
    "model": "llama3",  # O el nombre del modelo que estés usando
    "messages": [{"role": "user", "content": "What is a Capybara?"}],
    "stream": True  # Habilitar el streaming de tokens
}

# Cabeceras para la solicitud (puedes agregar si necesitas autenticación)
headers = {
    "Content-Type": "application/json"
}

# Realizar la solicitud POST a la API de LM Studio
response = requests.post(api_url, json=data, headers=headers, stream=True)

# Comprobar si la respuesta es exitosa
if response.status_code == 200:
    # Iterar sobre el contenido del flujo y extraer el texto
    for chunk in response.iter_lines(decode_unicode=True):
        if chunk:  # Ignorar líneas vacías
            try:
                # Verificar el contenido crudo
                print(f"Recibiendo chunk: {chunk}")

                # Convertir la respuesta en JSON para obtener el texto
                message = json.loads(chunk)
                print(f"Mensaje recibido: {message}")  # Ver contenido de mensaje

                if 'content' in message:
                    print(message['content'], end='', flush=True)  # Imprimir el texto generado
            except json.JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")
else:
    print(f"Error: {response.status_code} - {response.text}")

