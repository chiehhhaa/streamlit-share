# Streamlit Demo Applications

This repository showcases two demo applications built with Streamlit:

1. **Data Visualization Tool**
2. **GenAI Chat Bot (ChatGPT)**

## Requirements

To run these applications, ensure you have the following installed:

- Python 3.8 or later
- Streamlit
- openai (for the Chat Bot)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate    # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) For the Chat Bot, set up your OpenAI API Key in an `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Applications

### 1. Data Visualization Tool

This application allows users to upload a CSV file, preview the data, and dynamically visualize it using:

- Line Charts
- Pie Charts
- Bar Charts

#### How to Run

1. Start the application:

   ```bash
   streamlit run data_visualization.py
   ```

2. Open your browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload a CSV file to see:
   - The data table
   - Interactive chart options

#### Screenshot

---

### 2. GenAI Chat Bot (ChatGPT)

This application uses OpenAI's GPT model to provide instant responses to user queries.

#### How to Run

1. Start the application:

   ```bash
   streamlit run chat_bot.py
   ```

2. Open your browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter your OpenAI API Key (if not already set in the `.env` file).

4. Type a query and get a response from the AI!

#### Screenshot

---

## File Structure

```
.
├── data_visualization.py    # Code for the Data Visualization Tool
├── chat_bot.py              # Code for the GenAI Chat Bot
├── requirements.txt         # Python dependencies
├── .env                     # (Optional) OpenAI API Key
└── README.md                # Project Documentation
```

## Acknowledgments

- [Streamlit](https://streamlit.io/) for making web app development simple and accessible.
- [OpenAI](https://openai.com/) for providing the GPT API.
