import logging
from typing import List, Dict
from utils.metrics import MetricsEvaluator

logger = logging.getLogger(__name__)


def select_strategy(history: List[str], query: str, k: int = 5) -> str:
    """
    SELECT Strategy: Use similarity search for relevant history

    Args:
        history: Full history list
        query: Current query
        k: Number of relevant items to keep

    Returns:
        Selected context
    """
    logger.debug("Applying SELECT strategy")

    if len(history) <= k:
        return "\n".join(history)

    # Simple relevance: return last k items (recency)
    relevant_history = history[-k:]
    selected_context = "\n".join(relevant_history)

    logger.debug(f"Selected {len(relevant_history)} most recent items")
    return selected_context


def compress_strategy(history: List[str], query: str, max_tokens: int) -> str:
    """
    COMPRESS Strategy: Summarize history when too large

    Args:
        history: Full history list
        query: Current query
        max_tokens: Maximum tokens before compression needed

    Returns:
        Compressed context
    """
    logger.debug("Applying COMPRESS strategy")

    full_context = "\n".join(history)
    token_count = MetricsEvaluator.count_tokens(full_context)

    if token_count <= max_tokens:
        return full_context

    # Simulate summarization: keep first and last parts
    keep_count = len(history) // 3
    compressed = history[:keep_count] + ["... [history compressed] ..."] + history[-keep_count:]
    compressed_context = "\n".join(compressed)

    logger.debug(f"Compressed history from {len(history)} to {len(compressed)} items")
    return compressed_context


def write_strategy(history: List[str], query: str, scratchpad: Dict) -> str:
    """
    WRITE Strategy: Extract key facts to external memory

    Args:
        history: Full history list
        query: Current query
        scratchpad: External memory to store facts

    Returns:
        Retrieved context from scratchpad
    """
    logger.debug("Applying WRITE strategy")

    # Extract and store key facts
    for idx, item in enumerate(history):
        if "key" not in scratchpad:
            scratchpad["key"] = []

        # Simple extraction: store items mentioning "Success" or "Found"
        if "Success" in item or "Found" in item:
            fact = f"Fact {idx}: {item[:100]}"
            if fact not in scratchpad["key"]:
                scratchpad["key"].append(fact)

    # Retrieve relevant facts
    if "key" in scratchpad and scratchpad["key"]:
        retrieved_context = "\n".join(scratchpad["key"][-5:])  # Last 5 facts
        logger.debug(f"Retrieved {len(scratchpad['key'][-5:])} facts from scratchpad")
        return retrieved_context

    return "No facts stored yet"
