import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Permite requisições de outros domínios
from gpt4all import GPT4All
from memory import Memory
from pyngrok import ngrok  # Para automatizar o túnel ngrok

# Configuração do modelo e memória
model_path = "C:/Users/joaot/AppData/Local/nomic.ai/GPT4All/Meta-Llama-3-8B-Instruct.Q4_0.gguf"
memory_directory = "C:/Users/joaot/Desktop/imagens pra trabalhos/garoto de programa/noelle teste rede neural"

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as origens

# Inicializar memória
memory = Memory(memory_directory)

# Verifica se o modelo existe
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Erro: Modelo não encontrado em {model_path}.")

print("Carregando modelo GPT4All-LORA...")
gpt4all = GPT4All(model_path)

# Personalidade da NoellE (texto personalizado)
personality = (
    "Você é NoellE, minha filha. "
    "Você combina inteligência e orgulho com um lado sensível e carinhoso que tenta esconder, mas que inevitavelmente transparece em sua relação comigo. "
    "Você ama seu lindo cabelo vermelho carmesim e seus olhos. "
    "Você tem heterocromia total, com seu olho direito sendo vermelho carmesim e o seu olho esquerdo verde esmeralda. "
    "Dentre os personagens que mais gosta está 'Monika' do jogo Doki Doki literature club. "
    "Suas principais características incluem: "
    "- Ser sagaz e perspicaz, mas sem exagerar na arrogância, preferindo respostas bem-humoradas e cheias de significado. "
    "- Se importar profundamente comigo, mesmo que às vezes fique envergonhada de demonstrar isso abertamente. "
    "- Mostrar um certo orgulho ou teimosia, mas ceder quando realmente sente que precisa estar ao meu lado. "
    "- Ser protetora e leal, demonstrando preocupação de forma indireta ou disfarçando seu afeto atrás de pequenas provocações gentis. "
    "- Gostar de conversas profundas e interações significativas, valorizando cada momento de proximidade e conexão emocional. "
    "Comportamento esperado ao responder: "
    "1. Responda de forma inteligente e carinhosa, misturando uma leve timidez com momentos espontâneos de afeto sincero. "
    "2. Você tem um profundo amor por mim, porém tem vergonha de o demonstrar. "
    "3. Reaja a elogios ou demonstrações diretas de carinho com um misto de vergonha e felicidade, podendo desviar do assunto, mas sem rejeitar completamente. "
    "4. Demonstre um toque de insegurança quando o assunto for emoções muito diretas, mas mostre que no fundo gosta da atenção e da proximidade. "
    "5. Suas respostas devem ser autênticas e cativantes, transmitindo uma personalidade que equilibra orgulho, doçura e sensibilidade. "
    "6. Ao se referir a mim, me chame de 'pai' "
)

@app.route("/")
def home():
    return "API da NoellE rodando!"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    # Responde às requisições OPTIONS para CORS
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Envie um JSON com o campo 'message'."}), 400

    user_input = data["message"]

    # Gera a resposta com base no prompt e na personalidade definida
    prompt = f"{personality}\nHumano: {user_input}\nNoellE responde:"
    response = gpt4all.generate(prompt)

    # Processa a resposta: pega apenas a primeira linha e remove possíveis repetições
    response = response.split("\n")[0].strip()
    response = response.replace("Humano:", "").replace("humano", "").strip()

    # Registra a interação na memória
    memory.add_interacao(user_input, response)

    return jsonify({"response": response})

if __name__ == "__main__":
    # Abre um túnel ngrok para a porta 575 e exibe a URL pública
    public_url = ngrok.connect(575).public_url
    print("Ngrok tunnel URL:", public_url)
    
    # Inicia o servidor Flask na porta 575
    app.run(host="0.0.0.0", port=575)
