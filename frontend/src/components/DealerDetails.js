import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

function DealerDetails({ user }) {
  const { dealerId } = useParams();
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDealerDetails();
  }, [dealerId]);

  const fetchDealerDetails = async () => {
    try {
      // For now, use sample data
      const sampleDealer = {
        id: parseInt(dealerId),
        name: 'Best Cars Toyota',
        city: 'Austin',
        state: 'TX',
        zip: '78701',
        address: '123 Main St'
      };

      const sampleReviews = [
        {
          id: 1,
          name: 'John Smith',
          review: 'Great service and friendly staff. Highly recommend this dealership!',
          purchase: true,
          purchase_date: '2023-10-15',
          car_make: 'Toyota',
          car_model: 'Camry',
          car_year: 2023,
          sentiment: 'positive'
        },
        {
          id: 2,
          name: 'Sarah Johnson',
          review: 'Good experience overall, but the wait time was a bit long.',
          purchase: true,
          purchase_date: '2023-09-20',
          car_make: 'Toyota',
          car_model: 'Prius',
          car_year: 2023,
          sentiment: 'neutral'
        }
      ];

      setDealer(sampleDealer);
      setReviews(sampleReviews);
    } catch (error) {
      console.error('Error fetching dealer details:', error);
    } finally {
      setLoading(false);
    }
  };

  const getSentimentBadge = (sentiment) => {
    switch (sentiment) {
      case 'positive':
        return 'bg-success';
      case 'negative':
        return 'bg-danger';
      default:
        return 'bg-secondary';
    }
  };

  if (loading) {
    return <div className="text-center">Loading...</div>;
  }

  if (!dealer) {
    return <div className="alert alert-danger">Dealer not found</div>;
  }

  return (
    <div className="row">
      <div className="col-md-8">
        <h1>{dealer.name}</h1>
        <div className="card mb-4">
          <div className="card-body">
            <h5 className="card-title">Dealer Information</h5>
            <p className="card-text">
              <strong>Address:</strong> {dealer.address}<br />
              <strong>City:</strong> {dealer.city}, {dealer.state} {dealer.zip}<br />
            </p>
            {user && (
              <Link 
                to={`/dealer/${dealer.id}/review`} 
                className="btn btn-success"
              >
                Post Review
              </Link>
            )}
          </div>
        </div>

        <h2>Customer Reviews</h2>
        {reviews.map((review) => (
          <div key={review.id} className="card mb-3">
            <div className="card-body">
              <div className="d-flex justify-content-between align-items-start">
                <div>
                  <h5 className="card-title">{review.name}</h5>
                  {review.purchase && (
                    <span className="badge bg-success me-2">Verified Purchase</span>
                  )}
                  <span className={`badge ${getSentimentBadge(review.sentiment)}`}>
                    {review.sentiment.charAt(0).toUpperCase() + review.sentiment.slice(1)}
                  </span>
                </div>
              </div>
              <p className="card-text mt-2">{review.review}</p>
              {review.purchase && review.car_make && (
                <small className="text-muted">
                  Purchased: {review.car_year} {review.car_make} {review.car_model}
                  {review.purchase_date && ` on ${review.purchase_date}`}
                </small>
              )}
            </div>
          </div>
        ))}

        {reviews.length === 0 && (
          <div className="alert alert-info">
            No reviews yet. {user && (
              <Link to={`/dealer/${dealer.id}/review`}>
                Be the first to post a review!
              </Link>
            )}
          </div>
        )}
      </div>

      <div className="col-md-4">
        <div className="card">
          <div className="card-body">
            <h5 className="card-title">Quick Actions</h5>
            {user ? (
              <Link 
                to={`/dealer/${dealer.id}/review`} 
                className="btn btn-success w-100 mb-2"
              >
                Post Review
              </Link>
            ) : (
              <p className="text-muted">
                Please <Link to="/login">login</Link> to post a review.
              </p>
            )}
            <Link to="/" className="btn btn-outline-primary w-100">
              Back to Home
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default DealerDetails;