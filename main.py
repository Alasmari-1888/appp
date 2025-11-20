
from typing import List

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: str = Field(..., description="Stable identifier for the item")
    title: str = Field(..., description="Product title as shown by the merchant")
    merchant: str = Field(..., description="Seller or marketplace name")
    price: float = Field(..., description="Price in the provided currency")
    currency: str = Field(..., description="ISO currency code for the price")
    shipping: str = Field(..., description="Shipping cost or label")
    delivery_time: str = Field(..., description="Estimated delivery window")


class SearchResponse(BaseModel):
    query: str
    results: List[Product]


app = FastAPI(title="Price API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


_INVENTORY: List[Product] = [
    Product(
        id="p1",
        title="iPhone 15 Pro 256GB",
        merchant="Amazon.sa",
        price=3899,
        currency="SAR",
        shipping="Free",
        delivery_time="2-4 days",
    ),
    Product(
        id="p2",
        title="iPhone 15 Pro 256GB",
        merchant="Noon",
        price=3849,
        currency="SAR",
        shipping="15 SAR",
        delivery_time="3-5 days",
    ),
    Product(
        id="p3",
        title="Samsung Galaxy S24 Ultra 512GB",
        merchant="Extra",
        price=4699,
        currency="SAR",
        shipping="Free",
        delivery_time="Next day",
    ),
    Product(
        id="p4",
        title="Apple AirPods Pro 2",
        merchant="Jarir",
        price=999,
        currency="SAR",
        shipping="20 SAR",
        delivery_time="2-3 days",
    ),
]


@app.get("/search", response_model=SearchResponse)
def search(q: str = Query(..., min_length=1, description="Search term")) -> SearchResponse:
    """Return products whose title or merchant matches the query (case-insensitive)."""

    term = q.lower()
    filtered = [
        product
        for product in _INVENTORY
        if term in product.title.lower() or term in product.merchant.lower()
    ]

    return SearchResponse(query=q, results=filtered)
