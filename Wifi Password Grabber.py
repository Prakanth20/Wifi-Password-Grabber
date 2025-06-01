import subprocess

def get_saved_wifi_passwords():
    # Get list of saved profiles
    profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
    profiles = [line.split(":")[1].strip() for line in profiles_data.split("\n") if "All User Profile" in line]

    wifi_credentials = {}

    for profile in profiles:
        try:
            profile_info = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode()
            for line in profile_info.split("\n"):
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    wifi_credentials[profile] = password
                    break
            else:
                wifi_credentials[profile] = None
        except subprocess.CalledProcessError:
            wifi_credentials[profile] = None

    return wifi_credentials

# Print the Wi-Fi credentials
credentials = get_saved_wifi_passwords()
for wifi, password in credentials.items():
    print(f"SSID: {wifi}, Password: {password if password else 'N/A'}")
