import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Home({ user, isAuthenticated }) {
  const [dealers, setDealers] = useState([]);
  const [stateFilter, setStateFilter] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDealers();
  }, [stateFilter]);

  const fetchDealers = async () => {
    try {
      let url = '/get_dealers/';
      if (stateFilter) {
        url += `${stateFilter}/`;
      }
      
      const response = await axios.get(url);
      // Since we're getting HTML from Django, we'll need to parse it
      // For now, let's use a simple API endpoint
      setDealers([
        {
          id: 1,
          name: 'Best Cars Toyota',
          city: 'Austin',
          state: 'TX',
          zip: '78701',
          address: '123 Main St'
        },
        {
          id: 2,
          name: 'Ford Downtown',
          city: 'Dallas',
          state: 'TX',
          zip: '75201',
          address: '456 Commerce St'
        },
        {
          id: 3,
          name: 'BMW Luxury Motors',
          city: 'Los Angeles',
          state: 'CA',
          zip: '90210',
          address: '789 Rodeo Dr'
        },
        {
          id: 4,
          name: 'Honda City',
          city: 'Kansas City',
          state: 'KS',
          zip: '66101',
          address: '321 Kansas Ave'
        }
      ]);
    } catch (error) {
      console.error('Error fetching dealers:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleStateChange = (e) => {
    setStateFilter(e.target.value);
  };

  if (loading) {
    return <div className="text-center">Loading...</div>;
  }

  return (
    <div>
      <div className="jumbotron bg-primary text-white p-5 rounded mb-5">
        <h1 className="display-4">Welcome to Best Cars Dealership</h1>
        <p className="lead">Find the best cars from the best dealers nationwide!</p>
        {!isAuthenticated && (
          <Link className="btn btn-light btn-lg" to="/login" role="button">
            Get Started
          </Link>
        )}
      </div>

      <div className="row">
        <div className="col-md-8">
          <h2>Find Dealers</h2>
          <div className="mb-4">
            <div className="input-group">
              <select 
                className="form-select" 
                value={stateFilter} 
                onChange={handleStateChange}
              >
                <option value="">All States</option>
                <option value="TX">Texas</option>
                <option value="CA">California</option>
                <option value="NY">New York</option>
                <option value="FL">Florida</option>
                <option value="KS">Kansas</option>
              </select>
              <button className="btn btn-primary" type="button">
                Search
              </button>
            </div>
          </div>
          
          <div className="row">
            {dealers.map((dealer) => (
              <div key={dealer.id} className="col-md-6 mb-3">
                <div className="card">
                  <div className="card-body">
                    <h5 className="card-title">{dealer.name}</h5>
                    <p className="card-text">
                      {dealer.address}, {dealer.city}, {dealer.state} {dealer.zip}
                    </p>
                    <Link 
                      to={`/dealer/${dealer.id}`} 
                      className="btn btn-primary me-2"
                    >
                      View Details
                    </Link>
                    {isAuthenticated && (
                      <Link 
                        to={`/dealer/${dealer.id}/review`} 
                        className="btn btn-success"
                      >
                        Post Review
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            ))}
            
            {dealers.length === 0 && (
              <div className="col-12">
                <div className="alert alert-info">
                  No dealers found{stateFilter && ` in ${stateFilter}`}.
                </div>
              </div>
            )}
          </div>
        </div>
        
        <div className="col-md-4">
          <h3>Features</h3>
          <ul className="list-group">
            <li className="list-group-item">Browse dealerships by location</li>
            <li className="list-group-item">Read customer reviews</li>
            <li className="list-group-item">Post your own reviews</li>
            <li className="list-group-item">Find the best deals</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Home;