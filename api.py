from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from contextlib import asynccontextmanager
import analysis
import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_table()
    yield

app = FastAPI(lifespan=lifespan) 

@app.post("/analyze")
async def analyze(file: UploadFile = File(...),
                  company: str = Form(...),
                  report_year: int = Form(...)):
    if not file.filename or not file.filename.lower().endswith(".txt"):
        raise HTTPException(status_code=400,
                            detail="Please upload a .txt file.")

    try:
        content = await file.read()
        if not content:
           raise HTTPException(status_code=400,
                               detail="The uploaded file is empty.")
        source_text = content.decode("utf-8")
        result,report_data=analysis.analyze_report(source_text,company,report_year)
        database.insert_analysis(report_data)
        return result
    except ValueError as e:
        raise HTTPException(status_code=500,detail=str(e))