from config import MODEL
from ollama import chat
from brain.prompt import SYSTEM_PROMPT


def ask_nexa(messages):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            *messages
        ],
        options={
            "temperature": 0.4,
            "num_predict": 200,
            "num_ctx": 2048
        }
    )

    return response.message.content