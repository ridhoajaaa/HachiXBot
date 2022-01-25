import threading

from sqlalchemy import Column, String

from HachiBot.modules.sql import BASE, SESSION

class SylChats(BASE):
    __tablename__ = "syl_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

SylChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_syl(chat_id):
    try:
        chat = SESSION.query(SylChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def rem_syl(chat_id):
    with INSERTION_LOCK:
        sylchat = SESSION.query(SylChats).get(str(chat_id))
        if not sylchat:
            sylchat = SylChats(str(chat_id))
        SESSION.add(sylchat)
        SESSION.commit()


def set_syl(chat_id):
    with INSERTION_LOCK:
        sylchat = SESSION.query(SylChats).get(str(chat_id))
        if sylchat:
            SESSION.delete(sylchat)
        SESSION.commit()
