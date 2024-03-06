import React, { useState, useEffect } from 'react';
import './CSS583ProjectStyle.css';
import ApiClient from '../api/ApiClient.js';



function CSS583Project() {
  const [options, setOptions] = useState([]);

  const [selectedOption, setSelectedOption] = useState(null);

  const [userInput, setUserInput] = useState('');
  const [userInputSearch, setUserInputSearch] = useState('');
  const [inputHistory, setInputHistory] = useState([]);

  const [LLMResponse, setLLMResponse] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const words = await ApiClient.getAllWords();
        setOptions(words);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleOptionClick = (index) => {
    setSelectedOption(index === selectedOption ? null : index);
  };

  const handleUserInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleUserInputChangeSearch = (event) => {
    setUserInputSearch(event.target.value);
  };

  const handleUserInputSubmitSearch = async () => {

    try {
      // getWordByWord
      const response = await ApiClient.getWordbyWord(userInput);
    } catch (error) {
      console.error('Error fetching data:', error);
    }


    setUserInputSearch('');
  };


  const handleUserInputSubmit = async () => {
    //postLlmCall(userInput)
    setInputHistory((prevHistory) => [...prevHistory, userInput]);

    // try {
    //   //LLM response API 
    //   const response = await fetch(`LLM RESPONSE API${userInput}`);
    //   const data = await response.json();
    //   setApiResponse(data.response); // Adjust this based on your API structure
    // } catch (error) {
    //   console.error('Error fetching data:', error);
    // }


    setUserInput('');
  };

  return (
    <div id="CSS583Project">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gridGap: 20 }}>
      <div className="side-panel-left">
        <ul>
        {options.map((option, index) => (
          <li
          key={index}
          className={index === selectedOption ? 'selected' : ''}
          onClick={() => handleOptionClick(index)}
          >
          {option.word} {/* Render the specific property you want */}
        </li>
        ))}
        </ul>
      </div>
      <div className="search-container">
        <input
          type="text"
          className="search-bar"
          placeholder="Search..."
          value={userInputSearch}
          onChange={handleUserInputChangeSearch}
        />
        <button onClick={handleUserInputSubmitSearch}>Submit</button>
      </div>
      <div className="side-panel-right">
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
      </div>
      </div>
    </div>
  );
}

export default CSS583Project;
