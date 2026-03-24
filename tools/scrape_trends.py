from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from schemas.trends import ScrapeTrendsRequest
from tools.scrape import Scraper


class ScrapeTrendsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        request_dict = ScrapeTrendsRequest(
            timeRange=tool_parameters.get("timeRange"),
            region=tool_parameters.get("region"),
            keywords=tool_parameters.get("keywords"),
            language=tool_parameters.get("language")
        ).model_dump(mode='json', by_alias=True)

        scraper = Scraper(
            api_key=self.runtime.credentials["api_key"]
        )

        result = scraper.scrape(uri="/api/v2/google/trends", **request_dict)
        yield self.create_json_message(result)
