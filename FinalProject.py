from datetime import datetime, timedelta
from functools import reduce # Import reduce
import threading

class Task:
    def __init__(self, title, description, due_date, priority, status="Open"):
        self._title = title  # Encapsulation: Private variable
        self._description = description
        self._due_date = self._parse_date(due_date)  # Store as datetime object
        self._priority = priority
        self._status = status

    # Getters and setters for private variables
    def get_title(self):
        return self._title

    def set_title(self, new_title):
        self._title = new_title

    def get_priority(self):
        return self._priority

    def set_priority(self, new_priority):
        self._priority = new_priority

    def get_status(self):
        return self._status

    def set_status(self, new_status):
        self._status = new_status

    def set_description(self, new_description):
        self._description = new_description

    def _parse_date(self, due_date_str):
        # Input validation using for loop with try-except block
        for fmt in ["%Y-%m-%d","%m-%d-%Y", "%m/%d/%Y", "%d/%m/%Y"]:
            try:
                return datetime.strptime(due_date_str, fmt)
            except ValueError:
                pass  # Ignore errors for invalid formats

        raise ValueError("Invalid date format. Please use MM-DD-YYYY.")

    def is_overdue(self):
        return self._due_date < datetime.now()

    def __str__(self):
        return f"Title: {self._title}\nDescription: {self._description}\nDue Date: {self._due_date.strftime('%Y-%m-%d')}\nPriority: {self._priority}\nStatus: {self._status}"


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def delete_task(self, title):
        # Removing the task using list comprehension and for loop
        self._tasks = [task for task in self._tasks if task.get_title() != title]

    def update_task(self, title, new_title, new_description, new_due_date, new_priority, new_status):
        # This will represent to updating the task using list comprehension and for loop
        for task in self._tasks:
            if task.get_title() == title:
                task.set_title(new_title)

    def get_upcoming_tasks(self):
        # Functional programming using filter
        return list(filter(lambda task: not task.is_overdue(), self._tasks))

    def get_overdue_tasks(self):
        # Functional programming using filter
        return list(filter(lambda task: task.is_overdue(), self._tasks))


# Jelin S: Singleton wrapper for TaskManager
class TaskManagerSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if TaskManagerSingleton._instance is None:
            TaskManagerSingleton._instance = TaskManager()
        return TaskManagerSingleton._instance



    # Tiffanie D - added reduce
    def get_completed_tasks(self):
        # functional programming using reduce to count completed tasks
        # assuming 'status' attribute is used to track task completion
        task_manager =  self.get_instance() # added task_manager = self.get_instance(), needed to work for case 8.
        completed_tasks = [task for task in self._tasks if task._status == "Completed"] # change to _status
        completed_count = reduce(lambda count, task: count + (1 if task._status == "Completed" else 0), self._tasks, 0) # change to _status
        return completed_tasks, completed_count # return count and list of completed task

#Je'Lin S: Concurrency
class Notification:
    def notify_overdue_tasks(self, tasks):
        # Imperative programming with a while loop for notification check
        while True:
            overdue_tasks = [task for task in tasks if task.is_overdue()]
            if overdue_tasks:
                print("Overdue tasks:")
                for task in overdue_tasks:
                    print(task)

            threading.Timer(30.0, self.notify_overdue_tasks, args=(tasks,)).start()  # Recursive call using threading.Timer
            break

# Create a pure function for task filtering (no side effects)
def filter_by_priority(tasks, priority):
    return [task for task in tasks if task.get_priority() == priority]

