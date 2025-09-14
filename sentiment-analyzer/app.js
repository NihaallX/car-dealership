const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const Sentiment = require('sentiment');

const app = express();
const PORT = process.env.PORT || 5000;
const sentiment = new Sentiment();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Analyze sentiment endpoint
app.post('/analyze', (req, res) => {
    try {
        const { text } = req.body;
        
        if (!text) {
            return res.status(400).json({ error: 'Text is required' });
        }

        const result = sentiment.analyze(text);
        
        let sentimentLabel;
        if (result.score > 0) {
            sentimentLabel = 'positive';
        } else if (result.score < 0) {
            sentimentLabel = 'negative';
        } else {
            sentimentLabel = 'neutral';
        }

        res.json({
            text: text,
            score: result.score,
            comparative: result.comparative,
            sentiment: sentimentLabel,
            positive: result.positive,
            negative: result.negative,
            calculation: result.calculation
        });
    } catch (error) {
        console.error('Error analyzing sentiment:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Batch analyze endpoint
app.post('/analyze-batch', (req, res) => {
    try {
        const { texts } = req.body;
        
        if (!texts || !Array.isArray(texts)) {
            return res.status(400).json({ error: 'Texts array is required' });
        }

        const results = texts.map(text => {
            const result = sentiment.analyze(text);
            
            let sentimentLabel;
            if (result.score > 0) {
                sentimentLabel = 'positive';
            } else if (result.score < 0) {
                sentimentLabel = 'negative';
            } else {
                sentimentLabel = 'neutral';
            }

            return {
                text: text,
                score: result.score,
                sentiment: sentimentLabel
            };
        });

        res.json({ results });
    } catch (error) {
        console.error('Error analyzing sentiment batch:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Health check
app.get('/health', (req, res) => {
    res.json({ status: 'OK', message: 'Sentiment Analyzer is running' });
});

// Root endpoint
app.get('/', (req, res) => {
    res.json({
        message: 'Sentiment Analyzer API',
        endpoints: {
            'POST /analyze': 'Analyze sentiment of a single text',
            'POST /analyze-batch': 'Analyze sentiment of multiple texts',
            'GET /health': 'Health check'
        },
        example: {
            analyze: {
                method: 'POST',
                url: '/analyze',
                body: { text: 'This is a great product!' }
            }
        }
    });
});

// Error handling
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
    console.log(`Sentiment Analyzer is running on http://localhost:${PORT}`);
});

module.exports = app;