"""
Module that contains chat intelligence model and its functions
"""
from collections.abc import AsyncGenerator
from typing import Any
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Intelligence:
    """
    Base Intelligence class
    """
    def __init__(self) -> None:
        self.llm = ChatOllama(model="gpt-oss", temperature=0.7)

    async def astream(self, query) -> AsyncGenerator[str, Any]:
        """
        chat response method
        """
        prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
            messages=[
                (
                    "system",
                    "You are a helpful assistant dedicated to providing clear and concise answers.",
                ),
                ("user", "{input}"),
            ]
        )
        chain = prompt | self.llm | StrOutputParser()
        async for chunk in chain.astream(input={"input": query}):
            yield chunk
