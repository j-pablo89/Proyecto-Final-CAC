from flask import Flask

app = Flask(__name__)

# Importa tus rutas y controladores aquí
from app import controller, database