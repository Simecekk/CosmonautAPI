# FastAPI Cosmonaut Registration App :rocket:

This FastAPI Python project is designed to manage the registration of cosmonauts, providing a robust REST API for Create, Read, Update, and Delete (CRUD) operations on cosmonaut records. Additionally, it supports retrieval of a limited number of cosmonauts.

## Features

- **Cosmonaut Management**: Add, update, retrieve, and delete cosmonaut records.
- **Database Integration**: Utilizes a database for persistent storage of cosmonaut information.
- **RabbitMQ Integration**: Implements an import functionality to consume messages from a RabbitMQ queue. The application is designed to handle a high throughput of messages, with the capacity to process thousands of messages per second.

## Getting Started

To start using this project, follow these steps:


1. **Set up Environment Variables**:
- Copy the `.env.sample` file to `.env` and fill in the necessary environment variables.

2. **Start RabbitMQ**:
- Ensure RabbitMQ is installed and running.

3. **Install Dependencies**:
- `pip install -r requirements.txt`

4. **Run the Application**:
- ```bash
  uvicorn main:app --reload
  ```

## RabbitMQ Speed Test

To evaluate the import speed of this application, a script named `rabbitmq_speed_test.py` is provided. This script is designed to simulate a high message throughput scenario by pushing thousands of messages into the RabbitMQ queue. This allows you to assess the performance of the application in handling a large volume of incoming data.

### Usage

To run the speed test script, follow these steps:

1. Ensure that RabbitMQ is running and accessible.
2. Open a terminal window and navigate to the project directory.
3. Execute the script with the following command:

```bash
python rabbitmq_speed_test.py 
```

## Next Steps

To further enhance and optimize the project, consider implementing the following:

1. **Implement Linting and Typing**:
   - Integrate a linter (e.g., Flake8) to enforce consistent code style and catch potential errors early. Utilize type annotations to enhance code clarity and enable better static analysis.

2. **Implement Unit Tests**:
   - Develop a comprehensive suite of unit tests to validate the functionality of different components of the application. This will help ensure robustness and facilitate future development.

3. **Explore Async Approach to DB Communication**:
   - Investigate the feasibility of utilizing asynchronous programming techniques for database communication. Note that the `databases` package has downgraded SQLAlchemy from v2 to v1.4.

4. **Evaluate Alternatives to aiormq**:
   - Research and test alternative libraries for RabbitMQ communication to identify potential performance improvements or additional features.

These steps will contribute to the overall quality, maintainability, and performance of the project.

## License

This project is licensed under the [MIT License](LICENSE).
