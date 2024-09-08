def correct_sentence(text):
    sentences = text.split('. ')
    corrected_sentences = []
    for sentence in sentences:
        sentence = sentence.strip().capitalize()
        if not sentence.endswith('.'):
            sentence += '.'
        corrected_sentences.append(sentence)
    return ' '.join(corrected_sentences)
# Тести
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print('ОК')
