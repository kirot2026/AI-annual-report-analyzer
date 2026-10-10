from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import analysis
import database

class AnalyzeRequest(BaseModel):
    company: str
    report_year:int
    source_text:str

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_table()
    yield

app = FastAPI(lifespan=lifespan) 

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        result,report_data=analysis.analyze_report(request.source_text,request.company,request.report_year)
        database.insert_analysis(report_data)
        return result
    except ValueError as e:
        raise HTTPException(status_code=500,detail=str(e))