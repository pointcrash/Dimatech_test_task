from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from passlib.context import CryptContext
from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(IntIdPkMixin, Base):
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)