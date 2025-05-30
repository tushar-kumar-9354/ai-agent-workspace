# file_engine/file_saver.py

import os
from datetime import datetime

WORKSPACE_DIR = "workspace"

def save_code_to_file(code: str, prefix: str = "generated_code") -> str:
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.py"
    filepath = os.path.join(WORKSPACE_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    
    return filepath
