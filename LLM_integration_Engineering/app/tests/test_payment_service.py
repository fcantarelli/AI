from app.services.payment_service import PaymentExplanationService
from app.models.payment import (
    PaymentExplanationRequest,
    PaymentStatus
)


class FakeLLMClient:

    @property
    def provider_name(self):
        return "FAKE"

    def generate(self, system_prompt, user_prompt):
        return "Payment rejected: insufficient funds."


def test_payment_explanation():
    # Arrange
    llm_client = FakeLLMClient()
    service = PaymentExplanationService(llm_client)

    request = PaymentExplanationRequest(
        payment_id=1025,
        customer_id=5001
    )

    # Act
    response = service.explain(request)

    # Assert
    assert response.payment_id == 1025
    assert response.status == PaymentStatus.REJECTED
    assert response.source == "FAKE"
    assert "insufficient funds" in response.explanation


class FailingLLMClient:

    @property
    def provider_name(self):
        return "FAILING"

    def generate(self, system_prompt, user_prompt):
        raise RuntimeError("LLM provider unavailable")

def test_payment_explanation_when_llm_fails():

    llm_client = FailingLLMClient()
    service = PaymentExplanationService(llm_client)

    request = PaymentExplanationRequest(
        payment_id=1025,
        customer_id=5001
    )

    try:
        service.explain(request)
        assert False, "Expected RuntimeError was not raised"

    except RuntimeError as error:
        assert str(error) == "LLM provider unavailable"
