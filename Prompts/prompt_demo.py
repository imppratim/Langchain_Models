
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#creation of prompts
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly science teacher."),
    ("human", "Explain {topic} to a 9th-grade student.")
])
#get the model to use
call_llm = ChatOpenAI(model="gpt-5-nano")

#connect the prompt with the model
chain = prompt | call_llm

# Get input from the user
user_input = input("What would you like to learn today? ").strip()
while not user_input:
    user_input = input("Please enter a topic: ").strip()

# generate the answer 
response = chain.invoke({"topic": user_input})

print(response.content)
