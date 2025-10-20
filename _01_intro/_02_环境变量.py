import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY1")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

llm=ChatOpenAI(
    # base_url=os.getenv('OPENAI_BASE_URL'),
    # api_key=os.getenv('OPENAI_API_KEY1'),
    model='gpt-4o-mini',
    temperature=0.8,
    max_tokens=20
)

res=llm.invoke('什么是langchain?')
print(res.content )