def main():
    task_manager = TaskManager()
    notification = Notification()

    while True:
        print("Task Management System:")
        print("-----")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. View Upcoming Tasks")
        print("6. View Overdue Tasks")
        print("7. View Completed Tasks")
        print("8. View Upcoming High Priority Tasks") # Miranda P. - added to pull up only HIGH PRIORITY tasks
        print("9. Exit")
        print("----")

        choice = input("Enter your choice: ")

        match choice:
          case "1":
                # Code to add a task
                print("Add New Task")
                print("\n")

                # Get the input from the user for title, description, due date,
                # and priority
                while True:  # Loop for title input
                  title = input("Title: ")
                  if title:
                      break
                  else:
                      print("Title cannot be empty. Please try again.")

                while True:  # Loop for description input
                  description = input("Description: ")
                  if description:
                      break
                  else:
                      print("Description cannot be empty. Please try again.")

                while True:  # Loop for due date input
                  due_date = input("Due Date (MM-DD-YYYY): ")
                  if due_date:
                    try:
                        # Attempt to parse the date to validate format
                        datetime.strptime(due_date, "%m-%d-%Y")
                        break  # Exit loop if date is valid
                    except ValueError:
                      print("Invalid date format. Please use MM-DD-YYYY.")
                  else:
                    print("Due Date cannot be empty. Please try again.")

                while True:  # Loop for priority input
                  priority = input("Priority (Low, Medium, High): ")
                  if priority:
                      break
                  else:
                      print("Priority cannot be empty. Please try again.")

                print("\n")

                # Create a Task instance with the provided information to the
                # constructor
                task = Task(title, description, due_date, priority)

                # Added task to the collection and print the confirmation
                task_manager.add_task(task)
                print("Task added successfully!")
                print("\n")

          #Lizbeth M
          case "2":
            # Code to update a task
                print("Update Task\n")

                if not task_manager._tasks:
                    print("There are no tasks available to update.\n")
                    break  # Exits if there are no existing tasks


                #Prints the current tasks, making it easier for users to know what to alter
                print("Current Tasks:\n")

                #Using enumerate to add an index to each task
                #Using map to format each task with an index, title, and due date
                task_list = list(map(lambda task: f" {task[0] + 1}. {task[1].get_title()} - Due: {task[1]._due_date.strftime('%Y-%m-%d')}", enumerate(task_manager._tasks)))

                for task in task_list:
                    print(task)
                print()

                # Gets valid task number
                while True:
                    try:
                        task_number = int(input("Enter the number of the task to update: ").strip())
                        if 1 <= task_number <= len(task_manager._tasks):
                            task_to_update = task_manager._tasks[task_number - 1]
                            break
                        else:
                            print("Error: Invalid task number.\n")
                    except ValueError:
                        print("Error: Please enter a valid number.\n")

                # Update Tittle
                while True:
                    print("Would you like to edit the title? 1. YES, 2. NO\n")
                    edit_title = input("Enter your choice: ").strip()
                    if edit_title in ["1", "2"]:  # Checks if input is 1 or 2
                        break  # breaks out of the loop if the input is not 1 or 2
                    else:
                        print("Invalid choice. Please enter 1 or 2\n")  # Print error message and repeat

                if edit_title == "1": #Enters the loop to change the title
                    while True:
                        new_title = input("Enter the new title: ").strip()
                        if new_title:
                            task_to_update.set_title(new_title)
                            break  # Exits the loop if title is not empty
                        print("Error: Title cannot be empty.\n")

                # Update Description
                while True:
                    print("Would you like to edit the description? 1. YES, 2. NO\n")
                    edit_desc = input("Enter your choice: ").strip()
                    if edit_desc in ["1", "2"]:  # Checks if input is 1 or 2
                        break  # breaks out of the loop if the input is not 1 or 2
                    else:
                        print("Invalid choice. Please enter 1 or 2\n")  # Print error message and repeat

                if edit_desc == "1":
                    while True:
                        new_description = input("Enter the new description: ").strip()
                        if new_description:
                            task_to_update.set_description(new_description)  # Use set_description method
                            break  # Exits the loop if the description is not empty
                        print("Error: Description cannot be empty.\n")

                # Update due date
                while True:
                    print("Would you like to edit the due date? 1. YES, 2. NO\n")
                    edit_due = input("Enter your choice: ").strip()
                    if edit_due in ["1", "2"]:  # Checks if input is 1 or 2
                        break  # breaks out of the loop if the input is not 1 or 2
                    else:
                        print("Invalid choice. Please enter 1 or 2\n")  # Print error message and repeat

                if edit_due == "1":
                    while True:
                        new_due_date = input("Enter the new due date (YYYY-MM-DD, MM-DD-YYYY, MM/DD/YYYY, DD/MM/YYYY): ").strip()
                        if not new_due_date:
                            print("Error: Due date cannot be empty.\n")
                            continue
                        try:
                            new_due_date = task_to_update._parse_date(new_due_date) # using parse date to filter through viable formats
                            task_to_update._due_date = new_due_date
                            break
                        except ValueError:
                            print("Error: Invalid date format. Use YYYY-MM-DD.\n")

                # update priority
                while True:
                    print("Would you like to edit the priority? 1. YES, 2. NO\n")
                    edit_priority = input("Enter your choice: ").strip()
                    if edit_priority in ["1", "2"]:  # Checks if input is 1 or 2
                        break  # breaks out of the loop if the input is not 1 or 2
                    else:
                        print("Invalid choice. Please enter 1 or 2\n")  # Print error message and repeat

                if edit_priority == "1":
                    valid_priorities = ["Low", "Medium", "High"]
                    while True:
                        new_priority = input("Enter the new priority (Low, Medium, High): ").strip()
                        if new_priority in valid_priorities:
                            task_to_update.set_priority(new_priority)
                            break
                        print(f"Error: Priority must be one of: {', '.join(valid_priorities)}\n")

                # update status
                while True:
                    print("Would you like to edit the status? 1. YES, 2. NO\n")
                    edit_status = input("Enter your choice: ").strip()
                    if edit_status in ["1", "2"]:  # Checks if input is 1 or 2
                        break  # # breaks out of the loop if the input is not 1 or 2
                    else:
                        print("Invalid choice. Please enter 1 or 2\n")  # Print error message and repeat

                if edit_status == "1":
                    valid_statuses = ["Open", "In Progress", "Completed"]
                    while True:
                        new_status = input("Enter the new status (Open, In Progress, Completed): ").strip()
                        if new_status in valid_statuses:
                            task_to_update.set_status(new_status)  # Use set_status method
                            break
                        print(f"Error: Status must be one of: {', '.join(valid_statuses)}\n")

                print("\nTask updated successfully!\n")

          case "3":
            # Code to delete a task
            print("Delete Task")
            print("\n")

            while True:
                title = input("Enter the title of the task to delete: ")
                if title:  # Check if title is not empty
                    break  # Exit the loop if title is valid
                else:
                    print("Title cannot be empty. Please try again.")
            print("\n")

            task_manager.delete_task(title)
            print("Task deleted successfully!")
            print("\n")

          case "4":
            # Code to view all tasks
            print("View All Tasks:")
            print("\n")

            if not task_manager._tasks:  # Check if the task list is empty
                print("No tasks found.")
            else:
                for task in task_manager._tasks:
                    print(task)
                    print("\n")

          case "5":
            # Code to view all upcoming tasks:
            upcoming_tasks = task_manager.get_upcoming_tasks()
            print("Upcoming Tasks:")
            print("\n")

            if not upcoming_tasks:  # Checks if the upcoming_tasks list is empty
                print("No upcoming tasks found.")
            else:
                for task in upcoming_tasks:
                    print(task)
                    print("\n")

          case "6":
            # Code to view all overdue tasks:
            overdue_tasks = task_manager.get_overdue_tasks()
            print("Overdue Tasks:")
            print("\n")

            if not overdue_tasks:  # Check if the overdue_tasks list is empty
                print("No overdue tasks found.")
            else:
                for task in overdue_tasks:
                    print(task)
                    print("\n")

          # Tiffanie D
          case "7":
              # Code to view all completed tasks:
              completed_tasks, completed_count = task_manager.get_completed_tasks()
              print(f"Completed Tasks ({completed_count}):") # Print the count
              print("\n")
              if not completed_tasks:  # Check if the completed_tasks list is empty
                  print("No completed tasks found.")
              else:
                  for task in completed_tasks:
                      print(task)
                      print("\n")

         # Miranda P. - to pull only HIGH PRIORITY tasks using filter() and map() functions
          case "8":
            print("Upcoming High Priority Tasks:")
            high_priority_tasks = filter(lambda t: not t.is_overdue() and t.get_priority().lower() == "high", task_manager._tasks)
            summaries = map(lambda t: f"{t.get_title()} - Due: {t._due_date.strftime('%Y-%m-%d')}", high_priority_tasks)
            for summary in summaries:
              print(summary)
            print("\n")

          case "9":
            print("Exiting the system. Goodbye!")
            break

          case _:
            print("Invalid choice. Please try again.")

    # Start notification thread after menu loop
    notification.notify_overdue_tasks(task_manager._tasks)

if __name__ == "__main__":
    main()