# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_utils.ipynb (unless otherwise specified).

__all__ = ['assert_and_print', 'remove_whitespaces_newline', 'remove_whitespaces_comments',
           'remove_redundant_whitespaces', 'mark_comments', 'identify_newline_chars', 'replace_newline_chars',
           'identify_select_from', 'split_by_select_from', 'add_whitespaces_between_symbols', 'identify_end_of_fields',
           'add_newline_indentation', 'extract_outer_subquery', 'format_subquery', 'check_sql_query',
           'check_skip_marker', 'identify_semicolon', 'split_by_semicolon']

# Cell
import re

# Cell
def assert_and_print(s_in, s_expected):
    "Assert equality of `s_in` and `s_expected` and print the result of `s_in` if the assertion worked"
    try:
        assert s_in == s_expected
    except:
        print("Assertion failed\n")
        print("Input:\n")
        print(s_in)
        print("\n")
        print("Expected:\n")
        print(s_expected)
        assert s_in == s_expected
    print(s_in)
    return None

# Cell
def remove_whitespaces_newline(s):
    "Remove whitespaces before and after newline in `s`"
    s = re.sub(r"\n[\r\t\f\v ]+", "\n", s)  # remove whitespaces after newline
    s = re.sub(r"[\r\t\f\v ]+\n", "\n", s)  # remove whitespaces before newline
    return s

# Cell
def remove_whitespaces_comments(s):
    "Remove whitespaces before and after comment tokens in `s`"
    s = re.sub(r"\[C\][\r\t\f\v ]+", "[C]", s)  # remove whitespaces after comment token [C]
    s = re.sub(r"[\r\t\f\v ]+\[C\]", "[C]", s)  # remove whitespaces before comment token [C]
    s = re.sub(r"\[CS\][\r\t\f\v ]+", "[CS]", s)  # remove whitespaces after comment token [CS]
    s = re.sub(r"[\r\t\f\v ]+\[CS\]", "[CS]", s)  # remove whitespaces before comment token [CS]
    return s

# Cell
def remove_redundant_whitespaces(s):
    "Strip and emove redundant (more than 2) whitespaces in `s` but no newlines in between"
    s = s.strip()
    s = re.sub(r"[\r\t\f\v ]{2,}", " ", s)  # remove too many whitespaces but not newlines
    return s

# Cell
def mark_comments(s):
    "Mark end of comments -- and begin of comments /* */ if they are in a new line with token [C]"
    s = re.sub(r"(--.*?)(\n)", r"\1[C]\2", s)  # mark end of -- comments
    s = re.sub(r"(\/\*.*?\*\/)", r"\1[C]", s, flags=re.DOTALL)  # mark end of /* */ comments
    s = re.sub(r"(\n)\s*(--.*?)", r"\1[CS]\2", s, flags=re.DOTALL)  # mark start of comment line with --
    s = re.sub(r"(\n)\s*(\/\*.*\*\/)", r"\1[CS]\2", s)  # mark start of comment line with /*
    s = re.sub(r"(\n)\s*(\/\*.*\*\/)", r"\1[CS]\2", s, flags=re.DOTALL)  # mark start of comment line with /*
    return s

# Cell
def identify_newline_chars(s):
    "Identify newline characters in `s` but not in the comments"
    # container for positions
    positions = []
    # counter for comments
    k = 0  # 0 = no comment range
    # loop over character positions
    for i in range(len(s)):
        if s[i:i+1] == "\n" and k == 0:  # catch newline position
            positions.append(i)
        elif s[i:i+2] == "/*": # if there is an opening comment
            k += 1
        elif s[i:i+2] == "*/":  # if there is a closing comment
            k -= 1
    return positions

# Cell
def replace_newline_chars(s):
    "Replace newline characters in `s` by whitespace but not in the comments"
    positions = identify_newline_chars(s)
    clean_s = "".join([c if i not in positions else " " for i, c in enumerate(s)])
    return clean_s

