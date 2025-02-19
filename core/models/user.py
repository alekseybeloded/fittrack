from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base
from core.models.workout import Workout


class User(Base):
    name: Mapped[str]

    workouts: Mapped[list["Workout"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="joined",
    )
