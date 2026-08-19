from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True, default=0.00)
    description: Mapped[str] = mapped_column(nullable=True)
    in_stock: Mapped[float] = mapped_column(nullable=True, default=0)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)

    # Bidirectional link for more convenient requests
    category_rel: Mapped[str] = relationship("Category", back_populates="products")
