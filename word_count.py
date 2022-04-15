import string


punctuations = str(string.punctuation) + "1234567890"


def format_text(file_name):
    with open(file_name) as f:
        content = f.read()
        content = content.lower()
        for word in content:
            if word in punctuations:
                content = content.replace(word, " ")
        content = content.split()
        return content


def word_count_generator(content):
    count = {}
    for word in content:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count


def find_statistics(count):
    vocabulary_count = len(count)
    word_count = sum(count.values())
    print("Word Frequency List")
    for key, value in count.items():
        print(key + ":", value)
    print("\n" + "Vocabulary count:", vocabulary_count)
    print("Number of words:", word_count, "\n")


def find_most_used_words(count, number_of_top_words=10):
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print("Top", number_of_top_words, "most used words")
    for i in range(0, number_of_top_words):
        print(sorted_count[i][0] + ":", sorted_count[i][1])


find_statistics(word_count_generator(format_text("hello.txt")))
find_most_used_words(word_count_generator(format_text("hello.txt")))
