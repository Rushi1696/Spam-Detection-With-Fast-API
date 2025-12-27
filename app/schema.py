from pydantic import BaseModel

class SpamRequest(BaseModel):
    text: str

class SpamResponse(BaseModel):
    prediction: str
    confidence: float
