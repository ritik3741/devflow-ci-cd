
---
```md
# 🚀 DevFlow – CI/CD, Kubernetes & DevOps Automation Platform

DevFlow is an end-to-end DevOps automation platform that demonstrates real-world CI/CD pipelines, Docker, Kubernetes, and internal developer tooling.

It includes a **published, installable CLI** that automates deployment, rollback, and operational workflows using a **configuration-driven design**.

This project is built to reflect **production-style DevOps and Platform Engineering practices**, not toy examples.

---

## 🧠 What DevFlow Does

DevFlow automates the complete DevOps lifecycle:

- CI/CD using **GitHub Actions**
- Containerization using **Docker**
- Orchestration using **Kubernetes**
- Deployment automation using a **custom CLI**
- Safe operations with **dry-run** and **rollback**
- Environment-based configuration (`dev` / `prod`)
- Automated release publishing to **PyPI**

---

## 🏗️ Architecture Overview

```

Developer
↓
GitHub Push
↓
GitHub Actions (CI/CD)
↓
Docker Build & Push
↓
Kubernetes Deployment
↓
DevFlow CLI (deploy / rollback / status)

```

---

## 📁 Project Structure

```

Devflow/
├── cli/                     # Installable DevFlow CLI
│   ├── **init**.py
│   └── devflow.py
├── app/                     # Sample application
├── docker/                  # Dockerfile
│   └── Dockerfile
├── k8s/                     # Kubernetes manifests
│   ├── dev/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── prod/
│       ├── deployment.yaml
│       └── service.yaml
├── .github/workflows/       # CI/CD workflows
│   ├── ci-cd.yml
│   └── publish-pypi.yml
├── devflow.yaml             # Config-driven CLI settings
├── setup.py                 # Python package configuration
├── pyproject.toml
├── requirements.txt
└── README.md

````

---

## 🧰 DevFlow CLI

DevFlow provides a **production-grade DevOps CLI** that is globally installable.

### 🔹 Install CLI

```bash
pip install ritik-devflow
````

---

### 🔹 Available Commands

```bash
devflow deploy --env dev
devflow deploy --env prod
devflow deploy --env dev --dry-run

devflow rollback
devflow status
devflow logs
devflow cleanup
```

---

### 🔹 Key Features

* Installable CLI (`devflow`)
* Environment-aware deployments
* Dry-run mode for safe previews
* Rollback support using Kubernetes rollout history
* Configuration-driven behavior using YAML

---

## ⚙️ Configuration (`devflow.yaml`)

All environment-specific values are externalized into a YAML config file.

```yaml
app:
  name: devflow

docker:
  image: devflow
  dockerfile: docker/Dockerfile

kubernetes:
  deployment_name: devflow-deployment
  service_name: devflow-service

environments:
  dev:
    image: devflow:latest
    deployment_path: k8s/dev
  prod:
    image: ritik3741/devflow:latest
    deployment_path: k8s/prod
```

This enables:

* Zero code changes between environments
* Clean separation of logic and configuration
* Safer and scalable deployments

---

## 🔄 CI/CD Pipelines

### 🔹 Application CI/CD

* Runs on every push
* Builds Docker images
* Validates builds using GitHub Actions

### 🔹 CLI Release Automation

* Triggered by Git tags (`v*`)
* Automatically builds the Python package
* Publishes the CLI to **PyPI**

```bash
git tag v1.0.2
git push origin v1.0.2
```

---

## 🛡️ Safety & Reliability

* Dry-run support to preview actions
* Rollback command for quick recovery
* Config validation to avoid runtime failures
* Secure secrets handling via GitHub Actions

---

## 🧪 Local Development

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install CLI in editable mode

```bash
pip install -e .
```

### Test CLI

```bash
devflow --help
```

---

## 🧠 Skills Demonstrated

* CI/CD with GitHub Actions
* Docker image lifecycle & build context
* Kubernetes deployments, services, and rollbacks
* Internal DevOps tooling with Python & Click
* Configuration-driven system design
* Python packaging & PyPI publishing
* Real-world debugging and release engineering

---

## 📌 Use Cases

* DevOps / Platform Engineering portfolio
* Learning CI/CD, Docker, and Kubernetes
* Internal tooling reference
* Interview project discussion

---

## 👤 Author

**Ritik Kumar**
DevOps | Platform Engineering | Cloud Enthusiast
```
