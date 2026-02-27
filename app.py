<div style="max-width:400px;margin:auto;font-family:Arial;">
  <h3 style="text-align:center;">🤖 AarohiAI</h3>

  <div id="chatbox" style="height:250px;border:1px solid #ccc;
  overflow-y:auto;padding:10px;margin-bottom:10px;background:#f9f9f9;">
  </div>

  <input type="text" id="userInput" placeholder="Type your message..."
  style="width:70%;padding:8px;">
  
  <button onclick="sendMessage()" 
  style="padding:8px 12px;background:#4a4aff;color:white;border:none;">
  Send
  </button>
</div>

<script>
async function sendMessage() {
  const inputField = document.getElementById("userInput");
  const message = inputField.value;
  const chatbox = document.getElementById("chatbox");

  if(message.trim() === "") return;

  chatbox.innerHTML += "<div><b>You:</b> " + message + "</div>";

  inputField.value = "";

  try {
    const response = await fetch("https://aarohai-server.onrender.com/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    const aiReply = data.choices[0].message.content;

    chatbox.innerHTML += "<div><b>AarohiAI:</b> " + aiReply + "</div>";

  } catch (error) {
    chatbox.innerHTML += "<div><b>Error:</b> Server not responding</div>";
  }
}
</script>
