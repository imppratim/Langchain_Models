from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

communicate = model.invoke("What is the latest update of Nvidia Stock")

print(communicate.content)
