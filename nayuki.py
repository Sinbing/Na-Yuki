# -*- coding: utf-8 -*-
import os
import time
from ruamel.yaml import YAML as yaml

#========= User variable =========#
MCDR_server_list_yaml_path = os.path.join(os.path.abspath('.'),'mcdrServerList.yaml')
minecraft_server_yaml_path = os.path.join(os.path.abspath('.'),'minecraftServer.yaml')
#========== String Here ==========#
kill_all_screen: str = '''screen -wipe
screen -ls | grep Detached | cut -d. -f1 | awk '{print $1}' | xargs kill
sleep 1
'''
help_message = '''今天想要yuki干点啥：
1. 重启所有服务器
2. 关闭所有服务器
3. 重载所有子服的MCDR
4. 重载所有子服的ChatBridge
'''
DEBUG_FLAG = True
#========== String Done ==========#


def send_cmd(cmd: str):
    os.system(cmd)


def execute_screen_command(operate_type: str, screen_name:str, server_path: str, run_command:str):
    # create new screen.
    if operate_type == 'create':
        command = ('screen -RU {0} -p 0 -X stuff "cd {1}\n{2}\n"'.format(screen_name, server_path, run_command))
        return command
    # run command in screen.
    elif operate_type == 'execute':
        command = ('screen -xU {0} -p 0 -X stuff "{1}\n"'.format(screen_name, run_command))
        return command


def run_command_from_yaml(operate_type: str, yaml_path: str, command: str):
    # open .yaml file to get server info.
    with open(yaml_path, encoding='utf-8') as file:
        server_dict = yaml().load(file)
    try:
        for server_path, server in server_dict.items():
            for server_name in server:
                server_full_path = os.path.join(server_path, server_name)
                if DEBUG_FLAG:
                    print(execute_screen_command(operate_type, server_name, server_full_path, command))
                else:
                    send_cmd(execute_screen_command(operate_type, server_name, server_full_path, command))
                    print('{} starting now.'.format(server_name))
                time.sleep(1)
    except AttributeError:
        print('no server in {}\n'.format(yaml_path))


def restart_server():
    # kill all exist screen.
    send_cmd(kill_all_screen)
    # start all minecraft server.
    run_command_from_yaml('create', minecraft_server_yaml_path, 'start.sh')
    run_command_from_yaml('create', MCDR_server_list_yaml_path, 'python3 -m mcdreforged')


def stoped_server():
    # stop all minecraft server.
    run_command_from_yaml('execute', MCDR_server_list_yaml_path, 'stop')
    run_command_from_yaml('execute', minecraft_server_yaml_path, 'stop')

def reload_mcdr():
    run_command_from_yaml('execute', MCDR_server_list_yaml_path, '!!MCDR r $1')


def reload_chatbridge():
    run_command_from_yaml('execute', MCDR_server_list_yaml_path, '!!ChatBridge $1')


def user_input_num():
    # format user input(1~3)
    while True:
        user_info = int(input(help_message))
        if user_info > 0:
            if user_info <= 4:
                break
        else:
            print("请输入选项所对应的数字\n  如: 1\n")
    return user_info



if __name__ == '__main__':
    user_selet_num = user_input_num()
    if user_selet_num == 1:
        restart_server()
    elif user_selet_num == 2:
        stoped_server()
    elif user_selet_num == 3:
        reload_mcdr()
    elif user_selet_num == 4:
        reload_chatbridge() 