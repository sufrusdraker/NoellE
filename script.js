// Alterna a exibição da barra lateral
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const main = document.getElementById('main');
    sidebar.classList.toggle('hidden');
    main.classList.toggle('collapsed');
}

// Exibe o conteúdo correspondente à aba selecionada
function showContent(contentId) {
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => content.classList.remove('active'));
    const selectedContent = document.getElementById(contentId + '-content');
    if (selectedContent) {
        selectedContent.classList.add('active');
    }
}

// Função para enviar a mensagem para a API e obter a resposta
// Variável global para armazenar a URL da API
let apiUrl = null;

// Função para carregar a API apenas uma vez
async function initializeAPI() {
    if (!apiUrl) {
        apiUrl = "https://b406-2001-8a0-f4da-f200-61bb-9472-2fb3-9b15.ngrok-free.app";
    }
}

// Chama a função ao carregar o site
initializeAPI();

// Função para enviar a mensagem para a API e obter a resposta
async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatHistory = document.getElementById("chat-history");

    if (userInput.trim() !== "") {
        // Adiciona a mensagem do usuário ao histórico
        const userMessage = document.createElement("p");
        userMessage.innerHTML = `<strong>Você:</strong> ${userInput}`;
        chatHistory.appendChild(userMessage);

        // Limpa o campo de entrada
        document.getElementById("user-input").value = "";

        try {
            const apiResponse = await fetch(`${apiUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userInput })
            });

            const data = await apiResponse.json();

            if (data.response) {
                const botMessage = document.createElement("p");
                botMessage.innerHTML = `<strong>NoellE:</strong> ${data.response}`;
                chatHistory.appendChild(botMessage);
            } else {
                throw new Error('Resposta inválida da API');
            }
        } catch (error) {
            console.error('Erro na comunicação com a API:', error);
            const botMessage = document.createElement("p");
            botMessage.innerHTML = `<strong>NoellE:</strong> Desculpe, houve um erro ao tentar responder. Tente novamente mais tarde.`;
            chatHistory.appendChild(botMessage);
        }

        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
}

// Garante que o botão Enviar funcione ao pressionar Enter também
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

// Função para permitir o arrasto de itens no Quarto da NoellE
function allowDrop(event) {
    event.preventDefault();
}

// Função para iniciar o arrasto
function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

// Função para realizar o drop de um item arrastado
function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text");
    const element = document.getElementById(data);
    const room = document.getElementById("room");

    const roomRect = room.getBoundingClientRect();
    const x = event.clientX - roomRect.left - element.offsetWidth / 2;
    const y = event.clientY - roomRect.top - element.offsetHeight / 2;

    element.style.left = Math.max(0, Math.min(x, roomRect.width - element.offsetWidth)) + "px";
    element.style.top = Math.max(0, Math.min(y, roomRect.height - element.offsetHeight)) + "px";
}

// Função para resetar a posição dos móveis no Quarto da NoellE
function resetRoom() {
    const bed = document.getElementById("bed");
    const desk = document.getElementById("desk");
    const shelf = document.getElementById("shelf");

    bed.style.left = "10px";
    bed.style.bottom = "10px";
    desk.style.right = "10px";
    desk.style.bottom = "10px";
    shelf.style.left = "50%";
    shelf.style.top = "10px";
    shelf.style.transform = "translateX(-50%)";
}

// Adiciona os eventos para arrastar e soltar
document.getElementById("room").addEventListener("dragover", allowDrop);
document.getElementById("room").addEventListener("drop", drop);

// Ajustes para garantir a interação com as abas de conteúdo
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', function() {
        showContent(tab.dataset.contentId);
    });
});

// Garante que o botão "Enviar" seja acionado ao clicar nele
document.getElementById("send-button").addEventListener("click", sendMessage);
