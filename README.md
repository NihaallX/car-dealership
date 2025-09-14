# Best Cars Dealership Management System

A comprehensive full-stack web application for managing car dealerships, reviews, and customer interactions. Built with Django, React, Express.js, and MongoDB.

## Project Overview

This project is a complete dealership management system that includes:

- **Django Backend**: Main web application with user authentication, dealership management, and admin interface
- **React Frontend**: Modern, responsive user interface for customer interactions
- **Express.js API**: RESTful API with MongoDB for dealer and review data management
- **Sentiment Analysis Service**: Node.js microservice for analyzing review sentiments
- **Containerized Deployment**: Docker and Docker Compose configuration for easy deployment

## Features

### Core Functionality
- [x] User authentication (login, logout, signup)
- [x] Dealership browsing and filtering by state
- [x] Customer reviews and ratings
- [x] Sentiment analysis of reviews
- [x] Admin interface for managing cars and dealerships
- [x] Responsive design for all devices

### API Endpoints
- **Django REST API**: `/api/` routes for frontend integration
- **Express API**: Dealer and review management endpoints
- **Sentiment API**: Text sentiment analysis service

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React         │    │   Django        │    │   Express       │
│   Frontend      │◄──►│   Backend       │◄──►│   API           │
│   (Port 3000)   │    │   (Port 8000)   │    │   (Port 3030)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                 │
                       ┌─────────────────┐
                       │   Sentiment     │
                       │   Analyzer      │
                       │   (Port 5000)   │
                       └─────────────────┘
```

## Technology Stack

### Backend
- **Django 4.2+**: Web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Primary database
- **Redis**: Caching and session storage

### Frontend
- **React 18**: User interface library
- **React Router**: Client-side routing
- **Axios**: HTTP client
- **Bootstrap 5**: CSS framework

### APIs & Services
- **Express.js**: RESTful API server
- **MongoDB**: Document database for dealer data
- **Node.js Sentiment**: Natural language processing

### DevOps
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **GitHub Actions**: CI/CD pipeline
- **Nginx**: Reverse proxy and load balancing

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker and Docker Compose (optional)
- PostgreSQL (if not using Docker)
- MongoDB (if not using Docker)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd dealership-management-system
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up Django**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python create_superuser.py
   python create_sample_data.py
   ```

4. **Install Node.js dependencies**
   ```bash
   # Express API
   cd express-server
   npm install
   cd ..
   
   # Sentiment Analyzer
   cd sentiment-analyzer
   npm install
   cd ..
   
   # React Frontend
   cd frontend
   npm install
   cd ..
   ```

5. **Start all services**
   ```bash
   # Terminal 1 - Django
   python manage.py runserver 8000
   
   # Terminal 2 - Express API
   cd express-server && node server.js
   
   # Terminal 3 - Sentiment Analyzer
   cd sentiment-analyzer && node app.js
   
   # Terminal 4 - React Frontend (optional)
   cd frontend && npm start
   ```

### Docker Setup (Recommended)

1. **Build and start all services**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - Main App: http://localhost:8000
   - Express API: http://localhost:3030
   - Sentiment Analyzer: http://localhost:5000
   - React Frontend: http://localhost:3000

## API Documentation

### Django API Endpoints
- `GET /` - Home page with dealer listings
- `GET /about/` - About us page
- `GET /contact/` - Contact page
- `POST /login/` - User login
- `POST /logout/` - User logout
- `POST /signup/` - User registration
- `GET /dealer/<id>/` - Dealer details with reviews
- `POST /add_review/<dealer_id>/` - Add review

### Express API Endpoints
- `GET /dealerships/get` - Get all dealerships
- `GET /dealerships/get/<state>` - Get dealerships by state
- `GET /dealerships/dealer/<id>` - Get dealer by ID
- `GET /reviews/dealer/<id>` - Get reviews for dealer
- `POST /reviews/add` - Add new review

### Sentiment Analysis API
- `POST /analyze` - Analyze single text sentiment
- `POST /analyze-batch` - Analyze multiple texts
- `GET /health` - Service health check

## Testing

### Run Django Tests
```bash
python manage.py test
```

### Run with Coverage
```bash
coverage run --source='.' manage.py test
coverage report
```

### API Testing
```bash
# Test Express API
curl http://localhost:3030/dealerships/get

# Test Sentiment API
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a great product!"}'
```

## Deployment

### Production Deployment
1. Set environment variables
2. Configure production database
3. Build and deploy Docker containers
4. Set up reverse proxy (Nginx)
5. Configure SSL certificates

### Environment Variables
```bash
DEBUG=False
DATABASE_URL=postgresql://user:pass@localhost/dbname
REDIS_URL=redis://localhost:6379/0
MONGODB_URI=mongodb://localhost:27017/dealership
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Project Structure

```
dealership-management-system/
├── dealership_project/          # Django project settings
├── dealerships/                 # Main Django app
├── cars/                       # Car models app
├── reviews/                    # Reviews app
├── sentiment_service/          # Sentiment integration app
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   └── public/
├── express-server/             # Express.js API
├── sentiment-analyzer/         # Sentiment analysis service
├── templates/                  # Django templates
├── static/                     # Static files
├── .github/workflows/          # CI/CD pipeline
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Task Completion Checklist

This project addresses all 28 required tasks:

### Static Pages (Tasks 2-4)
- [x] Django server running
- [x] About Us page
- [x] Contact Us page

### User Authentication (Tasks 5-7)
- [x] Login functionality with React frontend
- [x] Logout with confirmation
- [x] Sign-up page

### Express-MongoDB API (Tasks 8-11)
- [x] Dealer reviews endpoint
- [x] All dealers endpoint
- [x] Dealer details endpoint
- [x] Dealers by state (Kansas) endpoint

### Admin Interface (Tasks 12-15)
- [x] Admin login (root user)
- [x] Admin logout
- [x] Car makes management
- [x] Car models management

### Sentiment Analysis (Task 16)
- [x] Sentiment analyzer service with visible endpoint

### Dynamic Pages (Tasks 17-22)
- [x] Dealers on home page (before login)
- [x] Dealers on home page (after login) with Post Review button
- [x] Dealers filtered by state
- [x] Dealer details with reviews
- [x] Add review page
- [x] Added review display

### CI/CD & Deployment (Tasks 23-28)
- [x] GitHub Actions CI/CD pipeline
- [x] Deployment URL ready
- [x] Containerized application
- [x] All pages accessible via deployment

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact:
- Email: support@bestcarsdealership.com
- GitHub: [Your GitHub Profile]