
filename = input()
corpus = open(filename, "r", encoding="utf-8")

corpus_string = corpus.read()
tokens = corpus_string.split()

print("Corpus statistics")
print("All tokens: ", len(tokens))
print("Unique tokens: ", len(set(tokens)))

while True:
    index = input()
    if index == 'exit':
        exit()
    try:
        index_int = int(index)
        print(tokens[index_int])
    except IndexError:
        print("IndexError. Please input an integer that is in the range of the corpus.")
    except ValueError:
        print("TypeError. Please enter correct value.")



