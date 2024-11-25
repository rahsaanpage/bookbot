def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Convert text to lowercase
    text = text.lower()
    
    char_count = {}
    
    for char in text:
        if char.isalnum() or char in [' ', '.', ',', '!', '?']:  # Adjust this filter as needed
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count 

def print_report(aggregate):
    """
    Prints a report of character counts from the given aggregate dictionary.

    :param aggregate: A dictionary with characters as keys and counts as values.
    """
    if not isinstance(aggregate, dict):
        raise ValueError("Input must be a dictionary with character counts.")

    print("--- Begin report ---")
    
    # Sort the dictionary by count in descending order
    sorted_aggregate = sorted(aggregate.items(), key=lambda x: x[1], reverse=True)
    
    # Iterate through the sorted items
    for char, count in sorted_aggregate:
        if char.isalpha():  # Include only alphabetic characters
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")
  

def main():
    book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    print(text)

    print(get_num_words(text))
    print(count_characters(text))   

    print(f"--- Begin report of {book_path} ---") 
    print(f"{get_num_words(text)} words found in the document")
    print_report(text)

if __name__ == "__main__":
    main()
