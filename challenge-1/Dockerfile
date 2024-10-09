# Use a minimal Python base image
FROM python:alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set working directory
WORKDIR /app

# Copy the current directory content into the container
COPY index.py /app

# Install necessary dependencies (if any)
# RUN pip install --no-cache-dir -r requirements.txt || true

# Change ownership of the working directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose default port (8000)
EXPOSE 8000

# Default command to run the Python server
ENTRYPOINT ["python3", "index.py"]

