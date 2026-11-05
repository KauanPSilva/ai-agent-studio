from providers.base import BaseProvider


class MockProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"