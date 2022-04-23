
import os

def get_dir_size(start_path:str=".") -> float:
    total_size : float = 0.0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def size_file_in_megabytes(path_input:str) -> float:
    return round(
        os.stat(path_input).st_size / (1024 * 1024),
        3,
    )
