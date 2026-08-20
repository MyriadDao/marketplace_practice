from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Добавили импорт CORS
from app.routers.product import router as product_router

#==============================================================================================

app = FastAPI(title="marketplace_practice")

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
def read_root():
    return {"message": "Welcome to the marketplace_practice API!"}

#==============================================================================================

app.include_router(product_router)

#==============================================================================================

@app.get("/status", tags=["Project status"], summary="Узнать статус проекта")
def get_status():
    return {"status": "working"}