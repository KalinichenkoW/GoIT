from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    students = relationship("Student", secondary='teachers_to_students', back_populates="teachers")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    teachers = relationship("Teacher", secondary='teachers_to_students', back_populates="students")
    contacts = relationship("Contact", back_populates="student", cascade="all, delete-orphan")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    student_id = Column(ForeignKey("students.id", ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    student = relationship("Student", back_populates="contacts")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class TeacherStudent(Base):
    __tablename__ = 'teachers_to_students'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))


# class Grade:
#     pass
#
#
# class Group:
#     pass
#
#
# class Subject:
#     pass


# class Teacher(Base):
#     __tablename__ = 'teachers'
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String(120), nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String(120), nullable=False)
#     group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
#     group = relationship('Group', backref='students')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')

#
# class Grade(Base):
#     __tablename__ = 'grades'
#     id = Column(Integer, primary_key=True)
#     grade = Column(Integer, nullable=False)
#     date_of = Column('date_of', Date, nullable=True)
#     student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
#     subjects_id = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE'))
#     student = relationship('Student', backref='grade')
#     discipline = relationship('Discipline', backref='grade')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer , primary_key=True)
    grade = Column(Integer , nullable=False)  # Додайте атрибут grade