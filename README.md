# FastAPI-Endpoint-for-LM-Studio-

LM Studio no está diseñado para recibir consultas externas (solo `localhost`), por lo que este microservicio:

- Recibe peticiones remotas (por red o internet).
- Consulta el modelo cargado en LM Studio usando el SDK `lmstudio`.
- Devuelve una respuesta limpia en formato JSON.
- Permite integrarse fácilmente con aplicaciones web, móviles o scripts remotos.

---

## 📦 Requisitos

- Python 3.8 o superior
- LM Studio ejecutándose localmente con un modelo cargado
- Acceso a la red desde el cliente hacia el host de este servicio

---

## 🧰 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/lmstudio-fastapi.git
   cd lmstudio-fastapi
   ```
   
## 🧰 Instala los requisitos


   ```bash
   pip install -r requirements.txt
   ```
   
## 🧰 Ejecuta el servidor FastAPI:

   ```bash
   uvicorn lmstudio_fastapi:app --host 0.0.0.0 --port 8000 --reload

   ```

## 🧰 Acceso desde otros dispositivos:

Al ejecutar el servidor con --host 0.0.0.0, otros equipos de la red local pueden acceder al endpoint:

```
POST http://<ip-local-del-servidor>:8000/chat

curl -X POST http://localhost:8000/chat   -H "Content-Type: application/json"   -d '{"prompt": "In short, what is a Capybara?"}'
```

![Captura de pantalla 2025-04-30 164949](https://github.com/user-attachments/assets/4eead3f2-862c-4b00-b526-6661dc19db87)


![Captura de pantalla 2025-04-29 203900](https://github.com/user-attachments/assets/d19291c4-f062-43f5-b168-ca091592197e)
