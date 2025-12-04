"""
Context Windows Laboratory - Main Execution Script
Runs all experiments with CLI interface
Author: Context Windows Lab
"""

import argparse
import logging
import sys
from pathlib import Path

# Add parent directory to path for relative imports
sys.path.append(str(Path(__file__).parent))

from experiments.experiment_runner import (
    run_experiment_1,
    run_experiment_2,
    run_experiment_3,
    run_experiment_4,
    run_all_experiments
)
from utils.cli_utils import print_header





# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)








def main():
    """Main execution function with CLI"""
    parser = argparse.ArgumentParser(
        description='Context Windows Laboratory - Practical Experiments',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --experiment 1              # Run experiment 1 only
  python main.py --experiment all            # Run all experiments
  python main.py --experiment 3 --verbose    # Run experiment 3 with verbose output
        """
    )

    parser.add_argument(
        '--experiment',
        type=str,
        choices=['1', '2', '3', '4', 'all'],
        required=True,
        help='Experiment number to run (1-4) or "all"'
    )

    parser.add_argument(
        '--output-dir',
        type=str,
        default='src/data/results',
        help='Output directory for results (default: src/data/results)'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    # Configure logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Print welcome banner
    print("\n" + "=" * 70)
    print("  CONTEXT WINDOWS LABORATORY")
    print("  Lab: Context Windows in Practice")
    print("  © Dr. Segal Yoram - All Rights Reserved")
    print("=" * 70)

    # Run requested experiment(s)
    if args.experiment == 'all':
        success = run_all_experiments()
    elif args.experiment == '1':
        success = run_experiment_1()
    elif args.experiment == '2':
        success = run_experiment_2()
    elif args.experiment == '3':
        success = run_experiment_3()
    elif args.experiment == '4':
        success = run_experiment_4()
    else:
        logger.error(f"Invalid experiment: {args.experiment}")
        success = False

    # Exit with appropriate code
    if success:
        print_header("ALL EXPERIMENTS COMPLETED SUCCESSFULLY!")
        sys.exit(0)
    else:
        print_header("SOME EXPERIMENTS FAILED - CHECK LOGS")
        sys.exit(1)


if __name__ == "__main__":
    main()
