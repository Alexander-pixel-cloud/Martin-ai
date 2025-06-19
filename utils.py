import textstat
import numpy as np
import re

def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text.strip())

def analyze_text(text):
    try:
        readability = textstat.flesch_reading_ease(text)
    except:
        readability = 50.0

    words = text.split()
    unique_word_ratio = len(set(words)) / (len(words) + 1)
    burstiness = np.std([len(s.split()) for s in split_sentences(text)])
    perplexity = 100 - readability + (1 - unique_word_ratio) * 100

    ai_score = (100 - readability + (1 - unique_word_ratio) * 100 + burstiness) / 3
    ai_score = max(0, min(ai_score, 100))
    return ai_score, readability, perplexity, burstiness

def sentence_analysis(text):
    sentences = split_sentences(text)
    results = []
    for s in sentences:
        ai_score, _, _, _ = analyze_text(s)
        results.append((s, ai_score > 65))  # Threshold bisa disesuaikan
    return results
