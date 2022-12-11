import os
from slack_sdk.webhook import WebhookClient

url = os.environ.get('SLACK_WEBHOOK_URL')


def send_missing_id_notification(id):
    webhook = WebhookClient(url)
    response = webhook.send(text=f"Missing ID in spotify dictionary: {id}")