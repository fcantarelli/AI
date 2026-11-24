
class AlternativeLLMAdapter:

    @property
    def provider_name(self) -> str:
        return "ALTERNATIVE"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:
        return (
            "This payment was declined because "
            "the available account balance was insufficient."
        )
