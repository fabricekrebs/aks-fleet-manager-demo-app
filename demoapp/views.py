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
        * { box-sizing: border-box; }
        body { 
            font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; 
            margin: 0; 
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
            color: #e2e8f0; 
            min-height: 100vh;
        }
        .wrap { 
            max-width: 960px; 
            margin: 0 auto; 
            padding: 48px 24px; 
        }
        header { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            margin-bottom: 48px; 
        }
        .logo { 
            font-weight: 800; 
            font-size: 1.5rem; 
            letter-spacing: -0.025em;
            background: linear-gradient(135deg, #38bdf8, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .btn { 
            display: inline-block; 
            padding: 12px 24px; 
            border-radius: 12px; 
            color: #0f172a; 
            background: linear-gradient(135deg, #38bdf8, #0ea5e9); 
            text-decoration: none; 
            font-weight: 600; 
            font-size: 0.95rem;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        }
        .btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.5);
        }
        .hero { 
            background: rgba(17, 24, 39, 0.8); 
            backdrop-filter: blur(16px);
            border-radius: 24px; 
            padding: 48px; 
            box-shadow: 0 25px 50px rgba(0,0,0,0.25);
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
        }
        .hero h1 { 
            margin: 0 0 16px; 
            font-size: clamp(2.5rem, 6vw, 4rem); 
            font-weight: 800;
            line-height: 1.1;
            background: linear-gradient(135deg, #f8fafc, #e2e8f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .hero p { 
            margin: 0 0 24px; 
            color: #cbd5e1; 
            font-size: 1.25rem;
            line-height: 1.6;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        .hero .highlight {
            color: #38bdf8;
            font-weight: 600;
        }
        footer { 
            margin-top: 64px; 
            color: #94a3b8; 
            font-size: 0.875rem; 
            text-align: center;
            opacity: 0.8;
        }
        @media (max-width: 768px) {
            .wrap { padding: 32px 16px; }
            header { flex-direction: column; gap: 20px; text-align: center; }
            .hero { padding: 32px 24px; margin-top: 20px; }
        }
    </style>
</head>
<body>
    <div class="wrap">
        <header>
            <span class="logo">My Django Demo</span>
            <a class="btn" href="https://docs.djangoproject.com/" target="_blank" rel="noopener">Django Docs</a>
        </header>
        
        <section class="hero">
            <h1>Welcome to the Demo App</h1>
            <p>Managed by <span class="highlight">Azure Kubernetes Fleet Manager</span>.</p>
            <p>This is a simple homepage served by Django running on Kubernetes. Fully self-contained in a single view!</p>
            <a class="btn" href="https://azure.microsoft.com/" target="_blank" rel="noopener">Learn about Azure</a>
        </section>
        
        <footer>
            Powered by Django • Azure Kubernetes Fleet Manager Demo • 2025
        </footer>
    </div>
</body>
</html>
    """
    return HttpResponse(html)
