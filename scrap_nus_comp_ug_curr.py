import json
import re
from pathlib import Path
from urllib.parse import urlparse
from typing import Any

import requests
from bs4 import BeautifulSoup, Tag

TARGETS = [
    {
        "url": "https://www.comp.nus.edu.sg/programmes/ug/ba/curr/",
        "mode": "summary",
    },
    {
        "url": "https://www.comp.nus.edu.sg/programmes/ug/cs/curr/",
        "mode": "summary",
    },
    {
        "url": "https://www.comp.nus.edu.sg/programmes/ug/isc/curr/",
        "mode": "summary",
    },
    {
        "url": "https://www.comp.nus.edu.sg/programmes/ug/bais/curr/",
        "mode": "summary",
    },
    {
        "url": "https://ceg.nus.edu.sg/curriculum/requirements/",
        "mode": "requirements",
    },
]

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "raw" / "ug_curr"
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


def fetch_soup(url: str) -> BeautifulSoup:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.replace(".", "_")
    path = parsed.path.strip("/")
    path_part = path.replace("/", "_") if path else "root"
    slug = f"{host}_{path_part}"
    slug = re.sub(r"[^a-zA-Z0-9_\\-]", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return f"{slug}.json"


def heading_level(tag: Tag) -> int:
    return int(tag.name[1]) if tag.name and tag.name in HEADINGS else 7


def find_heading(soup: BeautifulSoup, keyword: str) -> Tag | None:
    lowered = keyword.lower()
    for heading in soup.find_all(list(HEADINGS)):
        if lowered in normalize_text(heading.get_text(" ", strip=True)).lower():
            return heading
    return None


def find_summary_accordion(soup: BeautifulSoup) -> tuple[Tag | None, str | None]:
    phrase = "summary of degree requirement"

    # Prefer accordion groups that actually contain the target phrase.
    for accordion_list in soup.select("div.eael-accordion-list"):
        list_text = normalize_text(accordion_list.get_text(" ", strip=True)).lower()
        if phrase not in list_text:
            continue

        for header in accordion_list.select("div.eael-accordion-header"):
            title_node = header.select_one(".eael-accordion-tab-title")
            title_text = normalize_text(
                title_node.get_text(" ", strip=True) if isinstance(title_node, Tag) else header.get_text(" ", strip=True)
            )
            if phrase in title_text.lower():
                return header, title_text

    # Fallback in case markup differs.
    for header in soup.select("div.eael-accordion-header"):
        title_node = header.select_one(".eael-accordion-tab-title")
        title_text = normalize_text(
            title_node.get_text(" ", strip=True) if isinstance(title_node, Tag) else header.get_text(" ", strip=True)
        )
        if phrase in title_text.lower():
            return header, title_text
    return None, None


def collect_accordion_section(header: Tag, soup: BeautifulSoup) -> list[Tag]:
    content_id = (header.get("aria-controls") or "").strip()
    if not content_id:
        return []

    content_node = soup.find(id=content_id)
    if not isinstance(content_node, Tag):
        content_node = header.find_next_sibling(id=content_id)
    if not isinstance(content_node, Tag):
        return []

    # The relevant content is frequently grouped one div above the tab-content node.
    parent = content_node.parent
    if isinstance(parent, Tag) and parent.name == "div":
        return [parent]
    return [content_node]


def collect_section(start_heading: Tag) -> list[Tag]:
    collected: list[Tag] = [start_heading]
    start_level = heading_level(start_heading)
    current = start_heading

    while True:
        current = current.find_next_sibling()
        if current is None:
            break
        if isinstance(current, Tag) and current.name in HEADINGS and heading_level(current) <= start_level:
            break
        if isinstance(current, Tag):
            collected.append(current)
    return collected


def extract_tables(nodes: list[Tag]) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    for node in nodes:
        for table in node.find_all("table"):
            table_rows: list[list[str]] = []
            for row in table.find_all("tr"):
                cells = row.find_all(["th", "td"])
                if not cells:
                    continue
                table_rows.append([normalize_text(cell.get_text(" ", strip=True)) for cell in cells])
            if table_rows:
                tables.append(table_rows)
    return tables


def extract_blocks(nodes: list[Tag]) -> list[str]:
    blocks: list[str] = []
    for node in nodes:
        text = normalize_text(node.get_text(" ", strip=True))
        if text:
            blocks.append(text)
    return blocks


def scrape_summary_page(url: str) -> dict[str, Any]:
    soup = fetch_soup(url)

    accordion_header, accordion_title = find_summary_accordion(soup)
    if accordion_header is not None:
        section_nodes = collect_accordion_section(accordion_header, soup)
        if section_nodes:
            return {
                "url": url,
                "status": "ok",
                "heading": accordion_title,
                "text_blocks": extract_blocks(section_nodes),
                "tables": extract_tables(section_nodes),
            }
        return {
            "url": url,
            "status": "accordion_found_content_missing",
            "heading": accordion_title,
            "text_blocks": [],
            "tables": [],
        }

    heading = find_heading(soup, "Summary of degree requirements")
    if heading is not None:
        section_nodes = collect_section(heading)
        return {
            "url": url,
            "status": "ok",
            "heading": normalize_text(heading.get_text(" ", strip=True)),
            "text_blocks": extract_blocks(section_nodes),
            "tables": extract_tables(section_nodes),
        }

    return {
        "url": url,
        "status": "heading_not_found",
        "heading": None,
        "text_blocks": [],
        "tables": [],
    }


def scrape_requirements_page(url: str) -> dict[str, Any]:
    soup = fetch_soup(url)
    heading = find_heading(soup, "Degree Requirements") or find_heading(soup, "Requirements")

    if heading is not None:
        section_nodes = collect_section(heading)
        return {
            "url": url,
            "status": "ok",
            "heading": normalize_text(heading.get_text(" ", strip=True)),
            "text_blocks": extract_blocks(section_nodes),
            "tables": extract_tables(section_nodes),
        }

    main = soup.find("main") or soup.body
    fallback_text = normalize_text(main.get_text(" ", strip=True)) if isinstance(main, Tag) else ""
    return {
        "url": url,
        "status": "heading_not_found_fallback_used",
        "heading": None,
        "text_blocks": [fallback_text] if fallback_text else [],
        "tables": [],
    }


def scrape_all() -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for target in TARGETS:
        url = target["url"]
        mode = target["mode"]
        try:
            if mode == "summary":
                results.append(scrape_summary_page(url))
            else:
                results.append(scrape_requirements_page(url))
        except requests.RequestException as exc:
            results.append(
                {
                    "url": url,
                    "status": "request_failed",
                    "error": str(exc),
                    "text_blocks": [],
                    "tables": [],
                }
            )

    return results


def main() -> None:
    results = scrape_all()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for result in results:
        url = result.get("url", "")
        output_path = OUTPUT_DIR / url_to_filename(url)
        output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved {url} to {output_path}")


if __name__ == "__main__":
    main()
