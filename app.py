from flask import Flask, render_template, abort

app = Flask(__name__)

# Expanded list of 7 articles with 'content' and 'author' added
articles = [
    {
        "id": 1,
        "title": "The Future of AI in DevOps",
        "category": "Technology",
        "date": "Oct 24, 2026",
        "author": "Sarah Jenkins",
        "content": "Artificial intelligence is no longer just a buzzword; it is fundamentally reshaping CI/CD pipelines. From predictive failure analysis to automated code reviews, AI is enabling DevOps teams to ship faster and safer than ever before. In this deep dive, we explore how AI-driven tools are identifying bottlenecks in real-time and automatically scaling infrastructure.",
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 2,
        "title": "Kubernetes 1.30 Released",
        "category": "Cloud",
        "date": "Oct 23, 2026",
        "author": "David Chen",
        "content": "The latest update to the world's most popular container orchestrator is here. Kubernetes 1.30 brings enhanced security features, better resource management, and significantly faster pod deployment times. We break down the top 5 features that DevOps engineers need to know about, including the new dynamic resource allocation API.",
        "image": "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 3,
        "title": "Docker Best Practices for 2026",
        "category": "DevOps",
        "date": "Oct 22, 2026",
        "author": "Elena Rodriguez",
        "content": "Stop using the 'latest' tag and learn how to optimize your Docker images for production environments. In this guide, we cover multi-stage builds, distroless images, and vulnerability scanning. Learn how to reduce your image sizes by up to 80% and improve your security posture.",
        "image": "https://images.unsplash.com/photo-1605745341112-85968b19335b?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 4,
        "title": "Mastering CI/CD with GitLab",
        "category": "Development",
        "date": "Oct 21, 2026",
        "author": "Marcus Johnson",
        "content": "GitLab CI/CD is one of the most powerful tools in a developer's arsenal. In this article, we demonstrate how to build a robust pipeline from scratch using YAML. We also cover caching strategies, environment variables, and how to run parallel jobs to speed up your build times.",
        "image": "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 5,
        "title": "Serverless vs Containers",
        "category": "Architecture",
        "date": "Oct 20, 2026",
        "author": "Priya Patel",
        "content": "Should you use AWS Lambda or Kubernetes? It depends on your workload. This article compares serverless architecture and containerized deployments in terms of cost, scalability, and cold-start latency. Discover which approach is best for your next microservice.",
        "image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 6,
        "title": "Terraform: Infrastructure as Code",
        "category": "Cloud",
        "date": "Oct 19, 2026",
        "author": "James Wilson",
        "content": "Manual infrastructure provisioning is a thing of the past. Terraform allows you to define your cloud resources (AWS, Azure, GCP) using declarative configuration files. Learn how to set up a remote backend to store your state files securely and manage complex multi-cloud deployments.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 7,
        "title": "Securing your APIs with OAuth",
        "category": "Security",
        "date": "Oct 18, 2026",
        "author": "Alex Mercer",
        "content": "Security is paramount in modern web applications. OAuth 2.0 provides a robust framework for authorization. In this tutorial, we implement a secure token-based authentication system for a REST API, discussing the differences between access tokens and refresh tokens.",
        "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&q=80&w=800"
    }
]

@app.route('/')
def home():
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article_data = next((a for a in articles if a["id"] == article_id), None)
    if article_data is None:
        abort(404)
    return render_template('article.html', article=article_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)