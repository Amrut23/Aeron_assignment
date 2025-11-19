# File Upload Portal

Welcome to the File Upload Portal — a small, friendly, and slightly whimsical app that helps you stash, track, and retrieve your files with charm.

This Flask app lets you upload files with metadata, see all uploads, download files, and delete items you no longer need. It's perfect for quick demos, experiments, or as a base for a more advanced media manager.

## Features ✨
- Upload files and add helpful metadata (log date/time, description, uploader are recorded).
- Supports `.log`, `.pdf`, `.csv`, `.zip` files — with a 16MB size limit.
- A playful, responsive UI with helpful hints and a tiny confetti celebration on success.
- Download or delete uploaded files with a single click.
- Metadata is stored locally as `metadata.json` for simple demo purposes.

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

## Running the Application — Quick Start 🚀
1. Change into the project folder:

```powershell
cd part1_file_upload
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the app (development mode):

```powershell
python app.py
```

4. Open the UI in your browser at `http://127.0.0.1:5000` — upload a file and watch the confetti!

## Directory Structure
- `app.py`: Main application file.
- `templates/`: HTML templates for rendering web pages.
- `static/`: Static files (CSS and JavaScript).
- `uploads/`: Directory where uploaded files are stored.
- `metadata.json`: JSON file to store metadata about uploaded files.

## Usage — Short and sweet
1. Upload a file with a memorable description so future-you can find it later.
2. Visit the Files page to download or remove files.
3. Want to re-run an upload? Use the "Upload Another File" button and savor the confetti.

Tips: Metadata is stored in `metadata.json` so you can open it or export it for other tools.

## Notes
- The max file size is 16MB.
- Metadata is stored in `metadata.json` at the root of the project; this is a demo-friendly format and can be migrated to a database later.
- This project is playful by design — feel free to customize the UI or animations to match your brand.

## License
This project is for educational purposes and is not licensed for commercial use.