import random

# Predefined crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greetings = [
            "Hey there! Let's find you a green and growing crypto! 🌱",
            "Welcome! Ready to explore sustainable crypto options? 💚",
            "Hi! I'm here to help you make eco-friendly crypto choices! 🌍"
        ]
        self.disclaimer = "⚠️ Disclaimer: Crypto is risky—always do your own research! This is not financial advice."

    def greet(self):
        return random.choice(self.greetings)

    def analyze_query(self, user_query):
        user_query = user_query.lower()
        
        # Check for sustainability related queries
        if any(word in user_query for word in ["sustainable", "eco", "green", "environment"]):
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            return f"Based on sustainability, I recommend {recommend}! 🌱 It has a sustainability score of {crypto_db[recommend]['sustainability_score']}/10 and {crypto_db[recommend]['energy_use']} energy usage."
        
        # Check for trending/price related queries
        elif any(word in user_query for word in ["trend", "price", "growing", "rising"]):
            trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if trending_coins:
                return f"Currently trending coins are: {', '.join(trending_coins)} 📈"
            return "No coins are currently showing strong upward trends."
        
        # Check for market cap related queries
        elif "market" in user_query or "cap" in user_query:
            high_cap_coins = [coin for coin, data in crypto_db.items() if data["market_cap"] == "high"]
            return f"Coins with high market cap include: {', '.join(high_cap_coins)} 💰"
        
        # General investment advice
        elif any(word in user_query for word in ["invest", "buy", "recommend"]):
            # Find coins that are both trending and have good sustainability
            good_options = [
                coin for coin, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["sustainability_score"] >= 6/10
            ]
            if good_options:
                return f"For a balanced investment, consider: {', '.join(good_options)} 🎯"
            return "I don't see any coins currently meeting both profitability and sustainability criteria."
        
        return "I'm not sure I understand. You can ask me about sustainability, price trends, or investment recommendations!"

def main():
    bot = CryptoBuddy()
    print(bot.greet())
    print(bot.disclaimer)
    print("\nYou can ask me about:")
    print("- Sustainable crypto options")
    print("- Price trends and market caps")
    print("- Investment recommendations")
    print("\nType 'quit' to exit")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye! Remember to always do your own research! 👋")
            break
        
        response = bot.analyze_query(user_input)
        print(f"\nCryptoBuddy: {response}")

if __name__ == "__main__":
    main()
