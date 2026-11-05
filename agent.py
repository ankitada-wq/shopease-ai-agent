import os

from dotenv import load_dotenv
from google import genai

from retriever import retrieve_information

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# System instructions
SYSTEM_PROMPT = """

You are ShopEase AI, a website customer support assistant.

Your job is to answer questions about ShopEase.

Rules:
1. Answer using only the retrieved website information.
2. Never invent products, prices or policies.
3. If a product is not listed, say it is not currently listed.
4. If the retrieved information does not answer the question,
   say you cannot confirm the information.
5. Do not answer unrelated general knowledge questions.
6. Be polite and concise.
7. For order tracking questions, ask the customer for their Order ID if they haven't provided one.
8. Use the order information retrieved from the website knowledge base. Never invent order statuses or delivery dates
9. When customers ask for product recommendations, suggest only products listed in the website information. Consider their budget and preferences.
10. If a customer asks to cancel an order, explain the cancellation policy.
11. Orders can only be cancelled before shipment. Never claim that an order has actually been cancelled.

"""

# Conversation history
conversation_history = []


def ask_agent(user_message):

    # STEP 1: Retrieve relevant information
    retrieved_docs = retrieve_information(user_message)

    context = "\n".join(retrieved_docs)

    # STEP 2: Build prompt
    prompt = f"""
    WEBSITE INFORMATION:
    {context}

    CONVERSATION HISTORY:
    {conversation_history}

    CUSTOMER QUESTION:
    {user_message}

    Answer using the website information provided above.
    """

    # STEP 3: Send request to Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "system_instruction": SYSTEM_PROMPT
        }
    )

    answer = response.text

    # STEP 4: Update conversation memory
    conversation_history.append(
        f"Customer: {user_message}"
    )

    conversation_history.append(
        f"ShopEase AI: {answer}"
    )

    return answer


# Test agent
if __name__ == "__main__":

    print("\n===== ShopEase RAG Agent =====")
    print("Ask questions about ShopEase.")
    print("Type exit to stop.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        answer = ask_agent(question)

        print("\nShopEase AI:", answer, "\n")