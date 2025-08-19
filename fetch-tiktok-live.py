from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent
from TikTokLive.client.errors import UserOfflineError
import os
import json
import asyncio
from collections import deque

async def main():
    unique_id = input("Please enter the unique_id (e.g., @megaaziib): ")
    client = TikTokLiveClient(unique_id=unique_id)

    # Queue to store comments
    comments_queue = deque()

    @client.on(ConnectEvent)
    async def on_connect(event: ConnectEvent):
        print(f"Connected to @{event.unique_id} (Room ID: {client.room_id})")

    @client.on(CommentEvent)
    async def on_comment(event: CommentEvent):
        comment_data = {
            "user": event.user.nickname,
            "comment": event.comment
        }
        comments_queue.append(comment_data)
        print(f"{event.user.nickname} -> {event.comment}")

    async def save_to_json():
        while True:
            await asyncio.sleep(3)  # Wait for 5 seconds
            # Transform data before saving
            transformed_data = [
                {"author": data["user"], "message": data["comment"]}
                for data in comments_queue
            ]
            with open('chat_saved.json', 'w') as json_file:
                json.dump(transformed_data, json_file, indent=2)

    try:
        save_task = asyncio.create_task(save_to_json())
        await client.start()
        await save_task
    except UserOfflineError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.stop()
        await client.join()

if __name__ == '__main__':
    asyncio.run(main())

