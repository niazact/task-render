#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

echo "=== Starting Django Deployment Build ==="

# Install dependencies
echo "Step 1: Installing Python dependencies..."
pip install -r requirements.txt

# Verify database connection
echo "Step 2: Checking database configuration..."
if [ -z "${DATABASE_URL:-}" ]; then
    echo "ERROR: DATABASE_URL environment variable is not set!"
    exit 1
fi

# Run migrations
echo "Step 3: Running database migrations..."
python manage.py migrate --no-input

# Collect static files
echo "Step 4: Collecting static files..."
python manage.py collectstatic --noinput --clear

# Optional: Create superuser (remove in production)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

echo "=== Build completed successfully! ==="