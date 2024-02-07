import axios from "axios";

const baseURL = `http://${process.env.API_HOST}:${process.env.API_PORT}`;

async function postWord(data) {
    url = `${baseURL}/definition/`
    const response = await axios.post(url, data);
    return response.data;
}

async function getAllWords() {
    url = `${baseURL}/definition/`
    const response = await axios.get();
    return response.data;
}

async function getWordbyWord(word) {
    url = `${baseURL}/definition/${word}`
    const response = await axios.get(url);
    return response.data;
}

async function getWordbyId(id) {
    url = `${baseURL}/definition/${id}`
    const response = await axios.get(url);
    return response.data;
}

async function updateWordbyId(id, data) {
    url = `${baseURL}/definition/${id}`
    const response = await axios.put(url, data);
    return response.data;
  }

async function deleteWordbyId(id) {
    url = `${baseURL}/definition/${id}`
    const response = await axios.delete(url);
    return response.data;
}

async function postLlmCall(data) {
    url = `${baseURL}/llm/`
    const response = await axios.post(url, data);
    return response.data;
}

async function postLlmKeywordsCall(data) {
    url = `${baseURL}/llm/keywords`
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