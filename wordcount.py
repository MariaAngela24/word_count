# put your code here.
def word_counter(txt_file):
    """Prints a count of how many times a word appears in a text file."""

    open_file = open(txt_file)

    collection_of_words = {}

    for line in open_file:
        line_clean = line.rstrip()
        words = line_clean.split(" ")
        #print line_split

        for word in words:
            current_word_count = collection_of_words.get(word, 0)
            collection_of_words[word] = current_word_count + 1

    for key, value in collection_of_words.items():
        print key, value

    open_file.close()
    #print lst_of_words

word_counter('test.txt')