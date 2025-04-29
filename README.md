# Final-Project-for-Org.-of-Comp.-Lang.
Organization of Computer Languages

## About the Project:

This is our final term project: a Smart CLI-Based Task Manager with Multimode Logic, developed using python on the Google Collab Platform. The primary goal of the system is to help users efficiently manage their tasks via the command line interface.

The system allows users to:
-Add new tasks
-Modify existing tasks
-Delete tasks
-View tasks in various filtered formats

## Technologies & Concepts Used

- Python
- Object-Oriented Programming (OOP)
- Functional Programming (`map`, `filter`, `reduce`)
- Singleton & Factory Design Patterns
- Abstract Base Classes
- Threading for periodic notifications
- Input validation
- Google Colab for collaborative development


## Running the Program
Once the program runs, users are greeted with a friendly menu-driven interface:

Task Management System:
1. Add Task
2. Update Task
3. Delete Task
4. View Tasks
5. View Upcoming Tasks
6. View Overdue Tasks
7. View Completed Tasks
8. View Upcoming High Priority Tasks
9. Exit

To make a selection and interact with the system, Users must enter the corresponding index number for their desired actions.
-For example, entering ‘1’ allows the user to add a new task. Each selection chosen, will guide the user through every step of the way. In when adding a new task, the user will be guided through also including inputs like task name, description, deadline, and priority.
-After completing an action, the system will return to the main menu to allow for further task management or exiting the program.


### Notes:

- The program uses input validation to prevent errors (e.g., wrong date formats, empty fields, or invalid priorities).
- Dates should be entered in `YYYY-MM-DD` format.
- Priority is case-insensitive but must match one of: `High`, `Medium`, or `Low`.
- All interactions are handled synchronously, and the interface remains active until the user chooses to exit.

## Contributors

- **Hector V.**
- **Je'Lin S.**
- **Tiffanie D.**
- **Lizbeth M.**
- **Miranda P.**
- **Stephano C.**
