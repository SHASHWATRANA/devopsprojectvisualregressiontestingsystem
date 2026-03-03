# 🚀 Visual Regression Testing System

**Student Name:** Shashwat Rana  
**Registration No:** 23FE10CSE00101  
**Course:** CSE3253 – DevOps  
**Semester:** VI  
**Project Type:** Testing & Automation (Selenium & CI/CD)  
**Difficulty Level:** Intermediate  

---

## 📌 Project Overview

This project implements a **containerized Visual Regression Testing System** integrated with a complete CI/CD pipeline.

The system automatically captures screenshots of web applications using Selenium, compares them against baseline images using a NumPy-based pixel comparison engine, and generates an HTML report highlighting differences.

The entire workflow is automated using **Docker** and **GitHub Actions**, demonstrating real-world DevOps practices.

---

## 🎯 Problem Statement

Manual UI testing is time-consuming and error-prone. Even small UI changes may go unnoticed.

This project automates UI validation by:

- Capturing screenshots
- Comparing pixel differences
- Generating regression reports
- Running automatically inside CI pipeline

---

## 🏗 Architecture Diagram

![Architecture Diagram](docs/architecture/architecture-diagram.png)

---

## 🔁 System Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions CI pipeline is triggered.
3. Docker image is built.
4. CLI runner executes inside container.
5. Selenium (headless Chromium) captures screenshot.
6. Visual engine compares current screenshot with baseline.
7. HTML report is generated.
8. Report is uploaded as CI artifact.

---

## ⚙️ Technology Stack

### Core Technologies
- Python 3.11
- Selenium
- NumPy
- Pillow

### DevOps Tools
- Git & GitHub
- Docker
- GitHub Actions
- Headless Chromium (Linux container)

---

## ✨ Key Features

- Headless browser automation
- Pixel-level image comparison
- Threshold-based regression detection
- Diff image generation
- HTML report generation
- Environment variable configuration
- Standalone CLI execution
- Docker containerization
- Automated CI/CD pipeline
- Artifact upload in GitHub Actions
- Environment-specific baseline management

---

## 🖥 Local Execution (CLI Mode)

Run the tool directly:

```bash
python -m src.main.run
```

### With Custom Environment Variables

Windows:
```bash
set URL=https://example.com
set THRESHOLD=1.0
python -m src.main.run
```

Linux/macOS:
```bash
export URL=https://example.com
export THRESHOLD=1.0
python -m src.main.run
```

---

## 🐳 Docker Execution

### Build Docker Image

```bash
docker build -t visual-regression-test -f infrastructure/docker/Dockerfile .
```

### Run Container

```bash
docker run --rm visual-regression-test
```

The system runs in headless mode using Chromium inside the container.

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow:

- Builds Docker image
- Runs CLI inside container
- Generates HTML regression report
- Uploads report as downloadable artifact

This demonstrates:

- Automated testing
- Containerized execution
- Continuous Integration
- Artifact management

---

## 📊 Report Generation

The system generates:

- Baseline image
- Current image
- Diff image
- HTML report summarizing:
  - Status (PASS/FAIL)
  - Difference percentage
  - Threshold value

---

## 🧠 DevOps Concepts Implemented

- Containerization for environment consistency
- CI automation with GitHub Actions
- Headless browser execution for CI compatibility
- Environment-variable driven configuration
- Artifact storage in CI
- Baseline management strategy
- Reproducible testing environment

---

## 📌 Learning Outcomes

- Implemented a real-world DevOps workflow
- Integrated automated testing with CI/CD
- Managed cross-platform rendering differences
- Designed configurable automation framework
- Handled container lifecycle behavior

---

## 📬 Contact

Shashwat Rana  
GitHub: https://github.com/SHASHWATRANA