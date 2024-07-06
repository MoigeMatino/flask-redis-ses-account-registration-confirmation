# Flask Redis AWS Account Registration Confirmation

This repository demonstrates how to build a Flask application to send confirmation emails using Amazon Simple Email Service (SES) and Redis Queue (RQ). The project includes a complete workflow for client/server email confirmation.

## Features

- User registration with email confirmation
- Sending emails using Amazon SES
- Asynchronous email processing with Redis Queue
- Simple and clean project structure

## Requirements

- Python 3.10+
- Flask
- Docker
- Redis
- Amazon SES credentials

## Installation

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

    ```sh
    export FLASK_APP=app.py
    export FLASK_ENV=development
    export AWS_ACCESS_KEY_ID=your-access-key-id
    export AWS_SECRET_ACCESS_KEY=your-secret-access-key
    export AWS_REGION=your-aws-region
    export REDIS_URL=redis://localhost:6379/0
    ```
## Configuration

Make sure to set up your AWS SES credentials and verify your sender email in the AWS SES console.

## Client/Server Email Confirmation Workflow

1. **User Registration**: The user fills out the registration form and submits it.
2. **Email Queue**: The server adds the email confirmation task to the Redis queue.
3. **Email Sending**: The Redis worker picks up the task and sends a confirmation email using Amazon SES.
4. **Email Confirmation**: The user receives the email and clicks on the confirmation link.
5. **Account Activation**: The server processes the confirmation link and activates the user's account.


