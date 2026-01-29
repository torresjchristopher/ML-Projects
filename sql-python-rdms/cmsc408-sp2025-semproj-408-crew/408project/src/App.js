import logo from './logo.svg';
import './App.css';
import Navbar from './NavBar/NavBar.js';
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div>
      <Navbar />
    </div>
    </BrowserRouter>
  );
}

export default App;
