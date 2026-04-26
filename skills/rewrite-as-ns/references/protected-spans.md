# Protected Spans

This file defines content that must be preserved exactly during rewriting.

## Primary Protected Pattern

Treat any content enclosed in double square brackets as fixed:

- `[[ ... ]]`

Do not modify, translate, paraphrase, reorder internally, or delete anything inside these brackets.

## Handling Rules

- preserve the exact character sequence inside the protected span
- do not change capitalization, punctuation, spacing, symbols, or placeholders inside the span
- you may rewrite the surrounding sentence, but the protected span itself must remain untouched
- if punctuation around the span must move for grammatical reasons, move only the external punctuation

## Default Additional Protected Content

Unless the user explicitly says otherwise, also treat the following as effectively protected when rewriting would risk corruption:

- equation fragments
- code-like identifiers
- variable names
- figure, table, and citation anchors whose exact formatting matters
- chemical formulas, gene names, or other symbol-heavy expressions when the exact form is important

## Conflict Rule

If a protected span makes the sentence awkward, preserve it anyway and repair only the surrounding syntax.

## Reporting Rule

If a protected span prevents a smoother rewrite, note that briefly in `editor_feedback` rather than altering the span.
