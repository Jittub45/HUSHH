from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from typing import List

try:
    from motor.motor_asyncio import AsyncIOMotorClient
except Exception:
    AsyncIOMotorClient = None

app = FastAPI(title="Template Backend")

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/template_db')

class Item(BaseModel):
    id: str
    name: str

@app.on_event('startup')
async def startup_db():
    if AsyncIOMotorClient is None:
        app.state.db = None
        return
    client = AsyncIOMotorClient(MONGO_URI)
    app.state.db = client.get_default_database()

@app.get('/health')
async def health():
    return {"status": "ok"}

@app.get('/metrics')
async def metrics():
    # simple human metrics endpoint for Prometheus scraping if needed
    return "# HELP template_up 1 if app is up\n# TYPE template_up gauge\ntemplate_up 1\n"

@app.get('/items', response_model=List[Item])
async def list_items():
    db = getattr(app.state, 'db', None)
    if db is None:
        # return static sample if DB not available
        return [Item(id='1', name='Sample item')]
    coll = db.get_collection('items')
    docs = await coll.find().to_list(50)
    return [Item(id=str(d.get('_id')), name=d.get('name','')) for d in docs]

@app.post('/items', response_model=Item)
async def create_item(item: Item):
    db = getattr(app.state, 'db', None)
    if db is None:
        raise HTTPException(status_code=500, detail='DB not configured')
    coll = db.get_collection('items')
    result = await coll.insert_one(item.dict())
    item.id = str(result.inserted_id)
    return item
