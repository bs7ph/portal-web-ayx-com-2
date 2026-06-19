import json
import sys


SITE_DATA = {
    "title": "Ayx Portal",
    "url": "https://portal-web-ayx.com",
    "keywords": ["ayx", "portal", "dashboard", "entry"],
    "tags": ["web", "gateway", "management"],
    "description": "Central access hub for Ayx enterprise services and tools."
}


def load_site_data(path=None):
    if path:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                return json.load(fh)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Warning: could not load data from {path}, using defaults.")
    return dict(SITE_DATA)


def create_summary(data):
    lines = []
    lines.append("=" * 56)
    lines.append(f"Site Summary — {data.get('title', 'Unknown')}")
    lines.append("=" * 56)

    lines.append(f"  Title       : {data.get('title', '')}")
    lines.append(f"  URL         : {data.get('url', '')}")
    keywords = data.get("keywords", [])
    if keywords:
        lines.append(f"  Keywords    : {', '.join(keywords)}")
    tags = data.get("tags", [])
    if tags:
        lines.append(f"  Tags        : {', '.join(tags)}")
    desc = data.get("description", "")
    if desc:
        lines.append(f"  Description : {desc}")

    lines.append("=" * 56)
    return "\n".join(lines)


def format_report(data):
    report_parts = []
    report_parts.append(f"<report>")
    report_parts.append(f"  <title>{data.get('title', '')}</title>")
    report_parts.append(f"  <url>{data.get('url', '')}</url>")
    report_parts.append(f"  <keywords>{', '.join(data.get('keywords', []))}</keywords>")
    report_parts.append(f"  <tags>{', '.join(data.get('tags', []))}</tags>")
    report_parts.append(f"  <description>{data.get('description', '')}</description>")
    report_parts.append(f"</report>")
    return "\n".join(report_parts)


def print_structured_output(data):
    print("Structured output:")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    data_source = None
    if len(sys.argv) > 1:
        data_source = sys.argv[1]

    site_data = load_site_data(data_source)

    print()
    print(create_summary(site_data))
    print()
    print(format_report(site_data))
    print()
    print_structured_output(site_data)
    print()


if __name__ == "__main__":
    main()