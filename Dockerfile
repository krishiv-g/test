# Start with a lightweight Python base image.
FROM python:3.8-slim

# Set the working directory in the container.
WORKDIR /app

# Install Poetry.
# Ensure that no virtual environment is created by Poetry.
RUN pip install poetry && \
    poetry config virtualenvs.create false

# Copy only the required files to install dependencies.
COPY pyproject.toml poetry.lock ./

# Install the project dependencies.
# This uses the system python environment.
RUN poetry install

# Copy the rest of your application into the container.
COPY . .

# Specify the command to run your application.
# Assuming `main.py` is the entry script.
CMD ["python", "main.py"]
