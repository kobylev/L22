"""
Configuration Management
Provides access to environment settings
"""

import sys
from pathlib import Path
from .env_loader import (
    get_env_int, get_env_float, get_env_bool,
    get_env_list, get_env_str, project_root
)


class Config:
    """Configuration settings from environment variables"""

    @staticmethod
    def get_experiment1_config() -> dict:
        """Experiment 1 configuration"""
        return {
            'num_docs': get_env_int('EXPERIMENT1_NUM_DOCS', 15),
            'words_per_doc': get_env_int('EXPERIMENT1_WORDS_PER_DOC', 200),
            'critical_fact': get_env_str('CRITICAL_FACT',
                'The CEO of the company is David Cohen')
        }

    @staticmethod
    def get_experiment2_config() -> dict:
        """Experiment 2 configuration"""
        doc_counts = [int(x) for x in get_env_list(
            'EXPERIMENT2_DOC_COUNTS', '2,5,10,20,50')]
        return {
            'doc_counts': doc_counts,
            'words_per_doc': get_env_int('EXPERIMENT2_WORDS_PER_DOC', 200)
        }

    @staticmethod
    def get_experiment3_config() -> dict:
        """Experiment 3 configuration"""
        return {
            'num_documents': get_env_int('EXPERIMENT3_NUM_DOCUMENTS', 20),
            'top_k': get_env_int('EXPERIMENT3_TOP_K', 3),
            'query': get_env_str('HEBREW_QUERY',
                'מה תופעות הלוואי של התרופה'),
            'topics': get_env_list('HEBREW_TOPICS',
                'technology,law,medicine')
        }

    @staticmethod
    def get_experiment4_config() -> dict:
        """Experiment 4 configuration"""
        return {
            'num_actions': get_env_int('EXPERIMENT4_NUM_ACTIONS', 10),
            'max_tokens': get_env_int('EXPERIMENT4_MAX_TOKENS', 2000)
        }

    @staticmethod
    def get_results_dir() -> Path:
        """Get results directory path"""
        results_dir = get_env_str('RESULTS_DIR', 'src/data/results')
        return project_root / results_dir

    @staticmethod
    def get_image_config() -> dict:
        """Image output configuration"""
        return {
            'dpi': get_env_int('IMAGE_DPI', 300),
            'format': get_env_str('IMAGE_FORMAT', 'png'),
            'width': get_env_float('IMAGE_WIDTH', 10),
            'height': get_env_float('IMAGE_HEIGHT', 6)
        }

    @staticmethod
    def get_log_level() -> str:
        """Get logging level"""
        return get_env_str('LOG_LEVEL', 'INFO')

    @staticmethod
    def get_random_seed() -> int:
        seed_str = get_env_str('RANDOM_SEED', '')
        return int(seed_str) if seed_str else None

    @staticmethod
    def get_chars_per_token() -> int:
        return get_env_int('CHARS_PER_TOKEN', 4)

    @staticmethod
    def get_accuracy_threshold() -> float:
        return get_env_float('ACCURACY_THRESHOLD', 0.6)

    @staticmethod
    def use_mock_llm() -> bool:
        """Check if mock LLM should be used"""
        return get_env_bool('USE_MOCK_LLM', 'true')

    @staticmethod
    def is_test_mode() -> bool:
        """Check if running in test mode"""
        return get_env_bool('TEST_MODE', 'false')

    @staticmethod
    def is_verbose() -> bool:
        """Check if verbose mode enabled"""
        return get_env_bool('VERBOSE', 'false')

    @staticmethod
    def auto_show_plots() -> bool:
        """Check if plots show automatically"""
        return get_env_bool('AUTO_SHOW_PLOTS', 'true')

    @staticmethod
    def auto_save_plots() -> bool:
        """Check if plots save automatically"""
        return get_env_bool('AUTO_SAVE_PLOTS', 'true')

    @staticmethod
    def get_color_scheme() -> dict:
        """Get color scheme"""
        return {
            'start': get_env_str('COLOR_START', '#2ecc71'),
            'middle': get_env_str('COLOR_MIDDLE', '#e74c3c'),
            'end': get_env_str('COLOR_END', '#3498db')
        }

    @staticmethod
    def print_config():
        """Print configuration"""
        if sys.platform == 'win32':
            try:
                sys.stdout.reconfigure(encoding='utf-8')
            except:
                pass
        print("\n" + "=" * 60)
        print("CURRENT CONFIGURATION")
        print("=" * 60)
        print(f"Experiment 1: {Config.get_experiment1_config()}")
        print(f"Experiment 2: {Config.get_experiment2_config()}")
        exp3 = Config.get_experiment3_config()
        try:
            print(f"Experiment 3: {exp3}")
        except UnicodeEncodeError:
            print(f"Experiment 3: (num_documents={exp3['num_documents']}, top_k={exp3['top_k']}, query=<Hebrew>)")
        print(f"Experiment 4: {Config.get_experiment4_config()}")
        print(f"Results Dir: {Config.get_results_dir()}")
        print(f"Log Level: {Config.get_log_level()}")
        print(f"Random Seed: {Config.get_random_seed()}")
        print(f"Mock LLM: {Config.use_mock_llm()}")
        print("=" * 60 + "\n")
