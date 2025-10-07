import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from backend.api.v1.users.api import router, lifespan
from starlette.responses import RedirectResponse
from backend.settings import API_VERSION
from backend.utils.logs import Logfire


app = FastAPI(title='users api service', version=API_VERSION, lifespan=lifespan)

app.include_router(router=router)

log = Logfire(name='users-service')


class HeathResponseSchema(BaseModel):
    status_code: int = 200
    server: str = 'healthy'


@app.get('/')
def root() -> RedirectResponse:
    return RedirectResponse(url='/docs')


@app.get('/health')
def health() -> HeathResponseSchema:
    return HeathResponseSchema().model_dump()


if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=89, use_colors=True)
