"""
Text Generation Utilities for Context Windows Lab
Generates synthetic documents and Hebrew text for experiments
Author: Context Windows Lab
"""

import random
import logging
from typing import List, Dict, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TextGenerator:
    """Generates synthetic text for context window experiments"""

    # Filler words for synthetic text generation
    FILLER_WORDS = [
        "system", "process", "data", "information", "analysis", "result",
        "performance", "evaluation", "implementation", "framework", "structure",
        "component", "interface", "protocol", "standard", "requirement",
        "specification", "documentation", "configuration", "optimization",
        "integration", "deployment", "monitoring", "validation", "testing"
    ]

    # Hebrew filler text samples by topic
    HEBREW_TOPICS = {
        "technology": [
            "מערכת המחשוב החדשה משפרת את הביצועים באופן משמעותי.",
            "הטכנולוגיה המתקדמת מאפשרת עיבוד מהיר של נתונים.",
            "הפיתוח כולל ארכיטקטורה מודולרית וגמישה.",
            "האינטגרציה עם מערכות קיימות בוצעה בהצלחה.",
            "הממשק החדש מספק חווית משתמש משופרת."
        ],
        "law": [
            "החוק החדש נכנס לתוקף בתחילת השנה.",
            "בית המשפט דחה את התביעה מחוסר סמכות.",
            "ההסכם החוזי כולל סעיפים מפורטים.",
            "הרגולציה החדשה משפיעה על כל המגזר.",
            "הפסיקה קובעת תקדים משפטי חשוב."
        ],
        "medicine": [
            "התרופה החדשה עברה ניסויים קליניים מקיפים.",
            "תופעות הלוואי כוללות כאבי ראש וסחרחורת.",
            "המינון המומלץ הוא פעמיים ביום אחרי אוכל.",
            "הטיפול משפר את איכות החיים של המטופלים.",
            "המחקר הרפואי מראה תוצאות מבטיחות."
        ]
    }

    @staticmethod
    def generate_action_output(action_num: int) -> str:
        """
        Generate output for a simulated action

        Args:
            action_num: Action number

        Returns:
            Generated output text
        """
        outputs = [
            f"Action {action_num}: Retrieved data from database. Found 15 records.",
            f"Action {action_num}: Processed user request. Status: Success.",
            f"Action {action_num}: Generated report with key metrics.",
            f"Action {action_num}: Updated system configuration.",
            f"Action {action_num}: Analyzed performance data.",
        ]
        return random.choice(outputs) + " " + TextGenerator.generate_filler_text(50)

    @staticmethod
    def generate_filler_text(words: int) -> str:
        """
        Generate synthetic filler text

        Args:
            words: Number of words to generate

        Returns:
            Generated text string
        """
        logger.debug(f"Generating {words} words of filler text")

        text_words = []
        for _ in range(words):
            word = random.choice(TextGenerator.FILLER_WORDS)
            text_words.append(word)

        # Create sentences (10-15 words per sentence)
        sentences = []
        for i in range(0, len(text_words), random.randint(10, 15)):
            sentence_words = text_words[i:i+random.randint(10, 15)]
            if sentence_words:
                sentence = " ".join(sentence_words).capitalize() + "."
                sentences.append(sentence)

        result = " ".join(sentences)
        logger.info(f"Generated filler text with {len(result.split())} words")
        return result

    @staticmethod
    def embed_critical_fact(
        text: str,
        fact: str,
        position: str
    ) -> Tuple[str, int]:
        """
        Embed a critical fact at specified position

        Args:
            text: Base text to embed fact into
            fact: Critical fact to embed
            position: 'start', 'middle', or 'end'

        Returns:
            Tuple of (modified text, fact position index)
        """
        logger.debug(f"Embedding fact at position: {position}")

        sentences = text.split(". ")
        total_sentences = len(sentences)

        if position == "start":
            insert_idx = 0
        elif position == "middle":
            insert_idx = total_sentences // 2
        elif position == "end":
            insert_idx = total_sentences - 1
        else:
            raise ValueError(f"Invalid position: {position}")

        # Insert the fact
        sentences.insert(insert_idx, fact)
        result = ". ".join(sentences)

        logger.info(f"Fact embedded at position {position} (index {insert_idx})")
        return result, insert_idx

    @staticmethod
    def create_documents(
        num_docs: int = 5,
        words_per_doc: int = 200,
        fact: str = "The CEO of the company is David Cohen"
    ) -> List[Dict]:
        """
        Create synthetic documents with embedded facts

        Args:
            num_docs: Number of documents to create
            words_per_doc: Words per document
            fact: Critical fact to embed

        Returns:
            List of document dictionaries with metadata
        """
        logger.info(f"Creating {num_docs} documents with {words_per_doc} words each")

        documents = []
        positions = ["start", "middle", "end"]

        for i in range(num_docs):
            base_text = TextGenerator.generate_filler_text(words_per_doc)
            position = random.choice(positions)
            doc_text, fact_idx = TextGenerator.embed_critical_fact(
                base_text, fact, position
            )

            documents.append({
                "id": i,
                "text": doc_text,
                "fact": fact,
                "fact_position": position,
                "fact_index": fact_idx,
                "word_count": len(doc_text.split())
            })

        logger.info(f"Created {len(documents)} documents successfully")
        return documents

    @staticmethod
    def create_hebrew_documents(
        count: int = 20,
        topics: List[str] = None
    ) -> List[Dict]:
        """
        Generate Hebrew documents for RAG testing

        Args:
            count: Number of documents to create
            topics: List of topics (default: all topics)

        Returns:
            List of Hebrew document dictionaries
        """
        if topics is None:
            topics = list(TextGenerator.HEBREW_TOPICS.keys())

        logger.info(f"Creating {count} Hebrew documents with topics: {topics}")

        documents = []
        for i in range(count):
            topic = random.choice(topics)
            sentences = random.sample(
                TextGenerator.HEBREW_TOPICS[topic],
                min(3, len(TextGenerator.HEBREW_TOPICS[topic]))
            )

            # Add some repetition for realistic document size
            doc_text = " ".join(sentences * 3)

            documents.append({
                "id": i,
                "text": doc_text,
                "topic": topic,
                "word_count": len(doc_text.split())
            })

        logger.info(f"Created {len(documents)} Hebrew documents")
        return documents

    @staticmethod
    def concatenate_documents(documents: List[Dict]) -> str:
        """
        Concatenate documents into single context

        Args:
            documents: List of document dictionaries

        Returns:
            Combined context string
        """
        texts = [doc['text'] for doc in documents]
        context = "\n\n".join(texts)
        return context
