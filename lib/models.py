from sqlalchemy import (
    PrimaryKeyConstraint,
    Column,
    String,
    Integer,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Worker(Base):
    __tablename__= "workers"
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    job = Column(String())
    years_experience = Column(Integer())
    hourly_pay = Column(Float())
    work_order_id = Column(Integer(), ForeignKey('work_orders.id'))

    def __repr__(self):
        return(
            f"Id: {self.id}, "
            +f"Name: {self.name}, "
            +f"Job: {self.job}, "
            +f"Years Experience: {self.years_experience}, "
            +f"Hourly Pay: {self.hourly_pay}"
        )
    
class Client(Base):
    __tablename__ = "clients"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    address = Column(String())
    phone = Column(Integer())
    email = Column(String())
    work_order = relationship("Work_Order", uselist=False, backref="client")
    
   

    def __repr__(self):
        return(
            f"Id: {self.id}, "
            +f"Name: {self.name}, "
            +f"Address: {self.address}, "
            +f"Phone: {self.phone}, "
            +f"Email: {self.email}"
        )
    
class Work_Order(Base):
    __tablename__ = "work_orders"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    job_request = Column(String())
    location = Column(String())
    number_of_employees_needed = Column(Integer())
    total_hours_needed = Column(Integer())
    client_id = Column(Integer(), ForeignKey('clients.id'))

    workers = relationship("Worker", backref=backref("work_orders"))
   

    def __repr__(self):
        return (
            f"Id: {self.id}, "
            + f"Job Request: {self.job_request}, "
            +f"Location: {self.location}, "
            +f"Number of Employees Needed: {self.number_of_employees_needed}, "
            +f"Total Hours Needed: {self.total_hours_needed}"
        )


