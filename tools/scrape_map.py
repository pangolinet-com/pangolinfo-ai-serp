from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from schemas.map import ScrapeMapRequest
from tools.scrape import Scraper


class ScrapeMapTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        request_dict = ScrapeMapRequest(
            query=tool_parameters.get("query"),
            hl=tool_parameters.get("hl", None),
            ll=tool_parameters.get("ll", None),
            num=tool_parameters.get("num", None),
            start=tool_parameters.get("from", None),
            timeout=tool_parameters.get("timeout", None),
            url=tool_parameters.get("url", None)
        ).model_dump(mode='json', by_alias=True)

        scraper = Scraper(
            api_key=self.runtime.credentials["api_key"]
        )

        result = scraper.scrape(uri="/api/v3/extract/search/maps", **request_dict)
        yield self.create_json_message(result)
