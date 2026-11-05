# ShopEase AI – LLM-Powered E-commerce Customer Support Agent

## 1. Project Overview

ShopEase AI is an AI-powered customer support assistant developed for a dummy e-commerce website.

It uses a Large Language Model (LLM) integrated with Retrieval-Augmented Generation (RAG) to answer customer queries using website-specific information.

The project demonstrates how LLMs and information retrieval can be integrated into a web-based customer support system.

## 2. Key Features

- AI-powered customer support using Google Gemini.
- Retrieval-Augmented Generation (RAG).
- TF-IDF-based information retrieval.
- Product information and recommendations.
- Dummy order tracking.
- Return and refund policy assistance.
- Shipping and payment information.
- Order cancellation policy assistance.
- Basic conversation memory.
- Interactive chatbot with quick-reply buttons.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Google Gemini API | Large Language Model |
| Flask | Web application backend |
| Scikit-learn | TF-IDF retrieval and similarity |
| HTML | Website structure |
| CSS | Website styling |
| JavaScript | Chatbot interactions |
| python-dotenv | API key management |

## 4. System Architecture

The system follows this workflow:

1. Customer enters a query through the website.
2. Flask receives the query.
3. The retriever searches the ShopEase knowledge base.
4. TF-IDF and category-based matching identify relevant information.
5. Retrieved information is passed to the Gemini LLM.
6. Gemini generates a contextual response.
7. Flask returns the response to the frontend chatbot.

## 5. Project Structure

```text
shopease-ai-agent/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── agent.py
├── knowledge.py
├── retriever.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 6. Installation and Setup

### Clone the repository

```bash
git clone https://github.com/ankitada-wq/shopease-ai-agent.git
cd shopease-ai-agent
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment (Windows)

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure the Gemini API key

Create a `.env` file in the project directory.

Add your own Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not upload your `.env` file to GitHub.

### Run the application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 7. Limitations

- Uses dummy product and order information.
- Order tracking is not connected to a real e-commerce database.
- Product availability and order statuses are demonstration data.
- The chatbot depends on the availability of the Gemini API.

## 8. Future Improvements

- Integration with a real product database.
- Real-time order tracking.
- User authentication.
- Session-based conversation memory.
- Semantic retrieval using embeddings.
- Deployment as a publicly accessible web application.

## 9. Project Information

**Project:** ShopEase AI  
**Domain:** Artificial Intelligence / Natural Language Processing  
**Implementation:** LLM Integration and Retrieval-Augmented Generation (RAG)  
**Year:** 2026