import nltk

file_name = input()
file = open(file_name, "r", encoding="utf-8")
bigrams = list(nltk.bigrams(file.read().split()))
file.close()

markov_model = {}
for head, tail in bigrams:
    markov_model.setdefault(head, {})
    markov_model[head].setdefault(tail, 0)
    markov_model[head][tail] += 1

request = input()
while request != 'exit':
    print(f"Head: {request}")
    try:
        for tail in markov_model[request]:
            print(f"Tail: {tail}    Count: {markov_model[request][tail]}")
    except KeyError:
        print('The requested word is not in the model. Please input another word.')
    request = input()
