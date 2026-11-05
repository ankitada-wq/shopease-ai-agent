from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knowledge import get_website_information


# Retrieve website information
website_data = get_website_information()


# Convert knowledge into searchable documents
documents = []

def flatten_data(data, prefix=""):

    for key, value in data.items():

        if isinstance(value, dict):
            flatten_data(value, prefix + key + " ")

        elif isinstance(value, list):
            documents.append(
                prefix + key + ": " + ", ".join(map(str, value))
            )

        else:
            documents.append(
                prefix + key + ": " + str(value)
            )


flatten_data(website_data)


# Create TF-IDF vectors
vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(documents)


# Retrieval function
def retrieve_information(query, top_k=3):

    query = query.lower()

    # Map common questions to website categories
    category_keywords = {
        "returns": [
            "return", "returns", "refund",
            "refunds", "exchange", "policy"
        ],

        "shipping": [
            "shipping", "delivery", "tracking",
            "track", "deliver"
        ],

        "products": [
            "product", "products", "sell",
            "selling", "price", "category"
        ],

        "payment": [
            "payment", "pay", "upi", "card", "cash"
        ],
        "orders": [
            "order", "orders", "tracking", "status", "shipped", "delivery"
        ],
        "cancellation": [
            "cancel", "cancellation", "cancelled", "canceled"
        ],

        "customer_support": [
            "support", "contact", "email", "help"
        ]
    }

    # Find matching category
    matched_category = None

    for category, keywords in category_keywords.items():

        if any(word in query for word in keywords):
            matched_category = category
            break

    # Retrieve all documents belonging to category
    if matched_category:

        results = [
            doc for doc in documents
            if doc.startswith(matched_category + " ")
        ]

        if results:
            return results[:top_k]

    # Fallback: TF-IDF similarity
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices:

        if similarities[index] > 0.05:
            results.append(documents[index])

        if len(results) >= top_k:
            break

    return results

    # Get documents with similarity scores
    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices:

        if similarities[index] > 0.05:
            results.append(documents[index])

        if len(results) == top_k:
            break

    return results

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    top_indices = similarities.argsort()[::-1][:top_k]

    results = []

    for index in top_indices:

        if similarities[index] > 0:
            results.append(documents[index])

    return results


# Test retrieval
if __name__ == "__main__":

    print("AVAILABLE DOCUMENTS:\n")

    for doc in documents:
        print(doc)

    question = input("\nAsk about ShopEase: ")

    print("\nRetrieved Information:\n")

    results = retrieve_information(question)

    for result in results:
        print("-", result)