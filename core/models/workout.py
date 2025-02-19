from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.user import User
    from core.models.workout_set import WorkoutSet


class Workout(Base):
    date: Mapped[datetime]
    notes: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(
        back_populates="workouts",
        lazy="joined",
    )

    workout_sets: Mapped[list["WorkoutSet"]] = relationship(
        back_populates="workout",
        cascade="all, delete-orphan",
        lazy="joined",
    )
