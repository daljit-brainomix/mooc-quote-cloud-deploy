# Use the official lightweight Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy your Python script into the container
COPY quote_of_the_day.py .

# Install required packages
RUN pip install --no-cache-dir requests

# Run the script
CMD ["python", "quote_of_the_day.py"]
