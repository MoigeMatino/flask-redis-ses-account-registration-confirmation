# Flask Redis AWS-SES Account Registration Confirmation
This project demonstrates how to build a Flask application to handle user registration and email confirmation using Redis Queue (RQ) for background job processing and Amazon Simple Email Service (SES) for sending emails. The application allows users to register, receive a confirmation email, and confirm their email address.

## Table of Contents

1. [Project Description](#project-description)
2. [Email confirmation Workflow](#email-confirmation-workflow)
3. [Features](#features)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Running the Application](#running-the-application)  
7. [Configuration](#configuration)

## Project Description
The application provides a simple user registration flow with email confirmation. It uses Redis Queue to handle the email sending process in the background, ensuring that the main application remains responsive. Amazon SES is used to send the confirmation emails, leveraging its reliability and scalability.

## Email Confirmation Workflow

1. **User Registration**:
    - User fills out the registration form with their email address and submits it.
    - The application creates a new user record in the database with a unique confirmation token and sets the email as unconfirmed.

2. **Sending Confirmation Email**:
    - The application enqueues a job to send a confirmation email to the user using Redis Queue.
    - A background worker processes the job and sends the email via Amazon SES.

3. **Email Confirmation**:
    - The user receives the email with a confirmation link.
    - The user clicks the confirmation link, which redirects to the application.
    - The application verifies the confirmation token and marks the email as confirmed.

## Features

- User registration with email confirmation
- Sending emails using Amazon SES
- Asynchronous email processing with Redis Queue

## Requirements

- Python 3.10+
- Flask
- Docker
- AWS account
- Amazon SES credentials

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:

    Using HTTPS:
    ```bash
    git clone https://github.com/yourusername/flask-redis-aws-registration-confirmation.git
    cd flask-redis-aws-registration-confirmation
    ```

    Using SSH:
    ```bash
    git clone git@github.com:yourusername/flask-redis-aws-registration-confirmation.git
    cd flask-redis-aws-registration-confirmation
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```
4. Set up your environment variables:
    Create a `.env` file in the project root and add the following variables:
    ```plaintext
    FLASK_DEBUG=1
    APP_SETTINGS=project.server.config.DevelopmentConfig
    
    SECRET_KEY=your_secret_key
    
    DATABASE_URL=db_url
    DATABASE_TEST_URL=test_db_url
    POSTGRES_USER=postgres_user
    POSTGRES_PASSWORD=postgres_password    
    
    REDIS_URL=redis://localhost:6379/0
    
    AWS_ACCESS_KEY=your_aws_access_key_id
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
    SES_REGION=your_aws_region
    SES_EMAIL_SOURCE=your_verified_email@example.com
    ```
## Running the Application

1. **Start the Flask application**:
   ```bash
   docker-compose up -d
   ```

2. **Setup database**:
    ```bash
   docker-compose exec users python manage.py create_db
   ```

3. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5003`.

## Configuration

Make sure to set up your AWS SES credentials and **verify** your sender email in the AWS SES console.
