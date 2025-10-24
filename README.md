# 🛍️ Galleria E-commerce Website

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Heroku-blue?style=for-the-badge&logo=heroku)](https://galleria-ecommerce.herokuapp.com/)
[![Django](https://img.shields.io/badge/Django-4.2+-green?style=for-the-badge&logo=django)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org/)

A modern, full-featured e-commerce platform built with Django, specializing in fashion and clothing. Galleria provides a seamless shopping experience with advanced features like real-time cart updates, wishlist functionality, and comprehensive order management.

## ✨ Features

### 🛒 Core E-commerce Features
- **Product Catalog**: Comprehensive product browsing with categories for Men's and Women's clothing
- **Smart Shopping Cart**: AJAX-powered cart with real-time price updates and quantity management
- **Wishlist**: Save favorite items for later purchase
- **Order Management**: Complete order tracking with status updates
- **User Authentication**: Secure registration and login system

### 🎨 User Experience
- **Responsive Design**: Mobile-first approach with Bootstrap and custom CSS
- **Product Filtering**: Advanced filtering and sorting capabilities
- **Product Ratings**: Customer rating system for products
- **Address Management**: Multiple shipping addresses per customer
- **Profile Management**: Comprehensive user profile system

### 🔧 Technical Features
- **Admin Panel**: Full Django admin integration for product and order management
- **Media Management**: Cloudinary integration for production image storage
- **Database**: SQLite for development, production-ready database support
- **Security**: Built-in Django security features and best practices

## 🚀 Live Demo

**Experience the full application**: [https://galleria-ecommerce.herokuapp.com/](https://galleria-ecommerce.herokuapp.com/)

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Django 4.2+, Python 3.8+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript, jQuery |
| **Database** | SQLite (Development), PostgreSQL (Production Ready) |
| **Media Storage** | Cloudinary API |
| **Deployment** | Heroku |
| **Additional** | AJAX, WhiteNoise, Pillow |

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Quick Start (Automated Setup)

```bash
# Clone the repository
git clone https://github.com/yourusername/galleria-ecommerce-website.git
cd galleria-ecommerce-website

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run automated setup script
python setup_local.py
```

### Manual Setup

1. **Clone and Setup Environment**
   ```bash
   git clone https://github.com/yourusername/galleria-ecommerce-website.git
   cd galleria-ecommerce-website
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Main Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
galleria-ecommerce-website/
├── app/                    # Main Django application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── forms.py           # Django forms
│   ├── urls.py            # URL routing
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS, images)
│   └── migrations/        # Database migrations
├── shoppinglyx/           # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
└── setup_local.py         # Automated setup script
```

## 🎯 Key Features Explained

### Product Management
- **Categories**: Organized by gender and product type (Shirts, T-shirts, Jeans, Shoes)
- **Pricing**: Support for both selling price and discounted price
- **Images**: High-quality product images with Cloudinary integration
- **Ratings**: Customer rating system for product quality assessment

### Shopping Experience
- **Real-time Cart**: AJAX-powered cart updates without page refresh
- **Wishlist**: Save items for future purchase
- **Order Tracking**: Complete order lifecycle management
- **Address Management**: Multiple shipping addresses per customer

### Admin Features
- **Product Management**: Add, edit, and manage products through Django admin
- **Order Management**: Track and update order status
- **Customer Management**: View and manage customer information
- **Analytics**: Basic sales and customer analytics

## 🔧 Configuration

### Environment Variables (Production)
```bash
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
CLOUDINARY_CLOUD_NAME=your-cloudinary-name
CLOUDINARY_API_KEY=your-cloudinary-key
CLOUDINARY_API_SECRET=your-cloudinary-secret
```

### Local Development
The project includes default configurations for local development. No additional setup required for basic functionality.

## 🚀 Deployment

### Heroku Deployment
1. Create a Heroku app
2. Set environment variables
3. Deploy using Git:
   ```bash
   git push heroku main
   ```

### Other Platforms
The application is compatible with any platform that supports Django:
- AWS Elastic Beanstalk
- DigitalOcean App Platform
- Railway
- Render

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abhishek Jaiswal**
- LinkedIn: [@abhishek-jaiswal-749b681a3](https://www.linkedin.com/in/abhishek-jaiswal-749b681a3/)
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive design components
- Cloudinary for media storage solutions
- All contributors who helped improve this project

## 📞 Support

If you have any questions or need help with the project, please:
- Open an issue on GitHub
- Contact the author via LinkedIn
- Check the [LOCAL_SETUP.md](LOCAL_SETUP.md) for detailed setup instructions

---

⭐ **Star this repository if you found it helpful!**
