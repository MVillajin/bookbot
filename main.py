#Main path to print out later
def main():
    find_path = "books/frankenstein.txt"
    text = get_book_text(find_path)
    num = get_num_words(text)
    counter= get_count_letters(text)
    sorted_list_char = sorted_list_of_chars(counter)

    print(f" --- Begin report of {find_path} --- ")
    print(f"{num} words found in the document")
    print()

    for item in sorted_list_char:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

# Get total number of words -> split words then return length
def get_num_words(text):
    words = text.split()
    return len(words)


#sort them
def sort_on(dict):
     return dict["num"]

def sorted_list_of_chars(num_chars_dict):
    sorted_value = []
    for ch in num_chars_dict:
        sorted_value.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_value.sort(reverse=True, key=sort_on)
    return sorted_value
     
# Count each letter and put them in a dictionairy -> lower their characters with.lower
def get_count_letters(count):
        count_list = {}
        for char in count:
            lowered = char.lower()
            if lowered in count_list:
                count_list[lowered] +=1
            else:
                count_list[lowered] = 1

        return count_list

#Textpath
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
                
 



#Recall function
main()

