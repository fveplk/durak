from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
import random

app = FastAPI()

# Подключаем статику (HTML/CSS/JS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Игровая сессия (в реальном проекте — БД)
game_sessions = {}

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("frontend/index.html", "r") as f:
        return f.read()

# WebSocket для обновления игры
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    
    try:
        while True:
            data = await websocket.receive_text()
            action = json.loads(data)
            
            # Обработка хода игрока
            if action["type"] == "play_card":
                card = action["card"]
                # Логика игры (проверка хода, обновление состояния)
                response = {"type": "game_update", "message": f"Игрок сыграл {card}"}
                await websocket.send_text(json.dumps(response))
                
    except WebSocketDisconnect:
        print("Игрок отключился")