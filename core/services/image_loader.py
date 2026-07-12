"""
Panel Cutter Pro

image_loader.py

Responsible for loading images.
"""

from PIL import Image
from pathlib import Path


class ImageLoader:
    """Loads image and returns basic information."""

    SUPPORTED_FORMATS = [".png", ".jpg", ".jpeg"]

    def load(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported file format: {path.suffix}")

        image = Image.open(path)

        width, height = image.size

        if height > width:
            orientation = "portrait"
        elif width > height:
            orientation = "landscape"
        else:
            orientation = "square"

        return {
            "image": image,
            "width": width,
            "height": height,
            "orientation": orientation,
            "filename": path.name,
            "path": str(path)
        }