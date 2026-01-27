# tests/conftest.py
import sys
from pathlib import Path

# Добавляем папку src в sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
