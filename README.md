# Todo App with AI Assistant

A modern Django REST API todo application with task management, AI-powered suggestions, deadline reminders, and smart archiving. Built with Django, Django REST Framework, and integrated with Groq's AI API.

![Django](https://img.shields.io/badge/Django-5.2+-green)
![Python](https://img.shields.io/badge/Python-3.13+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

✨ **Core Task Management**
- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Priority levels: High, Medium, Low
- Deadline tracking with countdown reminders
- Task status tracking: Active, Completed, Deleted
- One-click restore from archive or trash

🤖 **AI Assistant**
- Integrated with Groq's LLaMA API
- Ask questions and get instant answers
- Chat interface directly in the app
- Context-aware AI suggestions

📧 **Smart Reminders**
- Email notifications for upcoming deadlines
- Configurable reminder triggers
- Celery task scheduling (optional)
- Manual deadline check endpoint

👤 **Authentication & Authorization**
- JWT-based authentication (SimpleJWT)
- User registration and login
- Secure token refresh mechanism
- Per-user task isolation

🎨 **Modern UI**
- Single-page application (SPA) with vanilla JavaScript
- Responsive design (works on desktop, tablet, mobile)
- Real-time filter and sort controls
- Tabbed interface for Active/Completed/Deleted tasks
- Beautiful gradient design with smooth transitions

## Tech Stack

- **Backend**: Django 5.2, Django REST Framework
- **Authentication**: Django Simple JWT
- **Database**: SQLite (dev), PostgreSQL (production)
- **Background Tasks**: Celery + Redis (optional)
- **AI Integration**: Groq API (LLaMA 3.1)
- **Static Files**: WhiteNoise
- **Deployment**: Render, Gunicorn
- **Frontend**: Vanilla JavaScript (no framework needed)

## Installation

### Prerequisites
- Python 3.13+
- pip and virtualenv
- Redis (optional, for Celery)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and set your values
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` in your browser.

## Configuration

### Environment Variables

Create a `.env` file or set these in your system:

```bash
# Django settings
SECRET_KEY=your-super-secret-key-here
DEBUG=1                              # 0 for production
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional, uses SQLite if not set)
DATABASE_URL=postgresql://user:password@localhost/todoapp

# Groq API
GROQ_API_KEY=your-groq-api-key-here

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security (production only)
CSRF_TRUSTED_ORIGINS=https://yourdomain.com
```

### Generate SECRET_KEY

Use Django's utility:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use an online generator: https://djecrety.ir/

## Usage

### API Endpoints

#### Authentication
- `POST /api/users/register/` - Create new account
- `POST /api/users/login/` - Get JWT tokens
- `POST /api/users/refresh/` - Refresh access token

#### Tasks
- `GET /api/tasks/` - List user's tasks (with filters)
  - Query params: `status=active|completed|deleted`, `priority=1|2|3`, `ordering=-created_at`
- `POST /api/tasks/` - Create new task
- `GET /api/tasks/{id}/` - Get task details
- `PATCH /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Soft-delete task (marks as deleted)
- `POST /api/tasks/{id}/restore/` - Restore task from archive/trash
- `POST /api/tasks/check-deadlines/` - Manually trigger deadline check

#### AI Assistant
- `GET /api/ai/ask/?q=your-question` - Ask AI a question

### Task Status Flow

```
Active → (Mark Complete) → Completed
Active → (Delete) → Deleted
Completed → (Restore) → Active
Deleted → (Restore) → Active
Completed → (Delete Permanently) → Deleted
```

### Example API Usage

**Register & Login**
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password123",
    "password2": "secure_password123"
  }'

curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "secure_password123"
  }'
```

**Create Task with Deadline**
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project report",
    "description": "Finish Q4 report and submit",
    "priority": 3,
    "deadline": "2025-12-10T17:00:00Z"
  }'
```

**Get AI Answer**
```bash
curl "http://localhost:8000/api/ai/ask/?q=How%20do%20I%20manage%20tasks%20effectively"
```

## Deployment

### Deploy to Render

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Create Render Web Service**
   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Fill in:
     - **Name**: `todo-app`
     - **Build command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start command**: `gunicorn todo.wsgi:application`
     - **Plan**: Free

3. **Add Environment Variables** (in Render dashboard)
   ```
   SECRET_KEY=<generate-new-key>
   DEBUG=0
   ALLOWED_HOSTS=<your-app-name>.onrender.com
   GROQ_API_KEY=<your-groq-api-key>
   ```

4. **Add PostgreSQL** (optional but recommended)
   - Click "Database" → "PostgreSQL"
   - Render will automatically add `DATABASE_URL`

5. **Deploy**
   - Click "Deploy" button
   - Monitor logs in the dashboard

### Deploy to Other Platforms

- **Heroku**: Use `Procfile` and set config vars (note: Heroku free tier ended)
- **Railway**: Similar to Render, connect GitHub and add env vars
- **PythonAnywhere**: Upload code via web UI or git
- **DigitalOcean**: Use App Platform with Procfile and environment variables

## Development

### Project Structure
```
todo/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
├── .env.example
├── .gitignore
├── db.sqlite3
├── todo/                    # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── task/                    # Task app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tasks.py            # Celery tasks
│   └── templates/
│       └── index.html      # Frontend SPA
├── users/                   # User authentication
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── ai/                      # AI assistant
│   ├── views.py
│   └── urls.py
└── static/                  # Static files (CSS, JS, images)
```

### Running Tests
```bash
python manage.py test
```

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --plan          # Preview migrations
```

### Celery (Optional - for background tasks)
```bash
# Start Celery worker
celery -A todo worker -l info

# Start Celery beat scheduler
celery -A todo beat -l info
```

## API Documentation

Full API documentation is available at `/api/` endpoint (Django REST Framework Browsable API).

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Security Notes

⚠️ **Important for Production:**
1. Set `DEBUG=0` in production
2. Generate a strong `SECRET_KEY`
3. Set `ALLOWED_HOSTS` to your domain
4. Use HTTPS only (`SECURE_SSL_REDIRECT=True`)
5. Keep dependencies updated: `pip list --outdated`
6. Store secrets in environment variables, never in code
7. Enable CORS only for trusted domains if using separate frontend

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Database Issues
```bash
# Reset database (dev only!)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

### Migration Conflicts
```bash
python manage.py showmigrations task
python manage.py migrate task --plan
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Built with [Django](https://www.djangoproject.com/)
- AI powered by [Groq](https://www.groq.com/)
- Deployed on [Render](https://render.com/)

## Contact & Support

- 📧 Email: your-email@example.com
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)
- 💬 Issues: [GitHub Issues](https://github.com/yourusername/todo-app/issues)

## Roadmap

- [ ] Dark mode toggle
- [ ] Recurring tasks
- [ ] Shared task lists
- [ ] Email digest summaries
- [ ] Mobile app (React Native)
- [ ] Task templates
- [ ] Advanced filtering (tags, search)
- [ ] Calendar view
- [ ] Notifications (push, SMS)
- [ ] WebSocket real-time updates

---

**Made with ❤️ by Your Name**

Last updated: December 4, 2025
