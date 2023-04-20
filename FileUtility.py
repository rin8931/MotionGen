import os

def collect_path(dir_path):
    folder_file = os.listdir(dir_path)
    return folder_file

def collect_bvh_file_name(dir_path):
    result = []
    path_list = collect_path(dir_path)
    for path in path_list:
        root, ext = os.path.splitext(path)
        if ext == ".bvh":
            result.append(path)
    return result

def collect_bvh_file_path(dir_path):
    result = []
    path_list = collect_path(dir_path)
    for path in path_list:
        root, ext = os.path.splitext(path)
        if ext == ".bvh":
            result.append(dir_path + "/" + path)
    return result

if __name__ == "__main__":
    dir_path = "MotionData/data"
    path_list = collect_bvh_file_path(dir_path)


    print(path_list)