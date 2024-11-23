# Use the official Python 3.11 image based on Alpine
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables (optional, adjust if needed)
ENV PYTHONUNBUFFERED 1

# Expose the port the app will run on (default is usually 8000)
EXPOSE 8000

# Command to run your application (adjust if necessary)
CMD ["python", "run.py"]
