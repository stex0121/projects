import sys
import webbrowser
import urllib.parse
import platform

# Path to the Microsoft Edge executable
EDGE_PATH = {
    'Windows': 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'Darwin': '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',  # macOS
    'Linux': 'microsoft-edge'  # Usually just 'microsoft-edge' if it's in your PATH
}

# Determine the current operating system
OS = platform.system()

def register_edge():
    """Register Microsoft Edge with the webbrowser module."""
    if OS == 'Windows':
        path = EDGE_PATH['Windows']
    elif OS == 'Darwin':  # macOS
        path = EDGE_PATH['Darwin']
    elif OS == 'Linux':
        path = EDGE_PATH['Linux']
    else:
        raise EnvironmentError(f"Unsupported OS: {OS}")

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(path))

# List of predefined sites
PREDEFINED_SITES = {
    'reddit': 'https://www.reddit.com/search/?q=',
    'google': 'https://www.google.com/search?q=',
    'github': 'https://github.com/search?q=',
    'youtube':'https://www.youtube.com/results?search_query='
}

def open_search(query, sites):
    """Open the search query in the given sites."""
    encoded_query = urllib.parse.quote_plus(query)
    
    register_edge()
    
    for site in sites:
        if site in PREDEFINED_SITES:
            url = PREDEFINED_SITES[site] + encoded_query
            print(f"Opening {site} with query '{query}'...")
            webbrowser.get('edge').open_new_tab(url)
        else:
            print(f"Site '{site}' not recognized. Skipping...")

def main():
    if len(sys.argv) < 2:
        print("Usage: python search_open.py <query>")
        print("Example: python search.py 'Python programming'")
        sys.exit(1)
    
    query = sys.argv[1]
    # Default sites to search
    default_sites = ['google', 'reddit', 'geeksforgeeks', 'w3schools', 'github','youtube']
    
    open_search(query, default_sites)

if __name__ == "__main__":
    main()

    #Use command in cmd bash  "cd" and target where is "search" script 
    # Then enter  python search.py 'Python programming'
    #change predefined sites 
    #change web browser 
    #Simple Automatisation 