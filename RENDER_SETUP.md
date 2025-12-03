# Render Deployment Instructions

## Quick Setup Steps

### 1. Update Web Service Start Command (Critical!)

**In Render Dashboard:**
1. Go to your Web Service
2. Click **Settings** (gear icon) in top right
3. Find **Start Command** field
4. Replace everything with:
   ```
   gunicorn todo.wsgi:application --bind 0.0.0.0:$PORT
   ```
5. Click **Save Changes**
6. Click **Redeploy** button

### 2. Verify Environment Variables

In **Environment** section, ensure these are set:
```
SECRET_KEY=<your-secret-key>
DEBUG=0
ALLOWED_HOSTS=<your-app-name>.onrender.com
GROQ_API_KEY=<your-groq-api-key>
```

### 3. Generate SECRET_KEY (if needed)

Run this locally and copy the output:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Or use: https://djecrety.ir/

### 4. Monitor Deployment

After Redeploy:
1. Go to **Logs** tab
2. Watch for:
   - `==> Starting gunicorn...`
   - `==> Build successful`
   - Eventually `==> Listening on 0.0.0.0:PORT`

### Troubleshooting

**If still seeing "ModuleNotFoundError: No module named 'app'":**
- Double-check Start Command is correctly set (copy-paste from above)
- Make sure no extra spaces or typos
- Click Redeploy again after saving

**If migrations fail:**
- Check `DEBUG=0` is set in Environment
- Verify `SECRET_KEY` is not empty
- Check database URL if using PostgreSQL

**If static files not loading:**
- `collectstatic` should run in the release command
- Check Procfile `release:` line is correct

## Expected URLs After Successful Deploy

- **Main app**: `https://<your-app-name>.onrender.com/`
- **Admin**: `https://<your-app-name>.onrender.com/admin/`
- **API**: `https://<your-app-name>.onrender.com/api/`

---

**The key issue:** Render UI defaults to `gunicorn app:app` which doesn't work for Django.
We need `gunicorn todo.wsgi:application` (or with `--bind` for port binding).
