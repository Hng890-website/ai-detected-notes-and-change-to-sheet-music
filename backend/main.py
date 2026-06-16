from email.mime import audio
from fastapi import FastAPI, UploadFile, File
from basic_pitch import ICASSP_2022_MODEL_PATH, predict_and_save
import os

app = FastAPI()

os.makedirs("uploads", exist_ok=True)
os.makedirs("generated/midi", exist_ok=True)

@app.get("/")
def root():
    return {
        "message": "AI Sheet Music API"
    }

@app.post("/upload")
async def upload_audio(
    audio: UploadFile = File(...)
):

    if not audio.filename.endswith((".mp3", ".wav")):
    return {
        "success": False,
        "message": "Only MP3 and WAV files allowed"
    }

    filepath = f"uploads/{audio.filename}"
    predict_and_save(
    audio_path_list=[filepath],
    output_directory="generated/midi",
    save_midi=True,
    sonify_midi=False,
    save_model_outputs=False,
    save_notes=False,
    model_or_model_path=ICASSP_2022_MODEL_PATH
)
    
    with open(filepath, "wb") as buffer:
        buffer.write(
            await audio.read()
        )
    midi_filename = audio.filename.replace(".mp3", "_basic_pitch.mid")
    return {
    "success": True,
    "audio_file": audio.filename,
    "midi_file": midi_filename
    }
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)