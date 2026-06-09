from dataclasses import dataclass

from config import settings


@dataclass(frozen=True)
class User:
    """Учётные данные пользователя для авторизации."""

    login: str
    password: str


# Реестр тестовых пользователей по алиасу.
# Логин хранится в данных, пароль берётся из .env (секрет не коммитим в репозиторий).
USERS: dict[str, User] = {
    "КЗДТ": User(login="KZDTUSER", password=settings.PASSWORD),
}

DEFAULT_USER_ALIAS = "КЗДТ"


def get_user(alias: str = DEFAULT_USER_ALIAS) -> User:
    """Вернуть пользователя по алиасу.

    :raises KeyError: если алиас не зарегистрирован.
    """
    try:
        return USERS[alias]
    except KeyError:
        raise KeyError(
            f"Пользователь с алиасом '{alias}' не найден. Доступные: {list(USERS)}"
        )
