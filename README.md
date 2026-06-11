# zhengliu

`zhengliu` 是一个偏设计师工作流的人类蒸馏 Skill。

它专门做三件事：

1. 蒸馏人物
2. 蒸馏 leader 判断标准
3. 蒸馏设计评审逻辑和过稿风格

它现在不再承担 `Codex 自我蒸馏 / skill 审计 / worker 机制审计` 这类元能力任务，那部分已经拆成独立 skill，避免主 skill 过大、过泛、容易误触发。

## 这个 skill 适合干嘛

你可以把它理解成一个“设计判断提炼器”。

它适合这几类输入：

- 帮我蒸馏某个设计师/leader
- 帮我提炼某个 leader 的过稿标准
- 帮我提炼某类业务设计为什么总不过
- 帮我从评审记录里提炼稳定判断框架
- 帮我判断这个问题现在该回图、回标注、回方案，还是回未来判断

## 最适合谁

- 设计师
- 交互设计师
- 视觉设计师
- 商业化设计师
- 经常要过稿、评审、汇报的人

## 最常见的 5 种用法

### 1. 提炼 leader 的过稿标准

```text
用 zhengliu 提炼我 leader 的过稿标准，重点看他对商业化设计的判断逻辑。
```

### 2. 提炼某类设计工作的收稿逻辑

```text
用 zhengliu 提炼“概念版首页怎么更容易过稿”这套逻辑，做成一个可复用 skill。
```

### 3. 蒸馏一个设计师

```text
用 zhengliu 蒸馏 XXX，重点看他的设计判断、表达方式和过稿能力。
```

### 4. 判断该回什么交付

```text
我给你一个设计问题，你用 zhengliu 帮我判断现在该回图、回标注、回文案，还是回一个未来判断。
```

### 5. 拆会员状态与跳转链路

```text
用 zhengliu 帮我评这个会员权益需求，先拆非会员、会员无券、有券三类用户，再判断交互链路有没有问题。
```

## 它默认会帮你判断什么

这个 skill 不只会“总结”，还会先做设计分流：

- 这是一个要回图的问题，还是要回判断的问题
- 这是一个入口问题，还是一个资格分流问题
- 这是一个视觉问题，还是一个业务判断问题
- 这次最有价值的交付是图、标注、方案，还是未来判断

如果涉及会员、权益、券包、下载、购买弹窗，它还会默认检查：

- `非会员` 应不应该先拦截去卖会员
- `会员，但没券` 应不应该直接卖缺失能力
- `有券` 是否应该直接完成任务而不被多余打断

## Repo Structure

```text
.
├── SKILL.md
├── README.md
├── extras/
│   └── codex-self-distill/
│       └── SKILL.md
├── references/
│   ├── extraction-framework.md
│   ├── skill-template.md
│   └── research/
└── scripts/
    ├── download_subtitles.sh
    ├── merge_research.py
    ├── quality_check.py
    ├── smoke_test.py
    └── srt_to_transcript.py
```

说明：

- `SKILL.md`：主 skill，只负责人物 / leader / 设计评审蒸馏
- `extras/codex-self-distill/SKILL.md`：拆出去的 Codex 自我蒸馏 skill
- `scripts/smoke_test.py`：检查主 skill 的 frontmatter、触发词、关键 section 和示例路由

## Install

### 安装主 skill

把整个仓库目录放进你的 skill 目录，并确保目录名就是 `zhengliu`：

```bash
git clone <your-repo-url> zhengliu
cp -R zhengliu ~/.codex/skills/zhengliu
```

### 可选：安装独立的自我蒸馏 skill

如果你还需要审计 Codex 本地能力、skill 体系、worker/validator 落地情况，再额外复制：

```bash
cp -R zhengliu/extras/codex-self-distill ~/.codex/skills/codex-self-distill
```

## 推荐提问方式

```text
帮我蒸馏这个设计师的判断方式和表达风格
```

```text
帮我提炼我 leader 的过稿标准
```

```text
帮我把这批设计评审记录蒸馏成一个可复用 skill
```

```text
帮我判断这个问题现在该回图、回标注，还是回一个未来判断
```

## Notes

- `zhengliu` 现在是收窄后的主 skill，不再承担所有“元 skill”任务。
- 如果你要的是 Codex 自我审计、skill 审计、validator/worker 升级，请使用独立的 `codex-self-distill`。
- `references/research/` 里的文件仍然属于主 skill 结构的一部分，不建议随意删除。
