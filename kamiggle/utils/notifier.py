from typing import Optional

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_slack_message(token: str, channel: str, text: str) -> Optional[bool]:
    """指定したSlackチャネルにメッセージを送信します。

    Args:
        token (str): Slack APIのトークン。
        channel (str): メッセージを送信するチャネルの名前またはID。
        text (str): 送信するメッセージのテキスト。

    Returns:
        bool: メッセージ送信が成功したかどうかを示す。失敗した場合はNoneを返す。

    """
    client = WebClient(token=token)

    try:
        response = client.chat_postMessage(channel=channel, text=text)
        return response["ok"]
    except SlackApiError as e:
        # メッセージの送信に失敗した場合、エラーを出力
        print(f"Error sending message: {e}")
        return None
