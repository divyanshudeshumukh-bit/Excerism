# Task 1: 
def add_prefix_un(word):
    return "un" + word


# Task 2: 
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + words)


# Task 3: 
def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith("i"):
        root = root[:-1] + "y"
    return root


# Task 4: 
def adjective_to_verb(sentence, index):
    word = sentence.split()[index]
    return word.rstrip(".") + "en"