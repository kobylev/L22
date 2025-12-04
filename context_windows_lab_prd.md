# PRD: Context Windows Lab - Laboratory Experiments System

## 1. Project Overview

### 1.1 Project Name
Context Windows Laboratory - Practical Experiments in LLM Context Management

### 1.2 Purpose
Build a comprehensive Python-based laboratory system to conduct 4 experiments demonstrating critical phenomena in Large Language Models:
- Lost in the Middle phenomenon
- Context Window Size degradation
- RAG vs Full Context comparison
- Context Engineering strategies evaluation

### 1.3 Target Users
Students and researchers studying LLM context window behavior and optimization techniques

---

## 2. Technical Requirements

### 2.1 Technology Stack
- **Language**: Python 3.10+
- **LLM Framework**: Ollama (local LLM execution)
- **RAG Framework**: LangChain
- **Vector Database**: ChromaDB
- **Embedding Model**: nomic-embed-text
- **Data Visualization**: matplotlib, seaborn
- **Data Processing**: pandas, numpy

### 2.2 System Architecture
```
project_root/
├── src/
│   ├── experiments/
│   │   ├── experiment1_needle_haystack.py
│   │   ├── experiment2_context_size.py
│   │   ├── experiment3_rag_impact.py
│   │   └── experiment4_engineering.py
│   ├── utils/
│   │   ├── text_generator.py
│   │   ├── metrics.py
│   │   └── visualization.py
│   ├── data/
│   │   ├── documents/
│   │   └── results/
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
```

---

## 3. Experiment Specifications

### 3.1 Experiment 1: Needle in Haystack

**Objective**: Demonstrate the "Lost in the Middle" phenomenon

**Input Data**:
- 5 synthetic documents
- Each document: 200 words of filler text
- One critical fact embedded at: start/middle/end positions
- Example fact: "The CEO of the company is David Cohen"

**Implementation Requirements**:
1. `create_documents(num_docs, words_per_doc)`:
   - Generate synthetic filler text
   - Embed critical fact at random position
   - Return list of documents with metadata

2. `measure_accuracy_by_position(documents, query)`:
   - Query Ollama with each document
   - Evaluate response accuracy
   - Track accuracy by fact position (start/middle/end)
   - Return aggregated results

3. **Output**: Graph showing accuracy degradation at middle positions

**Success Criteria**:
- Accuracy at start: >90%
- Accuracy at end: >90%
- Accuracy at middle: <50%

---

### 3.2 Experiment 2: Context Window Size Impact

**Objective**: Measure performance degradation as context grows

**Input Data**:
- Variable document counts: 2, 5, 10, 20, 50 documents
- Each document: 200 words

**Implementation Requirements**:
1. `analyze_context_sizes(doc_counts)`:
   - For each document count:
     - Load documents
     - Concatenate into single context
     - Measure: token count, latency, accuracy
   - Return performance metrics per size

2. **Metrics to Track**:
   - `tokens_used`: Total tokens in context
   - `latency`: Response time (seconds)
   - `accuracy`: Correctness of answer (0-1 score)

3. **Output**:
   - Graph: Accuracy vs Context Size
   - Graph: Latency vs Context Size
   - Table: Performance breakdown

**Success Criteria**:
- Clear correlation between context size and degradation
- Latency increases exponentially
- Accuracy decreases after 10,000+ tokens

---

### 3.3 Experiment 3: RAG Impact

**Objective**: Compare RAG retrieval vs Full Context approach

**Input Data**:
- 20 Hebrew documents
- Topics: Technology, Law, Medicine
- Query: "What are the side effects of drug X?"

**Implementation Requirements**:

1. **RAG Pipeline**:
   ```python
   # Step 1: Chunking
   chunks = split_documents(documents, chunk_size=500)

   # Step 2: Embedding
   embeddings = nomic_embed_text(chunks)

   # Step 3: Vector Store
   vector_store = ChromaDB()
   vector_store.add(chunks, embeddings)

   # Step 4: Retrieval
   relevant_docs = vector_store.similarity_search(query, k=3)
   ```

2. **Comparison Function**:
   ```python
   def compare_modes(query):
       # Mode A: Full Context
       full_response = query_with_full_context(all_documents, query)

       # Mode B: RAG
       relevant_docs = vector_store.similarity_search(query, k=3)
       rag_response = query_with_context(relevant_docs, query)

       return {
           'full_accuracy': evaluate(full_response),
           'rag_accuracy': evaluate(rag_response),
           'full_latency': full_response.latency,
           'rag_latency': rag_response.latency,
           'full_tokens': count_tokens(all_documents),
           'rag_tokens': count_tokens(relevant_docs)
       }
   ```

