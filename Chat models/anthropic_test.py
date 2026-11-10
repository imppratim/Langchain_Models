from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-haiku-5-5")

result=model.invoke("Platforms to find jobs in Germany")

print(result.content)