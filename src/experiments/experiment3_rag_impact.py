"""
Experiment 3: RAG Impact
Compares RAG retrieval vs Full Context approach
Author: Context Windows Lab
"""




from pathlib import Path
from typing import List, Dict, Tuple

from utils.metrics import MetricsEvaluator
from utils.visualization import Visualizer
from utils.mock_llm import query_llm_mock
from utils.rag_utils import generate_documents
from experiments.experiment3_modes import run_full_context_mode, run_rag_mode

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RAGImpactExperiment:
    """
    Experiment to compare RAG vs Full Context
    Demonstrates benefits of targeted retrieval
    """

    def __init__(
        self,
        num_documents: int = 20,
        top_k: int = 3
    ):
        """
        Initialize experiment

        Args:
            num_documents: Total number of documents
            top_k: Number of documents to retrieve in RAG mode
        """
        self.num_documents = num_documents
        self.top_k = top_k
        self.documents = []
        self.results = {}

        logger.info(
            f"Initialized RAG Impact experiment: "
            f"{num_documents} documents, top-{top_k} retrieval"
        )







    def run_experiment(self) -> Dict:
        """
        Execute the experiment

        Returns:
            Results dictionary
        """
        logger.info("Running RAG Impact experiment")

        if not self.documents:
            self.documents = generate_documents(self.num_documents, ["technology", "law", "medicine"])

        query = "מה תופעות הלוואי של התרופה"

        # Run both modes
        full_result = run_full_context_mode(self.documents, query)
        rag_result = run_rag_mode(self.documents, query, self.top_k)

        # Compile results
        self.results = {
            'full_accuracy': full_result['accuracy'],
            'full_latency': full_result['latency'],
            'full_tokens': full_result['tokens_used'],
            'rag_accuracy': rag_result['accuracy'],
            'rag_latency': rag_result['latency'],
            'rag_tokens': rag_result['tokens_used'],
            'improvement': {
                'accuracy': rag_result['accuracy'] - full_result['accuracy'],
                'latency_reduction': (1 - rag_result['latency'] / full_result['latency']) * 100,
                'token_reduction': (1 - rag_result['tokens_used'] / full_result['tokens_used']) * 100
            }
        }

        logger.info("\n" + "="*50)
        logger.info("COMPARISON RESULTS:")
        logger.info(f"  Accuracy improvement: {self.results['improvement']['accuracy']:.2%}")
        logger.info(f"  Latency reduction: {self.results['improvement']['latency_reduction']:.1f}%")
        logger.info(f"  Token reduction: {self.results['improvement']['token_reduction']:.1f}%")
        logger.info("="*50)

        return self.results

    def visualize_results(self, output_dir: str = "src/data/results/experiment3"):
        """Create visualizations"""
        logger.info("Creating visualizations")

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        Visualizer.plot_rag_comparison(
            results=self.results,
            output_path=str(output_path / "rag_vs_full.png")
        )

    def save_results(self, output_dir: str = "src/data/results/experiment3"):
        """Save results to JSON"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        output_file = output_path / "comparison.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        logger.info(f"Results saved to {output_file}")


def main():
    """Main execution function"""
    logger.info("=" * 60)
    logger.info("EXPERIMENT 3: RAG IMPACT")
    logger.info("=" * 60)

    experiment = RAGImpactExperiment(num_documents=20, top_k=3)
    experiment.run_experiment()
    experiment.visualize_results()
    experiment.save_results()

    logger.info("\nExperiment 3 completed successfully!")


if __name__ == "__main__":
    main()
