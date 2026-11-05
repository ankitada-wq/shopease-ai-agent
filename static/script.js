const chatToggle = document.getElementById("chat-toggle");
const chatWindow = document.getElementById("chat-window");
const closeChat = document.getElementById("close-chat");

const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatMessages = document.getElementById("chat-messages");


// Open chatbot
chatToggle.addEventListener("click", () => {
    chatWindow.style.display = "block";
    chatToggle.style.display = "none";
    userInput.focus();
});


// Close chatbot
closeChat.addEventListener("click", () => {
    chatWindow.style.display = "none";
    chatToggle.style.display = "block";
});


// Display messages
function addMessage(message, className) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(className);

    // Prevent HTML injection
    messageDiv.textContent = message;

    chatMessages.appendChild(messageDiv);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


// Send message to backend
async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") return;

    // Display user message
    addMessage(message, "user-message");

    userInput.value = "";

    // Loading message
    const loading = document.createElement("div");

    loading.classList.add("bot-message");
    loading.textContent = "Thinking...";

    chatMessages.appendChild(loading);

    sendBtn.disabled = true;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();

        loading.remove();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        addMessage(data.response, "bot-message");

    }

    catch (error) {

        loading.remove();

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot-message"
        );

        console.error(error);

    }

    finally {

        sendBtn.disabled = false;
        userInput.focus();

    }

}


// Send button
sendBtn.addEventListener("click", sendMessage);


// Enter key
userInput.addEventListener("keypress", (event) => {

    if (event.key === "Enter") {
        sendMessage();
    }

});
function sendQuickReply(message) {
    userInput.value = message;
    sendMessage();
}