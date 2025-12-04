# Environment Configuration Guide

## 📋 Overview

The Context Windows Laboratory uses a `.env` file for configuration management. This allows you to customize experiment parameters, output settings, and behavior without modifying code.

---

## 🚀 Quick Start

### 1. Copy the Example File

```bash
# Copy the example to create your own .env file
cp .env.example .env
```

The `.env` file is already created with default values, but you can customize it.

### 2. Edit Configuration

Open `.env` in your text editor and modify values as needed.

### 3. Run Experiments

The configuration will be automatically loaded:

```bash
python src/main.py --experiment all
```

---

## 🔧 Configuration Options

### Experiment 1: Needle in Haystack

```ini
# Number of documents to generate
EXPERIMENT1_NUM_DOCS=15

# Words per document
EXPERIMENT1_WORDS_PER_DOC=200

# Critical fact to embed
CRITICAL_FACT=The CEO of the company is David Cohen
```

**Usage Example:**
- Increase `EXPERIMENT1_NUM_DOCS=30` for better statistics
- Decrease `EXPERIMENT1_WORDS_PER_DOC=100` for faster execution

---

### Experiment 2: Context Window Size Impact

```ini
# Document counts to test (comma-separated)
EXPERIMENT2_DOC_COUNTS=2,5,10,20,50

# Words per document
EXPERIMENT2_WORDS_PER_DOC=200
```

**Usage Example:**
- Add more sizes: `EXPERIMENT2_DOC_COUNTS=2,5,10,20,50,100`
- Test smaller contexts: `EXPERIMENT2_DOC_COUNTS=1,2,3,5`

---

### Experiment 3: RAG Impact

```ini
# Total number of documents
EXPERIMENT3_NUM_DOCUMENTS=20

# Number of documents to retrieve (RAG)
EXPERIMENT3_TOP_K=3

# Hebrew query
HEBREW_QUERY=מה תופעות הלוואי של התרופה

# Topics (comma-separated)
HEBREW_TOPICS=technology,law,medicine
```

**Usage Example:**
- Test different retrieval sizes: `EXPERIMENT3_TOP_K=5`
- More documents: `EXPERIMENT3_NUM_DOCUMENTS=50`

---

### Experiment 4: Context Engineering Strategies

```ini
# Number of sequential actions
EXPERIMENT4_NUM_ACTIONS=10

# Maximum tokens before compression
EXPERIMENT4_MAX_TOKENS=2000
```

**Usage Example:**
- Longer simulation: `EXPERIMENT4_NUM_ACTIONS=20`
- Test compression earlier: `EXPERIMENT4_MAX_TOKENS=1000`

---

## 📊 Output Configuration

### Results Directory

```ini
# Base directory for results
RESULTS_DIR=src/data/results
```

**Change output location:**
```ini
RESULTS_DIR=results  # Save to project root
RESULTS_DIR=/tmp/context_lab_results  # Save to temp folder
```

---

### Image Settings

```ini
# Resolution (DPI)
IMAGE_DPI=300

# Format: png, jpg, pdf, svg
IMAGE_FORMAT=png

# Figure size (inches)
IMAGE_WIDTH=10
IMAGE_HEIGHT=6
```

**High-quality output:**
```ini
IMAGE_DPI=600
IMAGE_FORMAT=pdf
```

**Web-optimized:**
```ini
IMAGE_DPI=150
IMAGE_FORMAT=jpg
```

---

## 📝 Logging Configuration

```ini
# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL=INFO

# Log file (empty = console only)
LOG_FILE=

# Log format
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

**Debug mode:**
```ini
LOG_LEVEL=DEBUG
LOG_FILE=logs/debug.log
```

**Production mode:**
```ini
LOG_LEVEL=WARNING
```

---

## 🎲 Reproducibility

```ini
# Random seed for reproducible results
RANDOM_SEED=42
```

**Usage:**
- Set `RANDOM_SEED=42` for consistent results across runs
- Leave empty or comment out for random behavior each time

```ini
# Different runs, same results
RANDOM_SEED=42

# Different runs, different results
RANDOM_SEED=
```

---

## 🎨 Visualization

```ini
# Color scheme (hex codes)
COLOR_START=#2ecc71    # Green
COLOR_MIDDLE=#e74c3c   # Red
COLOR_END=#3498db      # Blue

# Automatically show plots
AUTO_SHOW_PLOTS=true

# Automatically save plots
AUTO_SAVE_PLOTS=true
```

**Customization:**
```ini
# Custom color scheme
COLOR_START=#ff6b6b
COLOR_MIDDLE=#4ecdc4
COLOR_END=#45b7d1

# Disable auto-show for server environments
AUTO_SHOW_PLOTS=false
```

---

## ⚙️ Performance Settings

```ini
# Use mock LLM (true) or real LLM (false)
USE_MOCK_LLM=true

# Run in test mode (reduced datasets)
TEST_MODE=false

