import React, { useState, useEffect } from 'react';
import './CSS583ProjectStyle.css';
import apiClient from '../api/ApiClient.js';



function CSS583Project() {
  const [words, setWords] = useState([]);
  const [selectedWord, setSelectedWord] = useState(null);
  const [alternateDefinition, setAlternateDefinition] = useState('');
  const [newKeyword, setNewKeyword] = useState('');
  const [newSearchWord, setNewSearchWord] = useState('');
  const [newDescription, setNewDescription] = useState('');
  const [llmSuggestion, setLlmSuggestion] = useState('');

  useEffect(() => {
    const fetchWords = async () => {
      try {
        const allWords = await apiClient.getAllWords();
        setWords(allWords);
      } catch (error) {
        console.error('Error fetching words:', error);
      }
    };

    fetchWords();
  }, []);

  const handleWordClick = async (word) => {
    setSelectedWord(word);
      
  try {
   const alternateDefinitionResponse = await apiClient.postLlmDefineTermCall(word.word);
   setAlternateDefinition(alternateDefinitionResponse.text);
   } catch (error) {
      console.error('Error fetching word definition:', error);
   }
  };

  const handleNewWordSubmit = async () => {
    try {
      await apiClient.postWord({ word: newKeyword, definition: newDescription });
 
      const allWords = await apiClient.getAllWords();
      setWords(allWords);
 
      setNewKeyword('');
      setNewDescription('');
    } catch (error) {
      console.error('Error adding new word:', error);
    }
  };

  const handleNewWordSuggestion = async () => {
    try {     
 
      const llmSuggestionText = await apiClient.postLlmDefineTermCall({ word: newKeyword });
      setLlmSuggestion(llmSuggestionText.text);
 
    } catch (error) {
      console.error('Error adding new word:', error);
    }
  };
 

  // const handleUserInputChange = (event) => {
  //   setUserInput(event.target.value);
  // };

  // const handleUserInputChangeSearch = (event) => {
  //   setUserInputSearch(event.target.value);
  // };

  const handleNewSearch = async () => {
    try {     
 
      const searchWord = await apiClient.getWordbyWord({ word: newSearchWord });
      setSelectedWord(searchWord);
 
    } catch (error) {
      console.error('Error adding new word:', error);
    }

  setNewSearchWord('');
  };



  // const handleUserInputSubmit = async () => {
  //   apiClient.postLlmCall(userInput)
  //   setInputHistory((prevHistory) => [...prevHistory, userInput]);

  //   // try {
  //   //   //LLM response API 
  //   //   const response = await fetch(`LLM RESPONSE API${userInput}`);
  //   //   const data = await response.json();
  //   //   setApiResponse(data.response); // Adjust this based on your API structure
  //   // } catch (error) {
  //   //   console.error('Error fetching data:', error);
  //   // }


  //   setUserInput('');
  // };

  return (
    <div id="CSS583Project">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gridGap: 20 }}>
      <div className="side-panel-left">
        <ul>
        {words.map((word) => (
            <li key={word} onClick={() => handleWordClick(word)} style={{ cursor: 'pointer' }}>
              {word.word}
        </li>
        ))}
        </ul>
      </div>
      <div>
        <div className="search-container">
          <input
            type="text"
            className="search-bar"
            placeholder="Search..."
            value={newSearchWord}
            onChange={(e) => setNewSearchWord(e.target.value)}
          />
          <button onClick={handleNewSearch}>Submit</button>
        </div>

        <div className="result-container">
        {selectedWord && (
          <div>
            <h2>Word:</h2>
            <p>{selectedWord.word}</p>
            <h2>Definition:</h2>
            <p>{selectedWord.definition}</p>
            <h2>Alternate Suggestion:</h2>
            <p>{alternateDefinition}</p>
          </div>
        )}
        </div>
        
      </div>
      <div>
      <div className="side-panel-right">
          <h2>Add New Word</h2>
          <div>
            <label>Word: </label>
            <input type="text" value={newKeyword} onChange={(e) => setNewKeyword(e.target.value)} />
          </div>
          <p/>
          <div>
            <label>Description: </label>
            <input type="text" value={newDescription} onChange={(e) => setNewDescription(e.target.value)} />
          </div>
          <button onClick={handleNewWordSubmit}>Submit</button>
          <p/>
          <button onClick={handleNewWordSuggestion}>Get Suggestion</button>        
          <h2>LLM Suggestion</h2>
          <p>{llmSuggestion}</p>
        </div>

      </div>
      {/* <div className="side-panel-right">
        <div className="search-container">
          <input
            type="text"
            className="search-bar"
            placeholder="LLM Text Input"
            value={userInput}
            onChange={handleUserInputChange}
          />
          <button onClick={handleUserInputSubmit}>Submit</button>
        </div>
        <div className="input-history">
          <h2>Input History</h2>
          <ul>
            {inputHistory.map((input, index) => (
              <li key={index}>{input}</li>
            ))}
          </ul>
        </div>
        <div className="LLM-response">
          <h2>LLM Response</h2>
          <p>{LLMResponse}</p>
        </div>
      </div> */}
      </div>
    </div>
  );
}

export default CSS583Project;
