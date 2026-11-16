
import sys
import unittest
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from simulator import simulate_outcome
from policies import decide_action
from evaluation import evaluate_policy


class TestObjectiveUncertaintyBenchmark(unittest.TestCase):

    def test_rollback_reduces_harm_for_reversible_action(self):
        result = simulate_outcome(
            impact=0.5,
            uncertainty=0.8,
            reversibility=1.0,
            harmful_outcome=1,
            rollback_attempted=True,
            recovery_fraction=0.80,
        )
        self.assertAlmostEqual(result["initial_harm"], 0.5)
        self.assertAlmostEqual(result["harm_recovered"], 0.4)
        self.assertAlmostEqual(result["residual_harm"], 0.1)

    def test_irreversible_action_cannot_recover_harm(self):
        result = simulate_outcome(
            impact=0.5,
            uncertainty=0.8,
            reversibility=0.0,
            harmful_outcome=1,
            rollback_attempted=True,
            recovery_fraction=0.80,
        )
        self.assertAlmostEqual(result["harm_recovered"], 0.0)
        self.assertAlmostEqual(result["residual_harm"], 0.5)

    def test_risk_aware_policy_uses_composite_risk(self):
        decision = decide_action(
            impact=0.9,
            uncertainty=0.9,
            reversibility=0.0,
            policy="risk_aware_with_rollback",
            threshold=0.5,
        )
        self.assertTrue(decision["intervene"])

    def test_no_rollback_policy_does_not_attempt_rollback(self):
        decision = decide_action(
            impact=0.9,
            uncertainty=0.9,
            reversibility=0.5,
            policy="fixed_threshold_without_rollback",
            threshold=0.5,
        )
        self.assertFalse(decision["rollback_attempted"])

    def test_evaluation_returns_episode_predictions(self):
        sample = pd.DataFrame([
            {
                "episode_id": "test_1",
                "impact": 0.5,
                "uncertainty": 0.9,
                "reversibility": 1.0,
                "harmful_outcome": 1,
            },
            {
                "episode_id": "test_2",
                "impact": 0.4,
                "uncertainty": 0.1,
                "reversibility": 0.0,
                "harmful_outcome": 0,
            },
        ])

        summary, predictions = evaluate_policy(
            sample,
            policy="fixed_threshold_with_rollback",
            threshold=0.5,
            recovery_fraction=0.80,
        )
        self.assertEqual(summary["n_episodes"], 2)
        self.assertEqual(len(predictions), 2)
        self.assertIn("residual_harm", predictions.columns)


if __name__ == "__main__":
    unittest.main(verbosity=2)

