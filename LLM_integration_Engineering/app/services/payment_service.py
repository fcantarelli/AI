
from app.adapters.llm_client import LLMClient
from app.models.payment import (
    PaymentExplanationRequest,
    PaymentExplanationResponse,
    PaymentStatus
)


class PaymentExplanationService:

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def explain(
        self,
        request: PaymentExplanationRequest
    ) -> PaymentExplanationResponse:

        system_prompt = """
        Explain payment information using
        only the facts supplied.

        Never invent a rejection reason.
        """

        user_prompt = (
            "Payment ID: {request.payment_id}. "
            "Status: REJECTED. "
            "Reason: INSUFFICIENT_FUNDS."
        )

        explanation = self.llm_client.generate(
            system_prompt,
            user_prompt
        )

        return PaymentExplanationResponse(
            payment_id=request.payment_id,
            status=PaymentStatus.REJECTED,
            explanation=explanation,
            source=self.llm_client.provider_name
        )
