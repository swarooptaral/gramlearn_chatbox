from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

def initiateGemini(query):
    result = llm.invoke(f"{query}")
    return result.content

if __name__ == "__main__":
    print(initiateGemini("Hello"))