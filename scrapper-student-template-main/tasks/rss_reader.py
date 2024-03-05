# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET

class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    rss_data = []
    root = ET.fromstring(xml)

    # Parse channel data
    channel = root.find("channel")
    rss_data.append(f"Feed: {channel.find('title').text}")
    rss_data.append(f"Link: {channel.find('link').text}")
    last_build_date = channel.find('lastBuildDate')
    if last_build_date is not None:
        rss_data.append(f"Last Build Date: {channel.find('lastBuildDate').text}")
    pub_date = channel.find('pubDate')
    if pub_date is not None:
        rss_data.append(f"Publish Date: {channel.find('pubDate').text}")
    language = channel.find('language')
    if language is not None:
        rss_data.append(f"Language: {channel.find('language').text}")
    category = channel.find('category')
    if category is not None:
            rss_data.append(f"Categories: {', '.join(cat.text for cat in channel.findall('category'))}")
    editor = channel.find('managinEditor')
    if editor is not None:
        rss_data.append(f"Editor: {channel.find('managinEditor').text}")
    rss_data.append(f"Description: {channel.find('description').text}")


    # Parse item data
    items = channel.findall("item")
    if limit is not None:
        items = items[:limit]

    for item in items:
        title = item.find('title')
        if title is not None:
            rss_data.append(f"\nTitle: {item.find('title').text}")
        author = item.find('author')
        if author is not None:
            rss_data.append(f"Author: {author.text}")
        pub_date = item.find('pubDate')
        if pub_date is not None:
            rss_data.append(f"Published: {item.find('pubDate').text}")
        link = item.find('link')
        if link is not None:
            rss_data.append(f"Link: {item.find('link').text}")
        category = item.find('category')
        if category is not None:
            rss_data.append(f"Categories: {', '.join(cat.text for cat in item.findall('category'))}")
        description = item.find('description')
        if description is not None:
            rss_data.append(f"Description: {item.find('description').text}\n")

    if json:
        import json
        channel_data = {
            "title": channel.find("title").text if channel.find
            ("title") is not None else None,
            "link": channel.find("link").text if channel.find
            ("link") is not None else None,
            "lastBuildDate": channel.find("lastBuildDate").text if channel.find("lastBuildDate") is not None else None,
            "pubDate": channel.find("pubDate").text if channel.find
            ("pubDate") is not None else None,
            "language": channel.find("language").text if channel.find
            ("language") is not None else None,
            "category": [cat.text for cat in channel.findall("category")
                         if channel.findall("category")],
            "managinEditor": channel.find("managinEditor").text if channel.find("managinEditor") is not None else None,
            "description": channel.find("description").text if channel.find("description") is not None else None,
            "items": [
                {
                    "title": item.find("title").text if item.find
                    ("title") is not None else None,
                    "author": item.find("author").text if item.find("author") is not None else None,
                    "pubDate": item.find("pubDate").text if item.find
                    ("pubDate") is not None else None,
                    "link": item.find("link").text if item.find
                    ("link") is not None else None,
                    "category": [cat.text for cat in item.findall("category") if item.findall("category")],
                    "description": item.find("description").text if item.find("description") is not None else None,
                }
                for item in items
            ],
        }
        return [json.dumps(channel_data, indent=2)]
    else:
        return rss_data

def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    if args.source is None:
        parser.error("RSS URL is required")

    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
