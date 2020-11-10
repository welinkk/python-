# Author:xqkang
# Date:2020/10/11 上午11:35
import os
'''
# 获取当前的目录 /home/xqkang/PycharmProjects/pythonProject1/day9
print(os.getcwd())

# 切换目录 /
# os.chdir("/")
# print(os.getcwd())

# 当前目录 只打印 .
print(os.curdir)

# 上级目录 只打印 ..
print(os.pardir)

# 创建一个文件夹
os.mkdir("a")

os.makedirs('/home/xqkang/a/b')

# 删除dir 为空则删除目录
os.removedirs('/home/xqkang/a/b')

os.mkdir("a")
# 只删除一层
os.rmdir("a")

# 列出当前目录
# print(os.listdir(".."))

# 列出dir 的状态信息 os.stat_result(st_mode=16893, st_ino=3022883, st_dev=2050, st_nlink=2, st_uid=1000, st_gid=1000, st_size=4096, st_atime=1602464867, st_mtime=1602464867, st_ctime=1602464867)
print(os.stat("a"))

# 文件分隔符 解决不同系统不一致的问题
print(os.sep)
# 换行符
print(os.linesep)
# 查看系统环境变量
# environ({'PATH': '/home/xqkang/PycharmProjects/pythonProject1/venv/bin:/home/xqkang/.local/bin:/usr/local/jdk1.8/lib:/usr/local/hadoop/bin:/usr/local/jdk1.8/jre/lib:/opt/apache-maven-3.6.3/bin:/usr/local/jdk1.8/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/mongodb/bin', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'XMODIFIERS': '@im=fcitx', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'GDMSESSION': 'ubuntu', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'TEXTDOMAINDIR': '/usr/share/locale/', 'GTK_IM_MODULE': 'fcitx', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'PS1': '(venv) ', 'XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'JRE_HOME': '/usr/local/jdk1.8/jre', 'SSH_AGENT_PID': '3859', 'QT4_IM_MODULE': 'fcitx', 'SESSION_MANAGER': 'local/xqkang:@/tmp/.ICE-unix/3759,unix/xqkang:/tmp/.ICE-unix/3759', 'USERNAME': 'xqkang', 'LOGNAME': 'xqkang', 'PWD': '/home/xqkang/PycharmProjects/pythonProject1/day9', 'IM_CONFIG_PHASE': '2', 'PYCHARM_HOSTED': '1', 'LANGUAGE': 'zh_CN:zh', 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG', 'PYTHONPATH': '/home/xqkang/PycharmProjects/pythonProject1', 'SHELL': '/bin/bash', 'GIO_LAUNCHED_DESKTOP_FILE': '/usr/share/applications/pycharm.desktop', 'OLDPWD': '/qj/python-pycham/pycharm-community-2020.2.1/bin', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'GTK_MODULES': 'gail:atk-bridge', 'VIRTUAL_ENV': '/home/xqkang/PycharmProjects/pythonProject1/venv', 'CLUTTER_IM_MODULE': 'xim', 'TEXTDOMAIN': 'im-config', 'HADOOP_HOME': '/usr/local/hadoop', 'M2_HOME': '/opt/apache-maven-3.6.3', 'XDG_SESSION_DESKTOP': 'ubuntu', 'SHLVL': '0', 'QT_IM_MODULE': 'fcitx', 'JAVA_HOME': '/usr/local/jdk1.8', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'LANG': 'zh_CN.UTF-8', 'XDG_SESSION_ID': '2', 'XDG_SESSION_TYPE': 'x11', 'MONGODB_HOME': '/usr/local/mongodb', 'DISPLAY': ':0', 'LIBVIRT_DEFAULT_URI': 'qemu:///system', 'PYTHONIOENCODING': 'UTF-8', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'DESKTOP_SESSION': 'ubuntu', 'USER': 'xqkang', 'CLASSPATH': '/qj/python-pycham/pycharm-community-2020.2.1/lib/bootstrap.jar:/qj/python-pycham/pycharm-community-2020.2.1/lib/extensions.jar:/qj/python-pycham/pycharm-community-2020.2.1/lib/util.jar:/qj/python-pycham/pycharm-community-2020.2.1/lib/jdom.jar:/qj/python-pycham/pycharm-community-2020.2.1/lib/log4j.jar:/qj/python-pycham/pycharm-community-2020.2.1/lib/trove4j.jar:/qj/python-pycham/pycharm-community-2020.2.1/lib/jna.jar', 'XDG_MENU_PREFIX': 'gnome-', 'GIO_LAUNCHED_DESKTOP_FILE_PID': '4373', 'QT_ACCESSIBILITY': '1', 'WINDOWPATH': '2', 'GJS_DEBUG_OUTPUT': 'stderr', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'XDG_SEAT': 'seat0', 'PYTHONUNBUFFERED': '1', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'XDG_VTNR': '2', 'XDG_RUNTIME_DIR': '/run/user/1000', 'HOME': '/home/xqkang'})
print(os.environ)

# 环境变量的分隔符 ：
print(os.pathsep)

# 当前系统名： posix
print(os.name)

# 执行系统命令：例如列出当前dir test_datetime.py  test_os.py  test.py  test_random.py  test_time.py  验证码.py
print(os.system("dir"))
'''
print(os.system("ls"))

