def greet(name):
    return f"Hello, {name}! This is my DevOps project."

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Demo</title>
    <style>
        body {{ font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0; }}
        h1 {{ color: #2c3e50; }}
        p {{ color: #27ae60; font-size: 20px; }}
    </style>
</head>
<body>
    <h1>{greet("DevOps")}</h1>
    <p>✅ Automatically deployed using GitHub Actions CI/CD Pipeline</p>
    <p>Built by Fizah Iman</p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html created successfully!")
