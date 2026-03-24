# Pangolinfo AI SERP Plugin

**Author**: Pangolinfo
**Version**: 0.0.1
**Type**: tool (search_and_intelligence)

---

## Introduction

**Pangolinfo AI SERP** empowers your Dify agents with real-time, **synthesized search intelligence**. Beyond traditional link-fetching, it merges cutting-edge **AI Overviews** with organic SERP data, global Search Trends, and Local Map insights. This official plugin delivers **clean, LLM-ready structured data**, making it the ultimate foundation for building **hallucination-free** AI search engines (Perplexity-style), automated fact-checking bots, and local SEO intelligence.

🎁 **Quick Start Bonus:** New users receive **60 complimentary credits** upon registration at [Pangolinfo](https://en.pangolinfo.com/)—start building your first production-grade search agent for **free**!

**Features**

**Direct AI Answers (AI Mode):** Generate highly condensed AI summaries instantly. **Bypass secondary LLM processing** to drastically reduce token consumption and response latency.

**Evidence-Based RAG (AI Overview):** Retrieve rich organic results paired with AI citations. Perfect for building **trustworthy, citation-ready** agents with zero hallucination.

**Local Intelligence (Map Data):** Extract high-fidelity map data (ratings, contact info, and **precise coordinates**) for automated lead generation and local SEO.

**Predictive Market Insights:** Access global search interest and trend data to power data-driven market research and content strategy.

**Enterprise-Grade Resilience:** Seamlessly bypass anti-bot systems across global regions and languages with consistent uptime.

## Setup

### Prerequisites

Before integrating this plugin, ensure you have:

A **Pangolinfo account** with an active balance.

**🎁 60 Free Credits:** New users receive 60 complimentary credits upon registration—perfect for testing your first search-driven AI agents!

A **Production-grade API Key** (obtained via the [Authentication API](https://docs.pangolinfo.com) for long-term stability).

An understanding of your target search actions: **aiMode** (Speed & Cost), **aiOverview** (Citations & RAG), **map** (Local Info), or **trends** (Market Insights).

### Configuration Steps

**Generate your API Key**:

 - Visit the [Pangolinfo Official Portal](https://en.pangolinfo.com/) and sign up.
 - **Claim your Reward**: Your 60 free credits will be automatically added to your dashboard.
  - Generate a **long-term API Key** via the Authentication API.

  > **Note:** To prevent Dify workflow interruptions, avoid using temporary playground tokens. Always use a production-grade long-term key. |

**Configure the Plugin in Dify**:

  - Navigate to the plugins/tools section in Dify
  - Select **Pangolinfo AI SERP**
  - Click **To Authorize**
  - **API Key**: Enter your long-term Pangolinfo API key
  - Click `Save` to store the configuration

### Usage

**High-Speed Fact Checking (aiMode)**

To extract a pure AI-generated summary without the bloat of traditional web pages:

**Parameters:**
  - **Query** (required): Core announcements from Apple Spring Event 2026
  - **gl**: us
  - **hl**: en

**Perplexity-Style Search (aiOverview)**

To retrieve both an AI summary and traditional SERP links for citations: 

**Parameters:**
  - **Query** (required): What is Agentic Workflow in AI?
  - **gl**: us
  - **hl**: en

**Local Business Extraction (map)**

To extract structured data of local businesses: 

**Parameters:**
  - **Query** (required): Plumbers in Austin, Texas
  - **gl**: us
  - **hl**: en

**Understanding Core Actions**

| Action | Description |
|--------|-------------|
| `aiMode` | Returns **only** the pure AI-generated summary. Ultra-fast and highly token-efficient. |
| `aiOverview` | Returns both the AI summary **and** the traditional SERP organic result list (links & snippets). |
| `map` | Searches for local businesses and extracts structured map data (addresses, coordinates, ratings). |
| `trends` | Fetches search volume and interest trend data for a specific keyword over time. |

**Output Format**

The plugin returns structured data for each query. Example for aiOverview:

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

## How It Works

1. **Job Initialization**: The plugin sends your query and parameters to the Pangolinfo API.
2. **Anti-Bot Routing**: Pangolinfo routes the request through residential proxies, bypassing CAPTCHAs.
3. **Data Retrieval**: Search engine results, AI summaries, or map data are fetched in real-time.
4. **Content Structuring**: Raw HTML is formatted and converted into clean JSON.
5. **Result Delivery**: Structured intelligence is returned directly to your Dify LLM or workflow.

## Use Cases

1. **AI Search Assistant (Perplexity-style)**

Create a hallucination-free search agent:

```plaintext
Action: aiOverview
Query: {user_input}
Prompt: Use the AI overview to answer, and list the organic\_results as citations at the bottom.
```

2. **Automated News Briefing**

Extract high-speed daily updates with minimal token cost:

```plaintext
Action: aiMode
Query: Top tech news today Prompt: Format the retrieved AI summary into a 100-word daily briefing.
```

3. **Local SEO Lead Generation**

Gather structured data from local businesses:

```plaintext
Action: map
Query: Coffee shops in New York
Prompt: Extract businesses with a rating > 4.5 and format as a Markdown table.
```

4. **Market Trend Tracking**

Track niche popularity over time:

```plaintext
Action: trends
Query: Mechanical keyboards
```

## Best Practices

* **Choose the Right Action**: Use aiMode for speed and saving tokens; use aiOverview when citations and deep links are required.

* **Specify Locations for Maps**: When using the map action, always include the location in the query (e.g., "Electricians in Seattle" instead of just "Electricians").

* **Use Long-Term Keys**: Always use API keys generated via the Authentication API to prevent workflow disruptions.

* **Prompt Clearly**: Instruct your LLMs on exactly how to parse the returned JSON fields (e.g., "Read the ai\_overview field...").

## Performance Considerations

* **Real-Time Synthesis**: Fetching an aiOverview may take slightly longer than a standard query as the search engine needs time to generate the AI response.

* **Token Efficiency**: aiMode is the most token-efficient action as it completely eliminates the need for the LLM to read through multiple SERP snippets.

* **Rate Limiting**: Monitored via your Pangolinfo account credits.

## Troubleshooting

**Common Issues**

* **"API key is required" or Authentication error**:
  * Verify your API key is correctly entered.
  * Ensure you are using a long-term key, not a temporary playground token.

* **Empty Map Results**:
  * Check if your query contains a geographical identifier (e.g., city or state).
  * Verify that the requested business type exists in that area.

* **No AI Overview Returned**:
  * Some highly sensitive or extremely obscure queries may not trigger the search engine's AI overview feature. In such cases, the API will return standard organic results.

* **API Limits**
  * Available credits are based on your Pangolinfo account plan.
  * All new accounts receive **60 complimentary credits** upon registration. This provides enough power for **50 to 60 deep-level tasks**, allowing you to test your AI Agent for free.
  * Check your [account dashboard](https://tool.pangolinfo.com) on the Pangolinfo website for usage statistics.

## Security Considerations

* API keys are transmitted securely via HTTPS.
* Your specific search queries are processed securely by Pangolinfo's infrastructure.
* Do not expose your API key in public Dify App configurations.

**Privacy**

Please refer to the Privacy Policy on the Pangolinfo website for information on how your data is handled when using this plugin.

**Support**

For issues or questions:

* **Plugin Support**: Support@pangolinfo.com
* **API Documentation**: [Pangolinfo Scrape API Documentation](https://docs.pangolinfo.com/en-index)
* **Official Website**: Visit [Pangolinfo](https://en.pangolinfo.com/)

## Updates and Changelog

**Version 0.0.1** (Current)

Initial release for Dify.
Support for aiMode, aiOverview, Map Data, and Trends.
Last updated: March 2026
