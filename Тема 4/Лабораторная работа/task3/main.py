def delete(ls, index=None) -> list:
    if index is None:
        return ls [: -1].copy()

    if index < 0 or index > len(ls):
        return  ls.copy()

    return ls[: index] + ls[index + 1:]

print(delete([0, 0, 1, 2, 3, 4]))
print(delete([0, 0, 1, 2, 3, 4], index=0))
print(delete([0, 0, 1, 2, 3, 4], index=10))
print(delete([0, 0, 1, 2, 3, 4], index=2))
print(delete([0, 0, 1, 2, 3, 4], index=5))
