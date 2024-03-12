import React from "react"; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import "./styles.css"

import Navbar from "./components/Navbar";

import CSS583Project from "./pages/CSS583Project";



  function App() {
    return (
      <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path='./CSS583Project' element={<CSS583Project/>} />
        </Routes>
      </Router>
      </div>
    );
  }
    
  export default App;

    