3. **Output**:
   - Comparison table: RAG vs Full Context
   - Metrics: Accuracy, Latency, Token Count, Cost Estimation

**Success Criteria**:
- RAG accuracy >= Full Context accuracy
- RAG latency < Full Context latency (at least 2x faster)
- RAG tokens < 20% of Full Context tokens

---

### 3.4 Experiment 4: Context Engineering Strategies

**Objective**: Evaluate advanced context management strategies

**Strategies to Implement**:

1. **SELECT Strategy (RAG-based)**:
   - Use similarity search to retrieve only relevant history
   - Keep only top-k relevant chunks

2. **COMPRESS Strategy**:
   - Automatically summarize history when exceeding MAX_TOKENS
   - Use LLM to generate concise summaries

3. **WRITE Strategy (External Memory)**:
   - Extract key facts from history
   - Store in external scratchpad
   - Retrieve relevant facts per query

**Implementation Requirements**:

1. **Multi-Turn Agent Simulation**:
   - Simulate 10 sequential actions
   - Each action generates output that accumulates in history
   - Test each strategy's ability to maintain accuracy

2. **Strategy Functions**:
   ```python
   def select_strategy(history, query):
       relevant = rag_search(history, query, k=5)
       return query_llm(relevant, query)

   def compress_strategy(history, query):
       if len(history) > MAX_TOKENS:
           history = summarize(history)
       return query_llm(history, query)

   def write_strategy(history, query, scratchpad):
       key_facts = extract_key_facts(history)
       scratchpad.store(key_facts)
       return query_llm(scratchpad.retrieve(query), query)
   ```

3. **Output**:
   - Performance table across 10 actions
   - Metrics per strategy: accuracy, latency, memory usage
   - Degradation curve over time

**Success Criteria**:
- SELECT strategy maintains >85% accuracy across all 10 actions
- COMPRESS strategy reduces context by >50%
- WRITE strategy shows no degradation over time

---

## 4. Core Utilities

### 4.1 Text Generation (`text_generator.py`)

```python
class TextGenerator:
    def generate_filler_text(words: int) -> str:
        """Generate synthetic filler text"""

    def embed_critical_fact(text: str, fact: str, position: str) -> str:
        """Embed fact at specified position (start/middle/end)"""

    def create_hebrew_documents(count: int, topics: List[str]) -> List[str]:
        """Generate Hebrew documents for RAG testing"""
```

### 4.2 Metrics (`metrics.py`)

```python
class MetricsEvaluator:
    def evaluate_accuracy(response: str, expected: str) -> float:
        """Calculate response accuracy (0-1 score)"""

    def measure_latency(func: Callable) -> float:
        """Measure function execution time"""

    def count_tokens(text: str) -> int:
        """Count tokens in text"""

    def calculate_cost(tokens: int, model: str) -> float:
        """Estimate API cost based on tokens"""
```

### 4.3 Visualization (`visualization.py`)

```python
class Visualizer:
    def plot_accuracy_by_position(results: Dict) -> None:
        """Bar chart: accuracy by fact position"""

    def plot_context_size_impact(results: List[Dict]) -> None:
        """Line graphs: accuracy & latency vs context size"""

    def plot_rag_comparison(results: Dict) -> None:
        """Side-by-side comparison: RAG vs Full Context"""

    def plot_strategy_performance(results: Dict) -> None:
        """Multi-line graph: strategies over time"""
```

---

## 5. Main Execution Flow

### 5.1 CLI Interface

```python
# main.py
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment', choices=[1,2,3,4,'all'], required=True)
    parser.add_argument('--output-dir', default='./results')
    args = parser.parse_args()

    if args.experiment == 'all':
        run_all_experiments()
    else:
        run_experiment(args.experiment)
```

### 5.2 Usage Examples

```bash
# Run single experiment
python main.py --experiment 1

# Run all experiments
python main.py --experiment all --output-dir ./my_results

# Run with custom parameters
python main.py --experiment 3 --num-docs 30 --chunk-size 300
```

---

## 6. Output Requirements

### 6.1 Results Structure

