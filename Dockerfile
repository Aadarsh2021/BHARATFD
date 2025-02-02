# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy everything before installing dependencies
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
