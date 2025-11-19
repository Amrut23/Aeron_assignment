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
UPLOAD_FOLDER = 'uploads'
METADATA_FILE = 'metadata.json'
ALLOWED_EXTENSIONS = {'log', 'pdf', 'csv', 'zip'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_metadata():
    """Load metadata from JSON file"""
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_metadata(metadata):
    """Save metadata to JSON file"""
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

@app.route('/')
def index():
    """Main page - file upload form"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload with metadata"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    log_datetime = request.form.get('log_datetime', '')
    description = request.form.get('description', '')
    uploader_name = request.form.get('uploader_name', '')
    
    # Validate required fields
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not log_datetime:
        return jsonify({'error': 'Log date/time is required'}), 400
    
    if not uploader_name:
        return jsonify({'error': 'Uploader name is required'}), 400
    
    # Check file extension
    if not allowed_file(file.filename):
        return jsonify({'error': f'Invalid file type. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
    
    try:
        # Generate unique filename to avoid conflicts
        original_filename = secure_filename(file.filename)
        file_extension = original_filename.rsplit('.', 1)[1].lower()
        unique_id = str(uuid.uuid4())[:8]
        stored_filename = f"{unique_id}_{original_filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], stored_filename)
        
        # Save file
        file.save(file_path)
        
        # Get file size
        file_size = os.path.getsize(file_path)
        
        # Create metadata entry
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
        
        # Load existing metadata and add new entry
        metadata = load_metadata()
        metadata.append(metadata_entry)
        save_metadata(metadata)
        
        # Redirect to confirmation page
        return redirect(url_for('confirmation', file_id=unique_id))
    
    except Exception as e:
        return jsonify({'error': f'Error uploading file: {str(e)}'}), 500

@app.route('/confirmation/<file_id>')
def confirmation(file_id):
    """Show confirmation page after successful upload"""
    metadata = load_metadata()
    file_info = next((f for f in metadata if f['id'] == file_id), None)
    
    if not file_info:
        return redirect(url_for('index'))
    
    return render_template('confirmation.html', file_info=file_info)

@app.route('/files')
def list_files():
    """Display list of all uploaded files"""
    metadata = load_metadata()
    # Sort by upload timestamp (newest first)
    metadata.sort(key=lambda x: x.get('upload_timestamp', ''), reverse=True)
    return render_template('files.html', files=metadata)

@app.route('/download/<file_id>')
def download_file(file_id):
    """Download a file by its ID"""
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
        download_name=file_info['original_filename']
    )

@app.route('/delete/<file_id>', methods=['POST'])
def delete_file(file_id):
    """Delete a file and its metadata"""
    metadata = load_metadata()
    file_info = next((f for f in metadata if f['id'] == file_id), None)
    
    if not file_info:
        return jsonify({'error': 'File not found'}), 404
    
    # Delete physical file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_info['stored_filename'])
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Remove from metadata
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

