# Railway Deployment Quick Guide

## 🚀 One-Click Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

## Step-by-Step Deployment

### 1. Prepare Your Repository

This repository is already configured with:
- ✅ `railway.toml` - Railway configuration
- ✅ `nixpacks.toml` - Build configuration
- ✅ `.env.example` - Environment template
- ✅ Health check endpoint at `/health`
- ✅ Python 3.11 support

### 2. Deploy to Railway

**Option A: From GitHub**

1. Push this repository to GitHub
2. Go to [Railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Railway will auto-detect the configuration

**Option B: Using Railway CLI**

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link to project (first time)
railway init

# Deploy
railway up
```

### 3. Configure Environment Variables

In Railway dashboard:

1. Click on your deployed service
2. Navigate to **Variables** tab
3. Add the following:

```
OPENAI_API_KEY=sk-...your-key-here
```

### 4. Verify Deployment

Once deployed, Railway will provide a URL like:
```
https://your-service.up.railway.app
```

Test the endpoints:

```bash
# Health check
curl https://your-service.up.railway.app/health

# API docs
open https://your-service.up.railway.app/docs

# Orchestrate endpoint
curl -X POST https://your-service.up.railway.app/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"instruction": "Create a plan for a web application"}'
```

## Configuration Files Explained

### railway.toml
Defines how Railway should deploy and run your service:
- Health check path: `/health`
- Restart policy: `ON_FAILURE`
- Start command: Runs uvicorn with FastAPI

### nixpacks.toml
Configures the build process:
- Python 3.11 installation
- Dependencies from `requirements.txt`
- Correct working directory setup

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | ✅ Yes | Your OpenAI API key |
| `PORT` | ⚙️ Auto | Set by Railway (default: 8080) |
| `PYTHONUNBUFFERED` | ⚙️ Auto | Set to 1 for logging |

## Monitoring & Logs

### View Logs
```bash
# Using Railway CLI
railway logs

# Or in Railway Dashboard
Project → Service → Deployments → View Logs
```

### Health Monitoring
Railway automatically monitors the `/health` endpoint:
- Response time
- Uptime status
- Auto-restart on failures

## Troubleshooting

### Build Fails

**Issue:** Dependencies not installing
```bash
# Solution: Check requirements.txt exists in prompt-orchestrator/
ls prompt-orchestrator/requirements.txt
```

**Issue:** Python version mismatch
```bash
# Solution: Verify nixpacks.toml specifies python311
cat nixpacks.toml
```

### Runtime Errors

**Issue:** `OPENAI_API_KEY not found`
- Go to Railway Variables tab
- Add `OPENAI_API_KEY`
- Redeploy

**Issue:** Port binding errors
- Railway sets `PORT` automatically
- Verify start command uses `${PORT:-8080}`

**Issue:** Health check failing
- Check `/health` endpoint is accessible
- Review logs for startup errors
- Ensure uvicorn is binding to `0.0.0.0`

### Performance Issues

**Issue:** Slow response times
- Check OpenAI API quota/limits
- Review Railway metrics for CPU/memory
- Consider upgrading Railway plan

## Railway Features Used

- ✅ **Nixpacks** - Automatic build detection
- ✅ **Health Checks** - Auto-restart on failure
- ✅ **Auto-deployment** - Deploy on git push
- ✅ **Environment Variables** - Secure config management
- ✅ **Logging** - Centralized log aggregation
- ✅ **Metrics** - CPU, memory, network monitoring

## Scaling

Railway supports horizontal and vertical scaling:

```bash
# View current resources
railway status

# Scale vertically (requires Railway Pro)
# Configure in Railway Dashboard → Settings → Resources
```

## Custom Domain

1. Go to Railway Dashboard
2. Select your service
3. Click "Settings" → "Domains"
4. Add your custom domain
5. Configure DNS records as instructed

## CI/CD

Railway auto-deploys on git push:

1. Make changes locally
2. Commit and push to GitHub
3. Railway automatically builds and deploys
4. Monitor deployment in Railway dashboard

## Cost Optimization

- Start with Railway's free tier ($5 credit)
- Monitor usage in billing dashboard
- Optimize API calls to OpenAI
- Consider caching responses
- Use environment-based rate limiting

## Support

- 📚 [Railway Docs](https://docs.railway.app)
- 💬 [Railway Discord](https://discord.gg/railway)
- 🐛 [Report Issues](https://github.com/railwayapp/railway/issues)

## Next Steps

1. ✅ Deploy to Railway
2. ✅ Set environment variables
3. ✅ Test endpoints
4. 📊 Monitor logs and metrics
5. 🔒 Set up custom domain (optional)
6. 📈 Scale as needed
