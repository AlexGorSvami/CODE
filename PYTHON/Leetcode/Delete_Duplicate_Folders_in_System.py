def deleteDuplicateFolder(paths: list) -> list:
    from collections import defaultdict 

    def Try():
        return defaultdict(Try)
    root = Try()

    for path in paths:
        node = root 
        for folder in path:
            node = node[folder]

    seen = defaultdict(list)

    def serialize(node):
        if not node:
            return ''
        serial = []
        for key in sorted(node.keys()):
            sub_serial = serialize(node[key])
            serial.append('{}({})'.format(key, sub_serial))
        res = ''.join(serial)
        seen[res].append(node)
        return res 

    serialize(root)
    to_delete_ids = set()
    for nodes in seen.values():
        if len(nodes) > 1:
            for node in nodes:
                to_delete_ids.add(id(node))
    result = []

    def dfs(node, path):
        for name, child in node.items():
            if id(child) not in to_delete_ids:
                new_path = path + [name]
                result.append(new_path)
                dfs(child, new_path)

    dfs(root, [])

    return result 
