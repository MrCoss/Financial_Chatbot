from flask import Flask, render_template, request
import pandas as pd
import logging
import re

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename="flask_chatbot.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

# Load dataset
try:
    df = pd.read_csv("data/financial_data.csv")
except Exception as e:
    logging.error(f"❌ Failed to load data: {e}")
    raise RuntimeError("Critical error loading financial data.")

# Sanitize user input
def sanitize_input(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower()).strip()

# Chatbot response logic
def get_response(user_query: str) -> str:
    try:
        query = sanitize_input(user_query)

        if "total revenue" in query and "apple" in query:
            value = df.query("Company == 'Apple' and Year == 2023")["Total Revenue"].values[0]
            return f"Apple's total revenue in 2023 was ${value:,.0f} million."

        elif "net income" in query and "microsoft" in query:
            start = df.query("Company == 'Microsoft' and Year == 2021")["Net Income"].values[0]
            end = df.query("Company == 'Microsoft' and Year == 2023")["Net Income"].values[0]
            trend = "increased" if end > start else "decreased"
            return f"Microsoft's net income {trend} from ${start:,.0f}M in 2021 to ${end:,.0f}M in 2023."

        elif "operating cash flow" in query and "tesla" in query:
            return "Tesla’s operating cash flow increased from $11B in 2021 to $16B in 2023."

        elif "total assets" in query and "apple" in query:
            value = df.query("Company == 'Apple' and Year == 2023")["Total Assets"].values[0]
            return f"Apple reported total assets of ${value:,.0f} million in 2023."

        elif "liabilities" in query and "microsoft" in query:
            start = df.query("Company == 'Microsoft' and Year == 2021")["Total Liabilities"].values[0]
            end = df.query("Company == 'Microsoft' and Year == 2022")["Total Liabilities"].values[0]
            return f"Microsoft’s total liabilities increased from ${start:,.0f}M (2021) to ${end:,.0f}M (2022)."

        else:
            return "Sorry, I can only answer a few predefined financial questions. Try asking about revenue, assets, or income for Apple or Microsoft."

    except Exception as e:
        logging.exception(f"Error in chatbot logic: {e}")
        return "An error occurred while processing your question. Please try again later."

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_query = ""
    if request.method == "POST":
        user_query = request.form["user_query"]
        response = get_response(user_query)
    return render_template("index.html", response=response, user_query=user_query)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
