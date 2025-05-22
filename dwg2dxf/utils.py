import os
import shutil

def find_oda_converter():
    oda_cmd = shutil.which("ODAFileConverter")
    if oda_cmd:
        return oda_cmd

    paths = [
        "C:\\Program Files\\ODAFileConverter\\ODAFileConverter.exe",
        "C:\\ODAFileConverter\\ODAFileConverter.exe"
    ]
    for path in paths:
        if os.path.exists(path):
            return path

    return None
