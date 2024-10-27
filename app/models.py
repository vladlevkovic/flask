from sqlalchemy import String, func, Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from datetime import datetime


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now())


class Group(Base):
    __tablename__ = 'groups'

    name: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self):
        return f'{self.name}'


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


student_group_assoc_table = Table(
    'student_group_assoc_table',
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


lesson_group_assoc_table = Table(
    "lesson_group_assoc_table",
    Base.metadata,
    Column("lesson_id", ForeignKey("lessons.id"), primary_key=True),
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
)



class Lesson(Base):
    __tablename__ = 'lessons'

    title: Mapped[str] = mapped_column(String(50))
    groups: Mapped[List[Group]] = relationship(secondary=lesson_group_assoc_table)
