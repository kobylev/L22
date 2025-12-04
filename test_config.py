"""
Configuration Test Script
Demonstrates how to use environment configuration
"""

from src.utils.config import Config

def main():
    """Test configuration loading"""

    print("\n" + "=" * 70)
    print("CONTEXT WINDOWS LABORATORY - CONFIGURATION TEST")
    print("=" * 70)

    # Display full configuration
    Config.print_config()

    print("\n" + "=" * 70)
    print("DETAILED CONFIGURATION VALUES")
    print("=" * 70)

    # Experiment configurations
    print("\n📊 Experiment Configurations:")
    print(f"  Exp 1 - Docs: {Config.get_experiment1_config()['num_docs']}")
    print(f"  Exp 1 - Words/Doc: {Config.get_experiment1_config()['words_per_doc']}")
    print(f"  Exp 2 - Doc Counts: {Config.get_experiment2_config()['doc_counts']}")
    print(f"  Exp 3 - Num Documents: {Config.get_experiment3_config()['num_documents']}")
    print(f"  Exp 3 - Top-K: {Config.get_experiment3_config()['top_k']}")
    print(f"  Exp 4 - Actions: {Config.get_experiment4_config()['num_actions']}")

    # Output settings
    print("\n📁 Output Settings:")
    print(f"  Results Directory: {Config.get_results_dir()}")
    img_config = Config.get_image_config()
    print(f"  Image DPI: {img_config['dpi']}")
    print(f"  Image Format: {img_config['format']}")

    # Logging settings
    print("\n📝 Logging Settings:")
    print(f"  Log Level: {Config.get_log_level()}")
    print(f"  Log File: {Config.get_log_file() or 'Console only'}")

    # Random seed
    print("\n🎲 Reproducibility:")
    seed = Config.get_random_seed()
    print(f"  Random Seed: {seed if seed else 'Not set (random)'}")

    # Metrics
    print("\n📈 Metrics Configuration:")
    print(f"  Chars per Token: {Config.get_chars_per_token()}")
    print(f"  Cost per 1K Tokens: ${Config.get_cost_per_1k_tokens()}")
    print(f"  Accuracy Threshold: {Config.get_accuracy_threshold()}")

    # Mode flags
    print("\n⚙️  Mode Flags:")
    print(f"  Use Mock LLM: {Config.use_mock_llm()}")
    print(f"  Test Mode: {Config.is_test_mode()}")
    print(f"  Verbose: {Config.is_verbose()}")
    print(f"  Auto Show Plots: {Config.auto_show_plots()}")
    print(f"  Auto Save Plots: {Config.auto_save_plots()}")

    # Visualization
    print("\n🎨 Visualization:")
    colors = Config.get_color_scheme()
    print(f"  Start Color: {colors['start']}")
    print(f"  Middle Color: {colors['middle']}")
    print(f"  End Color: {colors['end']}")

    print("\n" + "=" * 70)
    print("✅ Configuration loaded successfully!")
    print("=" * 70 + "\n")

    # Test accessing specific values
    print("🧪 Usage Example:")
    print("-" * 70)
    print("from src.utils.config import Config")
    print("")
    print("# Get experiment 1 config")
    print("exp1 = Config.get_experiment1_config()")
    print(f"print(exp1['num_docs'])  # Output: {Config.get_experiment1_config()['num_docs']}")
    print("")
    print("# Check if verbose mode")
    print("if Config.is_verbose():")
    print("    print('Verbose mode enabled')")
    print("-" * 70 + "\n")


if __name__ == "__main__":
    main()
