def find_path(node, filename):
    """
    Recursively searches the JSON tree for the given filename and returns the path to it.

    :param node: The current node in the JSON tree.
    :param filename: The name of the file to find.
    :return: A list representing the path from the root to the file, or None if not found.
    """
    if node['name'] == filename:
        return [node['name']]
    if 'children' in node:
        for child in node['children']:
            child_path = find_path(child, filename)
            if child_path:
                return [node['name']] + child_path
    return None

# Example usage:

# Sample JSON directory tree
directory_tree = {
    "name": "root",
    "children": [
        {
            "name": "dir1",
            "children": [
                {"name": "file1.txt"},
                {"name": "file2.txt"}
            ]
        },
        {
            "name": "dir2",
            "children": [
                {
                    "name": "dir3",
                    "children": [
                        {"name": "file3.txt"}
                    ]
                }
            ]
        }
    ]
}

# Find the path to 'file3.txt'
file_name = 'file1.txt'
path = find_path(directory_tree, file_name)

if path:
    full_path = '/'.join(path)
    print(f"The path to '{file_name}' is: {full_path}")
else:
    print(f"File '{file_name}' not found in the directory tree.")
