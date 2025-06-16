"""
textminer-pro: 고급 텍스트 분석 패키지
"""

from .cleaner import remove_stopwords, extract_keywords
from .summarizer import summarize
from .detector import detect_language

__version__ = "0.1.0"
__author__ = "본인이름"
__email__ = "your.email@example.com"

__all__ = [
    "remove_stopwords",
    "extract_keywords", 
    "summarize",
    "detect_language"
]