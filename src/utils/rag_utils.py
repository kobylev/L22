import logging
from typing import List, Dict, Tuple
from utils.text_generator import TextGenerator

logger = logging.getLogger(__name__)


def generate_documents(num_documents: int, topics: List[str]) -> List[Dict]:
    """
    Generate Hebrew documents with topics

    Args:
        num_documents: Total number of documents
        topics: List of topics for document generation

    Returns:
        List of document dictionaries
    """
    logger.info("Generating Hebrew documents")

    documents = TextGenerator.create_hebrew_documents(
        count=num_documents,
        topics=topics
    )

    # Add a specific answer to medicine documents
    medicine_fact = "תופעות הלוואי כוללות כאבי ראש וסחרחורת"
    for doc in documents:
        if doc['topic'] == 'medicine':
            doc['text'] += f" {medicine_fact}"
            doc['contains_answer'] = True
        else:
            doc['contains_answer'] = False

    logger.info(f"Generated {len(documents)} documents")
    return documents


def simple_similarity_search(documents: List[Dict], query: str, k: int = 3) -> List[Dict]:
    """
    Simple keyword-based similarity search (mock RAG)

    Args:
        documents: List of all available documents
        query: Search query
        k: Number of documents to retrieve

    Returns:
        List of most relevant documents
    """
    logger.debug(f"Performing similarity search for: {query}")

    # Simple keyword matching
    query_words = set(query.lower().split())
    scored_docs = []

    for doc in documents:
        doc_words = set(doc['text'].lower().split())
        overlap = len(query_words & doc_words)
        scored_docs.append((overlap, doc))

    # Sort by score and return top-k
    scored_docs.sort(reverse=True, key=lambda x: x[0])
    top_docs = [doc for score, doc in scored_docs[:k]]

    logger.debug(f"Retrieved {len(top_docs)} relevant documents")
    return top_docs
