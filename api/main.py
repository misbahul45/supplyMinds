from fastapi import FastAPI

app = FastAPI(
    title="Supply Minds API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Supply Minds API Running"}