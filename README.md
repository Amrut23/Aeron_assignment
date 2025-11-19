# AI Intern Assignment - File Upload Portal & CSV Plotter

This repository contains two utilities built for the AI Intern Assignment:
1. **File Upload Portal** - A web application for uploading and managing files
2. **Python CSV Plotter** - A command-line tool for plotting CSV data

---

## Table of Contents

- [Part 1: Weather Data Viewer](#part-1-weather-data-viewer)
- [Part 2: Python CSV Plotter](#part-2-python-csv-plotter)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [AI Tools Used](#ai-tools-used)
- [Manual Changes](#manual-changes)
- [Project Structure](#project-structure)

---

## Part 1: File Upload Portal

A web application for uploading files with metadata and managing uploaded files.

### Features

- **File Upload**: Upload .log, .pdf, .csv, and .zip files
- **Metadata Entry**: Enter log date/time, description, and uploader's name
- **File Storage**: Secure file storage with unique identifiers
- **Confirmation Page**: Shows details after successful upload
- **File Listing**: View all uploaded files with metadata
- **Download Functionality**: Download any uploaded file
- **File Management**: Delete files from the portal
- **Responsive Design**: Works on desktop and mobile devices

### Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: Local file system with JSON metadata

---

## Part 2: Python CSV Plotter

A command-line Python script that loads CSV files and creates customizable plots.

### Features

- **CSV Loading**: Load any CSV file
- **Column Selection**: Choose X and Y axes from available columns
- **Graph Types**: Support for line charts and bar graphs
- **Interactive**: User-friendly command-line interface
- **Error Handling**: Robust error handling for invalid inputs

### Technology Stack

- **Python 3.x**
- **pandas**: For CSV data manipulation
- **matplotlib**: For data visualization

---

## Requirements

### System Requirements

- **OS**: Windows, Linux, or macOS
- **Python**: 3.8 or higher

### Python Libraries

#### Part 1 (File Upload Portal)
```
Flask==3.0.0
Werkzeug==3.0.1
```

#### Part 2 (CSV Plotter)
```
pandas==2.1.3
matplotlib==3.8.2
```

---

## Installation & Setup

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Python Dependencies

#### For Weather Viewer:
```bash
cd part1_weather_viewer
pip install -r requirements.txt
```

#### For CSV Plotter:
```bash
cd part2_csv_plotter
pip install -r requirements.txt
```

### 3. File Upload Portal Setup

The File Upload Portal requires no additional setup. Files are stored locally in the `uploads/` directory, and metadata is stored in `metadata.json`.

---

## Usage

### Part 1: File Upload Portal

1. **Navigate to the file upload directory:**
   ```bash
   cd part1_file_upload
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your web browser:**
   - Navigate to `http://localhost:5000`
   - Fill in the upload form:
     - Select a file (.log, .pdf, .csv, or .zip)
     - Enter log date/time
     - Enter description (optional)
     - Enter uploader's name
   - Click "Upload File"
   - View confirmation page
   - Navigate to "View All Files" to see all uploaded files

4. **Stop the server:**
   - Press `Ctrl+C` in the terminal

### Part 2: Python CSV Plotter

1. **Navigate to the CSV plotter directory:**
   ```bash
   cd part2_csv_plotter
   ```

2. **Run the script:**
   ```bash
   python csv_plotter.py
   ```

   Or with a CSV file path as argument:
   ```bash
   python csv_plotter.py path/to/your/file.csv
   ```

3. **Follow the prompts:**
   - Enter CSV file path (if not provided as argument)
   - Select column number for X-axis
   - Select column number for Y-axis
   - Choose graph type (Line Chart or Bar Graph)
   - View the generated plot

4. **Example with sample data:**
   ```bash
   python csv_plotter.py sample_data.csv
   ```

---

## AI Tools Used

### Primary AI Tool: Cursor AI (Auto)

This entire project was built using **Cursor AI** (Auto), an AI-powered coding assistant. The development process involved iterative prompting and refinement.

### AI Prompts Used

#### Initial Setup Prompt:
```
"Solve the PDF assignment"
```

The AI assistant:
1. Extracted and analyzed the assignment requirements from the PDF
2. Created a structured plan with todos
3. Built both utilities from scratch
4. Generated comprehensive documentation

#### Development Process:

The AI was used for:
- **Code Generation**: Generated complete Flask application, HTML templates, CSS styling, and JavaScript functionality
- **Error Handling**: Added robust error handling and user input validation
- **Code Structure**: Organized code into proper file structure with separation of concerns
- **Documentation**: Created comprehensive README with setup instructions

### Manual Changes Made

While the AI generated the initial code, the following manual adjustments were made:

1. **API Key Configuration**: 
   - Added environment variable support for API key
   - Added warning message if API key is not set

2. **Error Messages**:
   - Enhanced error messages for better user experience
   - Added specific error handling for API failures

3. **Code Comments**:
   - Added detailed docstrings to functions
   - Added inline comments for complex logic

4. **File Organization**:
   - Created proper directory structure
   - Separated static files (CSS, JS) from templates

5. **Sample Data**:
   - Created sample CSV file for testing the plotter

6. **Documentation**:
   - Expanded README with detailed setup instructions
   - Added troubleshooting section
   - Included screenshots descriptions

---

## Project Structure

```
.
├── README.md                          # This file
├── part1_file_upload/                # File Upload Portal Application
│   ├── app.py                         # Flask backend application
│   ├── requirements.txt               # Python dependencies
│   ├── .gitignore                     # Ignore uploads and metadata
│   ├── templates/
│   │   ├── index.html                 # Upload form page
│   │   ├── confirmation.html          # Upload confirmation page
│   │   └── files.html                 # File listing page
│   └── static/
│       ├── style.css                   # CSS styling
│       └── script.js                   # JavaScript functionality
│
├── part2_csv_plotter/                 # CSV Plotter Script
│   ├── csv_plotter.py                 # Main Python script
│   ├── requirements.txt               # Python dependencies
│   └── sample_data.csv                # Sample CSV for testing
│
└── assignment_text.txt                 # Extracted assignment text
```

---

## Troubleshooting

### File Upload Portal Issues

**Problem**: "File not found" error
- **Solution**: Ensure the `uploads/` directory exists and has write permissions

**Problem**: "Invalid file type"
- **Solution**: Only .log, .pdf, .csv, and .zip files are allowed

**Problem**: "File size exceeds limit"
- **Solution**: Maximum file size is 16MB. Compress larger files or split them

**Problem**: Port 5000 already in use
- **Solution**: Change the port in `app.py` (line: `app.run(debug=True, host='0.0.0.0', port=5000)`)

### CSV Plotter Issues

**Problem**: "File not found"
- **Solution**: Ensure the CSV file path is correct and the file exists

**Problem**: "Column could not be converted to numeric"
- **Solution**: The script will use categorical data. Ensure your data columns are appropriate for plotting

**Problem**: Graph window doesn't appear
- **Solution**: Ensure matplotlib backend is properly configured. On Linux, you may need: `sudo apt-get install python3-tk`

---

## Screenshots

### File Upload Portal
- Modern, responsive upload form with gradient background
- File upload with metadata entry (date/time, description, uploader name)
- Confirmation page showing upload details
- File listing page with download and delete functionality

### CSV Plotter
- Command-line interface with step-by-step prompts
- Interactive column selection
- Multiple graph type options (line/bar)
- Clear error messages and validation

---

## Future Enhancements (Optional)

### File Upload Portal:
- User authentication and access control
- File preview functionality
- Search and filter uploaded files
- Bulk file operations
- File versioning

### CSV Plotter:
- Support for multiple Y-axes
- Additional graph types (scatter, pie, etc.)
- Export plots as images
- Batch processing multiple CSV files

---

## License

This project is created for educational purposes as part of the AI Intern Assignment evaluation.

---

## Contact

For questions or issues, please refer to the assignment submission guidelines.

---

**Note**: This assignment was completed using AI assistance (Cursor AI) as part of the evaluation criteria. All code, documentation, and structure were developed with AI collaboration while maintaining understanding and ability to explain the implementation.

