# api_models.py
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# ----------------------------------------------------------------------
# Example 1:  A simple "Product" model
# ----------------------------------------------------------------------

class Product(BaseModel):
    product_id: int = Field(..., description="Unique identifier")
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(None, description="Optional description")
    price: float = Field(..., gt=0, description="Price (positive)")
    is_available: bool = Field(True, description="Availability status")


# ----------------------------------------------------------------------
# Example 2:  A "User" model with nested address
# ----------------------------------------------------------------------

class Address(BaseModel):
    street: str = Field(..., description="Street address")
    city: str = Field(..., description="City")
    zip_code: str = Field(..., description="Postal code")
    country: str = Field("USA", description="Country")  # Default value

class User(BaseModel):
    user_id: int = Field(..., description="Unique user identifier")
    username: str = Field(..., description="Username")
    email: str = Field(..., description="Email address")
    full_name: Optional[str] = Field(None, description="Full name")
    address: Address = Field(..., description="User's address")
    is_active: bool = Field(True, description="Account status")


# ----------------------------------------------------------------------
# Example 3:  A "Blog Post" model with tags (list of strings)
# ----------------------------------------------------------------------

class BlogPost(BaseModel):
    post_id: int = Field(..., description="Unique identifier")
    title: str = Field(..., description="Title")
    content: str = Field(..., description="Content")
    author_id: int = Field(..., description="Author's ID")
    publication_date: str = Field(..., description="Publication date (ISO 8601)")
    tags: List[str] = Field([], description="Tags")  # Default empty list
    metadata: Dict[str, Any] = Field({}, description="Arbitrary metadata") # Default empty dict
