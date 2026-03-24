from pydantic import BaseModel, Field, HttpUrl
from enum import Enum
from typing import Optional


class OutputFormat(str, Enum):
    JSON = "json"
    HTML = "html"
    MARKDOWN = "markdown"


class ParserName(str, Enum):
    GOOGLE_SEARCH = "googleSearch"
    GOOGLE_AI_SEARCH = "googleAISearch"


class ScrapeRequest(BaseModel):
    url: HttpUrl = Field(
        ...,
        description="目标网页的完整URL",
        examples=["https://example.com"]
    )
    format: OutputFormat = Field(
        ...,
        description="数据输出格式, 可选项: json, html, markdown"
    )
    parser_name: ParserName = Field(
        ...,
        alias="parserName",
        description="HTML解析器名称"
    )
    screenshot: Optional[bool] = Field(
        default=False,
        description="是否截图"
    )
    param: Optional[list[str]] = Field(
        None,
        description="多轮对话参数"
    )
