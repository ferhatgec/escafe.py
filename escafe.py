# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#
# escafe.py - parser & generator for escape sequences (external whitespace sequence support (\w))
#           - python3 implementation of escafe
#
# github.com/ferhatgec/escafe.py
# github.com/ferhatgec/escafe

class escafe:
    @staticmethod
    def run(data: str) -> str:
        __data = ''

        is_escape, is_ansi = False, False

        collect = ''

        for ch in data:
            if not is_ansi and not len(collect) == 0:
                if collect == '033':
                    __data += '\033'
                elif collect == 'x1b':
                    __data += '\x1b'

                collect = ''

            if is_escape:
                if ch == '\'':
                    __data += '\''
                elif ch == '"':
                    __data += '"'
                elif ch == '?':
                    __data += '?'
                elif ch == '\\':
                    __data += '\\'
                elif ch == 'a':
                    __data += '\a'
                elif ch == 'b':
                    if is_ansi:
                        collect += 'b'

                        is_escape = is_ansi = False

                        continue

                    __data += '\b'
                elif ch == 'f':
                    __data += '\f'
                elif ch == 'n':
                    __data += '\n'
                elif ch == 'r':
                    __data += '\r'
                elif ch == 't':
                    __data += '\t'
                elif ch == 'v':
                    __data += '\v'
                elif ch == 'w':
                    __data += ' '
                elif ch == 'x':
                    is_ansi = True
                    collect += 'x'

                    continue
                elif ch == '0':
                    if not is_ansi:
                        is_ansi = True

                    if is_ansi:
                        collect += '0'

                    continue
                elif ch == '1':
                    if is_ansi:
                        collect += '1'

                    continue
                elif ch == '3':
                    if collect.endswith('3'):
                        is_ansi = is_escape = False

                    # if is_ansi:
                    collect += '3'

                    continue

                is_escape = False
                continue

            if ch == '\\':
                is_escape = True
                continue

            __data += ch

        return __data
