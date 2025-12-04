"""
Experiment 4: Context Engineering Strategies
Evaluates SELECT, COMPRESS, and WRITE strategies
Author: Context Windows Lab
"""

import logging
import json
from pathlib import Path
from typing import List, Dict


from utils.text_generator import TextGenerator
from utils.metrics import MetricsEvaluator
from utils.visualization import Visualizer
from utils.mock_llm import query_llm_mock
from experiments.experiment4_strategies import (
    select_strategy,
    compress_strategy,
    write_strategy
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ContextEngineeringExperiment:
    """
    Experiment to compare context engineering strategies
    Tests SELECT, COMPRESS, and WRITE approaches
    """

    def __init__(self, num_actions: int = 10, max_tokens: int = 2000):
        """
        Initialize experiment

        Args:
            num_actions: Number of sequential actions to simulate
            max_tokens: Maximum tokens before compression needed
        """
        self.num_actions = num_actions
        self.max_tokens = max_tokens
        self.history = []
        self.scratchpad = {}
        self.results = {'select': [], 'compress': [], 'write': []}

        logger.info(
            f"Initialized Context Engineering experiment: "
            f"{num_actions} actions, max {max_tokens} tokens"
        )

    




    def run_strategy_simulation(self, strategy_name: str) -> List[Dict]:
        """
        Run simulation for a specific strategy

        Args:
            strategy_name: 'select', 'compress', or 'write'

        Returns:
            List of action results
        """
        logger.info(f"\nRunning {strategy_name.upper()} strategy simulation...")

        strategy_history = []
        strategy_results = []

        for action_num in range(1, self.num_actions + 1):
            # Generate action output
            output = TextGenerator.generate_action_output(action_num)
            strategy_history.append(output)

            # Apply strategy
            query = f"What happened in action {action_num}?"

            if strategy_name == 'select':
                context = select_strategy(strategy_history, query, k=5)
            elif strategy_name == 'compress':
                context = compress_strategy(strategy_history, query, max_tokens=self.max_tokens)
            elif strategy_name == 'write':
                context = write_strategy(strategy_history, query, scratchpad=self.scratchpad)
            else:
                raise ValueError(f"Unknown strategy: {strategy_name}")

            # Query LLM
            response, accuracy = query_llm_mock(context, query)

            # Store result
            result = {
                'action': action_num,
                'accuracy': accuracy,
                'context_tokens': MetricsEvaluator.count_tokens(context),
                'history_size': len(strategy_history)
            }
            strategy_results.append(result)

            logger.debug(
                f"  Action {action_num}: "
                f"Accuracy={accuracy:.3f}, "
                f"Tokens={result['context_tokens']}"
            )

        # Calculate average accuracy
        avg_accuracy = sum(r['accuracy'] for r in strategy_results) / len(strategy_results)
        logger.info(f"{strategy_name.upper()} average accuracy: {avg_accuracy:.3f}")

        return strategy_results

    def run_experiment(self) -> Dict[str, List[Dict]]:
        """
        Execute the experiment

        Returns:
            Results dictionary with all strategies
        """
        logger.info("Running Context Engineering Strategies experiment")

        # Run each strategy
        for strategy in ['select', 'compress', 'write']:
            # Reset state for each strategy
            self.history = []
            self.scratchpad = {}

            # Run simulation
            self.results[strategy] = self.run_strategy_simulation(strategy)

        logger.info("\nExperiment completed successfully")
        return self.results

    def visualize_results(self, output_dir: str = "src/data/results/experiment4"):
        """Create visualizations"""
        logger.info("Creating visualizations")

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        Visualizer.plot_strategy_performance(
            results=self.results,
            output_path=str(output_path / "strategy_performance.png")
        )

    def save_results(self, output_dir: str = "src/data/results/experiment4"):
        """Save results to JSON"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Save detailed results
        output_file = output_path / "strategies.json"
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        logger.info(f"Results saved to {output_file}")

        # Create summary
        summary = {}
        for strategy, results_list in self.results.items():
            avg_accuracy = sum(r['accuracy'] for r in results_list) / len(results_list)
            avg_tokens = sum(r['context_tokens'] for r in results_list) / len(results_list)

            summary[strategy] = {
                'average_accuracy': avg_accuracy,
                'average_tokens': avg_tokens,
                'total_actions': len(results_list)
            }

        summary_file = output_path / "summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)

        logger.info(f"Summary saved to {summary_file}")


def main():
    """Main execution function"""
    logger.info("=" * 60)
    logger.info("EXPERIMENT 4: CONTEXT ENGINEERING STRATEGIES")
    logger.info("=" * 60)

    experiment = ContextEngineeringExperiment(num_actions=10, max_tokens=2000)
    experiment.run_experiment()
    experiment.visualize_results()
    experiment.save_results()

    logger.info("\nExperiment 4 completed successfully!")


if __name__ == "__main__":
    main()
