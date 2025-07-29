
function login() {
    const user = document.getElementById("user").value;
    const pass = document.getElementById("pass").value;
    if (user === "admin" && pass === "eco123") {
        document.getElementById("painel").style.display = "block";
    } else {
        alert("Credenciais incorretas.");
    }
}

function enviarMensagem() {
    const msg = document.getElementById("chat").value;
    document.getElementById("resposta").innerText = "🤖 Agente: (resposta simulada) "" + msg + """;
}

function criarAgente() {
    document.getElementById("resposta").innerText = "✨ Novo agente criado (simulação). Em breve ele aprenderá sozinho!";
}
