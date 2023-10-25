import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

class Question:
    def __init__(self, question, response, difficulty, punctuation):
        self.question = question
        self.response = response
        self.difficulty = difficulty
        self.punctuation = punctuation
    
class Response:
    def __init__(self, option, response_correct):
        self.option = option
        self.response_correct = response_correct

app = FastAPI()

# HOME
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/home.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    
    return HTMLResponse(content=html_content)

# JSON
@app.get("/animes")
def get_animes():
    with open('animes.json', 'r', encoding='utf-8') as f:
        json_question = json.load(f)  # Upload question JSON file 

    return json_question



       

