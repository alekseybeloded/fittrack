from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.exercise import Exercise
    from core.models.workout import Workout


class WorkoutSet(Base):
    sets: Mapped[int]
    reps: Mapped[int]
    weight: Mapped[float]

    workout_id: Mapped[int] = mapped_column(ForeignKey("workouts.id"))
    workout: Mapped["Workout"] = relationship(
        back_populates="workout_sets",
        lazy="joined",
    )

    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id"))
    exercise: Mapped["Exercise"] = relationship(
        back_populates="workout_sets",
        lazy="joined",
    )
