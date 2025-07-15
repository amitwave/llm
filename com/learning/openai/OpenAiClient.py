from typing import Optional
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv, dotenv_values


class OpenAiClient:

    def __init__(self):
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert extraction algorithm. "
                    "Only extract relevant information from the text. "
                    "If you do not know the value of an attribute asked to extract, "
                    "return null for the attribute's value.",
                ),
                ("human", "{text}")
            ]
        )
        self.apiKey = os.getenv('OPENAI_API_KEY')
        self.llm = OpenAI()
        self.runnable = self.prompt | self.llm

    def runLLM(self, message):
        return self.runnable.invoke({"text":message})
