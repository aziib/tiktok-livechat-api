from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent
from TikTokLive.client.errors import UserOfflineError
import os

def main():
    unique_id = input("Please enter the unique_id (e.g., @megaaziib): ")
    client = TikTokLiveClient(unique_id=unique_id)

    @client.on(ConnectEvent)
    async def on_connect(event: ConnectEvent):
        print(f"Connected to @{event.unique_id} (Room ID: {client.room_id})")

    async def on_comment(event: CommentEvent) -> None:
        print(f"{event.user.nickname} -> {event.comment}")

    client.add_listener(CommentEvent, on_comment)

    try:
        # Try to connect to the TikTok LIVE stream
        client.run()
    except UserOfflineError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':

    main()
