# Release notes

## 0.6.2

### :tada: Bugfixes:
* [FIX] Table names that include the substring select in them break subsequent formatting ([#167](https://github.com/PabloRMira/sql_formatter/pull/167))
* [FIX] Variable names ending with `and` get split in WHERE statements ([#165](https://github.com/PabloRMira/sql_formatter/pull/165))

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Update contributing guidelines ([#164](https://github.com/PabloRMira/sql_formatter/pull/164))
* [MNT] Add .pre-commit-hooks.yaml ([#159](https://github.com/PabloRMira/sql_formatter/pull/159))

## 0.6.1

### :tada: Bugfixes:
* [FIX] reformating of long lines with in (...) not working ([#154](https://github.com/PabloRMira/sql_formatter/pull/154))
* [FIX] line comments with -- cancel further formatting ([#152](https://github.com/PabloRMira/sql_formatter/pull/152))
* [FIX] Unbound error in reformat_too_long_line ([#150](https://github.com/PabloRMira/sql_formatter/pull/150))

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Add a --version (-v) flag to the CLI ([#157](https://github.com/PabloRMira/sql_formatter/pull/157))

## 0.6.0

### :rocket: New features:
* [FEA] Add newline and indentation for too long lines ([#148](https://github.com/PabloRMira/sql_formatter/pull/148))

## 0.5.6

### :tada: Bugfixes:
* [FIX] Formatter does not add space after comma ([#147](https://github.com/PabloRMira/sql_formatter/pull/147))

## 0.5.5

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Change set based jacard distance by word count based disimilarity measure to robustify comment assignment ([#145](https://github.com/PabloRMira/sql_formatter/pull/145))

## 0.5.4

### :bulb: Documentation:
* [DOC] Add hint on how to install via conda

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] remove fastcore dependency ([#144](https://github.com/PabloRMira/sql_formatter/pull/144))
* [MNT] Remove deprecated CLIs

## 0.5.3

### :tada: Bugfixes:
* [FIX] Whole line comments should be aligned with the line under them ([#140](https://github.com/PabloRMira/sql_formatter/pull/140))
* [FIX] Semicolon under line with comment not properly formatted ([#139](https://github.com/PabloRMira/sql_formatter/pull/139))
* [FIX] PARTITION BY with newline not properly formatted ([#138](https://github.com/PabloRMira/sql_formatter/pull/138))

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Simplify package by removing release module ([#142](https://github.com/PabloRMira/sql_formatter/pull/142))
* [MNT] Robustify comment assignment ([#141](https://github.com/PabloRMira/sql_formatter/pull/141))

## 0.5.2

### :tada: Bugfixes:
* [FIX] case when wrongly formatted if case when at least in second argument and preceded by text in quotes ([#133](https://github.com/PabloRMira/sql_formatter/pull/133))
* [FIX] comment assignment fails sometimes ([#130](https://github.com/PabloRMira/sql_formatter/pull/130))

### :bulb: Documentation:
* [DOC] Fix wrong formatting in README ([#127](https://github.com/PabloRMira/sql_formatter/pull/127))

## 0.5.1

### :tada: Bugfixes:
* [FIX] Formatter adds whitespaces between symbols inside of quotes ([#121](https://github.com/PabloRMira/sql_formatter/pull/121))

### :bulb: Documentation:
* [DOC] Add docs for versioning and changelog ([#125](https://github.com/PabloRMira/sql_formatter/pull/125))
* [DOC] Add docs for formatting logic ([#123](https://github.com/PabloRMira/sql_formatter/pull/123))
* [DOC] Correct docs for contributing: fork instead of branch ([#122](https://github.com/PabloRMira/sql_formatter/pull/122))

## 0.5.0

### :rocket: New features:
* [FEA] Add newline for each case when ... end condition and make functions robust against keywords in comments ([#112](https://github.com/PabloRMira/sql_formatter/pull/112))

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Add link to pull request in changelog ([#114](https://github.com/PabloRMira/sql_formatter/pull/114))

## 0.4.0

### :tada: Bugfixes:
* [FIX] case when wrongly formatted if comment after condition ([#106](https://github.com/PabloRMira/sql_formatter/pull/106))
* [FIX] Formatting of comment after semicolon ([#104](https://github.com/PabloRMira/sql_formatter/pull/104))

### :rocket: New features:
* [FEA] Add validator for case when ... end ([#102](https://github.com/PabloRMira/sql_formatter/pull/102))

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Refactor code basis ([#105](https://github.com/PabloRMira/sql_formatter/pull/105))

## 0.3.2

### :tada: Bugfixes:
* [FIX] comment marker [CI] failing sometimes ([#97](https://github.com/PabloRMira/sql_formatter/pull/97))
* [FIX] SELECT DISTINCT fields not being formatted properly ([#96](https://github.com/PabloRMira/sql_formatter/pull/96))

## 0.3.1

### :tada: Bugfixes:
* [FIX] Semicolon / CREATE validation fails ([#85](https://github.com/PabloRMira/sql_formatter/pull/85))
* [FIX] Fields in ORDER BY in PARTITION BY with wrong indentation ([#84](https://github.com/PabloRMira/sql_formatter/pull/84))
* [FIX] View name is wrongly written uppercase in CREATE OR REPLACE VIEW my_view AS ([#79](https://github.com/PabloRMira/sql_formatter/pull/79))

### :rocket: New features:
* [FEA] Add CLI to handle git release and changelog creation programmatically via commit messages ([#87](https://github.com/PabloRMira/sql_formatter/pull/87))
* [FEA] Add formatting for multiline comments ([#86](https://github.com/PabloRMira/sql_formatter/pull/86))
* [FEA] Separate each ON join by newline ([#80](https://github.com/PabloRMira/sql_formatter/pull/80))

### :bulb: Documentation:
* [DOC] Add docs for maintenance / refactoring ([#89](https://github.com/PabloRMira/sql_formatter/pull/89))
* [DOC] Update README ([#82](https://github.com/PabloRMira/sql_formatter/pull/82))
* [DOC] Add hint for contributors to install the package in editable mode for the CLI to incorporate changes in code basis ([#81](https://github.com/PabloRMira/sql_formatter/pull/81))

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Refactor / Simplify code basis, remove deprecated functions, adjust docs ([#90](https://github.com/PabloRMira/sql_formatter/pull/90))

## 0.2.0

### :tada: Bugfixes:
* [FIX] SELECT .. FROM split if some of they keywords in quotes ([#71](https://github.com/PabloRMira/sql_formatter/pull/71))
* [FIX] case when in function does not get proper indentation ([#65](https://github.com/PabloRMira/sql_formatter/pull/65))
* [FIX] ORDER BY formatting within PARTITION BY ([#63](https://github.com/PabloRMira/sql_formatter/pull/63))
* [FIX] Text in quotes is wrongly lowercased ([#62](https://github.com/PabloRMira/sql_formatter/pull/62))
* [FIX] Do not split if ; is in comments ([#61](https://github.com/PabloRMira/sql_formatter/pull/61))
* [FIX] Formatting for CREATE ... TABLE / VIEW should be more general ([#60](https://github.com/PabloRMira/sql_formatter/pull/60))
* [FIX] Ambiguous report message ([#58](https://github.com/PabloRMira/sql_formatter/pull/58))
* [FIX] UNION (join) has no formatting ([#57](https://github.com/PabloRMira/sql_formatter/pull/57))

### :rocket: New features:
* [FEA] Add validation for balanced parenthesis ([#73](https://github.com/PabloRMira/sql_formatter/pull/73))
* [FEA] Add validation for missing semicolon ; ([#72](https://github.com/PabloRMira/sql_formatter/pull/72))
* [FEA] Add CLI funcitonality to format files recursively in subfolders ([#68](https://github.com/PabloRMira/sql_formatter/pull/68))
* [FEA] Add CLI functionality for wildcards * ([#59](https://github.com/PabloRMira/sql_formatter/pull/59))

### :bulb: Documentation:
* [DOC] Add docs for how to contribute ([#74](https://github.com/PabloRMira/sql_formatter/pull/74))

## 0.1.2

### :tada: Bugfixes:
* [FIX] CREATE TASK wrongly identified as query ([#42](https://github.com/PabloRMira/sql_formatter/pull/42))
* [FIX] PARTITION BY, SELECT DISTINCT and tests for ORDER BY and PARTITION BY ([#39](https://github.com/PabloRMira/sql_formatter/pull/39))

### :bulb: Documentation:
* [DOC] Write docs for how to install and add CI and Pypi images ([#40](https://github.com/PabloRMira/sql_formatter/pull/40))

## 0.1.1

### :tada: Bugfixes:
* [FIX] SELECT adds newline for function arguments and outsource auxiliary functions to utils ([#35](https://github.com/PabloRMira/sql_formatter/pull/35))
* [FIX] PARTITION BY not properly formatted and No formatting for ORDER BY ([#33](https://github.com/PabloRMira/sql_formatter/pull/33))
* [FIX] ON formatting does not work properly ([#31](https://github.com/PabloRMira/sql_formatter/pull/31))