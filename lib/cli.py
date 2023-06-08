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
    print("4) Go back to main menu")
    choice = int(input("Enter your choice >>>"))

    if choice == 1:
        clients = session.query(Client).all()
        for client in clients:
            print(client)
        print()  # provides a line break
    elif choice == 2:
        searched_client = input("Enter client name: ")
        clients = session.query(Client).filter(Client.name.like(f"%{searched_client}%")).all()
        if clients:
            for client in clients:
                print(client)
        else:
            print("No matching clients found.")
        print()
    elif choice == 3:
        print("Returning to main menu...")
    else:
        print("Invalid choice. Please try again.\n")

    

def display_workers():
    print("*** Worker List ***")
    print("Display all workers")
    print("")
    workers = session.query(Worker).all()
    for worker in workers:
        print(worker)
    print()

def display_work_orders():
    print("*** Work Order List ***")
    work_orders = session.query(Work_Order).all()
    for work_order in work_orders:
        print(work_order)
    print()

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
