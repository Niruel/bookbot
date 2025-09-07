from stats import get_num_words
from stats import get_num_of_characters
from stats import sort_characters
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

    
def print_report(book_path, num_of_words, chars_sorted_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_of_words} total words")  
  print("--------- Character Count -------")
  for item in chars_sorted_list:
    if not item["char"].isalpha():
            continue
    print(f"{item['char']}: {item['num']}")

  print("============= END ===============")


def main():
  if len(sys.argv) !=  2:
    print("Usage: python3 main.py <path_to_book>")
    return sys.exit(1)

  book_path = sys.argv[1]
  file_txt = get_book_text(book_path)
  num_of_words = get_num_words(file_txt) 
  test_dict = get_num_of_characters(file_txt)
  char_list_sorted = sort_characters(test_dict)
  print_report(book_path, num_of_words, char_list_sorted)
  #print(test_dict)
main()
