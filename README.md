# AI Intern Assignment - File Upload Portal & CSV Plotter

This repository contains two small utilities created for the AI Intern Assignment:

- `part1_file_upload`: a Flask-based File Upload Portal for uploading files with simple metadata.
- `part2_csv_plotter`: a command-line Python script to load CSV data and generate plots.

---

## Table of Contents

- [Part 1: File Upload Portal](#part-1-file-upload-portal)
- [Part 2: CSV Plotter](#part-2-csv-plotter)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [AI Tools Used](#ai-tools-used)
- [Project Structure](#project-structure)
- [License](#license)

---

## Part 1: File Upload Portal

A simple Flask app to upload files and store lightweight metadata in `metadata.json`. Supported file types: `.log`, `.pdf`, `.csv`, `.zip`. Files are stored under `part1_file_upload/uploads/`.

## Part 2: CSV Plotter

A small Python CLI tool that reads a CSV file and generates line or bar plots using `pandas` and `matplotlib`.

---

## Requirements

- Python 3.8 or higher

Python dependencies are listed in each subproject's `requirements.txt`.

---

## Installation & Setup

1. Clone or download the repository:

```powershell
git clone <repository-url>
cd <repository-folder>
```

2. Install dependencies for each part separately.

For the File Upload Portal:

```powershell
cd part1_file_upload
pip install -r requirements.txt
```

For the CSV Plotter:

```powershell
cd ..\part2_csv_plotter
pip install -r requirements.txt
```

---

## Usage

Part 1 — File Upload Portal:

```powershell
cd part1_file_upload
python app.py
# Open http://127.0.0.1:5000 in your browser
```

Part 2 — CSV Plotter:

```powershell
cd part2_csv_plotter
python csv_plotter.py [path/to/file.csv]
```

Follow the prompts in the CSV Plotter to select columns and chart type.

---

## AI Tools Used

This project used **Copilot (within VS Code)** and **GitHub Copilot** to assist with code authoring and suggestions. The base project structure was designed using **Claude** and **Gemini**.

No API keys or external services are required to run the included code.

---

## Project Structure

```
.
├── README.md
├── part1_file_upload/
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   ├── static/
│   └── uploads/
└── part2_csv_plotter/
    ├── csv_plotter.py
    ├── requirements.txt
    └── sample_data.csv
```

---

