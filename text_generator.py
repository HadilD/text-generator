import nltk
import random

file_name = input()
file = open(file_name, "r", encoding="utf-8")
# nltk.trigrams returns a list of 3-tuples
trigrams = list(nltk.trigrams(file.read().split()))
file.close()

model = {}
for trigram in trigrams:
    head = trigram[0] + " " + trigram[1]
    tail = trigram[2]
    model.setdefault(head, {})
    model[head].setdefault(tail, 0)
    model[head][tail] += 1

possible_starting_heads = []
sentence_ending_punctuation = (".", "!", "?")
for key in model.keys():
    if key[0].isupper() and not key.split(" ")[0].endswith(sentence_ending_punctuation):
        possible_starting_heads.append(key)

# Generate 10 pseudo-sentences based on model
for _ in range(10):
    tokens = []
    # Chooses a random starting head from list
    head = random.choice(possible_starting_heads)
    # print("Head: ", head)
    tokens.append(head)
    while True:
        possible_tails = list(model[head].keys())
        weights = list(model[head].values())
        # Randomly select elements from list taking their weights into account
        most_probable_tail = random.choices(possible_tails, weights, k=1)[0]
        # print("Most probable tail: ", most_probable_tail)

        if most_probable_tail.endswith(sentence_ending_punctuation) and len(tokens) >= 5:
            tokens.append(most_probable_tail)
            # print("Chosen tail and ending sentence: ", most_probable_tail)
            break
        elif not most_probable_tail.endswith(sentence_ending_punctuation):
            tokens.append(most_probable_tail)
            # print("Chosen tail: ", most_probable_tail)
            head = head.split(" ")[1] + " " + most_probable_tail
        elif most_probable_tail.endswith(sentence_ending_punctuation) and len(tokens) < 5:
            # print("Ignoring tail: ", most_probable_tail)
            tokens = []
            head = random.choice(possible_starting_heads)
            tokens.append(head)

    pseudo_sentence = " ".join(tokens)
    print(pseudo_sentence)
