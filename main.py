


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "325435 asu World"}