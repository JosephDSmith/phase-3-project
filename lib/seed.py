from faker import Faker
import random 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Worker, Client, Work_Order

if __name__ == "__main__":
    engine = create_engine("sqlite:///temp_workers.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Worker).delete()
    session.query(Client).delete()
    session.query(Work_Order).delete()
  
    fake = Faker()

    temp_jobs = ["landscaper", "house cleaner", "janitor", "road worker", "receptionist", "general event staff", "delivery driver", "administrative assistant", "call center agent", "office clerk", "sign holder", "data analyst", "handyman"]

    clients = []
    
    for _ in range(40):
        client = Client(
            name=fake.name(),
            address=fake.address(),
            phone=random.randint(1000000000, 9999999999),
            email=fake.email()
        )

        clients.append(client)
        session.add(client)  
        session.commit()

    work_orders = []

    for client in clients:
        work_order = Work_Order(
            job_request=random.choice(temp_jobs),
            location=fake.address(),
            number_of_employees_needed=random.randint(1, 10),
            total_hours_needed=random.randint(5, 8),
            client_id=client.id
        )

        work_orders.append(work_order)
        session.add(work_order)
        session.commit()

    workers = []
    
    for work_order in work_orders:
        number_of_employees_needed = work_order.number_of_employees_needed

        for _ in range(number_of_employees_needed):
            worker = Worker(
                name=fake.name(),
                job=work_order.job_request,
                years_experience=random.randint(0, 5),
                hourly_pay=round(random.uniform(20.50, 50.50), 2),
                client_id=work_order.client_id,
                work_order_id= work_order.id
            )
         
            workers.append(worker)
            session.add(worker)
            session.commit()
    
    session.commit()

