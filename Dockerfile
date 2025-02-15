FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
# Previously, only app.py was copied. Now, we're copying the entire directory containing app.py and tasksA.py.
COPY . /app

# Expose port 8000
EXPOSE 8000

# Explicitly set the correct binary path and use `sh -c` to run the FastAPI app
CMD ["/root/.local/bin/uv", "run", "app.py"]