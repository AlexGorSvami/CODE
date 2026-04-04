def decodeCiphertext(encodedText: str, rows: int) -> str:
    n = len(encodedText)
    cols = n // rows
    res = []
    for i in range(cols):
        for j in range(min(rows, cols-i)):
            res.append(encodedText[j*cols + i + j])
    return ''.join(res).rstrip()
