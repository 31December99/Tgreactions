# -*- coding: utf-8 -*-
import asyncio
from group import Group


def validate_user_input(topics: list) -> int:
    while True:
        index = input(f"Choose which topic you want to check (0-{len(topics) - 1}): ")
        if index.isnumeric():
            topic_index = int(index)
            if 0 <= topic_index <= len(topics) - 1:
                topic_id, topic_title = topics[topic_index]
                return topic_id


async def main():
    # New Group istance
    group = Group()
    # Connect to group
    await group.connect()
    # Get your Topics list

    list_of_topics = await group.forum_topics()
    if list_of_topics:
        topic_id = validate_user_input(list_of_topics)
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
