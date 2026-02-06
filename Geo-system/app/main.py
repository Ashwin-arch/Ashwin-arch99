from fastapi import FastAPI, UploadFile, File
from app.services.nlp import analyze_text
from app.services.geo import reverse_geocode
from app.utils.image_meta import extract_gps

app = FastAPI(title="Geo NLP System")

@app.get("/")
def root():
    return {"status": "Geo System Running"}

@app.post("/analyze-text/")
async def analyze(text: str):
    return analyze_text(text)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    gps = extract_gps(contents)
    location = reverse_geocode(gps) if gps else None
    return {"gps": gps, "location": location}
