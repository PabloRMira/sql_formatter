# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_format_file.ipynb (unless otherwise specified).

__all__ = ['check_sql_query', 'format_sql_commands', 'format_sql_file', 'format_sql_files']

# Cell
import re
import os
from fastcore.script import call_parse, Param
from .core import format_sql, assert_and_print

# Cell
def check_sql_query(s):
    "Checks whether `s` is a SQL query"
    return bool(re.match(pattern=r"^\n*(?:select|create)", string=s, flags=re.I))

# Cell
def format_sql_commands(s):
    "Format SQL commands in `s`"
    s = s.strip()  # strip file contents
    split_s = s.split(";")  # split by semicolon
    # format only SQL queries, let everything else unchanged
    formatted_split_s = [
        "\n\n" + format_sql(sp, add_semicolon=False)
        if check_sql_query(sp)
        else sp
        for sp in split_s
    ]
    # join by semicolon
    formatted_s = ";".join(formatted_split_s)
    # add newline at the end of file
    formatted_s = formatted_s + "\n"
    return formatted_s

# Cell
def format_sql_file(f):
    """Format file `f` with SQL commands and overwrite the file.
    Return 0 for no change and 1 for formatting adjustments"""
    # open the file
    with open(f, "r") as file:
        sql_commands = file.read()
    # format SQL statements
    formatted_file = format_sql_commands(sql_commands)
    exit_code = 0 if sql_commands == formatted_file else 1
    # overwrite file
    with open(f, "w") as f:
        f.write(formatted_file)
    return exit_code

# Cell
@call_parse
def format_sql_files(
    files: Param(help="Path to SQL files", type=str, nargs="+")
):
    "Format SQL `files`"
    exit_codes = []
    for file in files:
        exit_codes.append(format_sql_file(file))
    if sum(exit_codes) == 0:
        print("Nothing to format, everything is fine!")
    else:
        print("All done!")