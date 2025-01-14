# To Do List Application

## Description
This is a task management application built using Django. It allows users to create, edit, and delete tasks. The application includes user authentication, ensuring that each user can manage their own tasks securely.

## Features
- **User Authentication**: Users can sign up, log in, and log out.
- **Task Management**: Users can create, edit, and delete tasks.
- **User-Specific Data**: Tasks are associated with individual users, ensuring privacy and organization.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-list.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-list
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and navigate to `http://localhost:8000` to access the application.

## Usage Instructions
1. **Sign Up**: Create a new account by providing a username, email, and password.
2. **Log In**: Use your credentials to log in to the application.
3. **Manage Tasks**:
   - **Add Task**: Enter a task title and click "Add Task".
   - **Edit Task**: Click the edit icon to modify a task's title.
   - **Delete Task**: Click the delete icon to remove a task.
4. **Log Out**: Click the logout icon to securely log out of the application.

## Screenshots
![Signup Page](static/js/Screenshot (24).png)
![Login Page](static/js/Screenshot (25).png)
![Todo Page](static/js/Screenshot (26).png)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
