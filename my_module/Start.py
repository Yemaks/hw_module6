
"""
Contains functionality for selecting most relevant vines and for summarization users description.
"""

from normalize_text import normalize
from text_cleanup import cleanup
from generate_summary import summary
from search_by_description import top_search_by_description

print("1: Obtaining a summarization from the description of wine\n2: Obtaining the top-5 wines that best match the description")
choice = input("Select work option: ")
while(True):
    if choice == '1':
        text = input("Enter text to summarize: ")
        print("\nOriginal Text:\n")
        print(text)
        print('\nSummarized text:\n')
        print(summary(cleanup(normalize(text))[0], normalize(text)))
        break
    elif choice == '2':
        text = input("Enter text to summarize: ")
        top_search_by_description(summary(cleanup(normalize(text))[0], normalize(text)))
        break
    else:
        choice = input("Invalid input format. Select one of the options below: ")
