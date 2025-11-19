// File Upload Portal - JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // File input change handler
    const fileInput = document.getElementById('file');
    const fileInfo = document.getElementById('fileInfo');
    
    if (fileInput && fileInfo) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const fileSize = (file.size / 1024).toFixed(2);
                fileInfo.textContent = `Selected: ${file.name} (${fileSize} KB)`;
                fileInfo.style.color = '#4caf50';
            } else {
                fileInfo.textContent = 'No file selected';
                fileInfo.style.color = '#666';
            }
        });
    }
    
    // Form validation
    const uploadForm = document.getElementById('uploadForm');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            const fileInput = document.getElementById('file');
            const logDateTime = document.getElementById('log_datetime');
            const uploaderName = document.getElementById('uploader_name');
            
            // Check if file is selected
            if (!fileInput.files || fileInput.files.length === 0) {
                e.preventDefault();
                alert('Please select a file to upload');
                return false;
            }
            
            // Check file type
            const fileName = fileInput.files[0].name;
            const fileExtension = fileName.split('.').pop().toLowerCase();
            const allowedExtensions = ['log', 'pdf', 'csv', 'zip'];
            
            if (!allowedExtensions.includes(fileExtension)) {
                e.preventDefault();
                alert('Invalid file type. Allowed types: .log, .pdf, .csv, .zip');
                return false;
            }
            
            // Check file size (16MB max)
            const maxSize = 16 * 1024 * 1024; // 16MB
            if (fileInput.files[0].size > maxSize) {
                e.preventDefault();
                alert('File size exceeds 16MB limit');
                return false;
            }
            
            // Check required fields
            if (!logDateTime.value) {
                e.preventDefault();
                alert('Please enter log date/time');
                return false;
            }
            
            if (!uploaderName.value.trim()) {
                e.preventDefault();
                alert('Please enter uploader name');
                return false;
            }
        });
    }
});

