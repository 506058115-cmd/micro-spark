#!/usr/bin/env python3
"""Render newline-separated numbers as a compact sparkline."""

import argparse
import math
from pathlib import Path
import sys


LEVELS = "▁▂▃▄▅▆▇█"


def terminal_safe(value):
    return "".join(
        char if char.isprintable() else char.encode("unicode_escape").decode("ascii")
        for char in value
    )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="把每行一个数字画成终端微型图表。"
    )
    parser.add_argument(
        "source", nargs="?", default="-", help="文本文件；省略时从标准输入读取"
    )
    args = parser.parse_args(argv)

    try:
        if args.source == "-":
            content = sys.stdin.read()
        else:
            content = Path(args.source).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"micro-spark: {terminal_safe(str(error))}", file=sys.stderr)
        return 2

    # ponytail: keep the full input for exact scaling; spool or sample huge streams if needed.
    values = []
    for line_number, line in enumerate(content.splitlines(), 1):
        token = line.strip()
        if not token:
            continue
        try:
            value = float(token)
        except ValueError:
            print(f"micro-spark: 第 {line_number} 行不是数字：{token!r}", file=sys.stderr)
            return 2
        if not math.isfinite(value):
            print(f"micro-spark: 第 {line_number} 行不是有限数字。", file=sys.stderr)
            return 2
        values.append(value)

    if not values:
        print("micro-spark: 没有读到数字。", file=sys.stderr)
        return 1

    low, high = min(values), max(values)
    graph_low, graph_high = low, high
    graph_values = iter(values)
    if high != low and not math.isfinite(high - low):
        graph_low, graph_high = low / 2, high / 2
        graph_values = (value / 2 for value in values)
    span = graph_high - graph_low
    levels = LEVELS
    try:
        levels.encode(sys.stdout.encoding or "utf-8")
    except (LookupError, UnicodeEncodeError):
        levels = ".:-=+*#@"
    middle = len(levels) // 2
    sparkline = "".join(
        levels[
            middle
            if high == low
            else round((value - graph_low) / span * (len(levels) - 1))
        ]
        for value in graph_values
    )
    print(sparkline)
    print(f"最小值 {low:g} · 最大值 {high:g} · 共 {len(values)} 个")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
