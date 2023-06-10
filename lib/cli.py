from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Worker, Client, Work_Order

engine = create_engine("sqlite:///temp_workers.db")
Session = sessionmaker(bind=engine)
session = Session()

def display_clients():
    print("*** Client List ***")
    print("1) Display all clients")
    print("2) Search for client by name")
    print("3) Add a new cient")
    print("4) Go back to main menu")
    choice = int(input("Enter your choice >>>"))

    if choice == 1:
        clients = session.query(Client).all()
        for client in clients:
            print(client)
        print()  # provides a line break
    elif choice == 2:
        searched_client = input("Enter client name>>>")
        clients = session.query(Client).filter(Client.name.like(f"%{searched_client}%")).all()
        if clients:
            for client in clients:
                print(client)
        else:
            print("No matching clients found.")
        print()
    elif choice == 3:
        name = input("Enter client name>>>")
        address = input ("Enter client address>>>")
        phone = input ("Enter client phone>>>")
        email = input ("Enter client email>>>")

        new_client = Client(
            name = name,
            address = address,
            phone = phone,
            email = email
        )
        session.add(new_client)
        session.commit()
        print("Client successfully added!")
    elif choice == 4:
        print("Returning to main menu...")
    else:
        print("Invalid choice. Please try again.\n")

    

def display_workers():
    print("*** Worker List ***")
    print("1) Display all workers")
    print("2) Search for worker by name")
    print("3) Search for worker by worker specialty")
    print("4) Display all workers by payscale (low to high)")
    print("5) Go back to main menu")
    choice = int(input("Enter your choice >>>"))

    if choice == 1:
        workers = session.query(Worker).all()
        for worker in workers:
            print(worker)
        print()
    elif choice == 2:
        searched_worker = input("Enter worker name>>>")
        workers = session.query(Worker).filter(Worker.name.like(f"%{searched_worker}%")).all()
        for worker in workers:
            print(worker)
        print()
    elif choice == 3:
        searched_specialty = input("Enter worker specialty>>>")
        workers = session.query(Worker).filter(Worker.job.like(f"%{searched_specialty}%"))
        for worker in workers:
            print(worker)
        print()
    elif choice == 4:
        workers = session.query(Worker).all()
        workers_by_pay = sorted(workers, key=lambda w: w.hourly_pay)
        for worker in workers_by_pay:
            print(worker)
        print()
    elif choice == 5:
        print("Returning to main menu...")
    else:
        print ("Invalid choice. Please try again.\n")


def display_work_orders():
    print("*** Work Order List ***")
    print("1) Display all work orders")
    print("2) Display work orders for a client")
    print("3) Display all workers in a work order")
    print("4) Display total cost of a work order")
    print("5) Go back to main menu")
    choice = int(input("Enter your choice >>>"))

    if choice == 1: 
        work_orders = session.query(Work_Order).all()
        for work_order in work_orders:
            print(work_order)
        print()
    elif choice == 2:
        searched_client = input("Search by client id>>>")
        work_orders = session.query(Work_Order).filter(Work_Order.client_id == searched_client).all()
        for work_order in work_orders:
            print(work_order)
        print()
    elif choice == 3:
        searched_id = input("Enter work order id>>>")
        workers = session.query(Worker).filter(Worker.work_order_id == searched_id)
        for worker in workers:
            print(worker)
        print()
    elif choice == 4:
        searched_id = input("Enter work order id>>>")
        total_hours_needed = session.query(Work_Order).filter(Work_Order.id == searched_id).first().total_hours_needed
        workers = session.query(Worker).filter(Worker.work_order_id == searched_id)
        pay = 0
        for worker in workers:
            pay += worker.hourly_pay * total_hours_needed
        print(pay)
        print()
    elif choice == 5:
        print("Returning to main menu...")
    else:
        print ("Invalid choice. Please try again.\n")

def main():
    choice = 0
    while choice != 4:
        print("*** Welcome to Work-Order Manager! ***")
        print("1) Look up clients")
        print("2) Look up workers")
        print("3) Look up work orders")
        print("4) Exit program")
        choice = int(input("Enter your choice >>> "))

        if choice == 1:
            display_clients()
        elif choice == 2:
            display_workers()
        elif choice == 3:
            display_work_orders()
        elif choice == 4:
            print("Exiting program...")
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
