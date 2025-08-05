from flask import Flask, request, jsonify
import os
import requests
import json
import time
import uuid
from datetime import datetime
import subprocess
import tempfile
import shutil
from urllib.parse import urlparse
import re

app = Flask(__name__)

# Configuración de variables de entorno
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
NETLIFY_TOKEN = os.environ.get('NETLIFY_TOKEN')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
MEMORY_SPREADSHEET_ID = os.environ.get('MEMORY_SPREADSHEET_ID')

# (...) CONTENIDO OMITIDO PARA RESUMIR
# Inserta aquí el contenido completo de tu main.py si deseas cargar el archivo real.
app.run(host="0.0.0.0", port=8080, debug=True)
