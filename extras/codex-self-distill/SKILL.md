---
name: codex-self-distill
description: '审计 Codex 本地能力、skills、workers、validators、receipts 与失败模式，生成 patch candidate、validator candidate 和安装建议。只用于本地能力自我蒸馏，不用于人物或设计评审蒸馏。'
description_zh: 审计 Codex 本地能力并输出候选升级方案
description_en: Audit Codex local capabilities and generate upgrade candidates
version: 1.0.0
---

# codex-self-distill

这是从 `zhengliu` 主 skill 里拆出来的独立 skill。

## 什么时候用

当你的目标是这些事情时，应该用它：

- 审计 Codex 最近都在干什么
- 看哪些 skill 装了但没触发
- 审计 worker / subagent 有没有真的落地
- 生成 validator / patch / installation plan
- 复盘失败案例并沉淀到规则里

## 什么时候不要用

下面这些不属于它，而属于 `zhengliu`：

- 蒸馏某个人物
- 提炼 leader 判断标准
- 提炼设计评审逻辑
- 判断一版稿该怎么改更容易过稿

## 默认产出

- `skill patch candidates`
- `validator candidates`
- `worker/subagent candidates`
- `installation plan and rollback`
- `P0/P1 问题清单`

## 最小工作流

1. 先审计，后生成 candidate
2. 所有判断尽量绑定证据路径
3. 不直接覆盖正式 skill 或正式规则
4. 至少做一次真实或半真实验证
5. 最终明确哪些需要人工确认安装
