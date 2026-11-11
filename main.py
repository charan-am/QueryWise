
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# ==========================================
# 1. DEVELOPER KNOWLEDGE BASE
# ==========================================

knowledge_base = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted, general-purpose programming language. It is useful for automation, web development, data science, AI and machine learning because of its simple syntax and extensive libraries."
    },
    {
        "question": "What is a Python list?",
        "answer": "A list is an ordered, mutable collection in Python. Example: numbers = [10, 20, 30]."
    },
    {
        "question": "How do I install Python packages?",
        "answer": "Use pip, Python's package installer. Example: pip install numpy."
    },
    {
        "question": "What is a virtual environment?",
        "answer": "A virtual environment creates an isolated Python environment so different projects can use separate dependencies."
    },
    {
        "question": "What is Git?",
        "answer": "Git is a distributed version control system used to track code changes and collaborate with developers."
    },
    {
        "question": "What is GitHub?",
        "answer": "GitHub is a platform for hosting Git repositories and collaborating on software projects."
    },
    {
        "question": "What is a Git commit?",
        "answer": "A commit is a saved snapshot of changes in a Git repository. Use git commit to record changes."
    },
    {
        "question": "How do I push code to GitHub?",
        "answer": "Use git push to upload your local commits to a remote repository, such as GitHub."
    },
    {
        "question": "What is a Git branch?",
        "answer": "A branch is an independent line of development in Git. It allows developers to work on features separately."
    },
    {
        "question": "What is VS Code?",
        "answer": "Visual Studio Code is a lightweight, extensible code editor that supports many programming languages."
    },
    {
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a field of AI where systems learn patterns from data to make predictions or decisions."
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning trains a model using labelled data, where each training example has a known target."
    },
    {
        "question": "What is overfitting in machine learning?",
        "answer": "Overfitting occurs when a model learns training data too closely and performs poorly on unseen data."
    },
    {
        "question": "What is Artificial Intelligence (AI)?",
        "answer": "Artificial Intelligence (AI) is a field of computer science that develops systems capable of performing tasks that normally require human intelligence."
    }
]


# ==========================================
# 2. PREPARE QUESTIONS AND ANSWERS
# ==========================================

faq_questions = [
    item["question"] for item in knowledge_base
]

faq_answers = [
    item["answer"] for item in knowledge_base
]


# ==========================================
# 3. TF-IDF VECTORIZATION
# ==========================================

# Separate vectorizers for questions and answers
question_vectorizer = TfidfVectorizer(
    stop_words="english"
)

answer_vectorizer = TfidfVectorizer(
    stop_words="english"
)

# Convert FAQ questions into numerical vectors
question_vectors = question_vectorizer.fit_transform(
    faq_questions
)

# Convert FAQ answers into numerical vectors
answer_vectors = answer_vectorizer.fit_transform(
    faq_answers
)


# ==========================================
# 4. QUESTION RETRIEVAL ENGINE
# ==========================================

def get_answer(user_question, threshold=0.30):

    # Convert user's question into numerical vectors
    query_question_vector = question_vectorizer.transform(
        [user_question]
    )

    query_answer_vector = answer_vectorizer.transform(
        [user_question]
    )

    # Reject queries containing no known vocabulary
    if (
        query_question_vector.nnz == 0
        and query_answer_vector.nnz == 0
    ):
        return None, 0.0, None

    # Calculate question similarity
    if query_question_vector.nnz > 0:

        question_scores = cosine_similarity(
            query_question_vector,
            question_vectors
        ).flatten()

    else:
        question_scores = np.zeros(len(knowledge_base))

    # Calculate answer similarity
    if query_answer_vector.nnz > 0:

        answer_scores = cosine_similarity(
            query_answer_vector,
            answer_vectors
        ).flatten()

    else:
        answer_scores = np.zeros(len(knowledge_base))

    # Combine both similarity scores
    combined_scores = (
        0.7 * question_scores
        + 0.3 * answer_scores
    )

    # Find the best matching FAQ
    best_index = int(combined_scores.argmax())

    best_score = float(combined_scores[best_index])

    # Reject questions with low similarity
    if best_score < threshold:
        return None, best_score, None

    # Retrieve the corresponding answer
    matched_question = knowledge_base[best_index]["question"]

    answer = knowledge_base[best_index]["answer"]

    return answer, best_score, matched_question


# ==========================================
# 5. QUERYWISE INTERACTIVE APPLICATION
# ==========================================

def main():

    print("=" * 45)
    print("       WELCOME TO QUERYWISE")
    print("  Your Developer Knowledge Assistant")
    print("=" * 45)

    print("Ask questions about Python, Git, VS Code and ML.")
    print("Type 'exit' to close QueryWise.\n")

    while True:

        user_input = input("You: ").strip()

        # Exit application
        if user_input.lower() == "exit":

            print("QueryWise: Goodbye! Keep learning.")
            break

        # Handle empty input
        if not user_input:

            print("QueryWise: Please enter a question.\n")
            continue

        # Get the relevant answer
        answer, score, matched_question = get_answer(
            user_input
        )

        # Display the result
        if answer is None:

            print(
                "QueryWise: I couldn't find "
                "sufficiently relevant information."
            )

        else:

            print(f"\nMatched FAQ: {matched_question}")

            print(f"Similarity: {score:.2f}")

            print(f"QueryWise: {answer}")

        print()


# ==========================================
# 6. START APPLICATION
# ==========================================

if __name__ == "__main__":
    main()
