# -*- coding: utf-8 -*-

from mytelegram import MyTelegram
from telethon import functions, errors


class Group:

    def __init__(self):
        self.telegram = MyTelegram()

    async def connect(self):
        await self.telegram.login()
        print(f"-> [INVITE LINK] {self.telegram.INVITE_LINK}")
        print(f"-> [CHANNEL ID]  {self.telegram.channel.channel_id}")

    async def topic(self, topic_id=None) -> []:
        """
         Select a topic and add each photo to the media_list
        :return:
        """
        emoticons_list = []
        async for message in self.telegram.takeout.iter_messages(self.telegram.channel.channel_id,
                                                                 limit=None,
                                                                 reverse=False,
                                                                 wait_time=1,
                                                                 reply_to=topic_id,
                                                                 min_id=0,
                                                                 max_id=0):

            # Check each message for emoticonss
            if message.reactions:
                if message.reactions.results:
                    for result in message.reactions.results:
                        try:
                            # print('U+{:X}'.format(ord(result.reaction.emoticon)))
                            print(f"[Emoticon]: ** {result.reaction.emoticon} **\n")
                            emoticons_list.append(result.reaction.emoticon)
                        except AttributeError:
                            pass
            else:
                print(f"[Messaged ID]:{message.id} No Emoticon")
        return emoticons_list

    async def forum_topics(self) -> []:
        """
         Using TL reference : https://docs.telethon.dev/en/stable/concepts/full-api.html#functions
        Get a list of topics from a channel entity
        :param topic_id: topic ID
        :return: list of topics
        """
        try:
            result = await self.telegram.takeout(functions.channels.GetForumTopicsRequest(
                channel=self.telegram.channel,  # channel entity
                offset_date=None,
                offset_id=0,
                offset_topic=0,
                limit=100,  # Hardcoded see pagination - https://core.telegram.org/api/offsets
                q=None
            ))

        except errors.ChannelForumMissingError:
            print("No topics found.")
            return []

        print(".:LIST OF TOPICS:.")
        topic_ids = [[topic.id, topic.title] for topic in result.topics]
        for index, (topic_id, topic_title) in enumerate(topic_ids):
            print(f"[{index}] {topic_title} {topic_id}")
        return topic_ids
