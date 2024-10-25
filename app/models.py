from sqlalchemy import String, func, Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from datetime import datetime


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now())


class Group(Base):
    __tablename__ = 'groups'

    name: Mapped[str]


assoc_student_group = Table(
    'student_group_assoc',
    Base.metadata,
    Column(
        'group_id',
        ForeignKey('groups.id'),
        primary_key=True
    ),
    Column(
        'student_id',
        ForeignKey('students.id'),
        primary_key=True
    )
)


class Student(Base):
    __tablename__ = 'students'

    name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    groups: Mapped[List[Group]] = relationship(secondary=assoc_student_group)
