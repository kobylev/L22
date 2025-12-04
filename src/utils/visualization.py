"""
Visualization Utilities for Context Windows Lab
Creates graphs, charts, and visual comparisons of experiment results
Author: Context Windows Lab
"""

import logging
from typing import Dict, List
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10


class Visualizer:
    """Creates visualizations for experiment results"""

    @staticmethod
    def plot_accuracy_by_position(
        results: Dict[str, List[float]],
        output_path: str = None,
        title: str = "Accuracy by Fact Position"
    ) -> None:
        """
        Create bar chart showing accuracy by fact position

        Args:
            results: Dictionary with positions as keys, accuracy lists as values
            output_path: Path to save plot (optional)
            title: Plot title
        """
        logger.info("Creating accuracy by position plot")

        # Calculate averages
        positions = list(results.keys())
        averages = [sum(results[pos]) / len(results[pos]) for pos in positions]

        # Create bar plot
        plt.figure(figsize=(10, 6))
        bars = plt.bar(positions, averages, color=['#2ecc71', '#e74c3c', '#3498db'])

        # Add value labels on bars
        for bar, avg in zip(bars, averages):
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width()/2., height,
                f'{avg:.2%}',
                ha='center', va='bottom',
                fontsize=12, fontweight='bold'
            )

        plt.xlabel('Fact Position', fontsize=12, fontweight='bold')
        plt.ylabel('Accuracy', fontsize=12, fontweight='bold')
        plt.title(title, fontsize=14, fontweight='bold')
        plt.ylim(0, 1.1)
        plt.grid(axis='y', alpha=0.3)

        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            logger.info(f"Plot saved to {output_path}")

        plt.tight_layout()
        plt.show()
        plt.close()

    @staticmethod
    def plot_context_size_impact(
        results: List[Dict],
        output_path: str = None
    ) -> None:
        """
        Create line graphs showing accuracy and latency vs context size

        Args:
            results: List of result dictionaries with metrics
            output_path: Path to save plot (optional)
        """
        logger.info("Creating context size impact plots")

        df = pd.DataFrame(results)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Plot 1: Accuracy vs Context Size
        ax1.plot(
            df['num_docs'], df['accuracy'],
            marker='o', linewidth=2, markersize=8, color='#3498db'
        )
        ax1.set_xlabel('Number of Documents', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Accuracy', fontsize=12, fontweight='bold')
        ax1.set_title('Accuracy Degradation vs Context Size', fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.1)

        # Plot 2: Latency vs Context Size
        ax2.plot(
            df['num_docs'], df['latency'],
            marker='s', linewidth=2, markersize=8, color='#e74c3c'
        )
        ax2.set_xlabel('Number of Documents', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Latency (seconds)', fontsize=12, fontweight='bold')
        ax2.set_title('Response Time vs Context Size', fontsize=13, fontweight='bold')
        ax2.grid(True, alpha=0.3)

        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            logger.info(f"Plot saved to {output_path}")

        plt.tight_layout()
        plt.show()
        plt.close()

    @staticmethod
    def plot_rag_comparison(
        results: Dict,
        output_path: str = None
    ) -> None:
        """
        Create side-by-side comparison: RAG vs Full Context

        Args:
            results: Dictionary with comparison metrics
            output_path: Path to save plot (optional)
        """
        logger.info("Creating RAG comparison plot")

        metrics = ['accuracy', 'latency', 'tokens_used']
        full_values = [
            results.get('full_accuracy', 0),
            results.get('full_latency', 0),
            results.get('full_tokens', 0)
        ]
        rag_values = [
            results.get('rag_accuracy', 0),
            results.get('rag_latency', 0),
            results.get('rag_tokens', 0)
        ]

        # Normalize tokens for visualization (divide by 1000)
        full_values[2] = full_values[2] / 1000
        rag_values[2] = rag_values[2] / 1000

        x = range(len(metrics))
        width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))
        bars1 = ax.bar(
            [i - width/2 for i in x], full_values,
            width, label='Full Context', color='#e74c3c', alpha=0.8
        )
        bars2 = ax.bar(
            [i + width/2 for i in x], rag_values,
            width, label='RAG', color='#2ecc71', alpha=0.8
        )

        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontsize=10
                )

        ax.set_ylabel('Value', fontsize=12, fontweight='bold')
        ax.set_title('RAG vs Full Context Comparison', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(['Accuracy', 'Latency (s)', 'Tokens (K)'])
        ax.legend(fontsize=11)
        ax.grid(axis='y', alpha=0.3)

        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            logger.info(f"Plot saved to {output_path}")

        plt.tight_layout()
        plt.show()
        plt.close()

    @staticmethod
    def plot_strategy_performance(
        results: Dict[str, List[Dict]],
        output_path: str = None
    ) -> None:
        """
        Create multi-line graph showing strategies over time

        Args:
            results: Dictionary with strategy names as keys, result lists as values
            output_path: Path to save plot (optional)
        """
        logger.info("Creating strategy performance plot")

        fig, ax = plt.subplots(figsize=(12, 6))

        colors = {'select': '#3498db', 'compress': '#e74c3c', 'write': '#2ecc71'}
        markers = {'select': 'o', 'compress': 's', 'write': '^'}

        for strategy, strategy_results in results.items():
            actions = range(1, len(strategy_results) + 1)
            accuracies = [r.get('accuracy', 0) for r in strategy_results]

            ax.plot(
                actions, accuracies,
                marker=markers.get(strategy, 'o'),
                linewidth=2, markersize=8,
                color=colors.get(strategy, '#95a5a6'),
                label=strategy.upper()
            )

        ax.set_xlabel('Action Number', fontsize=12, fontweight='bold')
        ax.set_ylabel('Accuracy', fontsize=12, fontweight='bold')
        ax.set_title('Context Engineering Strategies Performance', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11, loc='best')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)

        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            logger.info(f"Plot saved to {output_path}")

        plt.tight_layout()
        plt.show()
        plt.close()
