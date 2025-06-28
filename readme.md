# 🌐 Live Demo

Access the deployed application here: [http://<your-ec2-ip>:5000](http://<your-ec2-ip>:5000)

> ⚠️ Replace `<your-ec2-ip>` with your actual EC2 Public IPv4 address.

---

# 🎤 Text-to-Speech Web Application

This is a Flask-based web application that allows users to upload PDF or DOCX files, converts the text to MP3 audio using open-source tools, and enables users to download the converted audio file.

> This project is fully containerized with Docker, deployed on AWS EC2, and supports GitHub Actions-based CI/CD.

---

## 🚀 Features

* ✉ Upload PDF or Word (DOCX) files.
* 🎧 Convert uploaded text into MP3 audio.
* 🔄 Download the audio file after processing.
* 📆 File size limit: 5MB.
* 🔄 Language and Voice dropdowns (currently default-only, ready for extension).
* ✨ Modern UI with CSS animations and conversion spinner.
* ♻️ Dockerized & CI/CD-enabled with GitHub Actions.

---

## 🛋 Tech Stack

* **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
* **Backend**: Python 3.10, Flask
* **TTS Engine**: gTTS (Google Text-to-Speech)
* **File Parsing**: `PyMuPDF`, `python-docx`
* **Deployment**: Docker, AWS EC2 (Ubuntu), GitHub Actions CI/CD

---

## 🔧 Project Structure

```
text-to-speech-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── .github/
│   └── workflows/
│       └── deploy.yml
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── spinner.gif
├── utils/
│   ├── text_extractor.py
│   └── tts_converter.py
```

---

## 🚪 Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/text-to-speech-app.git
cd text-to-speech-app
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧱 Docker Setup

### 1. Build Image

```bash
docker build -t tts-app .
```

### 2. Run Container

```bash
docker run -d -p 5000:5000 --name tts-app tts-app
```

Then open: [http://localhost:5000](http://localhost:5000)

---

## ✨ Live Deployment on AWS EC2

### 1. Launch EC2 Instance (Ubuntu 22.04)

* Type: t2.micro (Free Tier)
* Allow ports 22, 5000 in security group.

### 2. Install Docker & Git on EC2

```bash
sudo apt update
sudo apt install -y docker.io git
sudo usermod -aG docker $USER
```

### 3. Clone Repo & Build on EC2

```bash
git clone https://github.com/yourusername/text-to-speech-app.git
cd text-to-speech-app
docker build -t tts-app .
docker run -d -p 5000:5000 --name tts-app tts-app
```

---

## 🚜 CI/CD Setup with GitHub Actions

### 1. GitHub Secrets (Repository Settings > Secrets)

| Name      | Value                    |
| --------- | ------------------------ |
| EC2\_HOST | Your EC2 IP              |
| EC2\_KEY  | Contents of .pem SSH key |

### 2. Workflow File: `.github/workflows/deploy.yml`

Automates deployment on every push to `main` branch.

```yaml
name: Deploy to EC2

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Copy to EC2
        uses: appleboy/scp-action@v0.1.7
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_KEY }}
          source: "."
          target: "~/tts-app"

      - name: SSH and Deploy
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_KEY }}
          script: |
            cd ~/tts-app
            docker stop tts-app || true && docker rm tts-app || true
            docker build -t tts-app .
            docker run -d -p 5000:5000 --name tts-app tts-app
```

---

## 🎓 Learning Highlights / Skills Demonstrated

* Flask backend development
* File handling and validation
* Text extraction from DOCX and PDF
* Integration of gTTS for audio generation
* Frontend UX enhancements (spinner, download trigger)
* Dockerfile optimization and multistage build ready
* AWS EC2 server management
* GitHub Actions automation for CI/CD pipeline
* Writing production-grade Python, HTML/CSS with inline comments

---

## 🚀 Future Enhancements

* Add support for multiple voice options
* Use AWS Polly or ElevenLabs for natural TTS voices
* Add user authentication
* Upload history dashboard
* Frontend enhancements using React or Tailwind CSS

---

## 🌟 Author

**Ashutosh Dash**

> Connect with me on [LinkedIn](https://www.linkedin.com/in/your-link) | [GitHub](https://github.com/yourusername)

If you found this project helpful, feel free to ⭐ star the repo!

---

## 📊 License

This project is open-sourced under the MIT License. Feel free to fork and enhance!
