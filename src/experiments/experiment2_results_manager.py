import logging
import json
from pathlib import Path
from typing import List, Dict
from utils.visualization import Visualizer
from utils.metrics import MetricsEvaluator

logger = logging.getLogger(__name__)


def visualize_results(results: List[Dict], output_dir: str = "src/data/results/experiment2"):
    """
    Create visualizations of results

    Args:
        results: List of result dictionaries with metrics
        output_dir: Directory to save plots
    """
    logger.info("Creating visualizations")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Plot context size impact
    Visualizer.plot_context_size_impact(
        results=results,
        output_path=str(output_path / "context_size_impact.png")
    )


def save_results(results: List[Dict], output_dir: str = "src/data/results/experiment2"):
    """
    Save results to JSON

    Args:
        results: List of result dictionaries
        output_dir: Directory to save results
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Save detailed results
    output_file = output_path / "metrics.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    logger.info(f"Results saved to {output_file}")

    # Create summary statistics
    summary = {
        "total_tests": len(results),
        "average_accuracy": sum(r['accuracy'] for r in results) / len(results),
        "average_latency": sum(r['latency'] for r in results) / len(results),
        "max_tokens_tested": max(r['tokens_used'] for r in results)
    }

    summary_file = output_path / "summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)

    logger.info(f"Summary saved to {summary_file}")
