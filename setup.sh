#!/usr/bin/env bash
set -e

# Base app directory
BASE_DIR="app"

# List of directories to create
DIRS=(
  "${BASE_DIR}"
  "${BASE_DIR}/core"
  "${BASE_DIR}/db"
  "${BASE_DIR}/schemas"
  "${BASE_DIR}/repositories"
  "${BASE_DIR}/services"
  "${BASE_DIR}/routers"
  "${BASE_DIR}/ai"
)

# Create directories (with -p to avoid errors if they exist) :contentReference[oaicite:0]{index=0}
for dir in "${DIRS[@]}"; do
  mkdir -p "$dir"
done

# List of files to create
FILES=(
  "${BASE_DIR}/main.py"
  "${BASE_DIR}/core/config.py"
  "${BASE_DIR}/core/dependencies.py"
  "${BASE_DIR}/db/database.py"
  "${BASE_DIR}/db/models.py"
  "${BASE_DIR}/schemas/calculator.py"
  "${BASE_DIR}/repositories/calculator_repo.py"
  "${BASE_DIR}/services/calculator_service.py"
  "${BASE_DIR}/routers/calculator.py"
  "${BASE_DIR}/ai/llm_client.py"
  ".env"
  "alembic.ini"
)

# Create files (touch is safe even if file exists) :contentReference[oaicite:1]{index=1}
for file in "${FILES[@]}"; do
  touch "$file"
done

echo "Project structure created successfully."
