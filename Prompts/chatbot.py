from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-5")

# Keep the conversation in memory so later replies can use earlier messages.

chat_history = []

# Keep chatting until the user types "exit".
while True:
    user_input = input("User: ")
    if user_input.strip().lower() == "exit":
        break
    # Save the user's text with the human role to identify the speaker.
    chat_history.append(("human", user_input))
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("Chatbot:", result.content)

print(chat_history)