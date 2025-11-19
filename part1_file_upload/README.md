# File Upload Portal

This is a simple web application built using Flask that allows users to upload files along with metadata. The application supports file uploads, metadata storage, file downloads, and file deletion.

## Features
- Upload files with metadata (e.g., log date/time, description, uploader name).
- Supported file types: `.log`, `.pdf`, `.csv`, `.zip`.
- View a list of all uploaded files with metadata.
- Download uploaded files.
- Delete files and their associated metadata.

## Prerequisites
- Python 3.8 or higher
- Flask library

## Installation
1. Clone or download this repository.
2. Navigate to the `part1_file_upload` directory.
3. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Application
1. Ensure you are in the `part1_file_upload` directory.
2. Start the Flask development server:
   ```powershell
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Directory Structure
- `app.py`: Main application file.
- `templates/`: HTML templates for rendering web pages.
- `static/`: Static files (CSS and JavaScript).
- `uploads/`: Directory where uploaded files are stored.
- `metadata.json`: JSON file to store metadata about uploaded files.

## Usage
1. Open the application in your browser.
2. Use the upload form to upload a file along with metadata.
3. View the list of uploaded files on the "Files" page.
4. Download or delete files as needed.

## Notes
- The maximum file size for uploads is 16MB.
- Metadata is stored in `metadata.json` in the root directory.

## License
This project is for educational purposes and is not licensed for commercial use.