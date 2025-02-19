# Use the official Python base image
FROM python:3.10-slim

# Ensure stdout and stderr are displayed immediately
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Update package list and install postgresql-client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv .venv

# Add the virtual environment's bin directory to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Install required packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Copy entrypoint script and ensure it has execute permissions
COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# Use an entrypoint script to ensure Django is created **after** the container starts
ENTRYPOINT ["/app/entrypoint.sh"]
