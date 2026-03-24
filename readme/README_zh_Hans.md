# Pangolinfo AI SERP Plugin

**作者**: Pangolinfo
**版本**: 0.0.1
**类型**: tool (搜索与智能情报)

---

## 简介 (Introduction)

**Pangolinfo AI SERP** 为您的 Dify 智能体提供**实时合成的搜索情报**。它彻底超越了传统的网页链接抓取，将最前沿的 **AI 综述 (AI Overviews)**、实时搜索引擎结果 (SERP)、全球搜索趋势以及本地地图商家数据完美融合。作为官方插件，它提供**高度纯净、适配大模型**的结构化数据，是构建**零幻觉** AI 搜索引擎（Perplexity 式）、自动化事实核查机器人及本地 SEO 情报工具的首选基石。

🎁 **限时福利：** 注册即领 **80个免费积分**！访问 [Pangolinfo 官网](https://www.pangolinfo.com) 开启您的**零成本** AI 搜索开发之旅。

**核心功能 (Features)**

**AI 聚合回答**: 直接从搜索引擎底层获取高度凝练的实时 AI 摘要。

**丰富 SERP + 引用源**: 同时获取自然搜索结果与 AI 摘要，构建零幻觉、带权威引用的严谨回答。

**本地商家提取**: 深度抓取地图数据（商家名称、评分、地址、坐标），完美适用于本地 SEO 和拓客引流。

**市场趋势分析**: 获取关键词的历史搜索热度，为自动化市场调研提供数据支撑。

**全球化支持**: 底层自动绕过反爬系统，无缝获取不同国家、地区和语言的搜索情报。

**纯净 JSON 输出**: 将复杂的搜索情报转换为高度结构化、适配 LLM 的 JSON 格式。

## 初始设置 (Setup)

### 准备工作

在使用本插件前，您需要准备：

一个 Pangolinfo API Key（需通过 Authentication API 获取以保证长期稳定性）。

明确您需要使用的核心动作（aiMode, aiOverview, map, trends）。

### 配置步骤

**获取 Pangolinfo API Key**:

 - 访问 [Pangolinfo 官网](https://www.pangolinfo.com/zh/)
 - 注册并登录账户
 - 通过 [Authentication API](https://docs.pangolinfo.com/cn-api-reference/authApi/auth?playground=open) 获取长期有效的 API Key

**在 Dify 中配置插件**:

  - 导航至 Dify 的 插件 (Plugins) / 工具 (Tools) 模块
  - 选择 **Pangolinfo AI SERP**
  - 点击 **去授权 (To Authorize)**
  - **API Key**: 填入您的 Pangolinfo API Key
  - 点击 `保存` 以存储配置

### 基础用法 (Usage)

**极速事实核查 (aiMode)**

用于在不读取冗长网页的情况下，提取纯粹的 AI 聚合摘要：

**配置参数:**
  - **Query** (必填): 2026年苹果春季发布会核心内容
  - **gl**: us
  - **hl**: zh-cn

**Perplexity 式搜索 (aiOverview)**

用于同时获取 AI 摘要和传统 SERP 链接（用于参考引用）：

**配置参数:**
  - **Query** (必填): 什么是 AI Agentic Workflow？
  - **gl**: us
  - **hl**: zh-cn

**本地图商家提取 (map)**

用于提取本地商家的结构化数据：

**配置参数:**
  - **Query** (必填): 德克萨斯州奥斯汀市的水管工
  - **gl**: us
  - **hl**: zh-cn

**核心动作解析**

| 动作 (Action) | 描述 |
|--------|-------------|
| `aiMode` | 仅返回由搜索引擎生成的纯 AI 摘要回答。速度极快，极其节省大模型 Token。 |
| `aiOverview` | 同时返回 AI 摘要与传统的自然搜索结果列表（带网页标题、摘要和 URL 链接）。 |
| `map` | 搜索本地商家或地点，提取结构化的地图数据（地址、坐标、评分和评论）。 |
| `trends` | 获取特定关键词在一段时间内的搜索量和热度趋势数据。 |

**输出格式 (Output Format)**

插件将返回结构化的 JSON 数据。以 aiOverview 为例：

```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "ai_overview": "Agentic workflows refer to AI systems where autonomous agents...",
        "organic_results": [
            {
                "title": "What are AI Agents? - DeepLearning.AI",
                "link": "https://www.deeplearning.ai/...",
                "snippet": "An AI agent is a system that can use an LLM to reason through a problem..."
            }
        ]
    }
}
```

## 工作原理 (How It Works)

1. **任务初始化**: 插件将您的搜索词及参数发送至 Pangolinfo API。
2. **反爬处理**: Pangolinfo 将请求路由至住宅代理池，底层静默绕过验证码。
3. **数据获取**: 实时抓取搜索引擎结果、AI 摘要或地图数据。
4. **数据结构化**: 将获取到的网页 HTML 转化为干净的 JSON。
5. **结果返回**: 结构化情报直接返回到您的 Dify LLM 或工作流中。

## 典型用例 (Use Cases)

1. **AI 搜索助手 (Perplexity 式)**

创建零幻觉、带引用的搜索引擎智能体：

```plaintext
动作 (Action): aiOverview
搜索词 (Query): {用户输入}
提示词 (Prompt): 使用提取到的 AI 摘要作为核心回答，并在回答末尾将 organic\_results 里的链接列为“参考来源”。
```

2. **自动化资讯早报**

以极低的 Token 成本获取极速每日资讯：

```plaintext
动作 (Action): aiMode
搜索词 (Query): 科技圈今日头条 提示词 (Prompt): 将提取到的 AI 摘要格式化为一篇 100 字以内的每日早报。
```

3. **本地 SEO 线索挖掘**

从本地商家中收集结构化线索数据：

```plaintext
动作 (Action): map
搜索词 (Query): 纽约的咖啡馆。
提示词 (Prompt): 提取评分大于 4.5 的商家名称及地址，并格式化为 Markdown 表格。
```

4. **市场趋势追踪**

追踪某领域的搜索热度随时间的变化：

```plaintext
动作 (Action): trends
搜索词 (Query): 机械键盘
```

## 最佳实践 (Best Practices)

* **选择正确的动作**: 追求速度和节省 Token 时请使用 aiMode；需要权威网页链接和深度参考时请使用 aiOverview。

* **为地图搜索指定位置**: 使用 map 动作时，请务必在 Query 中包含地域名称（例如搜“西雅图的电工”而不是只搜“电工”）。

* **使用长效 Key**: 请始终使用通过 Auth API 获取的长效 API Key，避免由于 Token 过期导致工作流中断。

* **明确的 Prompt 指令**: 明确告诉 LLM 如何读取返回的 JSON 字段（例如：“请读取并总结 ai_overview 字段的内容...”）。

## 性能注意事项 (Performance Considerations)

* **实时生成延迟**: 请求 aiOverview 时可能比普通搜索稍慢，因为搜索引擎本身需要时间生成 AI 回答。

* **Token 消耗效率**: aiMode 是最高效的动作，因为它彻底免去了大模型阅读和总结十几个网页摘要的开销。

* **速率限制**: 抓取并发与速率由您的 Pangolinfo 账户余额及计划决定。

## 常见问题排查 (Troubleshooting)

**常见错误**

* **"API key is required" (鉴权失败)**:
  * 验证您的 API Key 是否输入正确。
  * 确保您使用的是正式的长期 API Key，而不是临时 Token。

* **地图抓取 (map) 结果为空**:
  * 检查您的查询词是否包含明确的城市或州等地理标识。
  * 核实该地区是否存在此类商家。

* **未返回 AI 摘要 (No AI Overview)**:
  * 某些高度敏感或极其冷门的搜索词可能无法触发搜索引擎的 AI 概览功能。在这种情况下，API 会降级返回标准的自然搜索列表。

* **API 限制 (API Limits)**
  * 可用额度取决于您的 Pangolinfo 账户套餐。
  * 所有新注册账户均可自动获得 **60个免费积分**。这足以支持 **50至60次** 深度抓取任务，助您零成本开启 AI Agent的开发。
  * 请访问 Pangolinfo 网站查看您的[仪表盘](https://tool.pangolinfo.com/)，了解使用统计信息。

## 安全与隐私 (Security & Privacy)

* API Key 和数据传输全程使用安全的 HTTPS 加密协议。
* 您的搜索查询由 Pangolinfo 安全的底层架构处理。
* 请注意不要在公开的 Dify 应用配置中明文暴露您的 API Key。
* 关于隐私处理详情，请参阅 Pangolinfo 官网的隐私政策。

**支持与联系方式 (Support)**

如遇任何问题：

* **插件支持**: Support@pangolinfo.com
* **API 官方文档**: [Pangolinfo Scrape API Documentation](https://docs.pangolinfo.com/en-index)
* **官方网站**: 访问 [Pangolinfo](https://www.pangolinfo.com/zh/)

## 更新与日志 (Updates and Changelog)

**版本 0.0.1** (当前版本)

首次在 Dify 上架。
全面支持 aiMode, aiOverview, Map Data 以及 Trends 功能。
最后更新：2026年3月
