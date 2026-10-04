import re
def clean_text(html):

    clean = re.sub(r'<[^>]+>', '', html)

    clean = re.sub(r'\s+', ' ', clean)
    
    return clean.strip()