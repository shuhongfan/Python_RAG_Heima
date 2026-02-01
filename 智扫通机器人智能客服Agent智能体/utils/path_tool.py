import os

def get_project_root()->str:
    # 当前文件夹的绝对路径
    current_file = os.path.abspath(__file__)

    # 获取工程根目录，先获取文件所在的文件夹的绝对路径
    current_dir = os.path.dirname(current_file)

    # 获取工程根目录
    project_root = os.path.dirname(current_dir)
    return project_root

def get_abs_path(relative_path:str)->str:
    project_root = get_project_root()
    return os.path.join(project_root,relative_path)

if __name__ == '__main__':
    print(get_abs_path("config_data.py"))