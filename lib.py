

from utils.metrics_time_helper import TimeHelper as th
import requests
import sqlite3

#== Configuration ==
import os

# Access config values like this

DB_URL = os.getenv("DATABASE_URL")

# == Logging setup ===
import logging

LOG_DIR = "logs"
LOG_FILE = "dsa_app.log"
os.makedirs (LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers = [
        logging.StreamHandler(), #console
        logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE)) # File
    ]
)
logger = logging.getLogger("dsa")
# === Exports ===
__all__ = [
    "requests", "sqlite3", "os",
    "DB_URL", "logger", "th"
]

