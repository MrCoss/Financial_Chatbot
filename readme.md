# GFC Financial Chatbot

[![Status: Completed](https://img.shields.io/badge/Status-Completed-green.svg)](https://shields.io/)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, AI-powered financial chatbot developed using **Python** and **Flask**. This application provides a simple, conversational interface for users to query predefined financial data for major tech companies, demonstrating a practical application of data-driven web development.
<img width="917" height="687" alt="image" src="https://github.com/user-attachments/assets/9b7cd600-d90f-41f8-9c04-4e788d8751c4" />



---

## Table of Contents
- [1. Project Rationale & Objective](#1-project-rationale--objective)
- [2. Features & Functionality](#2-features--functionality)
- [3. Technical Workflow: How It Works](#3-technical-workflow-how-it-works)
- [4. Project Structure Explained](#4-project-structure-explained)
- [5. Technical Stack](#5-technical-stack)
- [6. Setup & Installation Guide](#6-setup--installation-guide)
- [7. Limitations & Future Scope](#7-limitations--future-scope)
- [8. Author & License](#8-author--license)

---

## 1. Project Rationale & Objective

Financial reports and datasets are often dense and difficult for non-technical users to navigate. The objective of this project is to bridge that gap by creating an intuitive conversational interface for accessing key financial metrics.

Instead of parsing complex spreadsheets, a user can simply ask a question in plain English, such as:
- *"What was the total revenue for Apple in 2023?"*
- *"How did net income change for Microsoft from 2021 to 2023?"*
- *"Tell me about Tesla's operating cash flow."*

This project serves as a clear demonstration of how to build a simple, rule-based AI system and deploy it as a responsive web application using Flask.

---

## 2. Features & Functionality

- **Conversational Queries:** Allows users to ask questions in a natural, conversational manner to retrieve specific financial data points.
- **Focused Data Scope:** The chatbot is knowledgeable about key financial metrics (Revenue, Net Income, Operating Cash Flow) for **Apple, Microsoft, and Tesla** between the years **2021–2023**.
- **Lightweight & Fast Backend:** Built with **Flask**, ensuring a minimal footprint and fast response times.
- **Rule-Based Logic:** Implements a simple but effective rule-based engine to parse user intent without the overhead of complex NLP/ML models.
- **Clean & Responsive UI:** A simple, modern web interface built with standard HTML and CSS ensures a good user experience across devices.
- **Modular Codebase:** The project is structured with a clear separation of concerns, making the code readable, maintainable, and easy to extend.

---

## 3. Technical Workflow: How It Works

The chatbot operates on a straightforward request-response cycle orchestrated by Flask.

1.  **Data Loading:** Upon starting the application, the `final_financial_data.csv` file is loaded into a **Pandas DataFrame** and cached in memory.
2.  **User Interaction:** The user types a query into the chat interface (`templates/index.html`) and submits the form.
3.  **Backend Request:** The user's query is sent as a POST request to the Flask backend (`app.py`).
4.  **Intent Parsing (Rule-Based Engine):**
    - The core logic resides in the `get_response` function within `app.py`.
    - It uses simple string matching and keyword extraction (e.g., searching for "revenue," "apple," and "2023") to understand the user's request.
    - This approach avoids the complexity of NLP libraries while being effective for a predefined set of questions.
5.  **Data Retrieval:** Based on the parsed keywords, the application queries the Pandas DataFrame to locate the exact financial figure. For example, it filters the DataFrame for `Company == 'Apple'` and `Year == 2023` to retrieve the `Total Revenue`.
6.  **Response Generation:** A human-readable response string is formatted using the retrieved data. If no data is found, a fallback message is generated.
7.  **Display Response:** The generated response is sent back to the `index.html` template and dynamically rendered in the chat window.

---

## 4. Project Structure Explained

The repository is organized logically for clarity and scalability.

```

financial\_chatbot/
├── app.py                      \# Main Flask application file containing routing and logic.
├── templates/
│   └── index.html              \# The HTML template for the chatbot's user interface.
├── data/
│   └── final\_financial\_data.csv \# The pre-cleaned financial dataset used by the app.
├── static/                     \# Directory for future assets like custom CSS or JavaScript.
├── requirements.txt            \# A list of all Python dependencies for the project.
├── .gitignore                  \# Specifies which files Git should ignore (e.g., venv).
└── README.md                   \# This detailed project documentation.

````

---

## 5. Technical Stack

-   **Backend Framework:** Flask
-   **Data Manipulation:** Pandas
-   **Frontend:** HTML, CSS
-   **Core Language:** Python
-   **Development Environment:** Visual Studio Code

---

## 6. Setup & Installation Guide

To run this application on your local machine, please follow these steps.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/MrCoss/GFC-Financial-Chatbot.git](https://github.com/MrCoss/GFC-Financial-Chatbot.git)
    cd GFC-Financial-Chatbot
    ```

2.  **Create and Activate a Virtual Environment** (Recommended):
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application:**
    ```bash
    python app.py
    ```

5.  **Access the Chatbot:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 7. Limitations & Future Scope

This project was designed for simplicity and educational purposes. Key limitations and potential future enhancements include:

**Current Limitations:**
- The chatbot only understands a **predefined set of queries** and keywords.
- The financial dataset is **static** and must be updated manually by modifying the CSV file.
- There are no sophisticated NLP or machine learning models for intent recognition.

**Future Enhancements:**
- [ ] **Integrate a NLP Library:** Use libraries like **NLTK** or **spaCy** for more flexible and robust intent parsing.
- [ ] **Connect to a Live API:** Replace the static CSV with a live financial data API (e.g., Alpha Vantage, Yahoo Finance) for real-time information.
- [ ] **Expand the Knowledge Base:** Add more companies, financial metrics, and historical years to the dataset.
- [ ] **Database Integration:** Store financial data in a SQL or NoSQL database for better scalability and management.
- [ ] **User Authentication:** Add user accounts to save chat history or preferences.

---

## 8. Author & License

-   **Author:** Costas Pinto
-   **Context:** 2025 | BCG AI Insights | GFC Project
-   **License:** This project is licensed under the **MIT License**.
````
