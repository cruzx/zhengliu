#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'SKILL.md'
EXTRA = ROOT / 'extras' / 'codex-self-distill' / 'SKILL.md'
README = ROOT / 'README.md'

FAILURES = []
PASSES = []


def check(condition, ok, fail):
    if condition:
        PASSES.append(ok)
    else:
        FAILURES.append(fail)


skill_text = SKILL.read_text(encoding='utf-8')
readme_text = README.read_text(encoding='utf-8')

check('name: zhengliu' in skill_text, 'frontmatter includes name', 'frontmatter missing skill name')
check('version: 1.1.0' in skill_text, 'frontmatter version updated', 'frontmatter version not updated to 1.1.0')
check('不建议仅用泛词单独触发' in skill_text, 'trigger warning is present', 'missing warning about overly broad trigger words')
check('## 设计师优先模式' in skill_text, 'designer-first mode exists', 'missing designer-first mode section')
check('## 拆分说明：Codex 自我蒸馏已移出主技能' in skill_text, 'self-distill split note exists', 'missing split note for codex-self-distill')
check('## 扩展模式：Codex 本地能力自我蒸馏' not in skill_text, 'legacy self-distill block removed', 'legacy self-distill block still exists in main skill')
check('会员状态分流检查' in skill_text, 'membership routing check exists', 'missing membership routing check section')
check(EXTRA.exists(), 'separate codex-self-distill skill exists', 'missing extras/codex-self-distill/SKILL.md')
check('smoke_test.py' in readme_text, 'README documents smoke test', 'README does not mention smoke_test.py')
check('codex-self-distill' in readme_text, 'README documents split skill', 'README does not mention codex-self-distill')

examples = ['蒸馏XX', '提炼leader判断标准', '提炼设计评审逻辑']
for example in examples:
    check(example in skill_text, f'example trigger preserved: {example}', f'missing key trigger example: {example}')

if FAILURES:
    print('SMOKE TEST: FAIL')
    for item in FAILURES:
        print(f'- {item}')
    if PASSES:
        print('\nPASSING CHECKS:')
        for item in PASSES:
            print(f'- {item}')
    sys.exit(1)

print('SMOKE TEST: PASS')
for item in PASSES:
    print(f'- {item}')
