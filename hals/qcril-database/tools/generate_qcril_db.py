#!/usr/bin/env python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import os
import re
import sqlite3
import sys


def version_prefix(file_path):
    basename = os.path.basename(file_path)
    match = re.match(r'(\d+(\.\d+)?)', basename)
    return [int(part) for part in match.group(0).split('.')] if match else []


def main():
    if len(sys.argv) <= 2:
        print('syntax: generate_qcril_db.py qcrilNr.db 0_initial_qcrilnr.sql 1_...')
        sys.exit(1)

    requested_db = os.path.abspath(sys.argv[1])
    target_db = os.path.realpath(requested_db)
    working_root = os.path.realpath(os.getcwd())
    if (os.path.basename(target_db) != 'qcrilNr.db'
            or os.path.commonpath([working_root, target_db]) != working_root
            or os.path.islink(requested_db)):
        raise ValueError('Database output must be qcrilNr.db within the build working directory')
    sql_files = sys.argv[2:]

    if os.path.exists(target_db):
        os.remove(target_db)

    config_sql_files = [file for file in sql_files if file.endswith('_config.sql')]
    ecc_sql_files = [file for file in sql_files if not file.endswith('_config.sql')]
    config_sql_files.sort(key=version_prefix)
    ecc_sql_files.sort(key=version_prefix)

    with sqlite3.connect(target_db) as conn:
        cursor = conn.cursor()
        for file in ecc_sql_files + config_sql_files:
            try:
                with open(file, 'r') as sql_file:
                    cursor.executescript(sql_file.read())
            except Exception as error:
                print(f'Failed to apply {file}: {error}')
                sys.exit(1)


if __name__ == '__main__':
    main()
