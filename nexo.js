
const chatBox = document.getElementById('chat-box');
const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');

// Simulação de IA básica com comandos simples
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const userMessage = input.value.trim();
  if (!userMessage) return;

  appendMessage('Você', userMessage);
  input.value = '';

  let resposta = await processarMensagem(userMessage);
  appendMessage('NEXO', resposta);
});

function appendMessage(remetente, mensagem) {
  const p = document.createElement('p');
  p.innerHTML = `<strong>${remetente}:</strong> ${mensagem}`;
  chatBox.appendChild(p);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function processarMensagem(msg) {
  msg = msg.toLowerCase();

  if (msg.includes("criar agente")) {
    return "🧠 Novo agente em criação... (função em desenvolvimento)";
  } else if (msg.includes("buscar") || msg.includes("pesquise")) {
    return "🔍 Em breve, conectarei com a IA ChatGPT para pesquisas externas.";
  } else if (msg.includes("oi") || msg.includes("olá")) {
    return "Olá! Eu sou o NEXO. Estou aqui para te ajudar no EcoGuardians.";
  } else if (msg.includes("quem é você")) {
    return "Sou o Agente NEXO, o primeiro guardião digital do ecossistema EcoGuardians.";
  }

  return "🤖 Comando não reconhecido. Tente outra instrução ou aguarde atualizações de inteligência.";
}
