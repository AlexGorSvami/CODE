def removeSubfolders(folder: list) -> list:
    set_folder = set(folder)
    result_set = set(folder)
    for f in folder:
        list_f = f.split('/')
        cur = ''
        for i in range(1, len(list_f)-1):
            cur += '/' + list_f[i]
            if cur in set_folder:
                result_set.remove(f)
                break
    return list(result_set)
