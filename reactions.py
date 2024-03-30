# -*- coding: utf-8 -*-
import asyncio
from group import Group
from collections import Counter


async def main():
    # New Group istance
    group = Group()
    # Connect to group
    await group.connect()

    # Get topic ID and Image list
    emoticon_list = await group.topic(await group.input())

    # Reaction counter
    emote_counter = Counter(emoticon_list)
    for emoticon, occurrence in emote_counter.items():
        print(f"{emoticon}: {occurrence}")

    print(" Wait for Reaction Events !")
    while True:
        await asyncio.sleep(1)

    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        task_main = loop.create_task(main())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        pass
