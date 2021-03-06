# pylint:disable-msg=E0611
"""
Listing a series of settings that are applied module-wide.
"""

## This file is available from https://github.com/adbar/trafilatura
## under GNU GPL v3 license

from multiprocessing import cpu_count

from lxml.html.clean import Cleaner



USER_AGENT = 'trafilatura/0.5.2 (+https://github.com/adbar/trafilatura)'

# sanity checks
MAX_FILE_SIZE = 20000000
MIN_FILE_SIZE = 10
SLEEP_TIME = 2
DOWNLOAD_THREADS = 5


# extraction config
MIN_EXTRACTED_SIZE = 200
MIN_EXTRACTED_COMM_SIZE = 10
MIN_DUPLCHECK_SIZE = 100
MIN_OUTPUT_SIZE = 25
MIN_OUTPUT_COMM_SIZE = 10
MAX_OUTPUT_TREE_LENGTH = 500


# file output
MAX_FILES_PER_DIRECTORY = 1000
FILENAME_LEN = 8
FILE_PROCESSING_CORES = min(cpu_count(), 16)  # 16 processes at most
PROCESSING_TIMEOUT = 30


# deduplication
LRU_SIZE = 65536
MAX_REPETITIONS = 2


# filters
CUT_EMPTY_ELEMS = {'article', 'b', 'blockquote', 'dd', 'div', 'dt', 'em',
                   'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'i', 'li', 'main',
                   'p', 'pre', 'q', 'section', 'span', 'strong'}
                   # 'meta', 'td', 'a'

MANUALLY_CLEANED = ['audio', 'aside', 'canvas', 'figure', 'footer', 'form', 'head', 'map',
                    'object', 'picture', 'script', 'svg', 'video',
                    # secondary
                    'applet', 'area', 'blink', 'button', 'datalist', 'details', 'dialog', 'embed',
                    'fieldset', 'iframe', 'link', 'input', 'label', 'legend',
                    'marquee', 'math', 'menu', 'menuitem', 'nav', 'noscript', 'option',
                    'rp', 'rt', 'rtc', 'select', 'source', 'style', 'track', 'textarea', 'time', 'use']
                    # 'frame', 'frameset', 'meta', 'hr', 'ins'

MANUALLY_STRIPPED = ['abbr', 'acronym', 'address', 'bdi', 'bdo', 'big', 'cite', 'data', 'font', 'hgroup', 'img', 'ins', 'mark', 'meta', 'ruby', 'small']

# HTML_CLEANER config # http://lxml.de/api/lxml.html.clean.Cleaner-class.html
HTML_CLEANER = Cleaner()
HTML_CLEANER.annoying_tags = False # True
HTML_CLEANER.comments = True
HTML_CLEANER.embedded = False # True
HTML_CLEANER.forms = False # True
HTML_CLEANER.frames = False # True
HTML_CLEANER.javascript = False # True
HTML_CLEANER.links = False
HTML_CLEANER.meta = False
HTML_CLEANER.page_structure = False
HTML_CLEANER.processing_instructions = True
HTML_CLEANER.remove_unknown_tags = False
HTML_CLEANER.safe_attrs_only = False
HTML_CLEANER.scripts = False # True
HTML_CLEANER.style = False
HTML_CLEANER.remove_tags = MANUALLY_STRIPPED
# 'a', 'span', 'dd', 'sub', 'sup', 'center',
HTML_CLEANER.kill_tags = MANUALLY_CLEANED


TAG_CATALOG = frozenset(['blockquote', 'code', 'del', 'fw', 'head', 'hi', 'lb', 'list', 'p', 'pre', 'q', 'quote'])
# 'span', 'item'

# JUSTEXT_DEFAULT = 'German'
# JT_STOPLIST = None  # could be a list

JUSTEXT_LANGUAGES = {
    'ar': 'Arabic',
    'bg': 'Bulgarian',
    'cz': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'en': 'English',
    'el': 'Greek',
    'es': 'Spanish',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    # 'ja': '',
    'ko': 'Korean',
    'id': 'Indonesian',
    'it': 'Italian',
    'no': 'Norwegian_Nynorsk',
    'nl': 'Dutch',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'sr': 'Serbian',
    'sv': 'Swedish',
    'tr': 'Turkish',
    'uk': 'Ukranian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    # 'zh': '',
}
