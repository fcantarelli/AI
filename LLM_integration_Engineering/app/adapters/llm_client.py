from typing import Protocol


class LLMClient(Protocol):

    @property
    def provider_name(self) -> str:
        ...

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:
        ...
