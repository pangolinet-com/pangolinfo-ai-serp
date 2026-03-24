from pydantic import BaseModel, Field


class ScrapeTrendsRequest(BaseModel):
    timeRange: str = Field(
        ...,
        description="时间范围"
    )
    region: str = Field(
        ...,
        description="地区代码"
    )
    keywords: list[str] = Field(
        ...,
        description="搜索关键词列表"
    )
    language: str = Field(
        ...,
        description="语言"
    )
