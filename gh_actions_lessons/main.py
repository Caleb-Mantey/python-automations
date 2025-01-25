import requests

def send_discord_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}")

# Example usage
webhook_url = "https://discord.com/api/webhooks/1332483720296534087/jPo2eLAFw4uASEvlyEMPDlbwYOjys_Ffvq-5ueWDoM2AOOVjOsxqRCqtzNxqw_xmkFUa"
message = "This is from github actions!🤣🤣🤣🤣"
send_discord_message(webhook_url, message)