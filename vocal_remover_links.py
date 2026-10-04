"""NeuralSound tool pages.

A small reference list of the main NeuralSound tool pages, kept as plain data.
Run this file to print each tool name with its URL.
"""

NEURALSOUND_TOOLS = {
    "Vocal remover": "https://neuralsound.org/vocal-remover",
    "Background music remover": "https://neuralsound.org/background-music-remover",
    "Instrumental remover": "https://neuralsound.org/instrumental-remover",
}


def print_tools(tools=NEURALSOUND_TOOLS):
    """Print each tool name and its page URL, one per line."""
    width = max(len(name) for name in tools)
    for name, url in tools.items():
        print(f"{name:<{width}}  {url}")


if __name__ == "__main__":
    print_tools()
