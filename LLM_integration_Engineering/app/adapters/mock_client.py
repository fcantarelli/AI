class MockLLMAdapter:

    @property
    def provider_name(self) -> str:
        return "MOCK"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:

        return (
            "The payment was rejected "
            "due to insufficient funds."
        )
