from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Indian Recipes Data (30 Dishes)
recipes = [
    {
        "name": "Butter Chicken",
        "description": "A rich and creamy tomato-based chicken curry.",
        "ingredients": ["Chicken", "Butter", "Tomatoes", "Cream", "Spices"],
        "time": "40 minutes",
        "instructions": "1. Marinate chicken with spices and yogurt.\n2. Cook chicken in butter and tomatoes.\n3. Add cream and simmer until thick.",
        "video": "https://www.youtube.com/embed/YE7VzlLtp-4"
    },
    {
        "name": "Masala Dosa",
        "description": "Crispy dosa stuffed with spiced mashed potatoes.",
        "ingredients": ["Rice", "Lentils", "Potatoes", "Onion", "Spices"],
        "time": "30 minutes",
        "instructions": "1. Soak rice and lentils overnight.\n2. Make batter and ferment.\n3. Cook dosa and stuff with spiced potatoes.",
        "video": "https://www.youtube.com/embed/IgQkbjb6Vh0"
    },
    {
        "name": "Paneer Butter Masala",
        "description": "A delicious paneer curry with creamy tomato gravy.",
        "ingredients": ["Paneer", "Tomatoes", "Butter", "Cream", "Spices"],
        "time": "35 minutes",
        "instructions": "1. Fry paneer cubes.\n2. Prepare tomato gravy.\n3. Add paneer and cook in gravy.",
        "video": "https://www.youtube.com/embed/Z9Pplql43jM"
    },
    # Add 27 more recipes here...
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, query: str):
    results = [recipe for recipe in recipes if query.lower() in recipe["name"].lower()]
    if not results:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return templates.TemplateResponse("search.html", {"request": request, "recipes": results, "query": query})
