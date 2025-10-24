# Galleria E-commerce Website - Local Development Setup

This is a Django-based e-commerce website for clothing and accessories.

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Run setup script
python setup_local.py
```

### Option 2: Manual Setup

1. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables** (Optional - defaults are provided)
   ```bash
   export SECRET_KEY="django-insecure-local-development-key-change-in-production"
   export DEBUG="True"
   ```

4. **Setup Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

## Access Points

- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Default credentials: `admin` / `admin123` (if using automated setup)

## Features

- User registration and authentication
- Product catalog (Men's and Women's clothing)
- Shopping cart functionality
- Wishlist feature
- Order management
- Customer profiles and addresses
- Payment integration (basic)

## Project Structure

- `app/` - Main Django application
- `shoppinglyx/` - Django project settings
- `media/` - User uploaded files
- `static/` - Static files (CSS, JS, images)

## Database

The project uses SQLite for local development. The database file is `db.sqlite3`.

## Notes

- The project was originally configured for Heroku deployment with Cloudinary for image storage
- For local development, it falls back to local file storage
- Email functionality is configured but may require proper SMTP settings for production use
- All environment variables have default values for local development

## Troubleshooting

1. **Import Errors**: Make sure all dependencies are installed
2. **Database Errors**: Run migrations if you encounter database-related errors
3. **Static Files**: The project uses WhiteNoise for static file serving
4. **Media Files**: Images are served from the `media/` directory in development

## Original Configuration

This project was originally deployed on Heroku with:
- Cloudinary for image storage
- Environment variables for sensitive data
- Production-ready settings

For production deployment, make sure to:
- Set proper environment variables
- Use a production database
- Configure proper static file serving
- Set DEBUG=False
