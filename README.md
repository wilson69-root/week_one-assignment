CryptoBuddy - AI-Powered Crypto Investment Assistant 🤖
Overview
CryptoBuddy is a rule-based chatbot that provides cryptocurrency investment advice based on profitability and sustainability metrics. It analyzes predefined crypto data to offer recommendations while considering risk and market trends.

Features
💬 Interactive chat interface
📊 Analysis of crypto trends and sustainability
💰 Market cap information
🌱 Sustainability scoring
⚠️ Built-in risk disclaimers
How It Works
Data Structure
The bot uses a predefined database (crypto_db) containing information about different cryptocurrencies:

Python
{
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    # ... other cryptocurrencies
}
Decision Making Process
Query Analysis: The bot analyzes user input for keywords related to:

Sustainability
Price trends
Market capitalization
Investment recommendations
Response Generation: Based on the query type, the bot:

Calculates sustainability scores
Identifies trending cryptocurrencies
Filters by market cap
Provides balanced investment advice
Key Functions
greet(): Generates friendly welcome messages
analyze_query(): Processes user input and generates appropriate responses
main(): Handles the interactive chat loop
Usage
Run the script:

bash
python app.py
Interact with the bot using questions like:

"Which crypto is most sustainable?"
"What's trending right now?"
"What should I invest in?"
"Tell me about market caps"
Type 'quit' to exit the chat

AI Decision Making
The bot demonstrates basic AI principles through:

Pattern matching in user queries
Rule-based decision making
Data analysis and filtering
Contextual response generation
Disclaimer
⚠️ This is a demonstration project. The bot uses predefined data and should not be used for actual investment decisions. Always do your own research before investing in cryptocurrencies.

Future Improvements
Integration with real-time crypto data APIs
Enhanced natural language processing
More sophisticated analysis algorithms
Expanded cryptocurrency database
