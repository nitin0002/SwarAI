from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(title="SwarAI - AI Powered Cold Calling System")

app.include_router(endpoints.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
