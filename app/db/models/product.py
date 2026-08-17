from sqlalchemy import String, Numeric  # Импортируем всё нужное из sqlalchemy в одной строке
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


# ==============================================================================================

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0.00)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

