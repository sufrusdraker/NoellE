document.addEventListener("DOMContentLoaded", function () {
    const chatHistory = document.getElementById("chat-history");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    // URL da API do chatbot
    const chatbotAPI = "http://192.168.1.75:5000";

    // Função para enviar a mensagem do usuário
    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        // Exibir a mensagem do usuário no chat
        appendMessage("Você: " + message, "user");

        // Limpar o campo de entrada
        userInput.value = "";

        try {
            // Fazer requisição para a API
            const response = await fetch(chatbotAPI, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message }),
            });

            if (response.ok) {
                const data = await response.json();
                appendMessage("NoellE: " + data.reply, "bot");
            } else {
                appendMessage("Erro: Não foi possível se conectar ao chatbot.", "bot");
            }
        } catch (error) {
            appendMessage("Erro: " + error.message, "bot");
        }
    }

    // Função para adicionar mensagens ao histórico do chat
    function appendMessage(text, className) {
        const messageElement = document.createElement("p");
        messageElement.textContent = text;
        messageElement.className = className;
        chatHistory.appendChild(messageElement);

        // Rolar para o final
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    // Event listeners
    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});
