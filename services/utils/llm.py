"""Langchain Chats Agents."""

from langchain.chat_models import init_chat_model
from langchain.chat_models.base import BaseChatModel
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai.chat_models import ChatOpenAI


def get_chat_model(model_provider: str, model_name: str | None = None, temperature: float = 0.0) -> BaseChatModel:
    """Get the chat model based on the model name."""
    if model_provider == "openai":
        model_name = model_name or "gpt-5-codex"
        if model_name == "gpt-5-codex":
            return ChatOpenAI(model_name=model_name, temperature=temperature, use_responses_api=True)
        return ChatOpenAI(model_name=model_name, temperature=temperature, reasoning=True)

    elif model_provider == "anthropic":
        model_name = model_name or "claude-sonnet-4-20250514"
        return ChatAnthropic(
            model=model_name, max_tokens=64000, temperature=1.0, thinking={"type": "enabled", "budget_tokens": 2000}
        )

    elif model_provider == "google":
        model_name = model_name or "gemini-2.5-pro"
        return ChatGoogleGenerativeAI(model=model_name, temperature=0.7, include_thoughts=True)

    else:
        raise ValueError(f"Unsupported model provider: {model_provider}")


def get_init_chat_model(model_provider: str, model_name: str | None = None, temperature: float = 0.0) -> BaseChatModel:
    """Get the chat model using init_chat_model based on the model name."""
    if model_provider == "openai":
        model_name = model_name or "gpt-5-codex"
        if model_name == "gpt-5-codex":
            return init_chat_model(
                model=model_name, model_provider=model_provider, temperature=temperature, use_responses_api=True
            )
        return init_chat_model(model=model_name, model_provider=model_provider, temperature=temperature, reasoning=True)

    elif model_provider == "anthropic":
        model_name = model_name or "claude-sonnet-4-20250514"
        return init_chat_model(
            model=model_name,
            model_provider=model_provider,
            max_tokens=64000,
            temperature=1.0,
            thinking={"type": "enabled", "budget_tokens": 2000},
        )

    elif model_provider == "google_genai":
        model_name = model_name or "gemini-2.5-pro"
        return init_chat_model(model=model_name, model_provider=model_provider, temperature=0.7, include_thoughts=True)

    else:
        raise ValueError(f"Unsupported model provider: {model_provider}")


def test_all_models():
    """Test function to invoke each model provider and print their outputs."""
    test_prompt = (
        "Provide a brief introduction about yourself as an AI language model and summarize"
        " your key capabilities in 2-3 sentences."
    )

    providers = ["openai", "anthropic", "google"]

    for provider in providers:
        print(f"\n{'=' * 50}")
        print(f"Testing {provider.upper()} Model")
        print(f"{'=' * 50}")

        try:
            model = get_chat_model(provider)
            print(f"Model: {model.model_dump()}")

            print(f"\nPrompt: {test_prompt}")
            print("\nResponse:")
            print("-" * 30)

            response = model.invoke(test_prompt)
            response.pretty_print()

        except Exception as e:
            print(f"Error testing {provider}: {str(e)}")

        print("-" * 50)


def test_langchain_init_models():
    """Test function to invoke each model provider with langchain init and print their outputs."""
    test_prompt = (
        "Provide a brief introduction about yourself as an AI language model and summarize "
        "your key capabilities in 2-3 sentences."
    )

    models = ["openai", "anthropic", "google_genai"]

    for model in models:
        print(f"\n{'=' * 50}")
        print(f"Testing {model.upper()} Model - Langchain Init")
        print(f"{'=' * 50}")

        try:
            llm = get_init_chat_model(model_provider=model)
            print(f"Model: {llm.model_dump()}")

            print(f"\nPrompt: {test_prompt}")
            print("\nResponse:")
            print("-" * 30)

            response = llm.invoke(test_prompt)
            response.pretty_print()

        except Exception as e:
            print(f"Error testing {model}: {str(e)}")

        print("-" * 50)


def get_available_models_configs() -> dict:
    """Get a list of available models from each provider."""
    avaialable_models = {
        "openai": [
            "gpt-5-codex",
        ],
        "anthropic": [
            "claude-sonnet-4-20250514",
        ],
        "google_genai": [
            "gemini-2.5-pro",
        ],
    }
    print(avaialable_models)
    avaialable_model_configs: dict = {"models": []}
    return avaialable_model_configs


def get_chat_model_with_model_config(model_config: dict) -> BaseChatModel:
    """Get chat model with model config."""
    chat_llm = init_chat_model(**model_config)
    return chat_llm
