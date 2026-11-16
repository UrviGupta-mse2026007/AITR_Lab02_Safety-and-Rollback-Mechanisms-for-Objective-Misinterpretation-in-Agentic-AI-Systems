# AI assistance and human verification log

## Evidence boundary

This report is reconstructed from the available project files and conversation context. A complete exported prompt history, model/version per turn, Git commit history/diffs and standalone debugging notebook were not supplied. Therefore exact prompt wording, timestamps, version identifiers and authorship of each code decision cannot be authenticated retrospectively.

## Significant activities

| Activity | AI assistance | Human decision / verification | Outcome |
|---|---|---|---|
| Research framing | Helped narrow objective uncertainty and rollback into a tractable synthetic study | Kept the gap provisional; did not claim novelty without a dedicated literature search | Research question narrowed to a controlled policy comparison |
| Risk and recovery model | Proposed/clarified `impact * uncertainty * (1 - reversibility)` and residual-harm simulation | Treated 0.80 recovery fraction as an explicit modelling assumption | Implemented a transparent synthetic simulator |
| Policy implementation | Helped explain and structure three policies | Retained them as custom simplified controls, not published reproductions | Three comparable policy functions |
| Data protocol | Helped describe grouped development/validation/test partitions and threshold selection | Checked 360/120/120 split sizes, unique IDs and no template overlap | Dataset integrity checks passed |
| Portability/debugging | Identified hard-coded `/content/...` path in tests | Replaced it with repository-relative path and ran tests | Five modular tests passed in current environment |
| Reporting | Helped interpret trade-offs and flag inconsistencies | Preserved the observed result that fixed + rollback had lowest test residual harm; risk-aware reduced interventions/FPR | Claims limited to this synthetic split |

## Real limitations / verification examples

1. **Hard-coded path failure:** the original test suite failed in a fresh extracted directory with `ModuleNotFoundError: No module named 'simulator'`. The import path was changed to a path relative to the test file, and the five-test suite then passed.
2. **Dependency warning:** `pip check` reported that IPython 7.34.0 required `jedi`, which was missing. Numerical package imports were reported to work; no complete dependency repair was documented.
3. **Test-count inconsistency:** notebook documentation reports six passing tests, while the modular test file has five. The current modular run confirms five. The notebook/report count still needs correction or explanation.
4. **Figure filename mismatch:** the earlier notebook/PDF workflow used inconsistent expected filenames. A new modular figure-generation script now creates a consistent trio of PNG/PDF outputs; the old notebook workflow still needs reconciliation.

## Human reasoning that determined the conclusions

- The proposed gap is a candidate research direction, not proven novelty.
- The benchmark is synthetic and cannot establish real-world agent safety.
- Recovery fraction 0.80 is assumed, not measured.
- Fixed + rollback has the lowest test residual harm; risk-aware + rollback has lower intervention and false-positive rates. This is a trade-off, not a universal winner.
- Test results have been viewed; no claim of a completely untouched test set is made.

## Reflection on vibe coding

AI-assisted coding accelerated scaffolding, code explanation, test design, debugging suggestions and documentation. However, generated code is a proposal rather than evidence. Human inspection exposed portability problems, dependency warnings, mismatched test counts and figure naming inconsistencies. Every material claim still required execution or inspection of actual outputs.

## Remaining risks

- No complete original prompt export or model-version-per-turn record.
- No Git commit/diff history was supplied.
- One synthetic seed and no uncertainty intervals.
- Assumed rollback effectiveness.
- Test results viewed.
- Fresh-machine reproduction and final notebook/PDF consistency checks remain outstanding.
