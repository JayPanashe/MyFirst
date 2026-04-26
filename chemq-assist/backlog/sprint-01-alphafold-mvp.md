# Sprint 01 — AlphaFold MVP
## Goal
Build the first ChemQ AlphaFold-oriented MVP foundation: a protein target and partner scanner.

## Tasks
| ID | Task | Output | Priority |
|---|---|---|---|
| S01-01 | Research AlphaFold access routes | Technical note | High |
| S01-02 | Define target protein schema | `TargetProtein` model | High |
| S01-03 | Define structure evidence schema | `StructureEvidence` model | High |
| S01-04 | Build AlphaFold client scaffold | `alphafold/client.py` | High |
| S01-05 | Add offline fixtures | Test data | High |
| S01-06 | Add confidence scoring placeholder | `alphafold/scoring.py` | High |
| S01-07 | Create TB target pilot table | Starter dataset | Medium |
| S01-08 | Create enzyme pilot table | Starter dataset | Medium |
| S01-09 | Render first Markdown report | Prototype report | Medium |
| S01-10 | Add limitations note | Methods document | High |

## Definition of done
- AlphaFold module has schemas, client scaffold, scoring placeholder, and tests.
- No full AlphaFold DB download is attempted.
- External data access methods are documented.
- MVP limitations are clear.