# Cell
def identify_select_from(s):
    "Identify positions of SELECT and FROM in query `s`"
    # container for positions
    positions = []
    # counter for comments
    k = 0  # 0 = no comment range
    # loop over character positions
    for i in range(len(s)):
        if s[i:i+6].lower() == "select" and k == 0:  # catch SELECT
            positions.append(i)
        elif s[i:i+4].lower() == "from" and k == 0:  # catch FROM
            positions.append(i)
        elif s[i:i+2] in ("--" ,"/*"): # if there is an opening comment
            k += 1
        elif s[i:i+3] == "[C]":  # if there is a closing comment
            k -= 1
    return positions

# Cell
def split_by_select_from(s):
    "Split query `s` by statements SELECT and FROM"
    positions = identify_select_from(s)
    if 0 not in positions:
        positions = [0] + positions  # add the 0 position
    split_s = []
    # loop by pairs
    for start, end in zip(positions, positions[1:] + [None]):
        split_s.append(s[start:end])
    split_s = [elem for elem in split_s if elem != ""] # return non empty elements
    return split_s

# Cell
def add_whitespaces_between_symbols(s):
    "Add whitespaces between symbols in line `s`"
    s = re.sub(r"([^\s=!<>])([=!<>]+)", r"\1 \2", s, flags=re.I)  # no space left
    s = re.sub(r"([=!<>]+)([^\s=!<>])", r"\1 \2", s, flags=re.I)  # no space right
    s = re.sub(r"([^\s=!<>])([=!<>]+)([^\s=!<>])", r"\1 \2 \3", s, flags=re.I)  # no space left and right
    return s

# Cell
def identify_end_of_fields(s):
    "Identify end of fields in query `s`"
    # container for positions
    end_of_fields = []
    # counter for parenthesis and comments
    k = 0
    # loop over string characters
    for i, c in enumerate(s):
        if c == "," and k == 0:  # field without parenthesis or after closing parenthesis
            after_c = s[i:i+6]
            if not bool(re.search(r"(?:--|\/\*|\[C\]|\[CS\])", after_c)):
                end_of_fields.append(i)
        elif c == "(" or s[i:i+2] in ("--" ,"/*"): # if there is an opening parenthesis or comment
            k += 1
        elif c == ")" or s[i:i+3] == "[C]":  # if there is a closing parenthesis or closing comment
            k -= 1
    return end_of_fields

# Cell
def add_newline_indentation(s, indentation):
    "Add newline and indentation for end of fields in query `s`"
    split_s = []
    positions = identify_end_of_fields(s)
    if positions is []:
        return s
    else:  # add the first position 0
        # add + 1 for the end position
        positions = [0] + [pos + 1 for pos in positions]
    for start, end in zip(positions, positions[1:]+[None]):
        # strip from the left to remove whitespaces
        split_s.append(s[start:end].lstrip())  # get string part
        split_s.append("\n" + " " * indentation)  # add indentation
    s = "".join(split_s)
    s = s.strip()
    return s

# Cell
def extract_outer_subquery(s):
    "Extract outer subquery in query `s`"
    # initialize container for subquery positions
    # in string `s`
    subquery_pos = []
    # auxiliar indicator to get the subquery right
    ind = True
    # counter for parenthesis
    k = 0
    # loop over string characters
    for i, c in enumerate(s):
        if s[i:(i+8)] == "(\nSELECT" and ind: # query start
            subquery_pos.append(i)
            k = 0  # set the parenthesis counter to 0
            # turn off the indicator for the program to know
            # that we already hit the subquery start
            ind = False
        elif c == "(": # if there is a parenthesis not involving a subquery
            k += 1
        elif c == ")" and k == 0 and not ind: # end position for subquery
            subquery_pos.append(i)
            return subquery_pos
        elif c == ")":
            k -= 1

