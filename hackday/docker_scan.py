import subprocess

def list_running_containers():
    try:
        output = subprocess.check_output(["docker", "ps"])
        return output.decode().splitlines()
    except Exception as e:
        return [str(e)]
