
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Price API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(q: str):
    results = [
        {"id": "p1", "title": "iPhone 15 Pro 256GB", "merchant": "Amazon.sa", "price": 3899, "currency": "SAR", "shipping": "Free", "delivery_time": "2-4 days"},
        {"id": "p2", "title": "iPhone 15 Pro 256GB", "merchant": "Noon", "price": 3849, "currency": "SAR", "shipping": "15 SAR", "delivery_time": "3-5 days"}
    ]
    return {"query": q, "results": results}
