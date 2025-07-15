import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv, dotenv_values


class SimpleOpenAiClient:

    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
            # base_url="...",
            # organization="...",
            # other params...
        )


    def invokellm(self, message):
        messages = [
            # (
            #     "system",
            #     "You are a helpful assistant that translates English to French. Translate the user sentence.",
            # ),
            ("human", message),
        ]
        return self.llm.invoke(messages)
