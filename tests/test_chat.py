from models.chat import ChatRequest
from pydantic import ValidationError
import pytest


def test_chat_request_valid():
    chat_request = ChatRequest(prompt="Explique o funcionamento do FastAPI")
    assert chat_request.prompt == "Explique o funcionamento do FastAPI"


@pytest.mark.parametrize(
    "prompt",
    ["Olá", "", "              ", "A" * 501]
)


def test_chat_request_invalid_prompt(prompt):
    with pytest.raises(ValidationError):
        ChatRequest(prompt=prompt)