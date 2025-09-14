import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import axios from 'axios';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Login from './components/Login';
import Signup from './components/Signup';
import DealerDetails from './components/DealerDetails';

// Configure axios defaults
axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

function App() {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check if user is already logged in
    const checkAuth = async () => {
      try {
        const response = await axios.get('/api/auth/user/', {
          withCredentials: true
        });
        if (response.data.user) {
          setUser(response.data.user);
          setIsAuthenticated(true);
        }
      } catch (error) {
        console.log('Not authenticated');
      }
    };
    checkAuth();
  }, []);

  const handleLogin = (userData) => {
    setUser(userData);
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    setUser(null);
    setIsAuthenticated(false);
  };

  return (
    <Router>
      <div className="App">
        <Navbar user={user} isAuthenticated={isAuthenticated} onLogout={handleLogout} />
        <div className="container mt-4">
          <Routes>
            <Route path="/" element={<Home user={user} isAuthenticated={isAuthenticated} />} />
            <Route 
              path="/login" 
              element={
                isAuthenticated ? 
                <Navigate to="/" replace /> : 
                <Login onLogin={handleLogin} />
              } 
            />
            <Route 
              path="/signup" 
              element={
                isAuthenticated ? 
                <Navigate to="/" replace /> : 
                <Signup onLogin={handleLogin} />
              } 
            />
            <Route path="/dealer/:dealerId" element={<DealerDetails user={user} />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;