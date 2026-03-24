from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class ScrapeMapRequest(BaseModel):
    query: Optional[str] = Field(
        ...,
        description="检索关键词"
    )
    hl: Optional[str] = Field(
        None,
        description="界面语言"
    )
    ll: Optional[str] = Field(
        None,
        description="定位参数：纬度,经度,缩放"
    )
    num: Optional[int] = Field(
        None,
        description="每页数量"
    )
    start: Optional[int] = Field(
        None,
        alias="from",
        description="分页起始"
    )
    timeout: Optional[int] = Field(
        None,
        description="任务超时时间"
    )
    url: Optional[HttpUrl] = Field(
        description="指定地址采集，如果传这个参数其他参数无效",
        examples=["https://example.com"]
    )
