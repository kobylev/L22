"""
Metrics Evaluation System for Context Windows Lab
Measures accuracy, latency, token usage, and other performance metrics
Author: Context Windows Lab
"""

import time
import logging
from typing import Callable, Any, Dict
from functools import wraps
from difflib import SequenceMatcher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MetricsEvaluator:
    """Evaluates performance metrics for LLM experiments"""

    # Token estimation constants (rough approximation)
    CHARS_PER_TOKEN = 4
    COST_PER_1K_TOKENS = 0.0001  # Example cost

    @staticmethod
    def evaluate_accuracy(response: str, expected: str, threshold: float = 0.6) -> float:
        """
        Calculate response accuracy using sequence matching

        Args:
            response: LLM response text
            expected: Expected correct answer
            threshold: Minimum similarity threshold (0-1)

        Returns:
            Accuracy score (0-1)
        """
        if not response or not expected:
            logger.warning("Empty response or expected value")
            return 0.0

        # Normalize texts
        response_norm = response.lower().strip()
        expected_norm = expected.lower().strip()

        # Check for exact match
        if expected_norm in response_norm:
            logger.debug("Exact match found")
            return 1.0

        # Use sequence matching for fuzzy comparison
        similarity = SequenceMatcher(None, response_norm, expected_norm).ratio()

        # Binary accuracy based on threshold
        accuracy = 1.0 if similarity >= threshold else 0.0

        logger.debug(
            f"Similarity: {similarity:.3f}, "
            f"Threshold: {threshold}, "
            f"Accuracy: {accuracy}"
        )

        return accuracy

    @staticmethod
    def measure_latency(func: Callable) -> Callable:
        """
        Decorator to measure function execution time

        Args:
            func: Function to measure

        Returns:
            Wrapped function with latency measurement
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> tuple:
            logger.debug(f"Measuring latency for {func.__name__}")
            start_time = time.time()

            result = func(*args, **kwargs)

            latency = time.time() - start_time
            logger.info(f"{func.__name__} completed in {latency:.3f}s")

            return result, latency

        return wrapper

    @staticmethod
    def count_tokens(text: str) -> int:
        """
        Estimate token count from text

        Args:
            text: Input text

        Returns:
            Estimated token count
        """
        if not text:
            return 0

        # Rough estimation: ~4 characters per token
        token_count = len(text) // MetricsEvaluator.CHARS_PER_TOKEN

        logger.debug(f"Estimated {token_count} tokens from {len(text)} characters")
        return token_count

    @staticmethod
    def calculate_cost(tokens: int, model: str = "default") -> float:
        """
        Estimate API cost based on token count

        Args:
            tokens: Number of tokens
            model: Model name (for future cost differentiation)

        Returns:
            Estimated cost in USD
        """
        cost = (tokens / 1000) * MetricsEvaluator.COST_PER_1K_TOKENS

        logger.debug(f"Estimated cost: ${cost:.6f} for {tokens} tokens")
        return cost

    @staticmethod
    def evaluate_retrieval_quality(
        retrieved_docs: list,
        query: str,
        ground_truth_doc_ids: list = None
    ) -> Dict[str, float]:
        """
        Evaluate retrieval quality metrics

        Args:
            retrieved_docs: List of retrieved document IDs
            query: Search query
            ground_truth_doc_ids: Optional list of correct document IDs

        Returns:
            Dictionary with retrieval metrics
        """
        logger.info("Evaluating retrieval quality")

        metrics = {
            "num_retrieved": len(retrieved_docs),
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0
        }

        if ground_truth_doc_ids:
            retrieved_set = set(retrieved_docs)
            ground_truth_set = set(ground_truth_doc_ids)

            true_positives = len(retrieved_set & ground_truth_set)
            false_positives = len(retrieved_set - ground_truth_set)
            false_negatives = len(ground_truth_set - retrieved_set)

            # Precision: TP / (TP + FP)
            if len(retrieved_set) > 0:
                metrics["precision"] = true_positives / len(retrieved_set)

            # Recall: TP / (TP + FN)
            if len(ground_truth_set) > 0:
                metrics["recall"] = true_positives / len(ground_truth_set)

            # F1 Score
            if metrics["precision"] + metrics["recall"] > 0:
                metrics["f1"] = (
                    2 * metrics["precision"] * metrics["recall"] /
                    (metrics["precision"] + metrics["recall"])
                )

            logger.info(
                f"Retrieval metrics - "
                f"Precision: {metrics['precision']:.3f}, "
                f"Recall: {metrics['recall']:.3f}, "
                f"F1: {metrics['f1']:.3f}"
            )

        return metrics

    @staticmethod
    def aggregate_results(results: list, metric_key: str = "accuracy") -> Dict[str, float]:
        """
        Aggregate multiple experiment results

        Args:
            results: List of result dictionaries
            metric_key: Key of metric to aggregate

        Returns:
            Dictionary with aggregated statistics
        """
        if not results:
            logger.warning("No results to aggregate")
            return {"mean": 0.0, "min": 0.0, "max": 0.0, "std": 0.0}

        values = [r.get(metric_key, 0.0) for r in results]

        # Calculate statistics
        mean_val = sum(values) / len(values)
        min_val = min(values)
        max_val = max(values)

        # Standard deviation
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        std_val = variance ** 0.5

        stats = {
            "mean": mean_val,
            "min": min_val,
            "max": max_val,
            "std": std_val,
            "count": len(values)
        }

        logger.info(
            f"Aggregated {len(values)} results - "
            f"Mean: {mean_val:.3f}, "
            f"Std: {std_val:.3f}"
        )

        return stats
