import uvicorn
from fastapi import FastAPI
from update import post
app = FastAPI()


@app.get("/")
async def root():
    return {"message": f'''asuasas'''}


@app.post("/update")
async def update():
    pid = post()
    return "Hello World!" + pid


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
