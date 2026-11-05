from providers.mock import MockProvider


def test_mock_provider_generate():

    provider = MockProvider()
    response = provider.generate(prompt="Explique o Docker")

    assert response == f"Mock response: Explique o Docker"