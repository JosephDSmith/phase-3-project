# Work Order Manager CLI 

Work Order Manager CLI - Phase 3 Project Assignment by Joseph D Smith 


# Description:  

The Work-Order Manager CLI is a command-line application designed to manage clients, workers, and work orders for a temporary staffing agency. It provides a user-friendly interface to perform various operations related to client management, worker management, and work order management.

## Features

Client Management: Users can view all clients or search for a specific client by name. The application displays detailed information about clients, including their name, address, phone number, and email.

Worker Management: Users can view all workers or search for a worker by name or job specialty. Workers can be sorted by hourly pay in ascending order. The application provides information about workers, such as their name, job, years of experience, and hourly pay.

Work Order Management: Users can view all work orders or search for work orders by client. They can also view all workers assigned to a specific work order and calculate the total cost of a work order based on the workers' hourly pay and total hours needed. Work orders contain details such as the job request, location, number of employees needed, and total hours needed.

Adding Database Data: Users can add new workers to the system by providing their name, address, phone, and email. This script can also be modified to add new workers and new work orders. 

## Key Models

Worker:

Attributes: id, name, job, years_experience, hourly_pay, client_id, work_order_id
Relationships: Belongs to a client and a work order

Client:

Attributes: id, name, address, phone, email
Relationships: Has one work order

Work_Order:

Attributes: id, job_request, location, number_of_employees_needed, total_hours_needed, client_id
Relationships: Belongs to a client, has multiple workers

## Key Functions

Display Clients: Retrieves and displays detailed information about clients stored in the database. Users can choose to view all clients or search for a specific client by name.

Display Workers: Retrieves and displays detailed information about workers stored in the database. Users have multiple options to explore workers, including viewing all workers, searching workers by name, searching workers by specialty, and sorting workers by pay scale.

Display Work Orders: Retrieves and displays detailed information about work orders stored in the database. Users can choose to view all work orders or explore specific work orders based on client or work order ID. Additionally, users can view all workers assigned to a particular work order and calculate the total cost of a work order.

Add Client: Allows users to add a new client to the database by providing relevant details such as name, address, phone number, and email. The newly added client will be saved in the database for future reference.

Main Menu: Serves as the main entry point of the CLI application. Users are presented with a menu where they can choose different options to interact with the application, such as accessing client information, worker information, work order information, or exiting the program.

## Contributing

Pull requests are welcome for reiew. 
No major changes are allowed. 

Please reach out to support if you have any questions. 

## License

Licensing is not being offered at this time. 
For any questions, please reach out to our support team. 

## References

This CLI was built using a tutorial by Bek Brace. Special thanks to him and his amazing channel!
https://www.youtube.com/watch?v=kTaqR1WyT8A

## Blog

If you like what you see, check out my blog on Medium! 
https://medium.com/@joesmith40

## Support

For any questions or support, please reach out to joesmith40@gmail.com.

