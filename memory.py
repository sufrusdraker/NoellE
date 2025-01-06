import json
import os

class Memory:
    def __init__(self, directory):
        # Caminho para o diretório de memória
        self.directory = directory
        self.memory_file = os.path.join(directory, 'memory.json')

        # Se o arquivo não existir, cria um novo com a estrutura inicial
        if not os.path.exists(self.memory_file):
            self.initialize_memory()

    def initialize_memory(self):
        """Cria a estrutura inicial do arquivo de memória caso não exista."""
        memory_data = {
            "interacoes": [],
            "memorias_falsas": []
        }
        self.save_data(memory_data)

    def load_data(self):
        """Carrega os dados do arquivo memory.json."""
        try:
            with open(self.memory_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Arquivo {self.memory_file} não encontrado. Criando arquivo novo.")
            self.initialize_memory()
            return self.load_data()
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {self.memory_file}. O arquivo pode estar corrompido.")
            return {}

    def save_data(self, data):
        """Salva os dados no arquivo memory.json."""
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar o arquivo {self.memory_file}: {e}")

    def add_interacao(self, interacao, resposta):
        """Adiciona uma nova interação ao arquivo de memória."""
        memory_data = self.load_data()
        memory_data["interacoes"].append({"interacao": interacao, "resposta": resposta})
        self.save_data(memory_data)

    def add_memoria_falsa(self, interacao, resposta):
        """Adiciona uma memória falsa ao arquivo de memória."""
        memory_data = self.load_data()
        memory_data["memorias_falsas"].append({"interacao": interacao, "resposta": resposta})
        self.save_data(memory_data)

    def get_interacoes(self):
        """Retorna as interações armazenadas no arquivo de memória."""
        memory_data = self.load_data()
        return memory_data.get("interacoes", [])

    def get_memorias_falsas(self):
        """Retorna as memórias falsas armazenadas no arquivo de memória."""
        memory_data = self.load_data()
        return memory_data.get("memorias_falsas", [])
