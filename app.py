from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {
        "id": 1,
        "title": "The Future of AI in DevOps",
        "category": "Technology",
        "date": "Oct 24, 2026",
        "excerpt": "How artificial intelligence is reshaping CI/CD pipelines and automating infrastructure management.",
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 2,
        "title": "Kubernetes 1.30 Released",
        "category": "Cloud",
        "date": "Oct 23, 2026",
        "excerpt": "The latest update brings enhanced security features, better resource management, and faster deployments.",
        "image": "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 3,
        "title": "Docker Best Practices for 2026",
        "category": "DevOps",
        "date": "Oct 22, 2026",
        "excerpt": "Stop using 'latest' tags and learn how to optimize your Docker images for production environments.",
        "image": "https://images.unsplash.com/photo-1605745341112-85968b19335b?auto=format&fit=crop&q=80&w=800"
    }
]

@app.route('/')
def home():
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)