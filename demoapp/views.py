
from django.http import HttpResponse

def home(request):
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Demo Homepage</title>
        <style>
          body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }
          .wrap { max-width: 960px; margin: 0 auto; padding: 48px 24px; }
          header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
          .logo { font-weight: 700; letter-spacing: 0.5px; }
          a.btn { display: inline-block; padding: 10px 16px; border-radius: 8px; color: #0f172a; background: #38bdf8; text-decoration: none; font-weight: 600; }
          .hero { background: #111827; border-radius: 16px; padding: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
          .hero h1 { margin: 0 0 12px; font-size: 28px; }
          .hero p { margin: 0 0 20px; color: #cbd5e1; }
          footer { margin-top: 40px; color: #94a3b8; font-size: 14px; }
        </style>
      </head>
      <body>
        <div class="wrap">
          <header>
            <span class="logo">My Django Demo</span>
            <a class="btn" href="https://docs.djangoproject.com/" target="_blank" rel="noopeneron class="hero">
            <h1>Welcome to the Demo App</h1>
            <p>Managed by <strong>Azure Kubernetes Fleet Manager</strong>.</p>
            <p>This is a simple homepage served by Django.</p>
            <a class="btn" href    </section>
          <footer>
            Powered by Django • Azure Kubernetes Fleet Manager Demo
          </footer>
        </div>
      </body>
    </html>
    """
    return HttpResponse(html)
