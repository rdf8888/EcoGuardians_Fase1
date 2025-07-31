// chat.js

async function criarNovoAgente(descricaoDaTarefa) {
    // URL do nosso endpoint de API na Vercel
    const apiUrl = '/api/gerar_agente'; 

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: descricaoDaTarefa }),
        });

        const data = await response.json();

        if (response.ok) {
            // Se a requisição foi bem-sucedida, exibe o código gerado
            console.log("Código do novo agente gerado:");
            console.log(data.codigo_gerado);
            return data.codigo_gerado;
        } else {
            // Em caso de erro, exibe a mensagem de erro
            console.error("Erro ao gerar agente:", data.error);
            return null;
        }

    } catch (error) {
        console.error("Erro na comunicação com o servidor:", error);
        return null;
    }
}

// Exemplo de como você chamaria a função
// Isso poderia ser acionado por um botão ou um comando do usuário
// no seu chat.
// await criarNovoAgente("Agente para monitorar a poluição em rios.");
