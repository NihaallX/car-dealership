import React from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Navbar({ user, isAuthenticated, onLogout }) {
  const handleLogout = async () => {
    try {
      await axios.post('/logout/', {}, { withCredentials: true });
      onLogout();
      alert('Logged out successfully!');
    } catch (error) {
      console.error('Logout error:', error);
      onLogout(); // Logout locally even if API call fails
    }
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand fw-bold" to="/">Best Cars Dealership</Link>
        
        <button 
          className="navbar-toggler" 
          type="button" 
          data-bs-toggle="collapse" 
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
          </ul>
          
          <ul className="navbar-nav">
            {isAuthenticated ? (
              <>
                <li className="nav-item">
                  <span className="navbar-text me-3">
                    Welcome, {user?.username || user?.first_name || 'User'}!
                  </span>
                </li>
                <li className="nav-item">
                  <button 
                    className="nav-link btn btn-link" 
                    onClick={handleLogout}
                    style={{ border: 'none', background: 'none' }}
                  >
                    Logout
                  </button>
                </li>
              </>
            ) : (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/login">Login</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/signup">Sign Up</Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;