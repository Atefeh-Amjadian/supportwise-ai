const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const chatBox = document.getElementById("chat-box");

function addMessage(text, sender) {
  const messageDiv = document.createElement("div");

  messageDiv.classList.add("message", sender);
  messageDiv.textContent = text;

  chatBox.appendChild(messageDiv);

  chatBox.scrollTop = chatBox.scrollHeight;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const userMessage = input.value.trim();

  if (!userMessage) return;

  addMessage(userMessage, "user");

  input.value = "";

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: userMessage,
      }),
    });

    const data = await response.json();

    addMessage(data.reply, "bot");

  } catch (error) {
    addMessage("Failed to connect to backend.", "bot");
  }
});