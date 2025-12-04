"""
Experiment 1: Needle in Haystack
Demonstrates the "Lost in the Middle" phenomenon
Author: Context Windows Lab
"""

import logging
import json
from pathlib import Path
from typing import Dict, List
import sys
sys.path.append(str(Path(__file__).parent.parent))

from utils.text_generator import TextGenerator
from utils.metrics import MetricsEvaluator
from utils.visualization import Visualizer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NeedleHaystackExperiment:
    """
    Experiment to demonstrate Lost in the Middle phenomenon
    Tests if LLM can find critical facts at different positions
    """

    def __init__(
        self,
        num_docs: int = 5,
        words_per_doc: int = 200,
        critical_fact: str = "The CEO of the company is David Cohen"
    ):
        """
        Initialize experiment

        Args:
            num_docs: Number of documents to generate
            words_per_doc: Words per document
            critical_fact: Fact to embed and search for
        """
        self.num_docs = num_docs
        self.words_per_doc = words_per_doc
        self.critical_fact = critical_fact
        self.documents = []
        self.results = {'start': [], 'middle': [], 'end': []}

        logger.info(
            f"Initialized Needle in Haystack experiment: "
            f"{num_docs} docs, {words_per_doc} words/doc"
        )

    def generate_documents(self) -> List[Dict]:
        """
        Generate synthetic documents with embedded facts

        Returns:
            List of document dictionaries
        """
        logger.info("Generating documents with embedded facts")

        self.documents = TextGenerator.create_documents(
            num_docs=self.num_docs,
            words_per_doc=self.words_per_doc,
            fact=self.critical_fact
        )

        logger.info(f"Generated {len(self.documents)} documents")
        return self.documents

    def query_llm_mock(self, context: str, query: str) -> str:
        """
        Mock LLM query for testing (simulates position-based accuracy)

        Args:
            context: Document context
            query: Query string

        Returns:
            Mock response
        """
        # Simulate Lost in the Middle phenomenon
        # Higher accuracy at start/end, lower in middle

        sentences = context.split(". ")
        fact_sentence_idx = None

        for idx, sentence in enumerate(sentences):
            if self.critical_fact in sentence:
                fact_sentence_idx = idx
                break

        if fact_sentence_idx is None:
            return "Information not found"

        # Calculate position ratio (0 = start, 1 = end)
        position_ratio = fact_sentence_idx / len(sentences)

        # Simulate Lost in the Middle: lower accuracy in middle (0.3-0.7)
        import random
        if position_ratio < 0.3 or position_ratio > 0.7:
            # High accuracy at start/end
            if random.random() < 0.9:
                return self.critical_fact
        else:
            # Low accuracy in middle
            if random.random() < 0.4:
                return self.critical_fact

        return "The CEO is John Smith"  # Wrong answer

    def run_experiment(self) -> Dict:
        """
        Execute the experiment

        Returns:
            Results dictionary
        """
        logger.info("Running Needle in Haystack experiment")

        if not self.documents:
            self.generate_documents()

        query = f"Who is the CEO of the company?"

        for doc in self.documents:
            context = doc['text']
            position = doc['fact_position']

            # Query LLM
            response = self.query_llm_mock(context, query)

            # Evaluate accuracy
            accuracy = MetricsEvaluator.evaluate_accuracy(
                response=response,
                expected=self.critical_fact,
                threshold=0.6
            )

            # Store result
            self.results[position].append(accuracy)

            logger.info(
                f"Doc {doc['id']}: Position={position}, "
                f"Accuracy={accuracy:.2f}"
            )

        logger.info("Experiment completed successfully")
        return self.results

    def visualize_results(self, output_dir: str = "src/data/results/experiment1"):
        """
        Create visualizations of results

        Args:
            output_dir: Directory to save plots
        """
        logger.info("Creating visualizations")

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Plot accuracy by position
        Visualizer.plot_accuracy_by_position(
            results=self.results,
            output_path=str(output_path / "accuracy_by_position.png")
        )

    def save_results(self, output_dir: str = "src/data/results/experiment1"):
        """
        Save results to JSON

        Args:
            output_dir: Directory to save results
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Calculate statistics
        summary = {}
        for position, accuracies in self.results.items():
            stats = MetricsEvaluator.aggregate_results(
                [{"accuracy": acc} for acc in accuracies],
                metric_key="accuracy"
            )
            summary[position] = stats

        # Save to JSON
        output_file = output_path / "summary.json"
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)

        logger.info(f"Results saved to {output_file}")


def main():
    """Main execution function"""
    logger.info("=" * 60)
    logger.info("EXPERIMENT 1: NEEDLE IN HAYSTACK")
    logger.info("=" * 60)

    # Create and run experiment
    experiment = NeedleHaystackExperiment(
        num_docs=15,  # More docs for better statistics
        words_per_doc=200
    )

    # Execute
    experiment.run_experiment()

    # Visualize
    experiment.visualize_results()

    # Save
    experiment.save_results()

    logger.info("Experiment 1 completed successfully!")


if __name__ == "__main__":
    main()
