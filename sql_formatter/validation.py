# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_validation.ipynb (unless otherwise specified).

__all__ = ['validate_semicolon']

# Cell
from .utils import *

# Cell
def validate_semicolon(s):
    """Validate query `s` by looking for forgotten semicolon.
    The implication could be the keyword CREATE appearing twice"""
    positions = identify_create(s)
    if len(positions) > 1:
        validation = {
            "exit_code": 1,
            "val_lines": find_line_number(s, positions),
            "total_lines": count_lines(s)
        }
    else:
        validation = {
            "exit_code": 0,
            "total_lines": count_lines(s)
        }
    return validation