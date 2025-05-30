import subprocess
import os

def execute_code(file_path, timeout=10):
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Execution timed out."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
