# GFC Financial Chatbot

## Overview

This project is a lightweight AI-powered financial chatbot developed using **Python** and **Flask**.  
It allows users to query **predefined financial insights** related to **Apple, Microsoft, and Tesla** for the years **2021–2023**.

### Example Queries
- *"What is the total revenue for Apple in 2023?"*
- *"How has net income changed for Microsoft from 2021 to 2023?"*
- *"Tell me about Tesla's operating cash flow."*

---

## Features

- Rule-based chatbot logic (no ML/NLP for simplicity)
- Clean, responsive web interface using HTML/CSS
- Loads and processes financial data from CSV
- Secure and production-safe backend logic
- Modular, readable, and maintainable code
![alt text](image.png)
---

## Project Structure

```

financial\_chatbot/
├── app.py                        # Main Flask app
├── templates/
│   └── index.html               # Chat UI
├── data/
│   └── final\_financial\_data.csv # Cleaned financial dataset
├── static/                      # (optional for future assets like JS/CSS)
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignore untracked files
└── README.md                    # Project documentation

````

---

## Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
````

2. **Create and activate virtual environment**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python app.py
```

5. **Open in your browser**
   Navigate to: [http://localhost:5000](http://localhost:5000)

---

## Limitations

* The chatbot supports **only predefined queries**.
* No dynamic NLP or AI/ML models (can be extended later).
* Financial data updates must be done **manually**.

---

## Author

**Costas Pinto**
*2025 | BCG AI Insights | GFC Project*

---

## License

**MIT License**
