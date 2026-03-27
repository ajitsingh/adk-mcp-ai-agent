import os
import json
import re
import traceback
from toolbox_core import ToolboxSyncClient

MCP_TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL", "http://127.0.0.1:5000")


def strip_html(text: str) -> str:
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("&quot;", '"')
    text = text.replace("&#39;", "'")
    return text.strip()


def ask_agent(user_query: str) -> dict:
    try:
        toolbox = ToolboxSyncClient(MCP_TOOLBOX_URL)

        tool_name = "search_release_notes_bq"
        tool = toolbox.load_tool(tool_name)

        tool_result = tool()

        rows = tool_result

        if isinstance(tool_result, dict) and "content" in tool_result:
            rows = tool_result["content"]

        if isinstance(rows, str):
            try:
                rows = json.loads(rows)
            except Exception:
                rows = []

        summary_lines = []

        if isinstance(rows, list):
            for row in rows[:5]:
                if isinstance(row, dict):
                    product = row.get("product_name", "Unknown product")
                    description = row.get("description", "No description")
                    published_at = row.get("published_at", "Unknown date")

                    clean_description = strip_html(str(description))
                    clean_description = clean_description.replace("\n", " ").replace(
                        "\r", " "
                    )
                    if len(clean_description) > 180:
                        clean_description = clean_description[:180] + "..."

                    summary_lines.append(
                        f"- {product} | {published_at}\n  {clean_description}"
                    )

        final_answer = (
            "Based on MCP-retrieved structured data from BigQuery, here are the latest relevant Google Cloud release notes:\n\n"
            + (
                "\n\n".join(summary_lines)
                if summary_lines
                else "No release notes found."
            )
        )

        return {
            "query": user_query,
            "tool_used": tool_name,
            "grounded_answer": final_answer,
            "rows_found": len(rows) if isinstance(rows, list) else 0,
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "query": user_query,
            "error": str(e),
            "error_type": type(e).__name__,
            "mcp_toolbox_url": MCP_TOOLBOX_URL,
        }
