from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

# FastAPI 앱 인스턴스 생성
app = FastAPI()

# 요청 바디 모델 정의
class Message(BaseModel):
    user_message: str

# 간단한 응답을 생성하는 함수 (여기서는 미리 설정된 규칙을 사용)
def generate_response(user_message: str) -> str:
    user_message = user_message.lower()
    
    if "건휘님은" in user_message:
        return "존잘 섹시남"
    elif "how are you" in user_message:
        return "I'm doing great, thank you! How about you?"
    elif "bye" in user_message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# HTML 파일을 제공하는 엔드포인트 (루트 경로)
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html", "r") as f:
        content = f.read()
    return content

# 챗봇 API 엔드포인트
@app.post("/chat")
async def chat(message: Message):
    # 사용자가 보낸 메시지를 기반으로 응답 생성
    response = generate_response(message.user_message)
    return {"response": response}
