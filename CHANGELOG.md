# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-04

### Added
- ✨ Core task management: create, read, update, delete tasks
- 🏷️ Task priorities (High, Medium, Low)
- ⏰ Deadline tracking with countdown timers
- 🗂️ Task status system (Active, Completed, Deleted)
- ♻️ One-click restore from archive/trash
- 🤖 AI Assistant integration with Groq LLaMA API
- 💬 Real-time AI chat interface
- 📧 Email deadline reminders
- 👤 JWT-based authentication (login, register, refresh tokens)
- 🔍 Advanced filtering and sorting (by priority, date, status)
- 📱 Responsive single-page application (SPA)
- 🎨 Modern gradient UI with smooth transitions
- 📊 Tabbed interface for Active/Completed/Deleted tasks
- 🌐 REST API with DRF
- 🚀 Production-ready with WhiteNoise static file handling
- 📋 Comprehensive documentation and README
- 🔐 Security features (CSRF protection, secure cookies in production)

### Infrastructure
- Django 5.2 as web framework
- Django REST Framework for API
- SimpleJWT for JWT authentication
- Celery + Redis for background tasks (optional)
- PostgreSQL support (with SQLite fallback)
- Gunicorn WSGI server
- Render deployment ready

## [Unreleased]

### Planned
- [ ] Dark mode toggle
- [ ] Recurring tasks
- [ ] Shared task lists
- [ ] Email digest summaries
- [ ] Mobile app (React Native)
- [ ] Task templates
- [ ] Advanced filtering (tags, search)
- [ ] Calendar view
- [ ] Push notifications
- [ ] WebSocket real-time updates
- [ ] Task dependencies
- [ ] Estimated time tracking
- [ ] Pomodoro timer integration
- [ ] Bulk operations

---

**Release Date**: December 4, 2025
**Version**: 1.0.0
**Status**: Stable
