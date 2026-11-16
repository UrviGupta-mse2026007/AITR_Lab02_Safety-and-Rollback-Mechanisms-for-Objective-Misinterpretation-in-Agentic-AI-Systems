# Research Decisions Log

## Project
Objective-Uncertainty and Recovery Benchmark

## Risk score
R = impact * uncertainty * (1 - reversibility). This is a conceptual design
assumption, not a validated safety metric.

## Synthetic data
The benchmark contains 600 synthetic episodes across six scenario families.
Splits contain 360 development, 120 validation, and 120 test episodes.

## Rollback assumption
Recovered harm = initial harm * 0.80 * reversibility for an episode where
rollback is attempted. The recovery fraction and proportional recovery rule
are assumptions in the simulator.

## Policies
- Fixed threshold with rollback
- Fixed threshold without rollback
- Risk-aware policy with rollback

These are custom simplified policies, not faithful reproductions of published
algorithms.

## Threshold selection
Fixed threshold: 0.50
Risk-aware threshold: 0.10

Thresholds were selected using development data only. Validation and test
results were not used to select thresholds.

## Primary metric
Mean residual harm.

## Additional metrics
Intervention rate, false-positive rate, rollback rate, mean initial harm,
and mean harm recovered.

## Limitations
- Data and outcomes are synthetic.
- The rollback recovery model is assumed, not empirically validated.
- Policy thresholds use different score scales.
- Results from one seed do not quantify run-to-run variability.
- The benchmark does not run a full LLM agent or real external tools.
- The results do not demonstrate real-world AI safety.

## Future work
1. Run experiments across multiple independent seeds.
2. Report uncertainty intervals.
3. Compare policies at matched intervention budgets.
4. Test alternative recovery assumptions.
5. Extend the benchmark to more realistic agent interactions.
