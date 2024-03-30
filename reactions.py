# -*- coding: utf-8 -*-
import asyncio
from group import Group


async def main():
    # New Group istance
    group = Group()
    # Connect to group
    await group.connect()
    # Get your Topics list
    topic_id = None
    list_of_topics = await group.forum_topics()
    if list_of_topics:
        while True:
            index = input(f"Choose which topic you want to check (0-{len(list_of_topics) - 1}): ")
            if index.isnumeric():
                topic_index = int(index)
                if 0 <= topic_index <= len(list_of_topics) - 1:
                    topic_id, topic_title = list_of_topics[topic_index]
                    break

    await group.topic(topic_id)
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
