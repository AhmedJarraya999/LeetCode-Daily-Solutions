from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.path = []
        self.serial = ""
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # 1. Build the Trie
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
            node.path = path  # store path at leaf node

        # 2. Map serialized subtree to its count
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            parts = []
            for name in sorted(node.children):
                child = node.children[name]
                sub_serial = serialize(child)
                parts.append(f"{name}({sub_serial})")
            serial = "".join(parts)
            node.serial = serial
            serial_map[serial].append(node)
            return serial

        serialize(root)

        # 3. Mark duplicates for deletion
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # 4. Collect remaining valid paths
        res = []

        def collect(node, path):
            for name, child in node.children.items():
                if not child.deleted:
                    new_path = path + [name]
                    res.append(new_path)
                    collect(child, new_path)

        collect(root, [])
        return res
