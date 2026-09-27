import re

class Solution():
    def wordNGrams(self, string, n):
        # convert the string to all lowercases
        string = string.lower()

        # replace all non-alphaneumeric characters
        string = re.sub(r'[^a-zA-Z0-9\s]', ' ', string)

        ngrams = {}
        m = len(string)
        for i in range(m):
            if i+n > m:
                break
            token = string[i:i+n]
            if token not in ngrams.keys():
                ngrams[token] = 1
            else:
                ngrams[token] += 1
        return ngrams

    def sentenceNGrams(self, sentence, n):
        # convert the string to all lowercases
        sentence = sentence.lower()

        # replace all non-alphaneumeric characters
        sentence = re.sub(r'[^a-zA-Z0-9\s]', ' ', sentence)

        # replace \n with " "
        sentence = sentence.replace("\n", " ")

        # break sentence into tokens, remove empty spaces
        tokens = [token for token in sentence.split(" ") if token != ""]

        # use zip function to help us generate n-grams
        ngrams = zip(*[tokens[i:] for i in range(n)])

        # concatenate the tokens into ngrams and return
        return [" ".join(ngram) for ngram in ngrams]


# strings = "banana"
# N = 2
# q = Solution()
# print(q.wordNGrams(strings, N))

sentence = """
            Natural-language processing (NLP) is an area of 
            computer science and artificial intelligence 
            concerned with the interactions between computers 
            and human (natural) languages."""
N = 5
q = Solution()
print(q.sentenceNGrams(sentence, N))