from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 受信データの構造定義（JSONバリデーション）
class Item(BaseModel):
    name: str
    value: float

# POSTエンドポイント
@app.post("/api/data")
def receive_data(item: Item):
    # itemは自動的にJSON→Pythonオブジェクトに変換される
    print(f"Received: {item}")
    return {"status": "ok", "received": item.dict()}

# 動作確認用（GET）
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI (POST ready)!"}
