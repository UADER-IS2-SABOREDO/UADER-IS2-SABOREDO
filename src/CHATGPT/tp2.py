import os
import requests
from dotenv import load_dotenv

try:
    import readline  # Solo funciona en sistemas tipo Unix o con readline instalado
except ImportError:
    print("El módulo 'readline' no está disponible. La funcionalidad de flecha ↑ puede no funcionar en Windows sin WSL o Git Bash.")

# Cargar la API key desde .env
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Historial para readline
historial = []

def enviar_consulta(consulta):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [
            {"role": "user", "content": consulta}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    respuesta = response.json()["choices"][0]["message"]["content"]
    return respuesta

print("Escribí una consulta (usá ↑ para recuperar la anterior). Escribí 'salir' para terminar.")

while True:
    try:
        consulta = input(">>> ").strip()

        if consulta.lower() == "salir":
            break

        if consulta:
            print(f"You: {consulta}")
            try:
                respuesta = enviar_consulta(consulta)
                print(f"chatGPT: {respuesta}")
                historial.append(consulta)
                if 'readline' in globals():
                    readline.add_history(consulta)
            except requests.exceptions.RequestException as e:
                print("Error al invocar la API:", e)

        else:
            print("La consulta está vacía.")

    except Exception as e:
        print("Ocurrió un error:", e)
