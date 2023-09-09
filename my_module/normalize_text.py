
import re

def normalize(text):
    """Normalizes text.

    Remove all .*?<[^>]+>© and newline symbol from text.

    Args:
        text: text in str format.

    Returns:
        text in str format without .*?<[^>]+>© and newline symbol.
    
    Example usage:
        test_text = normalize(text='Hello world!?')
    """
    tm1 = re.sub('<pre>.*?</pre>', '', text, flags=re.DOTALL)
    tm2 = re.sub('<[^>]+>©', '', tm1, flags=re.DOTALL)
    return tm2.replace("\n", "")
