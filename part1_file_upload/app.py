"""
File Upload Portal - Part 1 of AI Intern Assignment
A simple web application for uploading files (.log, .pdf, .csv, .zip) with metadata.
"""

from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'  # Directory to store uploaded files
METADATA_FILE = 'metadata.json'  # File to store metadata about uploads
ALLOWED_EXTENSIONS = {'log', 'pdf', 'csv', 'zip'}  # Allowed file extensions
MAX_FILE_SIZE = 16 * 1024 * 1024  # Maximum file size (16MB)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_metadata():
    """Load metadata from the JSON file."""
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return []  # Return an empty list if the file is corrupted
    return []

def save_metadata(metadata):
    """Save metadata to the JSON file."""
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

@app.route('/')
def index():
    """Render the main page with the file upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads and save metadata."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400

    file = request.files['file']
    log_datetime = request.form.get('log_datetime', '')  # Log date/time provided by the user
    description = request.form.get('description', '')  # Optional description
    uploader_name = request.form.get('uploader_name', '')  # Name of the uploader

    # Validate required fields
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not log_datetime:
        return jsonify({'error': 'Log date/time is required'}), 400

    if not uploader_name:
        return jsonify({'error': 'Uploader name is required'}), 400

    # Check if the file type is allowed
    if not allowed_file(file.filename):
        return jsonify({'error': f'Invalid file type. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'}), 400

    try:
        # Generate a unique filename to avoid conflicts
        original_filename = secure_filename(file.filename)
        file_extension = original_filename.rsplit('.', 1)[1].lower()
        unique_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
        stored_filename = f"{unique_id}_{original_filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], stored_filename)

        # Save the uploaded file to the server
        file.save(file_path)

        # Get the size of the uploaded file
        file_size = os.path.getsize(file_path)

        # Create a metadata entry for the uploaded file
        metadata_entry = {
            'id': unique_id,
            'original_filename': original_filename,
            'stored_filename': stored_filename,
            'file_size': file_size,
            'file_type': file_extension,
            'log_datetime': log_datetime,
            'description': description,
            'uploader_name': uploader_name,
            'upload_timestamp': datetime.now().isoformat()
        }

        # Load existing metadata, add the new entry, and save it
        metadata = load_metadata()
        metadata.append(metadata_entry)
        save_metadata(metadata)

        # Redirect to the confirmation page
        return redirect(url_for('confirmation', file_id=unique_id))

    except Exception as e:
        # Handle any errors during the upload process
        return jsonify({'error': f'Error uploading file: {str(e)}'}), 500

@app.route('/confirmation/<file_id>')
def confirmation(file_id):
    """Display a confirmation page after a successful upload."""
    metadata = load_metadata()
    file_info = next((f for f in metadata if f['id'] == file_id), None)

    if not file_info:
        return redirect(url_for('index'))  # Redirect to the main page if file not found

    return render_template('confirmation.html', file_info=file_info)

@app.route('/files')
def list_files():
    """List all uploaded files with their metadata."""
    metadata = load_metadata()
    # Sort files by upload timestamp in descending order
    metadata.sort(key=lambda x: x.get('upload_timestamp', ''), reverse=True)
    return render_template('files.html', files=metadata)

@app.route('/download/<file_id>')
def download_file(file_id):
    """Allow users to download a file by its unique ID."""
    metadata = load_metadata()
    file_info = next((f for f in metadata if f['id'] == file_id), None)

    if not file_info:
        return jsonify({'error': 'File not found'}), 404

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_info['stored_filename'])

    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found on server'}), 404

    return send_file(
        file_path,
        as_attachment=True,
        download_name=file_info['original_filename']  # Use the original filename for download
    )

@app.route('/delete/<file_id>', methods=['POST'])
def delete_file(file_id):
    """Delete a file and its metadata entry."""
    metadata = load_metadata()
    file_info = next((f for f in metadata if f['id'] == file_id), None)

    if not file_info:
        return jsonify({'error': 'File not found'}), 404

    # Delete the physical file from the server
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_info['stored_filename'])
    if os.path.exists(file_path):
        os.remove(file_path)

    # Remove the file's metadata entry
    metadata = [f for f in metadata if f['id'] != file_id]
    save_metadata(metadata)

    return redirect(url_for('list_files'))

if __name__ == '__main__':
    print("File Upload Portal")
    print("=" * 50)
    print(f"Upload folder: {os.path.abspath(UPLOAD_FOLDER)}")
    print(f"Allowed file types: {', '.join(ALLOWED_EXTENSIONS)}")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)