# Verbose output
VERBOSE=false
```

**Test mode (faster execution):**
```ini
TEST_MODE=true  # Uses smaller datasets
EXPERIMENT1_NUM_DOCS=5
EXPERIMENT2_DOC_COUNTS=2,5,10
```

---

## 🔮 Future: Real LLM Integration

When ready to integrate real LLMs, configure these settings:

### Ollama

```ini
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
USE_MOCK_LLM=false
```

### OpenAI

```ini
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-3.5-turbo
USE_MOCK_LLM=false
```

### Anthropic Claude

```ini
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here
ANTHROPIC_MODEL=claude-3-sonnet-20240229
USE_MOCK_LLM=false
```

---

## 📚 Usage in Code

The configuration is automatically loaded via the `Config` class:

```python
from src.utils.config import Config

# Get experiment configuration
exp1_config = Config.get_experiment1_config()
print(exp1_config['num_docs'])  # 15

# Get results directory
results_dir = Config.get_results_dir()

# Check mode flags
if Config.is_verbose():
    print("Verbose mode enabled")

# Print all configuration
Config.print_config()
```

---

## 🛡️ Security Best Practices

### DO:
✅ Keep `.env` out of version control (it's in `.gitignore`)
✅ Use `.env.example` as a template for others
✅ Store API keys in `.env` (never in code)
✅ Use different `.env` files for dev/prod

### DON'T:
❌ Commit `.env` to Git
❌ Share `.env` files with API keys
❌ Hard-code sensitive values in code

---

## 🔍 Troubleshooting

### Issue: Configuration not loading

**Check:**
```bash
# Verify .env exists
ls -la .env

# Check file contents
cat .env

# Verify python-dotenv is installed
pip list | grep python-dotenv
```

**Solution:**
```bash
# Install if missing
pip install python-dotenv

# Copy from example
cp .env.example .env
```

---

### Issue: Invalid values

**Check syntax:**
```ini
# ✅ CORRECT
EXPERIMENT1_NUM_DOCS=15
LOG_LEVEL=INFO

# ❌ INCORRECT (no spaces around =)
EXPERIMENT1_NUM_DOCS = 15
LOG_LEVEL = INFO
```

---

### Issue: Boolean values not working

**Use lowercase:**
```ini
# ✅ CORRECT
USE_MOCK_LLM=true
VERBOSE=false

# ❌ INCORRECT
USE_MOCK_LLM=True
VERBOSE=False
```

---

## 📖 Examples

### Example 1: Quick Testing

```ini
# .env for quick testing
TEST_MODE=true
EXPERIMENT1_NUM_DOCS=5
EXPERIMENT2_DOC_COUNTS=2,5
EXPERIMENT3_NUM_DOCUMENTS=10
EXPERIMENT4_NUM_ACTIONS=5
LOG_LEVEL=WARNING
AUTO_SHOW_PLOTS=false
```

**Run:**
```bash
python src/main.py --experiment all  # Completes in ~10 seconds
```

---

### Example 2: High-Quality Research

```ini
# .env for research/publication
EXPERIMENT1_NUM_DOCS=50
EXPERIMENT2_DOC_COUNTS=2,5,10,20,50,100
EXPERIMENT3_NUM_DOCUMENTS=100
EXPERIMENT4_NUM_ACTIONS=20
IMAGE_DPI=600
IMAGE_FORMAT=pdf
RANDOM_SEED=42
LOG_LEVEL=INFO
```

**Run:**
```bash
python src/main.py --experiment all  # Higher quality, longer runtime
```

---

### Example 3: Production Mode

```ini
# .env for production
USE_MOCK_LLM=false
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
LOG_LEVEL=WARNING
LOG_FILE=logs/production.log
AUTO_SHOW_PLOTS=false
RESULTS_DIR=/var/lib/context_lab/results
```

---

## 🔄 Environment Variables Override

Command-line arguments override `.env` values:

```bash
# This overrides .env LOG_LEVEL
python src/main.py --experiment all --verbose

# Set env var temporarily
LOG_LEVEL=DEBUG python src/main.py --experiment 1
```

---

## 📊 Configuration Validation

Print current configuration before running:

```python
from src.utils.config import Config

# Print all settings
Config.print_config()
```

**Output:**
```
============================================================
CURRENT CONFIGURATION
============================================================
Experiment 1: {'num_docs': 15, 'words_per_doc': 200, ...}
Experiment 2: {'doc_counts': [2, 5, 10, 20, 50], ...}
...
============================================================
```

---

## ✅ Quick Reference

| Setting | Default | Purpose |
|---------|---------|---------|
| `EXPERIMENT1_NUM_DOCS` | 15 | Documents for Exp 1 |
| `RANDOM_SEED` | 42 | Reproducibility |
| `LOG_LEVEL` | INFO | Logging verbosity |
| `IMAGE_DPI` | 300 | Output resolution |
| `USE_MOCK_LLM` | true | Use mock vs real LLM |
| `AUTO_SHOW_PLOTS` | true | Display graphs |
| `RESULTS_DIR` | src/data/results | Output location |

---

**Need help? Check [README.md](README.md) for full documentation.**
