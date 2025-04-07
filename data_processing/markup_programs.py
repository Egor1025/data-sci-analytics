import pandas as pd
import re
import pymorphy2
import inspect
import os


MIN_MATCH_RATIO = 0.0218


def getargspec(func):
    spec = inspect.getfullargspec(func)
    return spec.args, spec.varargs, spec.varkw, spec.defaults
inspect.getargspec = getargspec


morph = pymorphy2.MorphAnalyzer()
keywords = [
    'большие данные', 'нейросети', 'нейронные сети', 'машинное обучение', 'искусственный интеллект',
    'интеллектуальный анализ', 'интеллектуальные системы', 'большие языковые модели',
    'глубокое обучение', 'ии', 'большие объемы информации', 'машинное зрение', 'компьютерное зрение',
    'data science', 'big data', 'artificial intelligence', 'deep learning', 'machine learning', 'computer vision', 'ml', 'llm', 'bigdata'
]


def lemmatize(text):
    text_clean = re.sub(r'[^\w\s]', ' ', text.lower())
    return [morph.normal_forms(word)[0] for word in text_clean.split()]

def classify_text(text):
    lemmas = lemmatize(text)
    count = 0
    for kw in keywords:
        kw_lemmas = [morph.normal_forms(token)[0] for token in kw.split()]
        if all(token in lemmas for token in kw_lemmas):
            count += 1

    global PROGRAMS
    PROGRAMS += 1
    if os.name != 'nt' and 'TERM' in os.environ:
        os.system('clear')
        print(f'Кол-во размеченных программ: {PROGRAMS}/{QUANTITY}')

    return count / len(lemmas) if len(lemmas) > 0 else 0


df = pd.read_json('../data/programs-info-lines.json')
PROGRAMS, QUANTITY = 0, len(df)

df['Matches'] = df['О программе'].apply(classify_text)

df_filtered = df[df['Matches'] > MIN_MATCH_RATIO].sort_values(by='Matches', ascending=False)
df_filtered.to_json('data-sci-programs.json', force_ascii=False, orient='records', indent=4)
