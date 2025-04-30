from fastapi import FastAPI, Request
from pydantic import BaseModel
import lmstudio as lms
import json

app = FastAPI()
llm = lms.llm()  # Conecta con LM Studio


class PromptRequest(BaseModel):
    prompt: str


@app.post("/chat")
def chat(request_data: PromptRequest):
    prompt = request_data.prompt
    prediction = llm.respond_stream(prompt)

    respuesta = ""
    for token in prediction:
        # Adaptarse al tipo del token
        if hasattr(token, 'to_dict'):
            token_data = token.to_dict()
        elif isinstance(token, dict):
            token_data = token
        else:
            token_data = json.loads(str(token))

        contenido = token_data.get("content")
        if contenido:
            respuesta += contenido

    return {"respuesta": respuesta}
