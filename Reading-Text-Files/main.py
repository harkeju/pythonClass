# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    
    with open('./story.txt', 'r') as f:
        file_content = f.read()
        return file_content

output = read_file_content('story.txt')
print(output)


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text_list = text.split(" ")
    # counts = dict()
    

    for i in text_list:
        dictionary = {i: text_list.count(i)}
        print(dictionary)


count_words()

    #return {"as": 10, "would": 20}