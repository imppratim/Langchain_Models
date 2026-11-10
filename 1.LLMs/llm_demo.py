from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
#this loads the environment varibale 
load_dotenv()
#making an object of open ai and calling the model
communicate = ChatOpenAI(model="gpt-5", temperature= 0.9, max_completion_tokens=30)
#invoke method will hit the model with this prompt and the model will generate the output and reply 
result = communicate.invoke("How does an llm work in 3 lines?")

print(result.content)