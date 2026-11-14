from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5')

messages =[
    SystemMessage(content= 'You are a helpful personal assistant for a lawyer'),
    HumanMessage(content='Tell me the pathway to blue card and their conditions')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)