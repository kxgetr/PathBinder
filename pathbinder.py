import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    import re
    from urllib.parse import quote
    return re.sub('\\{([A-Za-z_][A-Za-z0-9_]*)\\}', lambda m: quote(str(data['values'][m[1]]), safe=''), data['template'])

def main():
    parser = argparse.ArgumentParser(description='Yol şablonundaki parametreleri URL güvenli segmentlere çevirir.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
