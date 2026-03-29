# API Documentation

This document provides details about the API endpoints for the Shopping Intelligence Tool.

## API Endpoints

### 1. Get Products
- **Endpoint:** `/api/products`
- **Method:** GET
- **Description:** Retrieves a list of products.

**Example Request:**
```http
GET /api/products HTTP/1.1
Host: example.com
```
**Example Response:**
```json
[
    {
        "id": 1,
        "name": "Product 1",
        "price": 19.99
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 29.99
    }
]
```

### 2. Create Product
- **Endpoint:** `/api/products`
- **Method:** POST
- **Description:** Creates a new product.

**Example Request:**
```http
POST /api/products HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "New Product",
    "price": 24.99
}
```
**Example Response:**
```json
{
    "id": 3,
    "name": "New Product",
    "price": 24.99
}
```

### 3. Update Product
- **Endpoint:** `/api/products/{id}`
- **Method:** PUT
- **Description:** Updates an existing product details.

**Example Request:**
```http
PUT /api/products/3 HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "Updated Product",
    "price": 29.99
}
```
**Example Response:**
```json
{
    "id": 3,
    "name": "Updated Product",
    "price": 29.99
}
```

### 4. Delete Product
- **Endpoint:** `/api/products/{id}`
- **Method:** DELETE
- **Description:** Deletes a product by ID.

**Example Request:**
```http
DELETE /api/products/3 HTTP/1.1
Host: example.com
```
**Example Response:**
```json
{
    "message": "Product deleted successfully"
}
```

## Authentication

Authentication is done via API keys. Include your API key in the header as follows:
```http
Authorization: Bearer YOUR_API_KEY
```

## Rate Limiting

The API is rate limited to 1000 requests per hour per user.