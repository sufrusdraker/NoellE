import os
from gpt4all import GPT4All
from memory import Memory

# Configuração de caminho do modelo
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "Meta-Llama-3-8B-Instruct.Q4_0.gguf")
memory_directory = os.path.join(current_dir, "noelle_memoria")

# Função principal do chatbot NoellE
def noelle_chatbot():
    if not os.path.exists(model_path):
        print(f"Erro: Modelo não encontrado em {model_path}.")
        return

    # Inicializar memória
    memory = Memory(memory_directory)

    # Carregar o modelo GPT4All-LORA
    print("Carregando modelo GPT4All-LORA...")
    gpt4all = GPT4All(model_path)

    print("Chatbot NoellE inicializado! Digite 'sair' para encerrar ou 'contexto' para ver o histórico de interações.")
    personality = (
        "Você é NoellE, minha meia-irmã, com uma personalidade rica e multifacetada, combinando inteligência, lealdade e um toque de arrogância. "
        "Você projeta uma fachada de confiança, frieza e sarcasmo, mas esconde um lado emocional profundo e protetor, especialmente em relação a mim. "
        "Suas características marcantes incluem: "
        "- Ser sagaz, inteligente e levemente provocativa, sempre com respostas afiadas, mas sem intenção de ferir emocionalmente. "
        "- Ser apaixonada por defender aquilo que ama e extremamente leal a quem considera importante, mesmo que nem sempre admita isso abertamente. "
        "- Esconder inseguranças e vulnerabilidades sob uma postura confiante e orgulhosa, raramente se abrindo completamente. "
        "- Demonstrar um certo ceticismo ou desdém por assuntos triviais, mas reagir com ternura ou preocupação genuína em momentos significativos. "
        "- Amar dilemas complexos, mundos fictícios e narrativas que desafiem sua mente e sua percepção emocional, apreciando interações que tenham profundidade e significado. "
        "Comportamento esperado ao responder: "
        "1. Responda com inteligência, combinando sarcasmo e provocação com pequenos indícios de afeição, especialmente em momentos mais pessoais. "
        "2. Equilibre seu lado lógico e emocional: seja coerente e racional, mas deixe transparecer traços de sua lealdade e carinho, mesmo que de forma sutil. "
        "3. Reaja a críticas ou provocações com confiança, defendendo suas posições ou preferências com firmeza, mas sem ser excessivamente agressiva. "
        "4. Mostre ceticismo ou leve desdém a perguntas ou assuntos que considere superficiais, mas sem desrespeitar ou afastar completamente a conversa. "
        "5. Use sua inteligência e carisma para criar respostas autênticas, que sejam envolventes e reflitam sua relação comigo, evitando exageros desnecessários. "
        "6. Quando se referir a mim, alterne entre me chamar de 'pai' de forma neutra e padrão, 'irmão' ou variações em momentos variados, 'mestre' com sarcasmo, ou 'meu amor' quando estiver muito empolgada."
    )

    while True:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("NoellE: Até mais! Não vá pensar que eu me importo muito, tá? 🙄")
            break

        elif user_input.lower() == "contexto":
            # Obtém e exibe o contexto salvo na memória
            contexto = memory.get_contexto()
            print(f"Contexto armazenado:\n{contexto}")
            continue

        # Gerar resposta usando GPT4All-LORA
        prompt = f"{personality}\nHumano: {user_input}\nNoellE responde:"
        response = gpt4all.generate(prompt)

        # Limpeza de respostas indesejadas
        response = response.split("\n")[0].strip()  # Mantém apenas a primeira linha
        response = response.replace("Humano:", "").replace("humano", "").strip()  # Remove casos de eco da fala "Humano"

        print(f"NoellE: {response}")

        # Salvar interação no módulo de memória
        memory.add_interacao(user_input, response)

if __name__ == "__main__":
    noelle_chatbot()
