# https://github.com/OOPSpam/spam-words
# https://github.com/roumilb/spam_words_api_lists
import json

with open('telegram_bot/consts/files/referral_links_words.json') as f:
    _referral_links_words_file_content = json.loads(f.read())

_spam_words_files_content = []
with open('telegram_bot/consts/files/spam_words_en.json') as f:
    _spam_words_file_content_en = json.loads(f.read())
with open('telegram_bot/consts/files/spam_words_ru.json') as f:
    _spam_words_file_content_ru = json.loads(f.read())
with open('telegram_bot/consts/files/spam_words_uk.json') as f:
    _spam_words_file_content_uk = json.loads(f.read())
_spam_words_files_content.extend([
    _spam_words_file_content_en,
    _spam_words_file_content_ru,
    _spam_words_file_content_uk
])

REFERRAL_LINKS_WORDS_INSERTIONS = []
SPAM_WORDS_INSERTIONS = []

for w in _referral_links_words_file_content:
    REFERRAL_LINKS_WORDS_INSERTIONS.extend([
        formatting.format(word=w)
        for formatting in [
            "?{word}=",
            "#{word}="
        ]
    ])

for w_lst in _spam_words_files_content:
    SPAM_WORDS_INSERTIONS.extend([
        w.lower()
        for w in w_lst
    ])
