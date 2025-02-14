import openai
from dotenv import load_dotenv
import os

# Carregar a chave da API
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Configurar o cliente da OpenAI
openai.api_key = API_KEY

# Fazer uma pergunta de teste
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "O que é o Instituto de Computação da UFBA?"}]
)

print(response["choices"][0]["message"]["content"])
