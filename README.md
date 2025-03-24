command to run the server : python wsgi.py


# Background Remover Web App

A Flask web application that removes backgrounds from images using the rembg library.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/Moon145-iut/bg_remover.git
cd bg_remover
```

2. Create a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

### Running the Application

#### Development Mode
```bash
python main.py
```
Access the app at: http://localhost:5000

#### Production Mode
```bash
python wsgi.py
```
Access the app at: http://localhost:8090

## Usage

1. Open your web browser and go to http://localhost:8090
2. Click "Choose File" to select an image
3. Preview your image
4. Click "Remove Background"
5. The processed image will automatically download

## Project Structure
```
bg_remover/
├── main.py           # Main Flask application
├── wsgi.py          # Production server configuration
├── requirements.txt  # Python dependencies
├── static/          # Static files
└── templates/       # HTML templates
    └── upload.html  # Upload form template
```

## Technologies Used
- Flask
- rembg
- Pillow
- Waitress (Production Server)
- HTML/CSS/JavaScript

## Contributing
Pull requests are welcome. For major changes, please open an issue first.

## License
[MIT](https://choosealicense.com/licenses/mit/)
