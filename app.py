# app.py
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# --- Configuración ---
DEBUG = os.getenv("DEBUG", "False").lower() == "true"  # Habilitar el modo de depuración

# --- Rutas ---

@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    """Página de noticias."""
    return render_template('noticias.html')

@app.route('/temas')
def temas():
    """Página de temas."""
    return render_template('temas.html')

@app.route('/descargas')
def descargas():
    """Página de descargas."""
    return render_template('descargas.html')

@app.route('/podcast')
def podcast():
    """Página de podcasts."""
    return render_template('podcast.html')

@app.route('/youtube')
def youtube():
    """Sección para canal de YouTube."""
    return render_template('youtube.html')

# --- Manejo de archivos estáticos ---
@app.route('/static/<path:filename>')
def serve_static(filename):
    """Sirve archivos estáticos (CSS, JS, imágenes)."""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)
