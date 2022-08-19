from fastapi import FastAPI
import uvicorn

app = FastAPI(
    
)


@app.get('/')
async def main():
    return "Customer is running"


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
