import lmstudio as lms

llm = lms.llm() # Get any loaded LLM

prediction = llm.respond_stream("In short, what is a Capybara?")

respuesta = ""

for token in prediction:
    # Si el token es un diccionario (o se puede convertir a uno)
    if hasattr(token, 'to_dict'):
        token_data = token.to_dict()
    elif isinstance(token, dict):
        token_data = token
    else:
        # Si el token viene como string con JSON dentro (menos común, pero por si acaso)
        import json
        token_data = json.loads(str(token))

    contenido = token_data.get("content")
    if contenido:
        respuesta += contenido

print(respuesta)