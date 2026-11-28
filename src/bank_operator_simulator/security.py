import functools
from bank_operator_simulator import exceptions as exc

ADMIN_D = {'admin': '123'}

def require_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        admin_login = list(ADMIN_D.keys())[0]
        admin_password = list(ADMIN_D.values())[0]
        admin_list = [admin_login, admin_password]
        input_pass_list = [
            input('input admin login: '),
            input('input admin password: '),
        ]
        if admin_list != input_pass_list:
            raise exc.AdminAuthError()
        result = func(*args, **kwargs)
        return result
    return wrapper
