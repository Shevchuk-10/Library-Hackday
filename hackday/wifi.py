import subprocess

def list_wifi_networks():
    try:
        output = subprocess.check_output(["nmcli", "-t", "-f", "SSID", "dev", "wifi"])
        return output.decode().splitlines()
    except Exception as e:
        return [str(e)]
