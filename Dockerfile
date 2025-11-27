FROM python:3.11-slim

WORKDIR /app

# Install dependencies

COPY requirements/base.txt ./base.txt
RUN pip install --no-cache-dir -r base.txt


# Copy Application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]