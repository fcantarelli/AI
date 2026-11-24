from pydantic import BaseModel, Field
from enum import Enum


class PaymentStatus(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class PaymentExplanationRequest(BaseModel):
    payment_id: int = Field(gt=0)
    customer_id: int = Field(gt=0)


class PaymentExplanationResponse(BaseModel):
    payment_id: int
    status: PaymentStatus
    explanation: str
    source: str
