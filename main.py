import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import requests
import sys
from utils.backend import backend_request
from dotenv import load_dotenv

load_dotenv()

# Access in backend
auth:dict = backend_request('POST', '/auth/login', data={
    'email': 'user1@gmail.com',
    'password': '123456'
})

if auth == None:
    raise RuntimeError("Abortando...")


token = auth.get('token')

response = backend_request('GET', '/api/users', token=token)

print(response)
# users = response.json()


# df = pd.DataFrame(users)
# print(df)

