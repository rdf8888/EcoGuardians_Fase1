
function login() {
    const user = document.getElementById("user").value;
    const pass = document.getElementById("pass").value;
    if (user === "admin" && pass === "eco123") {
        document.getElementById("painel").style.display = "block";
        carregarHistorico();
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
            contents: [{ parts: [{ text: pergunta }] }]
        })
    });

    const data = await resposta.json();
    const respostaTexto = data?.candidates?.[0]?.content?.parts?.[0]?.text || "🤖 Erro ao responder.";

    document.getElementById("resposta").innerText = "🤖 Agente: " + respostaTexto;
    salvarNoHistorico(pergunta, respostaTexto);
}

async function salvarNoHistorico(pergunta, resposta) {
    await supabase.from("conversas").insert([
        {
            usuario: "admin",
            mensagem: pergunta,
            resposta: resposta
        }
    ]);
    carregarHistorico();
}

async function carregarHistorico() {
    const { data } = await supabase.from("conversas").select("*").order("data", { ascending: false }).limit(10);
    const div = document.getElementById("historico");
    div.innerHTML = "";
    data.forEach(item => {
        div.innerHTML += `<p><b>Você:</b> ${item.mensagem}<br/><b>IA:</b> ${item.resposta}</p><hr/>`;
    });
}

async function criarAgente() {
    const nome = prompt("Nome do novo agente:");
    const funcao = prompt("Qual será a função dele?");
    if (nome && funcao) {
        await supabase.from("agentes").insert([{ nome, função: funcao }]);
        alert("🤖 Novo agente registrado no sistema!");
    }
}
