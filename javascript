// api/generate-agent.js
import { GoogleGenerativeAI } from "@google/generative-ai";

export default async function handler(request, response) {
  // Sua chave de API deve ser lida de uma variável de ambiente (por segurança!)
  const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-pro" });

  try {
    const { prompt } = request.body;

    // O prompt é a instrução que seu agente EcoGuardians enviará para o Gemini
    // para que ele crie um novo agente autônomo.
    const result = await model.generateContent(prompt);
    const text = result.response.text();

    response.status(200).json({ newAgentCode: text });
  } catch (error) {
    console.error(error);
    response.status(500).json({ error: "Ocorreu um erro ao gerar o agente." });
  }
}
