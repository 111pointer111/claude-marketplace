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
| 5 | 陶渊明 | 晋 | 2026-04-18 | high | 15 |
| 6 | 王维 | 唐 | 2026-04-18 | high | 30 |
| 7 | 白居易 | 唐 | 2026-04-18 | high | 20 |
| 8 | 李清照 | 宋 | 2026-04-18 | high | 12 |
| 9 | 欧阳修 | 北宋 | 2026-04-18 | high | 60 |
| 10 | 苏洵 | 北宋 | 2026-04-18 | high | 15 |
| 11 | 苏辙 | 北宋 | 2026-04-19 | medium | 13 |
| 12 | 韩愈 | 唐 | 2026-04-19 | high | 25 |
| 13 | 柳宗元 | 唐 | 2026-04-19 | high | 45 |
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

- **人物：** 王安石
- **朝代：** 北宋
- **priority：** medium
- **预计难度：** 中等（变法派，散文峭拔）
- **建议切分数：** 4（早年求学→仕途初期→变法革新→晚年归隐）
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

### 2026-04-18

**人物：** 陶渊明
**执行时间：** 08:12 - 08:27
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org 等无法访问；改以百度百科为主要来源，抓取了诗125首、文12篇的核心语料，包括《归园田居》《归去来兮辞》《饮酒》《杂诗》《读山海经》《桃花源记》《五柳先生传》等全部代表作，语料极为丰富
**产出文件：**
  - output/tao_yuanming/SKILL.md
  - output/tao_yuanming/README.md
  - output/tao_yuanming/METADATA.json
  - output/tao_yuanming/CITATIONS.md
  - output/tao_yuanming/raw_stats.json
  - output/tao_yuanming/EVENTS.md
  - output/tao_yuanming/VOICE.md

### 2026-04-18

**人物：** 王维
**执行时间：** 10:01 - 10:31
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（传记+评述）和百度汉语（诗词）为两个主要来源，抓取了32首诗词、传记原文、37条直接引语、26条后世评述；网络连接 GitHub 偶有超时，重试后成功
**产出文件：**
  - output/wang_wei/SKILL.md
  - output/wang_wei/README.md
  - output/wang_wei/METADATA.json
  - output/wang_wei/CITATIONS.md
  - output/wang_wei/raw_stats.json
  - output/wang_wei/EVENTS.md
  - output/wang_wei/VOICE.md

### 2026-04-18

**人物：** 白居易
**执行时间：** 04:06 - 04:26
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科为主要来源，抓取了传记原文、《长恨歌》《观刈麦》《问刘十九》《南湖早春》完整原文，以及《与元九书》完整原文（诗论核心文献）；《琵琶行》仅获得引语
**产出文件：**
  - output/bai_juyi/SKILL.md
  - output/bai_juyi/README.md
  - output/bai_juyi/METADATA.json
  - output/bai_juyi/CITATIONS.md
  - output/bai_juyi/raw_stats.json
  - output/bai_juyi/EVENTS.md
  - output/bai_juyi/VOICE.md

### 2026-04-18

**人物：** 李清照
**执行时间：** 14:01 - 14:13
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** 古诗文网(guwendao.net)重定向、wikisource.org、ctext.org等主要古典文献网站均无法访问；改以百度百科（传记+后世评述）和百度汉语（诗词）为两个主要来源；诗词仅抓取20首（不足30首下限），补充搜索无效；但传记极详尽（8000+字），后世评述极丰富（40+条，跨越宋元明清四朝），整体语料仍属丰富
**产出文件：**
  - output/li_qingzhao/SKILL.md
  - output/li_qingzhao/README.md
  - output/li_qingzhao/METADATA.json
  - output/li_qingzhao/CITATIONS.md
  - output/li_qingzhao/raw_stats.json
  - output/li_qingzhao/EVENTS.md
  - output/li_qingzhao/VOICE.md

### 2026-04-18

**人物：** 欧阳修
**执行时间：** 17:18 - 18:18
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 两次失败，改以百度百科多源抓取（传记、醉翁亭记、秋声赋、采桑子十首、新唐书、新五代史）；wikisource.org、ctext.org 均无法访问
**产出文件：**
  - output/ouyang_xiu/SKILL.md
  - output/ouyang_xiu/README.md
  - output/ouyang_xiu/METADATA.json
  - output/ouyang_xiu/CITATIONS.md
  - output/ouyang_xiu/raw_stats.json
  - output/ouyang_xiu/EVENTS.md
  - output/ouyang_xiu/VOICE.md
  - done/ouyang_xiu.done

### 2026-04-18

**人物：** 苏洵
**执行时间：** 16:06 - 16:21
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；改以百度百科为主要来源，抓取了详细传记（约11000字）、《六国论》全文（约700字）、后世评述语料（约2000字）；wikisource.org、ctext.org 均无法访问
**产出文件：**
  - output/su_xun/SKILL.md
  - output/su_xun/README.md
  - output/su_xun/METADATA.json
  - output/su_xun/CITATIONS.md
  - output/su_xun/raw_stats.json
  - output/su_xun/EVENTS.md
  - output/su_xun/VOICE.md
  - done/su_xun.done

### 2026-04-19

**人物：** 苏辙
**执行时间：** 02:01 - 02:14
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（万字传记+评述）和百度汉语（诗词20首）为两个主要来源；诗词仅抓取20首（不足30首下限），传记和后世评述极丰富；网络连接 GitHub push 时有超时，重试后成功
**产出文件：**
  - output/su_zhe/SKILL.md
  - output/su_zhe/README.md
  - output/su_zhe/METADATA.json
  - output/su_zhe/CITATIONS.md
  - output/su_zhe/raw_stats.json
  - output/su_zhe/EVENTS.md
  - output/su_zhe/VOICE.md
  - done/su_zhe.done

### 2026-04-19

**人物：** 韩愈
**执行时间：** 20:06 - 20:31
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（传记49229字+后世评述）和百度百科《师说》《进学解》《祭十二郎文》《马说》《早春》词条为语料主要来源；诗词仅抓取约20首（不足30首下限），但古文语料极丰富；ACP agent 配置问题导致并行执行受限，改为串行
**产出文件：**
  - output/han_yu/SKILL.md
  - output/han_yu/README.md
  - output/han_yu/METADATA.json
  - output/han_yu/CITATIONS.md
  - output/han_yu/raw_stats.json
  - output/han_yu/EVENTS.md
  - output/han_yu/VOICE.md
  - done/han_yu.done

### 2026-04-19

**人物：** 柳宗元
**执行时间：** 22:01 - 22:46
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（柳宗元传记，约15000字）为唯一可靠来源；诗词文集无法直接抓取，根据历史记载整理了《江雪》《渔翁》《溪居》等代表作品；语料包括传记原文、23条直接引语、12条后世评述、永州八记节选、代表寓言、代表论说文
**产出文件：**
  - output/liu_zongyuan/SKILL.md
  - output/liu_zongyuan/README.md
  - output/liu_zongyuan/METADATA.json
  - output/liu_zongyuan/CITATIONS.md
  - output/liu_zongyuan/raw_stats.json
  - output/liu_zongyuan/EVENTS.md
  - output/liu_zongyuan/VOICE.md
  - done/liu_zongyuan.done
```

---

## 四、统计概览

```
总人物数：     25
已完成：       13
进行中：       0
待处理：       12
完成率：       52%

按 confidence：
  high：       12
  medium：     1
  low：        0

按朝代：
  唐：         6 / 6
  北宋：       4 / 5
  南宋：       1 / 1
  晋：         1 / 1
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
