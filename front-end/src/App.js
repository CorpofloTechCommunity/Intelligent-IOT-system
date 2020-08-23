import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter } from 'react-router-dom';
import Login from './components/loginComponent';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Login/>
      </div>
    </BrowserRouter>
  );
}

export default App;
