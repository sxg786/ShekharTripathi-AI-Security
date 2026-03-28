import re

def parse_auth_log(file_path):
    logs = []

    with open(file_path, 'r') as f:
        for line in f:
            logs.append({
                "raw": line,
                "failed_login": 1 if "Failed password" in line else 0,
                "success_login": 1 if "Accepted password" in line else 0,
                "sudo_usage": 1 if "sudo" in line else 0
            })

    return logs