# Cell
def format_subquery(s, previous_s):
    "Format subquery in line `s` based on indentation on `previous_s`"
    s = re.sub(r"^\(\nSELECT", "(SELECT", s)  # remove newline between parenthesis and SELECT
    # get reference line for the indentation level
    # and remove whitespaces from the left
    last_line = previous_s.split("\n")[-1]
    ref_line = last_line.lstrip()
    # if the line contains a JOIN statement then indent with
    # 4 whitespaces
    if re.match(r"\w+ join", ref_line, flags=re.I):
        ref_line = "    " + ref_line
    indentation = len(ref_line) + 1  # get indentation level
    split_s = s.split("\n")  # get lines in subquery
    indented_s = [
        " " * indentation + line  # indent all lines the same
        if not re.match(r"SELECT", line)
        else line
        for line in split_s[1:]
    ]
    # SELECT line + indented lines afterwards
    formatted_split = [split_s[0]] + indented_s
    # concatenate with newline character
    formatted_s = "\n".join(formatted_split)
    return formatted_s

# Cell
def check_sql_query(s):
    "Checks whether `s` is a SQL query"
    return (bool(re.search(pattern=r".*(?:select|create.{0,10}(?:table|view)).*", string=s, flags=re.I)) and
            not bool(re.search(pattern=r"create(?!.*(?:table|view))", string=s, flags=re.I)))

# Cell
def check_skip_marker(s):
    "Checks whether user set marker /*skip-formatter*/ to not format query"
    return bool(re.search(r"\/\*skip-formatter\*\/", s))

# Cell
def identify_semicolon(s):
    "Identify semicolons in `s` but not in comments or quotes"
    # container for positions
    positions = []
    # counter for comments
    k = 0  # 0 = no comment range
    comment_open1 = False # comment indicator for /* */ comments
    comment_open2 = False  # comment indicator for -- comments
    quote_open1 = False  # quote '
    quote_open2 = False # quote "
    # loop over character positions
    for i, c in enumerate(s):
        if c == ";" and k == 0:
            positions.append(i)
        elif (
            s[i:i+2] == "/*" and
            not comment_open1 and
            not comment_open2 and
            not quote_open1 and
            not quote_open2
        ):  # if there is an opening comment /*
            k += 1
            comment_open1 = True
        elif (
            s[i:i+2] == "*/" and
            comment_open1 and
            not comment_open2 and
            not quote_open1 and
            not quote_open2
        ):  # if there is a closing comment */
            k -= 1
            comment_open1 = False
        elif (
            s[i:i+2] == "--" and
            not comment_open1 and
            not comment_open2 and
            not quote_open1 and
            not quote_open2
        ):  # if there is an opening comment --
            k += 1
            comment_open2 = True
        elif (
            c == "\n" and
            not comment_open1 and
            comment_open2 and
            not quote_open1 and
            not quote_open2
        ):  # if the -- comment ends
            k -= 1
            comment_open2 = False
        elif (
            c == "'" and
            not comment_open1 and
            not comment_open2 and
            not quote_open1 and
            not quote_open2
        ):  # if opening quote '
            k += 1
            quote_open1 = True
        elif (
            c == "'" and
            not comment_open1 and
            not comment_open2 and
            quote_open1 and
            not quote_open2
        ):  # if opening quote '
            k -= 1
            quote_open1 = False
        elif (
            c == '"' and
            not comment_open1 and
            not comment_open2 and
            not quote_open1 and
            quote_open2
        ):  # if opening quote '
            k += 1
            quote_open2 = True
        elif (
            c == '"' and
            not comment_open1 and
            not comment_open2 and
            not quote_open1 and
            quote_open2
        ):  # if opening quote '
            k -= 1
            quote_open2 = False
    return positions

# Cell
def split_by_semicolon(s):
    "Split string `s` by semicolon but not between parenthesis or in comments"
    positions = identify_semicolon(s)  # get semicolon positions
    if positions is []:  # if no semicolon then return full string
        return s
    # add the 0 position if there is no one
    positions = [0] + positions if 0 not in positions else positions
    # loop on start-end of string pairs
    split_s = []  # initialize output
    for start, end in zip(positions, positions[1:]+[None]):
        # return splits
        if start == 0:
            split_s.append(s[start:end])
        else:
            split_s.append(s[start+1:end])  # do not take the semicolon
    return split_s