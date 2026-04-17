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

- **人物：** 李白
- **朝代：** 唐
- **priority：** high
- **预计难度：** 中等（浪漫主义诗人，创作风格豪放飘逸，需区分早中晚期）
- **建议切分数：** 3（蜀中漫游→长安待诏→流放夜郎）
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
```

---

## 四、统计概览

```
总人物数：     25
已完成：       2
进行中：       0
待处理：       23
完成率：       8%

按 confidence：
  high：       2
  medium：     0
  low：        0

按朝代：
  唐：         1 / 6
  北宋：       1 / 5
  南宋：       0 / 1
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
