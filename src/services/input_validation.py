def valid_login(login:str) -> bool:
    if(len(login) > 255 or len(login) == 0): return False

    return True

def valid_email(email:str) -> bool:
    if (len(email) > 255 or len(email) == 0): return False

    if (("@gmail.com" in email) or ("@mail.ru" in email) or ("@yandex.ru" in email) or ("@email.com" in email) or ("@email.ru" in email)):
        return True
    else:
        return False

def valid_password(password:str) -> bool:
    if(len(password) > 255 or len(password) == 0): return False

    return True