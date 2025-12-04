import logging
import time
from typing import List, Dict, Tuple
from utils.metrics import MetricsEvaluator
from utils.mock_llm import query_llm_mock
from utils.rag_utils import simple_similarity_search

logger = logging.getLogger(__name__)


def run_full_context_mode(documents: List[Dict], query: str) -> Dict:
    """
    Run query with full context (all documents)

    Args:
        documents: List of all documents
        query: Search query

    Returns:
        Results dictionary
    """
    logger.info("Running FULL CONTEXT mode...")

    # Concatenate all documents
    all_texts = [doc['text'] for doc in documents]
    full_context = "\n\n".join(all_texts)

    # Query LLM
    start_time = time.time()
    response, simulated_latency = query_llm_mock(
        full_context, query, mode='full_context'
    )
    actual_latency = time.time() - start_time

    # Evaluate
    tokens_used = MetricsEvaluator.count_tokens(full_context)
    accuracy = MetricsEvaluator.evaluate_accuracy(
        response=response,
        expected="כאבי ראש",
        threshold=0.5
    )

    result = {
        'mode': 'full_context',
        'accuracy': accuracy,
        'latency': actual_latency,
        'tokens_used': tokens_used,
        'num_docs': len(documents)
    }

    logger.info(
        f"  Accuracy: {accuracy:.2f}, "
        f"Latency: {actual_latency:.3f}s, "
        f"Tokens: {tokens_used}"
    )

    return result


def run_rag_mode(documents: List[Dict], query: str, top_k: int) -> Dict:
    """
    Run query with RAG (selective retrieval)

    Args:
        documents: List of all documents
        query: Search query
        top_k: Number of documents to retrieve

    Returns:
        Results dictionary
    """
    logger.info("Running RAG mode...")

    # Retrieve relevant documents
    relevant_docs = simple_similarity_search(documents, query, k=top_k)
    rag_context = "\n\n".join([doc['text'] for doc in relevant_docs])

    # Query LLM
    start_time = time.time()
    response, simulated_latency = query_llm_mock(
        rag_context, query, mode='rag'
    )
    actual_latency = time.time() - start_time

    # Evaluate
    tokens_used = MetricsEvaluator.count_tokens(rag_context)
    accuracy = MetricsEvaluator.evaluate_accuracy(
        response=response,
        expected="כאבי ראש",
        threshold=0.5
    )

    result = {
        'mode': 'rag',
        'accuracy': accuracy,
        'latency': actual_latency,
        'tokens_used': tokens_used,
        'num_docs': len(relevant_docs)
    }

    logger.info(
        f"  Accuracy: {accuracy:.2f}, "
        f"Latency: {actual_latency:.3f}s, "
        f"Tokens: {tokens_used}"
    )

    return result
