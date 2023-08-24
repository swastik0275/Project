# MyProject

Welcome to **MyProject**! This project showcases a custom user authentication system developed using Django's `AbstractBaseUser` and `BaseUserManager` classes.

## Overview

**MyProject** introduces a personalized user model named `CustomUser`, inheriting attributes from both `AbstractBaseUser` and `PermissionsMixin`. Additionally, a specialized manager, `CustomUserManager`, is included for streamlined user creation. The primary aim is to provide a comprehensive example of creating a custom user authentication system using Django.

## Installation

Follow these steps to set up and run **MyProject** on your local environment:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/swastik0275/Project.git
    cd myproject
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run tests:**

    ```bash
    python manage.py test
    ```

6. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

To effectively utilize the **MyProject** custom user authentication system, follow these guidelines:

1. **Customize `CustomUser` Model:**
    Adjust the `CustomUser` model in the `models.py` file according to your project's requirements. You can include additional fields, methods, or properties as necessary.

2. **Authentication Configuration:**
    In your project's settings, configure the `AUTH_USER_MODEL` to point to the `CustomUser` model. This ensures that your customized user model is used throughout the authentication system.

3. **Creating Users:**
    Utilize the `CustomUserManager` to create new user instances. This manager provides convenient methods for user creation while considering security and data integrity.

4. **Permissions and Authorization:**
    Leverage the `PermissionsMixin` attributes to manage user permissions and authorization. Define permissions based on your application's needs.

## Contributing

We welcome contributions to enhance **MyProject**! If you find bugs, have suggestions for improvements, or would like to add new features, please feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/swastik0275/Project).

