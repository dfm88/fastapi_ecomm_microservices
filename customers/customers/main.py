import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from customers.api.endpoints.api_v1.router import router
from customers.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# routers definition
app.include_router(router=router, prefix=settings.API_V1_STR)


@app.get('/')
async def main():
    return "Customer is running"


if __name__ == '__main__':
    debug = True
    uvicorn.run(
        "customers.main:app",
        host='0.0.0.0',
        port=8001,
        debug=debug,
        reload=debug,
        use_colors=True,
    )
