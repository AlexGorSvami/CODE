import textwrap 


def wrap(string, max_width):
    convert = list(string)
    lines = []
    line = ''

    for i in convert:
        if len(line) < max_width:
            line += i

        else:
            lines.append(line)
            line = i

    lines.append(line)

    return '\n'.join(lines)

if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


