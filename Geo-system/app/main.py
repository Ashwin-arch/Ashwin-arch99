from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services.spam_detector import detect_spam
from app.services.nlp import analyze_text
from app.services.geo import reverse_geocode
from app.utils.image_meta import extract_gps

app = FastAPI(title="Geo NLP System")


@app.get("/")
def root():
    return {"status": "Geo System Running"}


@app.post("/analyze-text/")
def analyze_text_endpoint(text: str):
    # 🔴 Spam check FIRST
    spam_check = detect_spam(text)

    if spam_check.get("is_spam"):
        raise HTTPException(
            status_code=400,
            detail={
                "status": "rejected",
                "reason": spam_check["reason"],
                "message": spam_check["message"]
            }
        )

    # ✅ Only valid text reaches NLP
    return analyze_text(text)


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    gps = extract_gps(contents)
    location = reverse_geocode(gps) if gps else None
    return {
        "gps": gps,
        "location": location
    }
