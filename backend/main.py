from fastapi import FastAPI
from pydantic import BaseModel
from backend.services.generator import generate_key
from backend.services.entropy import analyze_key
from backend.services.compare import compare_with_ntru

app = FastAPI(title="Post-Quantum Key Generator API",
              description="API for generating, analyzing, and comparing cryptographic keys using ML-based models.",
              version="1.0.0")

class GenerateRequest(BaseModel):
    entropy_threshold: float = 7.5  # Optional: minimum entropy for validity

class GenerateResponse(BaseModel):
    key_hex: str
    entropy: float
    min_entropy: float
    bit_ratio: dict
    nist_passed: bool

class CompareResponse(BaseModel):
    ml_key: dict
    ntru_key: dict

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    key_bin = generate_key()
    analysis = analyze_key(key_bin)
    return GenerateResponse(
        key_hex=hex(int(key_bin, 2))[2:],
        entropy=analysis["entropy"],
        min_entropy=analysis["min_entropy"],
        bit_ratio=analysis["bit_ratio"],
        nist_passed=analysis["nist_passed"]
    )

@app.get("/compare", response_model=CompareResponse)
def compare():
    return compare_with_ntru()
