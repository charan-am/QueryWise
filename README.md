# QueryWise – Intelligent Developer Knowledge Assistant

QueryWise is an NLP-powered developer knowledge assistant that answers questions about Python, Git, GitHub, Visual Studio Code, and Machine Learning.

It uses TF-IDF vectorization and cosine similarity to retrieve relevant information from a predefined FAQ knowledge base. A Streamlit interface provides an interactive chat experience.

## Features

- Natural-language question input.
- TF-IDF-based text representation.
- Cosine similarity for FAQ retrieval.
- Weighted question and answer matching.
- Similarity threshold for rejecting weak matches.
- Chat interface built with Streamlit.
- Conversation history within the active session.
- Retrieval details showing the matched FAQ and similarity score.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | TF-IDF and similarity calculations |
| NumPy | Numerical operations |
| Streamlit | Web application interface |

## How It Works

1. The developer FAQ knowledge base stores questions and answers.
2. TF-IDF converts FAQ questions and answers into numerical vectors.
3. The user's question is converted into corresponding vectors.
4. Cosine similarity calculates how closely the query matches the stored information.
5. A weighted score combines question similarity (70%) and answer similarity (30%).
6. If the best score meets the configured threshold, QueryWise returns the corresponding answer. Otherwise, it reports that it could not find sufficiently relevant information.

**Note:** Similarity scores indicate mathematical similarity, not the probability that an answer is correct.

## Project Structure

```text
QueryWise/
│
├── main.py           # NLP retrieval engine and FAQ knowledge base
├── app.py            # Streamlit web application
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
├── .gitignore        # Files excluded from Git
└── .venv/            # Local Python environment (not uploaded)
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/QueryWise.git
cd QueryWise
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run QueryWise

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## Sample Questions

Try asking:

- What is Python?
- What is a Python list?
- How do I push code to GitHub?
- What is Artificial Intelligence?
- What is supervised learning?
- What is overfitting in Machine Learning?

Questions outside the available knowledge base may be rejected.

## Current Limitations

- The knowledge base contains predefined FAQ entries rather than external documents.
- TF-IDF relies primarily on word overlap and does not provide deep semantic understanding.
- Similarity thresholds require testing and tuning.
- The system does not use an LLM or a document-based RAG pipeline.
- Answers are limited to the information stored in the knowledge base.

## Future Enhancements

- Document ingestion from PDF and text files.
- Semantic search using embedding models.
- Vector databases for scalable document retrieval.
- Retrieval-Augmented Generation (RAG) using an LLM.
- Source citations and document references.
- Improved evaluation and hallucination safeguards.
- Public deployment.

## Author

**Charan A M**

Artificial Intelligence and Machine Learning Engineering Student

GitHub: https://github.com/charan-am

---

*QueryWise is an educational project developed to explore Natural Language Processing, information retrieval, and the foundations of Retrieval-Augmented Generation.*