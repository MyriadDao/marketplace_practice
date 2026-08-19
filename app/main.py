from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Добавили импорт CORS
from app.db import Base, engine
from app.routers.product import router as product_router

#==============================================================================================

@asynccontextmanager
async def lifespan(_: FastAPI):
    # При старте сервера автоматически создаются все таблицы в базе данных
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

#==============================================================================================

# ИСПРАВЛЕНО: Передали lifespan в настройки приложения FastAPI
app = FastAPI(title="marketplace_practice", lifespan=lifespan)

#==============================================================================================
# ИСПРАВЛЕНО: Добавили CORS-настройки для вашего друга-фронтендера
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # На этапе разработки разрешаем запросы с любых адресов
    allow_credentials=True,
    allow_methods=["*"], # Разрешаем любые методы (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Разрешаем любые заголовки
)

#==============================================================================================

@app.get("/", tags=["Home page"], summary="Начальная страница")
async def read_root():
    return {"message": "Welcome to the marketplace_practice API!"}

#==============================================================================================

app.include_router(product_router)

#==============================================================================================

@app.get("/status", tags=["Project status"], summary="Узнать статус проекта")
async def get_status():
    return {"status": "working"}