```
results/
├── experiment1/
│   ├── accuracy_by_position.png
│   ├── raw_data.csv
│   └── summary.json
├── experiment2/
│   ├── context_size_impact.png
│   ├── latency_graph.png
│   └── metrics.csv
├── experiment3/
│   ├── rag_vs_full.png
│   ├── comparison_table.csv
│   └── token_analysis.json
├── experiment4/
│   ├── strategy_performance.png
│   ├── degradation_curves.png
│   └── strategies_summary.csv
└── final_report.pdf
```

### 6.2 Summary Report

Generate PDF report containing:
1. Executive summary of findings
2. All graphs and visualizations
3. Statistical analysis tables
4. Conclusions and recommendations

---

## 7. Non-Functional Requirements

### 7.1 Performance
- Each experiment should complete within specified time limits
- System should handle up to 100 documents without crashing
- Memory usage should not exceed 8GB

### 7.2 Reliability
- Experiments must be reproducible (set random seeds)
- Results should be statistically valid (run multiple iterations)
- Handle API failures gracefully with retry logic

### 7.3 Usability
- Clear progress indicators during execution
- Informative error messages
- Comprehensive logging

### 7.4 Documentation
- README with setup instructions
- API documentation for all functions
- Example notebooks for each experiment

---

## 8. Testing Requirements

### 8.1 Unit Tests
- Test text generation functions
- Test metrics calculation
- Test data processing utilities

### 8.2 Integration Tests
- Test Ollama connectivity
- Test ChromaDB operations
- Test end-to-end experiment flow

### 8.3 Validation Tests
- Verify statistical significance of results
- Validate graph generation
- Check output file formats

---

## 9. Deliverables

### 9.1 Code Deliverables
- ✅ Complete Python project with all 4 experiments
- ✅ Unit tests with >80% coverage
- ✅ Requirements.txt with pinned versions
- ✅ Docker configuration (optional)

### 9.2 Documentation Deliverables
- ✅ README with setup and usage instructions
- ✅ API documentation (Sphinx or similar)
- ✅ Jupyter notebooks with examples
- ✅ Final report PDF with findings

### 9.3 Results Deliverables
- ✅ All graphs and visualizations
- ✅ CSV files with raw experimental data
- ✅ Summary statistics JSON files
- ✅ Comparison tables

---

## 10. Success Metrics

### 10.1 Technical Success
- All 4 experiments execute without errors
- Results match expected patterns
- Statistical significance achieved (p < 0.05)

### 10.2 Educational Success
- Clear demonstration of "Lost in the Middle"
- Quantified impact of context window size
- Proven advantages of RAG approach
- Practical comparison of engineering strategies

### 10.3 Quality Success
- Code follows PEP 8 standards
- Comprehensive test coverage
- Professional documentation
- Reproducible results

---

## 11. Timeline Estimate

- **Experiment 1**: 15 minutes
- **Experiment 2**: 20 minutes
- **Experiment 3**: 25 minutes
- **Experiment 4**: 30 minutes
- **Integration & Testing**: 30 minutes
- **Documentation**: 20 minutes
- **Total**: ~2.5 hours

---

## 12. Dependencies

```txt
# requirements.txt
python>=3.10
ollama>=0.1.0
langchain>=0.1.0
langchain-community>=0.0.20
chromadb>=0.4.0
nomic>=1.0.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
pytest>=7.4.0
jupyter>=1.0.0
```

---

## 13. Future Enhancements

### Phase 2 (Optional)
- Add support for multiple LLM providers (OpenAI, Anthropic)
- Implement caching for faster re-runs
- Add web UI for interactive exploration
- Support for multilingual experiments
- Real-time performance monitoring dashboard

### Phase 3 (Advanced)
- Comparative analysis across different models
- Automatic hyperparameter tuning
- Cloud deployment with CI/CD
- API service for running experiments remotely

---

## 14. Risk Mitigation

### Identified Risks
1. **Ollama API instability**: Implement retry logic with exponential backoff
2. **Memory overflow with large contexts**: Add chunking and streaming
3. **Slow execution times**: Add parallel processing where possible
4. **Inconsistent results**: Set random seeds, run multiple iterations

---

## 15. Acceptance Criteria

### Project is complete when:
- ✅ All 4 experiments run successfully
- ✅ Expected patterns observed in results
- ✅ All visualizations generated correctly
- ✅ Documentation complete and clear
- ✅ Code passes all tests
- ✅ Results are reproducible

---

## 16. Contact & Support

For questions or issues:
- Refer to inline code documentation
- Check example notebooks
- Review test cases for usage patterns

---

**Document Version**: 1.0
**Last Updated**: 2025-12-04
**Author**: Koby Lev
**Course**: AI Expert Program - Lesson 22
