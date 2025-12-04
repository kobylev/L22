import logging
from typing import Dict
from experiments.experiment1_needle_haystack import NeedleHaystackExperiment
from experiments.experiment2_context_size import ContextSizeExperiment
from experiments.experiment3_rag_impact import RAGImpactExperiment
from experiments.experiment4_engineering import ContextEngineeringExperiment
from utils.cli_utils import print_header

logger = logging.getLogger(__name__)

def run_experiment_1() -> bool:
    """Run Experiment 1: Needle in Haystack"""
    print_header("EXPERIMENT 1: NEEDLE IN HAYSTACK")
    logger.info("Starting Experiment 1: Needle in Haystack")

    try:
        experiment = NeedleHaystackExperiment(
            num_docs=15,
            words_per_doc=200
        )
        experiment.run_experiment()
        experiment.visualize_results()
        experiment.save_results()

        logger.info("✓ Experiment 1 completed successfully")
        return True
    except Exception as e:
        logger.error(f"✗ Experiment 1 failed: {e}")
        return False


def run_experiment_2() -> bool:
    """Run Experiment 2: Context Window Size Impact"""
    print_header("EXPERIMENT 2: CONTEXT WINDOW SIZE IMPACT")
    logger.info("Starting Experiment 2: Context Window Size Impact")

    try:
        experiment = ContextSizeExperiment(
            doc_counts=[2, 5, 10, 20, 50],
            words_per_doc=200
        )
        experiment.run_experiment()
        experiment.visualize_results()
        experiment.save_results()

        logger.info("✓ Experiment 2 completed successfully")
        return True
    except Exception as e:
        logger.error(f"✗ Experiment 2 failed: {e}")
        return False


def run_experiment_3() -> bool:
    """Run Experiment 3: RAG Impact"""
    print_header("EXPERIMENT 3: RAG IMPACT")
    logger.info("Starting Experiment 3: RAG Impact")

    try:
        experiment = RAGImpactExperiment(
            num_documents=20,
            top_k=3
        )
        experiment.run_experiment()
        experiment.visualize_results()
        experiment.save_results()

        logger.info("✓ Experiment 3 completed successfully")
        return True
    except Exception as e:
        logger.error(f"✗ Experiment 3 failed: {e}")
        return False


def run_experiment_4() -> bool:
    """Run Experiment 4: Context Engineering Strategies"""
    print_header("EXPERIMENT 4: CONTEXT ENGINEERING STRATEGIES")
    logger.info("Starting Experiment 4: Context Engineering Strategies")

    try:
        experiment = ContextEngineeringExperiment(
            num_actions=10,
            max_tokens=2000
        )
        experiment.run_experiment()
        experiment.visualize_results()
        experiment.save_results()

        logger.info("✓ Experiment 4 completed successfully")
        return True
    except Exception as e:
        logger.error(f"✗ Experiment 4 failed: {e}")
        return False


def run_all_experiments() -> bool:
    """Run all experiments sequentially"""
    print_header("CONTEXT WINDOWS LAB - RUNNING ALL EXPERIMENTS")

    results = {
        "Experiment 1": run_experiment_1(),
        "Experiment 2": run_experiment_2(),
        "Experiment 3": run_experiment_3(),
        "Experiment 4": run_experiment_4()
    }

    # Print summary
    print_header("EXECUTION SUMMARY")
    for exp_name, success in results.items():
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"  {exp_name}: {status}")

    total_passed = sum(results.values())
    total_tests = len(results)
    print(f"\n  Total: {total_passed}/{total_tests} experiments completed successfully")

    return all(results.values())
