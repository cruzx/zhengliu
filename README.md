# zhengliu

`zhengliu` 是一个用于蒸馏人物、主题和本地工作方法的 Skill。

它适合两类任务：

1. 人物 / 主题蒸馏
- 蒸馏某个人的思维方式、判断标准、表达风格
- 生成可复用的 `SKILL.md`
- 支持人物视角、主题框架、更新已有 skill

2. Codex 自我蒸馏
- 审计本地 skills、rules、receipts、handoff、validators
- 提炼重复工作流、失败模式、leader 判断标准
- 生成 patch candidate、validator、worker/subagent candidate

## Repo Structure

```text
.
├── SKILL.md
├── README.md
├── references/
│   ├── extraction-framework.md
│   ├── skill-template.md
│   └── research/
└── scripts/
    ├── download_subtitles.sh
    ├── merge_research.py
    ├── quality_check.py
    └── srt_to_transcript.py
```

## Install

### Codex

把整个仓库目录放进你的 skill 目录，并确保目录名就是 `zhengliu`：

```bash
git clone <your-repo-url> zhengliu
cp -R zhengliu ~/.codex/skills/zhengliu
```

如果你已经在本地 clone 好，也可以直接复制：

```bash
cp -R /path/to/zhengliu ~/.codex/skills/zhengliu
```

### 其他本地 Skill 目录

如果你不是用 Codex，也可以把目录复制到你自己的 skill 根目录中，只要最终结构保持：

```text
<skills-root>/zhengliu/
  ├── SKILL.md
  ├── references/
  └── scripts/
```

## Typical Prompts

### 蒸馏一个人物

```text
用 zhengliu 蒸馏 XXX，重点看他的设计判断和表达方式。
```

### 蒸馏一个主题

```text
用 zhengliu 提炼“设计评审过稿能力”这个主题，做成可复用 skill。
```

### 审计 Codex 自己

```text
用 zhengliu 进入 Codex 自我蒸馏模式，
审计我最近 30 天的 skills、回执、handoff 和产物，
找出 P0 的能力缺口，并生成 patch candidate 和一次验证。
```

## Notes

- `references/research/` 里有一些模板和占位研究文件，它们属于 skill 结构的一部分，不要随意删。
- `scripts/` 主要用于字幕下载、转写清洗、研究汇总和质量检查。
- 这个仓库本身就是 skill 主体，不需要再套一层 `zhengliu/` 子目录。
