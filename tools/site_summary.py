import json

# 内置站点资料
SITE_DATA = {
    "name": "华体会官网",
    "url": "https://global-cn-huatihui.com",
    "keywords": ["华体会", "体育", "娱乐", "在线平台"],
    "tags": ["体育", "娱乐", "华体会", "综合"],
    "description": "华体会是一个综合性在线娱乐平台，提供丰富的体育赛事和娱乐项目。"
}

ADDITIONAL_SITES = [
    {
        "name": "华体会体育",
        "url": "https://global-cn-huatihui.com/sports",
        "keywords": ["华体会体育", "赛事", "投注"],
        "tags": ["体育", "华体会"],
        "description": "华体会体育板块，覆盖多种体育赛事投注和实时比分。"
    },
    {
        "name": "华体会娱乐",
        "url": "https://global-cn-huatihui.com/casino",
        "keywords": ["华体会娱乐", "游戏", "老虎机"],
        "tags": ["娱乐", "华体会"],
        "description": "华体会娱乐板块，提供丰富的在线游戏和老虎机体验。"
    }
]

def format_site_summary(site: dict) -> str:
    """将单个站点资料格式化为结构化摘要字符串"""
    lines = [
        "===== 站点摘要 =====",
        f"名称: {site['name']}",
        f"URL: {site['url']}",
        f"关键词: {', '.join(site['keywords'])}",
        f"标签: {', '.join(site['tags'])}",
        f"说明: {site['description']}",
        "===================="
    ]
    return "\n".join(lines)

def generate_all_summaries(sites: list) -> str:
    """生成所有站点资料的摘要"""
    result_parts = []
    for site in sites:
        result_parts.append(format_site_summary(site))
    return "\n\n".join(result_parts)

def main():
    """主函数：读取内置站点资料并输出结构化摘要"""
    all_sites = [SITE_DATA] + ADDITIONAL_SITES
    summary = generate_all_summaries(all_sites)
    print(summary)

if __name__ == "__main__":
    main()