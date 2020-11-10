# Author:xqkang
# Date:2020/10/7 上午9:19
def auth(auth_type):
    print("auth func:", auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                login_user = input("请输入登陆的用户名:")
                login_pwd = input("请输入登陆的密码:")
                if user == login_user and passwd == login_pwd:
                    print("\033[32;1m你已经成功登陆\033[0m")
                    return func(*args, **kwargs)
                else:
                    print("\033[31;1m验证失败\033[0m")
            elif auth_type == "ldap":
                print("搞毛线,不会")
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index!!!")

@auth(auth_type="local")
def home():
    print("welcome to home!!!")
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs")
user,passwd = "kxq","kxq123"



index()
print(home())
bbs()
