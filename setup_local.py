#!/usr/bin/env python
"""
Setup script for local development of Galleria E-commerce Website
Run this script to set up the project for local development
"""

import os
import sys
import subprocess
import django
from django.core.management import execute_from_command_line

def setup_environment():
    """Set up environment variables for local development"""
    print("Setting up environment variables for local development...")
    
    # Set default environment variables if not already set
    env_vars = {
        'SECRET_KEY': 'django-insecure-local-development-key-change-in-production',
        'DEBUG': 'True',
        'EMAIL_HOST_PASSWORD': '',
        'API_KEY': '',
        'API_SECRET': ''
    }
    
    for key, value in env_vars.items():
        if key not in os.environ:
            os.environ[key] = value
            print(f"Set {key} = {value}")

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        # Check if we're in a virtual environment
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("Virtual environment detected")
        else:
            print("WARNING: Not in a virtual environment. Consider creating one with: python3 -m venv venv")
        
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False
    return True

def setup_database():
    """Set up the database"""
    print("Setting up database...")
    try:
        # Set Django settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoppinglyx.settings')
        
        # Setup Django
        django.setup()
        
        # Run migrations
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("Database setup completed!")
        return True
    except Exception as e:
        print(f"Error setting up database: {e}")
        return False

def create_superuser():
    """Create a superuser for admin access"""
    print("Creating superuser...")
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("Superuser created: username='admin', password='admin123'")
        else:
            print("Superuser already exists")
        return True
    except Exception as e:
        print(f"Error creating superuser: {e}")
        return False

def main():
    """Main setup function"""
    print("=== Galleria E-commerce Website Local Setup ===")
    print()
    
    # Setup environment
    setup_environment()
    print()
    
    # Install requirements
    if not install_requirements():
        print("Failed to install requirements. Please check your Python environment.")
        return
    print()
    
    # Setup database
    if not setup_database():
        print("Failed to setup database. Please check your Django configuration.")
        return
    print()
    
    # Create superuser
    create_superuser()
    print()
    
    print("=== Setup Complete! ===")
    print()
    print("To start the development server, run:")
    print("source venv/bin/activate  # Activate virtual environment")
    print("python manage.py runserver")
    print()
    print("Or if you're already in the virtual environment:")
    print("python manage.py runserver")
    print()
    print("Admin access:")
    print("URL: http://127.0.0.1:8000/admin/")
    print("Username: admin")
    print("Password: admin123")
    print()
    print("Main site: http://127.0.0.1:8000/")
    print()
    print("Note: Make sure to activate the virtual environment before running the server!")

if __name__ == '__main__':
    main()
