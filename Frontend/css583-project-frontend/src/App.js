import React from "react"; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import "./styles.css"

import Navbar from "./components/Navbar";

// import Home from "./pages/Home"; 
// import Code from "./pages/Code"; 
// import PersonalBlog from "./pages/PersonalBlog"; 
// import WorkUpdates from "./pages/WorkUpdates";
import CSS583Project from "./pages/CSS583Project";



  function App() {
    return (
      <div className="App">
      <Router>
        <Navbar />
        <Routes>
          {/* <Route path='/' element={<Home/>} /> */}
          {/* <Route path='/resume' element={<Resume/>} /> */}
          {/* <Route path='/code' element={<Code/>} /> */}
          {/* <Route path='/workUpdates' element={<WorkUpdates/>} />
          <Route path='/personalBlog' element={<PersonalBlog/>} /> */}
          <Route path='/CSS583Project' element={<CSS583Project/>} />
        </Routes>
      </Router>
      </div>
    );
  }
    
  export default App;

    


