# File Hashing and Validation Utility

FileHashUtil is a **Streamlit-based** web application that allows users to generate and validate cryptographic hashes for files. It supports multiple hashing algorithms and provides an easy-to-use interface for validating file integrity.

## Features

- Generate hashes for uploaded files
- Validate file hashes against user-provided values
- Supports **MD5, SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512**
- Download hash results with file metadata as a `.csv` file
- Modern, responsive UI with enhanced styling

## Running Example

You can try out FileHashUtil online at:  
➡️ **[FileHashUtil Demo](https://filehashutil.streamlit.app/)**

## Dependencies

- Python 3.6+
- Streamlit
- Pandas
- Base64

## Installation

1. Clone the repository:
```sh
git clone https://github.com/wquinones/FileHashUtil.git
```

2. Navigate to the project folder:
```sh
cd FileHashUtil
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage

To start the application, run:
```sh
streamlit run FileHashUtil.py
```

This will launch the web interface in your default browser at `http://localhost:8501`.

## How It Works

- **Generate Hashes**: Upload a file to generate cryptographic hashes.
- **Validate Hashes**: Provide a hash and upload a file to check for a match.
- **Download Results**: Save the computed hashes and metadata as a `.csv` file.

## License

This project is licensed under the MIT License.
