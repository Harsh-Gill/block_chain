# Block Chain Code
Implementation of a Block Chain using Python and FastAPI as an interface


# To Run the Blockchain on FastAPI

```python
uvicorn main:app --reload   

```

### To get Current Transactions on chain after server is running

```python

curl -X GET "http://127.0.0.1:8000/chain" -H  "accept: application/json" 

```

### To Add Transaction and new block on chain after server is running
#### Replace the TRANSACTION_INFORMATION_TO_STORE with the format you'd prefer
```python

curl -X POST "http://localhost:8000/chain?transaction=TRANSACTION_INFORMATION_TO_STORE" -H  "accept: application/json" -d "" 

```
