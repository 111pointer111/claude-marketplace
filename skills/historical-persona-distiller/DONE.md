# 历史人物 Persona 蒸馏完成记录

> 本文件是流水线的唯一状态记录。OpenClaw 通过读取此文件确定下一个待蒸馏人物。
> 格式严格遵循「## 一、状态追踪格式」规范。

---

## 一、状态追踪格式

```
## 已完成

| # | 人物 | 朝代 | 完成日期 | confidence | 耗时(分钟) |
|---|------|------|----------|-----------|-----------|
| 1 | 苏轼 | 北宋 | 2026-04-18 | high | 60 |
| 2 | 杜甫 | 唐 | 2026-04-18 | high | 18 |
| 3 | 李白 | 唐 | 2026-04-18 | high | 60 |
| 4 | 辛弃疾 | 南宋 | 2026-04-18 | high | 60 |
```

**字段说明：**
- `#` — 序号，按完成顺序自动递增
- `人物` — 姓名
- `朝代` — 朝代
- `完成日期` — ISO 格式 `YYYY-MM-DD`
- `confidence` — 最终置信度评级 `high` / `medium` / `low`
- `耗时(分钟)` — 本次蒸馏总耗时（分钟）

---

## 二、下一待处理

从 backlog.md 中取 priority 最高且排在最前的人物。

```
### 下一待处理

- **人物：** 陶渊明
- **朝代：** 晋
- **priority：** high
- **预计难度：** 中等（田园诗开山，需区分前期仕途与后期归隐）
- **建议切分数：** 3（早年仕途→辞官归隐→晚年躬耕）
```

---

## 三、执行日志

每次执行后，在此追加一条：

```
### 2026-04-18

**人物：** 苏轼
**执行时间：** 00:07 - 01:07
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** 部分中文古典文献网站（wikisource.org, ctext.org）无法访问，改以百度百科为主要来源
**产出文件：**
  - output/su_shi/SKILL.md
  - output/su_shi/README.md
  - output/su_shi/METADATA.json
  - output/su_shi/CITATIONS.md
  - output/su_shi/raw_stats.json
  - output/su_shi/EVENTS.md
  - output/su_shi/VOICE.md

### 2026-04-18

**人物：** 杜甫
**执行时间：** 02:01 - 02:20
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** 部分中文网站抓取不稳定，改以古诗文网和百度百科为主要来源；wikisource.org 无法访问
**产出文件：**
  - output/du_fu/SKILL.md
  - output/du_fu/README.md
  - output/du_fu/METADATA.json
  - output/du_fu/CITATIONS.md
  - output/du_fu/raw_stats.json
  - output/du_fu/EVENTS.md
  - output/du_fu/VOICE.md

### 2026-04-18

**人物：** 李白
**执行时间：** 04:09 - 05:09
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、shicimingju.com 均无法访问；改以百度百科为唯一可靠来源，抓取了《将进酒》《静夜思》《早发白帝城》等完整诗词原文，以及传记、评价等语料
**产出文件：**
  - output/li_bai/SKILL.md
  - output/li_bai/README.md
  - output/li_bai/METADATA.json
  - output/li_bai/CITATIONS.md
  - output/li_bai/raw_stats.json
  - output/li_bai/EVENTS.md
  - output/li_bai/VOICE.md

### 2026-04-18

**人物：** 辛弃疾
**执行时间：** 05:01 - 06:01
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科为主要来源，抓取了600余首词的代表作50首、传记原文、36条直接引语、22条后世评述
**产出文件：**
  - output/xin_qiji/SKILL.md
  - output/xin_qiji/README.md
  - output/xin_qiji/METADATA.json
  - output/xin_qiji/CITATIONS.md
  - output/xin_qiji/raw_stats.json
  - output/xin_qiji/EVENTS.md
  - output/xin_qiji/VOICE.md
```

---

## 四、统计概览

```
总人物数：     25
已完成：       4
进行中：       0
待处理：       21
完成率：       16%

按 confidence：
  high：       4
  medium：     0
  low：        0

按朝代：
  唐：         2 / 6
  北宋：       1 / 5
  南宋：       1 / 1
  晋：         0 / 1
  战国：       0 / 3
  三国：       0 / 2
  清：         0 / 2
```

---

## 五、 backlog.md 同步规则

每次完成一个人物后：
1. 在「已完成」表格追加一行
2. 在 backlog.md 中将该人物的 `status` 从 `pending` 改为 `done`
3. 更新「统计概览」
4. 更新「下一待处理」
5. 若全部 high priority 完成，自动将下一个 medium priority 提升为「下一待处理」
