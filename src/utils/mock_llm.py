"""
Mock LLM for experiment simulations.
"""

import random
from typing import Tuple
from utils.metrics import MetricsEvaluator


def query_llm_mock(context: str, query: str, mode: str = None) -> Tuple[str, float]:
    """
    Mock LLM query

    Args:
        context: Context string
        query: Query string
        mode: 'full_context' or 'rag' (for experiment 3)

    Returns:
        Tuple of (response, accuracy)
    """
    token_count = MetricsEvaluator.count_tokens(context)

    # Experiment 4 (Context Engineering) accuracy simulation
    if mode is None:
        if token_count < 500:
            accuracy = random.uniform(0.85, 0.95)
        elif token_count < 1000:
            accuracy = random.uniform(0.70, 0.85)
        else:
            accuracy = random.uniform(0.50, 0.70)
        response = f"Query processed with context of {token_count} tokens"
                return response, accuracy
            # Experiment 3 (RAG Impact) accuracy simulation
            elif mode in ['full_context', 'rag']:
                expected_answer = "כאבי ראש וסחרחורת"
                contains_answer = expected_answer in context
        
                if mode == 'rag':
                    accuracy_prob = 0.95 if contains_answer else 0.1
                else:  # full context
                    accuracy_prob = 0.70 if contains_answer else 0.1
        
                if random.random() < accuracy_prob:
                    response = f"תופעות הלוואי כוללות {expected_answer}"
                else:
                    response = "לא נמצא מידע"
        
                # Simulate latency - moved from experiment3_rag_impact.py
                import time
                simulated_latency = 0.1 + (token_count / 5000) * 1.5
                time.sleep(simulated_latency / 10) # Speed up for testing
        
                return response, simulated_latency
            # Experiment 2 (Context Size Impact) accuracy simulation
            elif mode == 'context_size':
                simulated_latency = 0.1 + (token_count / 10000) * 2  # Linear growth
                import time
                time.sleep(simulated_latency)
        
                # Simulate accuracy degradation with larger contexts
                # Accuracy decreases as token count increases
                if token_count < 1000:
                    accuracy_prob = 0.95
                elif token_count < 5000:
                    accuracy_prob = 0.80
                elif token_count < 10000:
                    accuracy_prob = 0.65
                else:
                    accuracy_prob = 0.50
                
                expected_answer = "The CEO of the company is David Cohen" # Specific for Experiment 2
        
                if random.random() < accuracy_prob:
                    response = expected_answer
                else:
                    response = "I'm not sure who the CEO is"
                
                return response, simulated_latency    else:
        raise ValueError(f"Unknown mock LLM mode: {mode}")
