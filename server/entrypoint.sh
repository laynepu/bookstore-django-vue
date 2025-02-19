#!/bin/sh

# Print Python path and version
echo "Checking Python environment..."
which python
python --version

# Print Django version
echo "Checking Django version..."
python -m django --version

# Check if manage.py exists, if not, create a Django project
if [ ! -f "/app/manage.py" ]; then
    echo "Django project not found, creating one..."
    django-admin startproject backend /app
fi

# Define the secrets file location
SECRETS_FILE="/app/config/.env.secrets"

# Ensure the config directory exists
mkdir -p "$(dirname "$SECRETS_FILE")"

# Ensure the secrets file exists
if [ ! -f "$SECRETS_FILE" ]; then
  touch "$SECRETS_FILE"
fi

# Check if SECRET_KEY is already set in the environment or in the secrets file.
# If not, generate or load it.
if [ -z "${SECRET_KEY:-}" ]; then  # Check if SECRET_KEY is empty in env
  SECRET_KEY=$(awk -F'=' '/^SECRET_KEY=/{print substr($0, index($0,$2))}' "$SECRETS_FILE") # Try to load from file
  if [ -z "$SECRET_KEY" ]; then # if still empty after trying the file
    SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(50))") # generate a new secret
    printf 'SECRET_KEY=%s\n' "$SECRET_KEY" >> "$SECRETS_FILE" # save to file
    log_message="Generated and stored SECRET_KEY in $SECRETS_FILE" # Log message
  else
    log_message="Loaded SECRET_KEY from $SECRETS_FILE" #Log message
  fi
  export SECRET_KEY # export no matter if generated or loaded
else
  log_message="SECRET_KEY already set in the environment." #Log message
fi

# Conditionally log the message in debug mode
if [ "${DEBUG:-false}" = "true" ]; then
  echo "[entrypoint.sh] $log_message"
fi

# Run database migrations and start the Django server
python manage.py migrate

exec python manage.py runserver 0.0.0.0:8000