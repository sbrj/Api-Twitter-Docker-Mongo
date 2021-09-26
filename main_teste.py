from typing import List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from src.services import get_trends

client = MongoClient("mongodb://dio:dio@localhost:27017/")

db = client.dio_live

trends_collection = db.trends

class TrendItem(BaseModel):
    name: str
    url: str

BRAZIL_WOE_ID = 23424768

app = FastAPI()

@app.get('/trends', response_model=List[TrendItem])
def get_trends_route(): 

    trends = trends_collection.find({})

    return trends

if __name__ == '__main__':
    
    trends = get_trends(woe_id=BRAZIL_WOE_ID)

    trends_collection.insert_many(trends)

    uvicorn.run(app, host='0.0.0.0', port=8000)