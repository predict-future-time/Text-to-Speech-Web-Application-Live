from flask import Flask, request, render_template, send_file, redirect, url_for, flash
import os
import time
from utils.text_extractor import extract_text_from_pdf, extract_text_from_docx
from utils.tts_converter import convert_text_to_audio
from werkzeug.utils import secure_filename

# Folder paths for uploaded and audio files
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio'

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER
app.secret_key = "secret123"  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')

    # File presence validation
    if not file:
        flash("No file uploaded.")
        return redirect(url_for('index'))

    # File size validation (5MB max)
    file.seek(0, os.SEEK_END)
    if file.tell() > 5 * 1024 * 1024:
        flash("File too large. Max allowed size is 5MB.")
        return redirect(url_for('index'))
    file.seek(0)

    # Secure the filename
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Text extraction
    if filename.endswith('.pdf'):
        text = extract_text_from_pdf(filepath)
    elif filename.endswith('.docx'):
        text = extract_text_from_docx(filepath)
    else:
        flash("Only PDF and DOCX files are supported.")
        return redirect(url_for('index'))

    # Convert to MP3
    audio_filename = f"{os.path.splitext(filename)[0]}.mp3"
    audio_path = os.path.join(AUDIO_FOLDER, audio_filename)

    # Add a short sleep to ensure write completes before send
    convert_text_to_audio(text, audio_path, lang=request.form.get("output_lang", "en"))
    time.sleep(1)  # Ensure file write completes

    # Redirect to download
    return render_template('index.html', audio_url=url_for('download_file', filename=audio_filename))

@app.route('/download/<filename>')
def download_file(filename):
    audio_path = os.path.join(app.config['AUDIO_FOLDER'], filename)

    # Defensive check to avoid sending non-existent files
    if not os.path.exists(audio_path):
        flash("Audio file not found.")
        return redirect(url_for('index'))

    return send_file(
        audio_path,
        as_attachment=True,
        mimetype="audio/mpeg",  # Force correct type
        download_name=filename  # Ensure filename ends in .mp3
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
