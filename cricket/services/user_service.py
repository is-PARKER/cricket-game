from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto
import data.__db_session as db_session
from data.users import User


def get_user_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(User).count()
    finally:
        session.close()


def find_user_by_username(username: str) -> Optional[User]:
    session = db_session.create_session()
    try:
        return session.query(User).filter(User.username == username).first()
    finally:
        session.close()


def create_user(username: str, email: str, password: str) -> Optional[User]:

    if find_user_by_username(username):
        return None

    user = User()
    user.email = email
    user.name = username
    user.hashed_password = hash_text(password)

    session = db_session.create_session()

    try:
        session.add(user)
        session.commit()
    finally:
        session.close()

    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(username: str, password: str) -> Optional[User]:
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            return None

        if not verify_hash(user.hashed_password, password):
            return None

        return user
    finally:
        session.close()


def find_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    finally:
        session.close()