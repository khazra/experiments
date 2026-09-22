# Reproducible review contract

`rubric.json` is the complete executed rubric, including measurement rules, evidence locators, opinion boundaries and four explicitly unmeasurable dimensions. Private source paths are replaced by aliases.

`schemas.json` exports the actual stage schemas from the executed workflow. Validate a stage against its corresponding `$defs` entry. These definitions describe outputs; they are not an executable workflow or deployment. Private review records and their original identifiers are not bundled. The public individual Markdown reviews retain all original fields and limitations with sanitized locators.
