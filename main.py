


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "325435 asu World"}




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
