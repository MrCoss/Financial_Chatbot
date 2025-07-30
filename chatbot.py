import pandas as pd
import logging
import re
from typing import Optional

# Setup basic logging
logging.basicConfig(
    filename="chatbot_logs.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Load cleaned financial data
try:
    df = pd.read_csv("data/financial_data.csv")
    logging.info("✅ Financial data loaded successfully.")
except FileNotFoundError:
    logging.error("❌ Financial data file not found.")
    raise SystemExit("Critical Error: Data file missing.")
except Exception as e:
    logging.exception(f"❌ Unexpected error loading data: {e}")
    raise SystemExit("Critical Error: Unable to load financial data.")


# Utility to clean and standardize user input
def sanitize_input(query: str) -> str:
    return re.sub(r"[^\w\s]", "", query.lower()).strip()


# Core logic for handling predefined financial queries
def get_financial_response(user_query: str) -> str:
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
            logging.warning(f"⚠️ Unrecognized query: {user_query}")
            return "Sorry, I can only provide information on a few predefined financial queries. Please try again with keywords like 'revenue', 'net income', or 'assets'."

    except KeyError as ke:
        logging.error(f"KeyError in data lookup: {ke}")
        return "Oops! Some expected financial data is missing. Please check back later."
    except Exception as e:
        logging.exception(f"❌ Unexpected error in chatbot logic: {e}")
        return "An unexpected error occurred while processing your request. Please try again later."


# Optional: print supported queries
def print_supported_queries():
    print("\nSample queries you can ask:")
    print("• What is Apple’s total revenue?")
    print("• How has Microsoft’s net income changed?")
    print("• Tell me about Tesla's operating cash flow.")
    print("• What are Apple’s total assets?")
    print("• Microsoft’s liabilities trend")


# CLI entry point
if __name__ == "__main__":
    print("📊 Welcome to the GFC Financial Chatbot!")
    print("Type your financial question or type 'exit' to quit.")
    print_supported_queries()

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! 👋")
                break

            response = get_financial_response(user_input)
            print("Chatbot:", response)

        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Session ended by user.")
            break
        except Exception as e:
            logging.exception(f"⚠️ Fatal error during user interaction: {e}")
            print("Chatbot: Something went wrong. Please try again.")
