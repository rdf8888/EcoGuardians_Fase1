
function login() {
    const user = document.getElementById("user").value;
    const pass = document.getElementById("pass").value;
    if (user === "admin" && pass === "eco123") {
        document.getElementById("painel").style.display = "block";
    } else {
        alert("Credenciais incorretas.");
    }
}

function enviarPerguntaIA() {
    const pergunta = document.getElementById("chat").value;
    enviarParaGemini(pergunta);
}

async function enviarParaGemini(pergunta) {
    const resposta = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            contents: [
                {
                    parts: [{ text: pergunta }]
                }
            ]
        })
    });

    const data = await resposta.json();
    const respostaTexto = data?.candidates?.[0]?.content?.parts?.[0]?.text || "🤖 Erro ao responder.";
    document.getElementById("resposta").innerText = "🤖 Agente: " + respostaTexto;
}

function criarAgente() {
    document.getElementById("resposta").innerText = "✨ Novo agente criado! (Simulação ativa, em breve será real.)";
}
