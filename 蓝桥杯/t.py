class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0  # Number of segments satisfying the condition
        self.left = None
        self.right = None


def build_segment_tree(segments):
    if not segments:
        return None

    def build_tree(start, end):
        if start == end:
            return SegmentTreeNode(segments[start][0], segments[start][1])

        mid = (start + end) // 2
        root = SegmentTreeNode(segments[start][0], segments[end][1])
        root.left = build_tree(start, mid)
        root.right = build_tree(mid + 1, end)
        return root

    return build_tree(0, len(segments) - 1)


def count_segments(root, a, b):
    if not root or root.end <= a or root.start >= b:
        return 0

    if a <= root.start and root.end < b:
        return root.count

    return count_segments(root.left, a, b) + count_segments(root.right, a, b)


# Example usage
segments = [(1, 5), (2, 7), (6, 10), (12, 15)]
root = build_segment_tree(segments)

# Count segments containing a but not containing b
a = 3
b = 8
count = count_segments(root, a, b)
print(f"Number of segments containing {a} but not containing {b}: {count}")
