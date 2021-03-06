#!/usr/bin/env python
"""
Styled similar to tqdm, another progress bar implementation in Python.

See: https://github.com/noamraph/tqdm
"""
from __future__ import unicode_literals
from prompt_toolkit.shortcuts.progress_bar import progress_bar
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts.progress_bar import formatters
import time

style = Style.from_dict({
    '': 'cyan',
})


def main():
    custom_formatters = [
        formatters.Label(suffix=': '),
        formatters.Bar(start='|', end='|', sym_a='#', sym_b='#', sym_c='-'),
        formatters.Text(' '),
        formatters.Progress(),
        formatters.Text(' '),
        formatters.Percentage(),
        formatters.Text(' [elapsed: '),
        formatters.TimeElapsed(),
        formatters.Text(' left: '),
        formatters.TimeLeft(),
        formatters.Text(', '),
        formatters.IterationsPerSecond(),
        formatters.Text(' iters/sec]'),
        formatters.Text('  '),
    ]

    with progress_bar(style=style, formatters=custom_formatters) as pb:
        for i in pb(range(1600), label='Installing'):
            time.sleep(.01)


if __name__ == '__main__':
    main()
