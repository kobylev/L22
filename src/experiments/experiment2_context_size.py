"""
Experiment 2: Context Window Size Impact
Measures performance degradation as context grows
Author: Context Windows Lab
"""

import logging
import json
from pathlib import Path
from typing import List, Dict
import time

from utils.text_generator import TextGenerator
from utils.metrics import MetricsEvaluator
from utils.mock_llm import query_llm_mock
from experiments.experiment2_results_manager import visualize_results, save_results


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ContextSizeExperiment:
    """
    Experiment to measure context window size impact
    Tests accuracy and latency across different context sizes
    """

    def __init__(
        self,
        doc_counts: List[int] = None,
        words_per_doc: int = 200
    ):
        """
        Initialize experiment

        Args:
            doc_counts: List of document counts to test
            words_per_doc: Words per document
        """
        self.doc_counts = doc_counts or [2, 5, 10, 20, 50]
        self.words_per_doc = words_per_doc
        self.results = []

        logger.info(
            f"Initialized Context Size experiment: "
            f"Testing sizes {self.doc_counts}"
        )





    def run_experiment(self) -> List[Dict]:
        """
        Execute the experiment

        Returns:
            List of result dictionaries
        """
        logger.info("Running Context Size Impact experiment")

        expected_answer = "The CEO of the company is David Cohen"

        for num_docs in self.doc_counts:
            logger.info(f"\nTesting with {num_docs} documents...")

            # Generate documents
            documents = TextGenerator.create_documents(
                num_docs=num_docs,
                words_per_doc=self.words_per_doc,
                fact=expected_answer
            )

            # Concatenate into single context
            context = TextGenerator.concatenate_documents(documents)
            tokens_used = MetricsEvaluator.count_tokens(context)

            # Query LLM
            query = "Who is the CEO of the company?"
            start_time = time.time()
            response, simulated_latency = query_llm_mock(context, query, mode='context_size')
            actual_latency = time.time() - start_time

            # Evaluate accuracy
            accuracy = MetricsEvaluator.evaluate_accuracy(
                response=response,
                expected=expected_answer,
                threshold=0.6
            )

            # Store results
            result = {
                'num_docs': num_docs,
                'tokens_used': tokens_used,
                'latency': actual_latency,
                'accuracy': accuracy,
                'context_length': len(context)
            }
            self.results.append(result)

            logger.info(
                f"  Documents: {num_docs}, "
                f"Tokens: {tokens_used}, "
                f"Latency: {actual_latency:.3f}s, "
                f"Accuracy: {accuracy:.2f}"
            )

        logger.info("\nExperiment completed successfully")
        return self.results




def main():
    """Main execution function"""
    logger.info("=" * 60)
    logger.info("EXPERIMENT 2: CONTEXT WINDOW SIZE IMPACT")
    logger.info("=" * 60)

    # Create and run experiment
    experiment = ContextSizeExperiment(
        doc_counts=[2, 5, 10, 20, 50],
        words_per_doc=200
    )

    # Execute
    experiment.run_experiment()

    # Visualize
    visualize_results(experiment.results)

    # Save
    save_results(experiment.results)

    logger.info("\nExperiment 2 completed successfully!")


if __name__ == "__main__":
    main()
