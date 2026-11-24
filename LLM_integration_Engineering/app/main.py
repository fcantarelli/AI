
from fastapi import FastAPI, Depends

from app.adapters.llm_client import LLMClient
from app.adapters.mock_llm import MockLLMAdapter
from app.services.payment_service import PaymentExplanationService
from app.adapters.alternative_llm import AlternativeLLMAdapter

from app.models.payment import (
    PaymentExplanationRequest,
    PaymentExplanationResponse
)


app = FastAPI(
    title="Payment Explanation API",
    description="An AI-powered payment explanation service",
    version="1.0.0"
)


# Dependency 1: LLM provider
def get_llm_client() -> LLMClient:
    return AlternativeLLMAdapter()


# Dependency 2: Payment service
def get_payment_service(
    llm_client: LLMClient = Depends(get_llm_client)
) -> PaymentExplanationService:
    return PaymentExplanationService(llm_client)


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "payment-explanation-api"
    }


# Payment explanation endpoint
@app.post(
    "/api/v1/payments/explanation",
    response_model=PaymentExplanationResponse
)
def explain_payment(
    request: PaymentExplanationRequest,
    service: PaymentExplanationService = Depends(get_payment_service)
):
    return service.explain(request)
