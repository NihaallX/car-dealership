const express = require('express');
const cors = require('cors');
const { MongoClient } = require('mongodb');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3030;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// MongoDB connection (using in-memory data for now)
let db;
let dealersCollection;
let reviewsCollection;

// Sample data
const sampleDealers = [
  {
    id: 1,
    dealerId: 1,
    name: "Best Cars Toyota",
    city: "Austin",
    state: "TX", 
    zip: "78701",
    address: "123 Main St",
    lat: 30.2672,
    long: -97.7431,
    short_name: "Toyota Austin",
    st: "TX"
  },
  {
    id: 2,
    dealerId: 2,
    name: "Ford Downtown",
    city: "Dallas",
    state: "TX",
    zip: "75201", 
    address: "456 Commerce St",
    lat: 32.7767,
    long: -96.7970,
    short_name: "Ford Dallas",
    st: "TX"
  },
  {
    id: 3,
    dealerId: 3,
    name: "BMW Luxury Motors",
    city: "Los Angeles",
    state: "CA",
    zip: "90210",
    address: "789 Rodeo Dr",
    lat: 34.0522,
    long: -118.2437,
    short_name: "BMW LA",
    st: "CA"
  },
  {
    id: 4,
    dealerId: 4,
    name: "Honda City",
    city: "Kansas City",
    state: "KS",
    zip: "66101",
    address: "321 Kansas Ave", 
    lat: 39.0997,
    long: -94.5786,
    short_name: "Honda KC",
    st: "KS"
  }
];

const sampleReviews = [
  {
    id: 1,
    dealership: 1,
    name: "John Smith",
    purchase: true,
    review: "Great service and friendly staff. Highly recommend this dealership!",
    purchase_date: "10/15/2023",
    car_make: "Toyota",
    car_model: "Camry",
    car_year: 2023
  },
  {
    id: 2,
    dealership: 1,
    name: "Sarah Johnson", 
    purchase: true,
    review: "Good experience overall, but the wait time was a bit long.",
    purchase_date: "09/20/2023",
    car_make: "Toyota",
    car_model: "Prius",
    car_year: 2023
  },
  {
    id: 3,
    dealership: 2,
    name: "Mike Wilson",
    purchase: true,
    review: "Excellent customer service and great deals on Ford vehicles.",
    purchase_date: "08/05/2023",
    car_make: "Ford", 
    car_model: "F-150",
    car_year: 2023
  },
  {
    id: 4,
    dealership: 4,
    name: "Lisa Brown",
    purchase: true,
    review: "Professional staff and clean facility. Very satisfied with my Honda purchase.",
    purchase_date: "11/01/2023",
    car_make: "Honda",
    car_model: "Civic", 
    car_year: 2023
  }
];

// Initialize in-memory data
let dealers = [...sampleDealers];
let reviews = [...sampleReviews];

// Routes

// Get all dealerships
app.get('/dealerships/get', (req, res) => {
  res.json(dealers);
});

// Get dealerships by state
app.get('/dealerships/get/:state', (req, res) => {
  const state = req.params.state.toUpperCase();
  const filteredDealers = dealers.filter(dealer => 
    dealer.state.toUpperCase() === state || dealer.st.toUpperCase() === state
  );
  res.json(filteredDealers);
});

// Get dealer by ID
app.get('/dealerships/dealer/:id', (req, res) => {
  const dealerId = parseInt(req.params.id);
  const dealer = dealers.find(d => d.dealerId === dealerId || d.id === dealerId);
  
  if (dealer) {
    res.json(dealer);
  } else {
    res.status(404).json({ error: 'Dealer not found' });
  }
});

// Get reviews for a specific dealer
app.get('/reviews/dealer/:id', (req, res) => {
  const dealerId = parseInt(req.params.id);
  const dealerReviews = reviews.filter(review => review.dealership === dealerId);
  res.json(dealerReviews);
});

// Add a new review
app.post('/reviews/add', (req, res) => {
  const newReview = {
    id: reviews.length + 1,
    dealership: parseInt(req.body.dealership),
    name: req.body.name,
    purchase: req.body.purchase === 'true' || req.body.purchase === true,
    review: req.body.review,
    purchase_date: req.body.purchase_date,
    car_make: req.body.car_make,
    car_model: req.body.car_model,
    car_year: req.body.car_year ? parseInt(req.body.car_year) : null
  };
  
  reviews.push(newReview);
  res.status(201).json({ message: 'Review added successfully', review: newReview });
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'OK', message: 'Express-MongoDB API is running' });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({ 
    message: 'Dealership Express-MongoDB API',
    endpoints: {
      'GET /dealerships/get': 'Get all dealerships',
      'GET /dealerships/get/:state': 'Get dealerships by state',
      'GET /dealerships/dealer/:id': 'Get dealer by ID',
      'GET /reviews/dealer/:id': 'Get reviews for a dealer',
      'POST /reviews/add': 'Add a new review'
    }
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({ error: 'Endpoint not found' });
});

app.listen(PORT, () => {
  console.log(`Express server is running on http://localhost:${PORT}`);
  console.log('Available endpoints:');
  console.log('- GET /dealerships/get (all dealers)');
  console.log('- GET /dealerships/get/:state (dealers by state)');
  console.log('- GET /dealerships/dealer/:id (dealer details)');
  console.log('- GET /reviews/dealer/:id (dealer reviews)');
  console.log('- POST /reviews/add (add review)');
});

module.exports = app;