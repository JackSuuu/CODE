#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Task class definition
class Task {
private:
    string name;
    bool completed;

public:
    // Constructor
    Task(const string& taskName) : name(taskName), completed(false) {}

    // Get the task name
    string getName() const {
        return name;
    }

    // Mark task as completed
    void markCompleted() {
        completed = true;
    }

    // Mark task as not completed
    void markNotCompleted() {
        completed = false;
    }

    // Display task status
    void displayTask() const {
        cout << (completed ? "- [x] " : "- [ ] ") << name << endl;
    }

    // Check if the task is completed
    bool isCompleted() const {
        return completed;
    }
};

// ToDoList class definition
class ToDoList {
private:
    vector<Task> tasks;

public:
    // Add task to the list
    void addTask(const string& taskName) {
        tasks.push_back(Task(taskName));
    }

    // Delete a task by index
    void deleteTask(int index) {
        if (index >= 0 && index < tasks.size()) {
            tasks.erase(tasks.begin() + index);
        } else {
            cout << "Invalid task index." << endl;
        }
    }

    // Display all tasks
    void displayTasks() const {
        if (tasks.empty()) {
            cout << "No tasks to display!" << endl;
            return;
        }
        for (int i = 0; i < tasks.size(); ++i) {
            cout << i + 1 << ". ";
            tasks[i].displayTask();
        }
    }

    // Mark task as completed
    void markTaskCompleted(int index) {
        if (index >= 0 && index < tasks.size()) {
            tasks[index].markCompleted();
        } else {
            cout << "Invalid task index." << endl;
        }
    }

    // Mark task as not completed
    void markTaskNotCompleted(int index) {
        if (index >= 0 && index < tasks.size()) {
            tasks[index].markNotCompleted();
        } else {
            cout << "Invalid task index." << endl;
        }
    }
};

int main() {
    ToDoList myList;
    int choice;
    string taskName;
    int taskIndex;

    while (true) {
        // Menu
        cout << "\nTo-Do List Menu:\n";
        cout << "1. Add Task\n";
        cout << "2. Delete Task\n";
        cout << "3. Display Tasks\n";
        cout << "4. Mark Task as Completed\n";
        cout << "5. Mark Task as Not Completed\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore();  // To ignore the newline character after entering the choice

        switch (choice) {
            case 1:
                cout << "Enter task name: ";
                getline(cin, taskName);
                myList.addTask(taskName);
                break;

            case 2:
                cout << "Enter task index to delete: ";
                cin >> taskIndex;
                myList.deleteTask(taskIndex - 1); // Index starts from 1
                break;

            case 3:
                myList.displayTasks();
                break;

            case 4:
                cout << "Enter task index to mark as completed: ";
                cin >> taskIndex;
                myList.markTaskCompleted(taskIndex - 1); // Index starts from 1
                break;

            case 5:
                cout << "Enter task index to mark as not completed: ";
                cin >> taskIndex;
                myList.markTaskNotCompleted(taskIndex - 1); // Index starts from 1
                break;

            case 6:
                cout << "Exiting the To-Do List app. Goodbye!" << endl;
                return 0;

            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
