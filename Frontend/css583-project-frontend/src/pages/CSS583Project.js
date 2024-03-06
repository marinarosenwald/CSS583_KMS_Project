import React, { useState } from 'react';
import './CSS583ProjectStyle.css';

function CSS583Project() {
  const [options, setOptions] = useState([
    'Option 1',
    'Option 2',
    'Option 3',
    'Option 4',
  ]);

  const [selectedOption, setSelectedOption] = useState(null);

  const handleOptionClick = (index) => {
    setSelectedOption(index === selectedOption ? null : index);
  };

  const [userInput, setUserInput] = useState('');

  const handleUserInputChange = (event) => {
    setUserInput(event.target.value);
  };

  return (
    <div id="CSS583Project">
      <div className="search-container">
        <input type="text" className="search-bar" placeholder="Search..." />
      </div>
      <div className="side-panel-left">
        <ul>
          {options.map((option, index) => (
            <li
              key={index}
              className={index === selectedOption ? 'selected' : ''}
              onClick={() => handleOptionClick(index)}
            >
              {option}
            </li>
          ))}
        </ul>
      </div>
      <div className="side-panel-right">
        <input
          type="text"
          value={userInput}
          onChange={handleUserInputChange}
          placeholder="Enter your text here..."
        />
      </div>
    </div>
  );
}

export default CSS583Project;
