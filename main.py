from typing import List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


from src.services import get_trends

print('rodou!')

class TrendItem(BaseModel):
    name: str
    url: str

BRAZIL_WOE_ID = 23424768

app = FastAPI()

@app.get('/trends', response_model=List[TrendItem])
def get_trends_route():
    trends = get_trends(BRAZIL_WOE_ID) 
    return trends

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)