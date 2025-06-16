# TextMiner-Pro

고급 텍스트 분석을 위한 Python 패키지입니다.

## 주요 기능

- 불용어 제거 (remove_stopwords)
- 키워드 추출 (extract_keywords)
- 텍스트 요약 (summarize)
- 언어 감지 (detect_language)

## 설치

```bash
pip install textminer-pro-asddzxqw
```

## 사용법

```python

from textminer import remove_stopwords, extract_keywords, summarize, detect_language

text = "This is a sample text for analysis"
clean_text = remove_stopwords(text)
keywords = extract_keywords(text, top_n=5)
language = detect_language(text)
```