import jwt

from datetime import datetime, timedelta, timezone

from django.conf import settings

def translit_1(str_1): #Программа для транслитерации
    str_2 = ""
    ru_eng = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-', '(': '', ')': '',
        'А': 'a', 'Б': 'b', 'В': 'v', 'Г': 'g', 'Д': 'd',
        'Е': 'e', 'Ё': 'yo', 'Ж': 'zh', 'З': 'z', 'И': 'i',
        'Й': 'y', 'К': 'k', 'Л': 'l', 'М': 'm', 'Н': 'n',
        'О': 'o', 'П': 'p', 'Р': 'r', 'С': 's', 'Т': 't',
        'У': 'u', 'Ф': 'f', 'Х': 'kh', 'Ц': 'ts', 'Ч': 'ch',
        'Ш': 'sh', 'Щ': 'sch', 'Ы': 'y', 'Э': 'e', 'Ю': 'yu', 'Я': 'ya', 'Ъ': '',
        'Ь': ''
    }
    for i in range(len(str_1)):
        if str_1[i] in ru_eng:
            str_2 = str_2 + ru_eng[str_1[i]]
        else:
            str_2 = str_2 + str_1[i]

    return str_2

def create_access_token(user_id: int, username: str) -> str:

    expire = datetime.now(datetime.UTC) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": str(user_id), # subject — кому выдан токен
        "username": username,
        "exp": expire, # expiration — когда истекает
        "iat": datetime.now(timezone.utc), # issued at — когда выдан#
            }

    encoded_jwt = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt
