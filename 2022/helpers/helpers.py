def read_values(path: str, parser=None, separator='\n') -> tuple:
    """Reads values from a specific file. Applies a parser function if specified."""
    with open(path, 'r') as f:
        return parse_values(f.read(), parser, separator)


def parse_values(text: str, parser=None, separator='\n') -> tuple:
    """Reads values from a string. Applies a parser function if specified."""
    lines = text.split(separator)
    return tuple(map(parser, lines) if parser else lines)


def read_str(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()


def read_int(file: str) -> int:
    return int(read_str(file))
