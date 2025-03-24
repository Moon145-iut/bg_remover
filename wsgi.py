from waitress import serve
from main import app
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # Serve on localhost with port 8090
    logging.info("Starting production server on http://localhost:8090")
    serve(app, host='localhost', port=8090)
