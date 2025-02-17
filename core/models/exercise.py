from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.workout_set import WorkoutSet


class Exercise(Base):
    name: Mapped[str] = mapped_column(unique=True)

    workout_sets: Mapped[list["WorkoutSet"]] = relationship(
        back_populates="exercise",
        cascade="all, delete-orphan",
        lazy="joined",
    )
