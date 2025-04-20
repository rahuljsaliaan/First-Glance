# Start from an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Make sure Poetry is available in the PATH
ENV PATH="/root/.local/bin:$PATH"

# Install dependencies with Poetry
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-dev

# Copy the rest of the application code
COPY . /app/

# Expose the necessary port
EXPOSE 8000

# Command to run your app
CMD ["poetry", "run", "python", "app.py"]
