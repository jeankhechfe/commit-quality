import csv
import spacy
from spacy.symbols import ORTH

nlp = spacy.load("en_core_web_lg")

nlp.tokenizer.add_special_case('fix', [{ORTH: 'fixing'}])  # treat fix as verb
nlp.tokenizer.add_special_case('make', [{ORTH: 'making'}])  # treat fix as verb
nlp.tokenizer.add_special_case('fixed', [{ORTH: 'fixing'}])  # treat fixed as verb
nlp.tokenizer.add_special_case('update', [{ORTH: 'updating'}])  # treat update as verb
nlp.tokenizer.add_special_case('updated', [{ORTH: 'updating'}])  # treat updated as verb
nlp.tokenizer.add_special_case('added', [{ORTH: 'adding'}])  # treat added as verb
nlp.tokenizer.add_special_case('import', [{ORTH: 'importing'}])  # treat import as verb
nlp.tokenizer.add_special_case('load', [{ORTH: 'loading'}])  # treat load as verb
nlp.tokenizer.add_special_case('show', [{ORTH: 'showing'}])  # fix 'show' not being recognized

stop_words = ['DET', 'ADP', 'NUM', 'SCONJ', 'CCONJ', 'AUX', 'PRON', 'PART', 'SPACE', 'ADV', 'PROPN', 'INTJ']
with open('data/data_bag_of_words(new tags)_raw.csv', 'r') as input_file:
    lines = csv.reader(input_file)
    outputMessages = []
    outputLabels = []
    for line in lines:
        msg_lines = line[0].split('\n')
        temp = ''
        temp2 = ''
        for msg_line in msg_lines:
            words = msg_line.split(' ')
            doc = nlp(msg_line)
            for token in doc:
                if 2 < len(token.text) <= 16 and token.pos_ not in stop_words:
                    temp += token.lemma_ + ' '
        outputMessages.append(temp)
        outputLabels.append(line[1])

with open('data/data_bag_of_words(new tags).csv', 'w', newline='') as output_file:
    spam_writer = csv.writer(output_file)
    for message, label in zip(outputMessages, outputLabels):
        spam_writer.writerow([message, label])

