"""Retrieve and print words from a URL"""
import sys
from urllib import request


def fetch_words(url):
    """Fetch a list of words from a URL."""
    story=request.urlopen(url)
    story_words=[]
    for line in story:
        line_words=line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items one per line."""
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from at a URL"""
    words=fetch_words(url)
    print_items(words)


if __name__=='__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
