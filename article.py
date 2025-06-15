from dataclasses import dataclass


@dataclass
class Article:
    title: str
    content: str
    photo: str
    id: int = None


@dataclass
class User:
    email: str
    phone: str
    id: int = None
