"""Conexión a MySQL. Ajuste los datos según su instalación (XAMPP por defecto: root sin contraseña)."""
import os
import pymysql

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "ingenieria_web"),
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}


def obtener_conexion():
    return pymysql.connect(**CONFIG)
