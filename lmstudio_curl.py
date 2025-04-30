

url = "http://localhost:1234/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "llama-3.2-1b-instruct",
    "messages": [
        {"role": "system", "content": "Constesta como un profesor  de informática"},
        {"role": "user", "content": "En una frase, que es un lenguaje de programación"}
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Mostrar respuesta (puedes adaptarlo según lo que devuelva el servidor)
print(response.status_code)
respuesta_json = response.json()
mensaje = respuesta_json['choices'][0]['message']['content']
print(mensaje)
