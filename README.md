
# myproject

Welcome to myproject! This project is a custom user authentication system built using Django's AbstractBaseUser and BaseUserManager classes.

## Overview

This project provides a custom user model called `CustomUser` that inherits from Django's `AbstractBaseUser` and `PermissionsMixin`. It also includes a custom manager `CustomUserManager` for user creation. The goal is to demonstrate how to create a custom user authentication system in Django.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/swastik0275/Project.git
   cd myproject

## Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

## Install project dependencies:
   ```bash
   pip install -r requirements.txt

## Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

## Run tests:
   ```bash
   python manage.py test

## Start the development server:
   ```bash
   python manage.py runserver