def greet(name):
    return f"Hello, {name}!"

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fizah Iman | DevOps Project</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container {
            text-align: center;
            padding: 40px;
            max-width: 800px;
        }
        .badge {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 50px;
            padding: 8px 20px;
            font-size: 14px;
            display: inline-block;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }
        h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 15px;
            background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            font-size: 18px;
            color: rgba(255,255,255,0.7);
            margin-bottom: 40px;
        }
        .cards {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }
        .card {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 16px;
            padding: 25px 30px;
            backdrop-filter: blur(10px);
            transition: transform 0.3s;
            min-width: 180px;
        }
        .card:hover { transform: translateY(-5px); }
        .card .icon { font-size: 36px; margin-bottom: 10px; }
        .card h3 { font-size: 16px; font-weight: 600; margin-bottom: 5px; }
        .card p { font-size: 13px; color: rgba(255,255,255,0.6); }
        .pipeline {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 30px;
        }
        .pipeline h2 {
            font-size: 18px;
            margin-bottom: 20px;
            color: rgba(255,255,255,0.9);
        }
        .steps {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .step {
            background: linear-gradient(135deg, #a78bfa33, #60a5fa33);
            border: 1px solid rgba(167,139,250,0.4);
            border-radius: 10px;
            padding: 10px 16px;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .arrow { color: rgba(255,255,255,0.4); font-size: 20px; }
        .live-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(52, 211, 153, 0.15);
            border: 1px solid rgba(52, 211, 153, 0.4);
            border-radius: 50px;
            padding: 10px 24px;
            font-size: 15px;
            color: #34d399;
        }
        .dot {
            width: 8px; height: 8px;
            background: #34d399;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.3); }
        }
        .footer {
            margin-top: 30px;
            font-size: 13px;
            color: rgba(255,255,255,0.4);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">🚀 DevOps Internship Project</div>
        <h1>Fizah Iman</h1>
        <p class="subtitle">Full-Stack • Game • App Developer</p>

        <div class="cards">
            <div class="card">
                <div class="icon">⚙️</div>
                <h3>CI/CD Pipeline</h3>
                <p>GitHub Actions automation</p>
            </div>
            <div class="card">
                <div class="icon">🐧</div>
                <h3>Linux Server</h3>
                <p>Ubuntu cloud runner</p>
            </div>
            <div class="card">
                <div class="icon">🐍</div>
                <h3>Python App</h3>
                <p>Auto-generates this page</p>
            </div>
            <div class="card">
                <div class="icon">☁️</div>
                <h3>Cloud Deploy</h3>
                <p>GitHub Pages hosting</p>
            </div>
        </div>

        <div class="pipeline">
            <h2>🔄 Automated Pipeline Flow</h2>
            <div class="steps">
                <div class="step">📝 Code Push</div>
                <div class="arrow">→</div>
                <div class="step">🔍 CI Triggered</div>
                <div class="arrow">→</div>
                <div class="step">🐧 Ubuntu Server</div>
                <div class="arrow">→</div>
                <div class="step">🐍 Python Runs</div>
                <div class="arrow">→</div>
                <div class="step">🌐 Live Deploy</div>
            </div>
        </div>

        <div class="live-badge">
            <div class="dot"></div>
            Automatically deployed using GitHub Actions
        </div>

        <div class="footer">
            <p>University of Agriculture, Faisalabad • CS Student 2027</p>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html created successfully!")
