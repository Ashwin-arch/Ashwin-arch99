from PIL import Image
from io import BytesIO
import exifread

def extract_gps(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    img_bytes = BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    tags = exifread.process_file(img_bytes)
    if "GPS GPSLatitude" not in tags:
        return None

    lat = tags["GPS GPSLatitude"]
    lon = tags["GPS GPSLongitude"]

    def convert(value):
        d, m, s = value.values
        return float(d.num) + float(m.num)/60 + float(s.num)/3600

    return convert(lat), convert(lon)
