FROM python:3.11-bookworm

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# RUN apt update && apt install gunicorn -y

# Copy the source code into the container.
COPY . .

# Install project packages
RUN pip install -r requirements.txt

# Giving executable access to entrypoint.sh
RUN chmod +x entrypoint.sh

# Expose the port that the application listens on.
EXPOSE 8001
