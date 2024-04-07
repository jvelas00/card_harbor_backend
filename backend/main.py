
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pokemontcgsdk import Card
from Utilities.Censorship.CensorshipService import CheckCensorship
from Utilities.Database.DAO.Users import *
from cors import setup_cors

app = FastAPI()

setup_cors(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/GetCards")
async def get_cards():

    cards = Card.all()
    cards_json = []

    for card in cards:
        cards_json.append(card.__dict__)

    return cards_json

@app.get("/GetCardPage/{page}/{size}")
async def get_card_page(page: int, size: int):
    card_page = Card.where(page=page, pageSize=size)

    card_json = []

    for card in card_page:
        card_json.append(card.__dict__)

    return card_json

@app.post("/PredictFrame")
async def predict_frame(frame: str):
    #image_src = frame
    #if decode
    #image_decoded = base64.b64decode(image_src.split(',')[1 ?? or maybe 2 idk]) something like this
    return

@app.get("/CensorshipCheck")
async def censorship_check(testString: str) -> Response:
    result = CheckCensorship(testString)

    return JSONResponse(content={"result": str(result)})

@app.get("/GetUser/{username}/{password}")
async def get_user(username: str, password: str) -> Response:
    result = GetUser(username, password)

    print(result)

    return JSONResponse(content={"result": str(result)})