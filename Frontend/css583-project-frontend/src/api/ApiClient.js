import axios from "axios";

const baseUrl = process.env.REACT_APP_API_BASE_URL

async function postWord(data) {
    const url = `${baseUrl}/definition/`
    const response = await axios.post(url, data);
    return response.data;
}

async function getAllWords() {
    const url = `${baseUrl}/definition/`
    const response = await axios.get();
    return response.data;
}

async function getWordbyWord(word) {
    const url = `${baseUrl}/definition/${word}`
    const response = await axios.get(url);
    return response.data;
}

async function getWordbyId(id) {
    const url = `${baseUrl}/definition/${id}`
    const response = await axios.get(url);
    return response.data;
}

async function updateWordbyId(id, data) {
    const url = `${baseUrl}/definition/${id}`
    const response = await axios.put(url, data);
    return response.data;
  }

async function deleteWordbyId(id) {
    const url = `${baseUrl}/definition/${id}`
    const response = await axios.delete(url);
    return response.data;
}

async function postLlmCall(data) {
    const url = `${baseUrl}/llm/`
    const response = await axios.post(url, data);
    return response.data;
}

async function postLlmKeywordsCall(data) {
    const url = `${baseUrl}/llm/keywords`
    const response = await axios.post(url, data);
    return response.data;
}


export default {
  postWord,
  getAllWords,
  getWordbyWord,
  getWordbyId,
  updateWordbyId,
  deleteWordbyId,
  postLlmCall,
  postLlmKeywordsCall,
};