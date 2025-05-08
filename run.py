# run.py
import os
from app import app

PORT = int(os.getenv("PORT", 5000))  # Puerto de la aplicación
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
