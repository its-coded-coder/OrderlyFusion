# Customer and Orders Platform API 

Documentation

Welcome to the API documentation for the Customer and Orders platform. This platform provides RESTful APIs for managing customers and orders.

## Introduction

The Customer and Orders platform offers a set of APIs to interact with customer and order data. These APIs allow you to perform CRUD (Create, Read, Update, Delete) operations on customers and orders, facilitating seamless integration with other systems.

## Setup

## Without Docker

### Prerequisites
- Python 3 installed on your system
- PostgreSQL installed and running on your system
- pip installed

To set up the platform locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/frankjam/OrderlyFusion.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash 
    python manage.py migrate
    ```

4. Run the server:

    ```bash
    python manage.py runserver
    ```

4. Access the API documentation at `http://localhost:8000/docs/` in your browser.

## With Docker

### Prerequisites
- Docker installed on your system
- Docker Compose installed on your system

Setup Instructions

1. Clone the repository:
 ```bash
    git clone https://github.com/frankjam/OrderlyFusion.git
    
    cd OrderlyFusion
```
2. Build the Docker image:
```bash
docker-compose build
```

3. Start the Docker containers:
```
docker-compose up -d
```

4. Access the development server:
The server will be running inside the Docker container. You can access it at http://localhost:8000/

5. To stop the containers, run:
```bash 
docker-compose down
```
## Aquire API Token
curl -X POST \
  http://localhost:8000/api-token-auth/ \  
  -H 'Content-Type: application/json' \                               
  -d '{                                
    "username": "username",
    "password": "user_password"}'  

This will return a token which you need to include in the header of each request as follows:
Authorization: Token <your_token>


## API Endpoints

### Customers API

The Customers API allows you to manage customer data.

- GET `/api/v1/customers`: Get a list of all customers.
- GET `/api/v1/customers/{id}`: Get details of a specific customer.
- POST `/api/v1/customers`: Create a new customer.
- PUT `/api/v1/customers/{id}/`: Update an existing customer.
- DELETE `/api/v1/customers/{id}/`: Delete a customer.

### Orders API

The Orders API allows you to manage order data.

- GET `/api/v1/orders`: Get a list of all orders.
- GET `/api/v1/orders/{id}/`: Get details of a specific order.
- POST `/api/v1/orders`: Create a new order.
- PUT `/api/v1/orders/{id}/`: Update an existing order.
- DELETE `/api/v1/orders/{id}/`: Delete an order.

## Examples

Here are some examples of how to use the platform's APIs:
## Customers api examples 

## 1. List all customers

### Request

- Method: GET
- URL: `/api/v1/customers`

### Response

#### Success (HTTP 200 OK)

```json
[
    {
        "id": 1,
        "name": "John Doe",
        "code":"12",
        "email": "john@example.com",
        "phone": "123-456-7890"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "code":"13",
        "email": "jane@example.com",
        "phone": "987-654-3210"
    },
    // Other customers
]
```

## 2. Create a new customer:

### Request

    - Method: POST
    - URL: `/api/v1/customers`

   ### Request 
    
   ```json
        {   
            "id": 1,
            "name": "John Doe",
            "code":"12",
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
   ```

   ### Response

   #### Success (HTTP 200 OK)
   ``` 
    "Customer added successfully"
   ```
   

## 3.Update a Customer

### Request
- Method: PUT
- URL: `/api/v1/customers/<id>/`

Replace `<id>` with the ID of the customer to be updated.

#### Example Request Body

```json
        {
            "name": "Updated Name",
            "code":"12",
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
```

## 4. Delete a Customer

### Request

- Method: DELETE
- URL: `/api/v1/customers/<id>/`
 
    Replace `<id>` with the ID of the customer to be deleted.

### Response

#### Success (HTTP 204 No Content)

```plaintext
Deleted successfully
```

## Orders examples 
### 1. List all orders 

### Request

- Method: GET
- URL: `/api/v1/orders`

### Response

#### Success (HTTP 200 OK)

```json
[
    {
        "id": 1,
        "item": "book",
        "amount": "12.00",
        "time": "2024-04-21T16:12:18.015296Z",
        "customer": 3
    },
    {
        "id": 2,
        "item": "book",
        "amount": "12.00",
        "time": "2024-04-21T16:12:18.015296Z",
        "customer": 1
    },
    // Other orders
]
```

## 2. Create a new order:

### Request

    - Method: POST
    - URL: `/api/v1/orders`

   ### Request 
    
   ```json
        {   
            "item": "book",
            "amount": "12.00",
            "customer": 1
        }
   ```

   ### Response

   #### Success (HTTP 200 OK)
   ``` 
    "Order added successfully"
   ```
   
## 3.Update order

### Request
- Method: PUT
- URL: `/api/v1/orders/<id>/`

Replace `<id>` with the ID of the order to be updated.

#### Example Request Body

```json
        { 
            "item": "book updated",
            "amount": "18.00",
            "customer": 1
        }
```
## 4. Delete order

### Request

- Method: DELETE
- URL: `/api/v1/orders/<id>/`
 
    Replace `<id>` with the ID of the order to be deleted.

### Response

#### Success (HTTP 204 No Content)

```plaintext
Deleted successfully
```


## Contributing

Contributions are welcome! If you have suggestions or find any issues, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.