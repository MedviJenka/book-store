import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from backend.api.book import router
from starlette.responses import RedirectResponse


app = FastAPI()

app.include_router(router=router)


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
    uvicorn.run(app=app, host='0.0.0.0', port=88, use_colors=True)
