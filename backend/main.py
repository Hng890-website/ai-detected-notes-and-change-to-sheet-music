from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

os.makedirs("uploads", exist_ok=True)

@app.get("/")
def root():
    return {
        "message": "AI Sheet Music API"
    }

@app.post("/upload")
async def upload_audio(
    audio: UploadFile = File(...)
):

    filepath = f"uploads/{audio.filename}"

    with open(filepath, "wb") as buffer:
        buffer.write(
            await audio.read()
        )

    return {
        "success": True,
        "filename": audio.filename
    }