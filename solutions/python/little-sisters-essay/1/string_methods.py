# Task 1: Capitalize the title of the paper
def capitalize_title(title):
    return title.title()


# Task 2: Check if each sentence ends with a period
def check_sentence_ending(sentence):
    return sentence.endswith('.')


# Task 3: Clean up spacing
def clean_up_spacing(sentence):
    return sentence.strip()


# Task 4: Replace words with a synonym
def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)