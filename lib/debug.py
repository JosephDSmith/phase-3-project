from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Worker, Client, Work_Order

if __name__ == "__main__":
    engine = create_engine("sqlite:///temp_workers.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # all_workers = session.query(Worker).all()
    # for worker in all_workers:
    #     print(worker.name)
    
    # all_work_orders = session.query(Work_Order).all()
    # for work_order in all_work_orders:
    #     print(work_order.job_request)

    all_clients = session.query(Client).all()
    for client in all_clients:
        print(client.name)
    
    work_order_id = 1
    work_order = session.query(Work_Order).filter(Work_Order.id == work_order_id)
    

  

import ipdb; ipdb.set_trace()