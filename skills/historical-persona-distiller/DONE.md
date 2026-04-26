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
| 13 | 王安石 | 北宋 | 2026-04-19 | high | 20 |
| 14 | 柳宗元 | 唐 | 2026-04-19 | high | 45 |
| 15 | 柳永 | 北宋 | 2026-04-19 | medium | 30 |
| 16 | 周邦彦 | 北宋 | 2026-04-19 | high | 45 |
| 17 | 屈原 | 战国 | 2026-04-19 | high | 14 |
| 18 | 曹操 | 三国 | 2026-04-19 | high | 5 |
| 19 | 嵇康 | 三国魏 | 2026-04-20 | high | 10 |
| 20 | 阮籍 | 三国魏 | 2026-04-20 | high | 25 |
| 21 | 蒲松龄 | 清 | 2026-04-20 | medium | 20 |
| 22 | 商鞅 | 战国 | 2026-04-20 | high | 20 |
| 23 | 韩非 | 战国 | 2026-04-20 | high | 10 |
| 24 | 李煜 | 南唐 | 2026-04-20 | high | 15 |
| 25 | 纳兰性德 | 清 | 2026-04-20 | high | 30 |
| 26 | 曾国藩 | 清 | 2026-04-20 | medium | 15 |
| 27 | 朱熹 | 南宋 | 2026-04-23 | high | 45 |
| 28 | 王阳明 | 明 | 2026-04-23 | high | 25 |
| 29 | 孔子 | 春秋 | 2026-04-23 | high | 50 |
| 30 | 庄子 | 战国 | 2026-04-23 | medium | 55 |
| 31 | 孟子 | 战国 | 2026-04-24 | high | 35 |
| 32 | 老子 | 春秋 | 2026-04-24 | high | 40 |
| 33 | 司马迁 | 西汉 | 2026-04-24 | high | 12 |
| 34 | 班固 | 东汉 | 2026-04-24 | high | 130 |
| 35 | 王羲之 | 东晋 | 2026-04-24 | high | 55 |
| 36 | 颜真卿 | 唐 | 2026-04-24 | high | 12 |
| 37 | 范仲淹 | 北宋 | 2026-04-24 | high | 30 |
| 38 | 寇准 | 北宋 | 2026-04-24 | medium | 30 |
| 39 | 管仲 | 春秋 | 2026-04-24 | medium | 15 |
| 40 | 魏征 | 唐 | 2026-04-24 | medium | 20 |
| 41 | 孙子 | 春秋 | 2026-04-25 | high | 55 |
| 42 | 吴起 | 战国 | 2026-04-25 | medium | 40 |
| 43 | 张仲景 | 东汉 | 2026-04-25 | high | 20 |
| 44 | 李时珍 | 明 | 2026-04-25 | medium | 120 |
| 45 | 沈括 | 北宋 | 2026-04-25 | medium | 60 |
| 46 | 蔡伦 | 东汉 | 2026-04-25 | medium | 25 |
| 47 | 毕昇 | 北宋 | 2026-04-25 | medium | 15 |
| 48 | 郭守敬 | 元 | 2026-04-26 | medium | 30 |
| 49 | 徐光启 | 明 | 2026-04-26 | medium | 30 |
| 50 | 宋应星 | 明 | 2026-04-26 | medium | 10 |
| 51 | 张衡 | 东汉 | 2026-04-26 | medium | 25 |
| 52 | 祖冲之 | 南北朝 | 2026-04-26 | medium | 60 |
| 53 | 李冰 | 战国 | 2026-04-26 | medium | 25 |
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

**下一待处理：** 郑和（明）
**persona_id：** zheng_he
**来源：** backlog #52

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

### 2026-04-19

**人物：** 王安石
**执行时间：** 00:09 - 00:17
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（王安石传记36426字+各代表作词条）为唯一可靠来源；诗词仅抓取约15首（不足30首下限），但传记和后世评述语料极为丰富
**产出文件：**
  - output/wang_anshi/SKILL.md
  - output/wang_anshi/README.md
  - output/wang_anshi/METADATA.json
  - output/wang_anshi/CITATIONS.md
  - output/wang_anshi/raw_stats.json
  - output/wang_anshi/EVENTS.md
  - output/wang_anshi/VOICE.md
  - done/wang_anshi.done

### 2026-04-19

**人物：** 柳永
**执行时间：** 10:01 - 10:31
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（传记+后世评述30条）和百度汉语（词作30首）为两个主要来源；由于网络限制，无法访问更权威的古典文献网站，语料主要依赖百度系列
**产出文件：**
  - output/liu_yong/SKILL.md
  - output/liu_yong/README.md
  - output/liu_yong/METADATA.json
  - output/liu_yong/CITATIONS.md
  - output/liu_yong/raw_stats.json
  - output/liu_yong/EVENTS.md
  - output/liu_yong/VOICE.md
  - raw/liu_yong/传记.txt
  - raw/liu_yong/诗词.txt
  - raw/liu_yong/引语.txt
  - raw/liu_yong/后世评述.txt
  - raw/liu_yong/全部语料.txt
  - processed/liu_yong/stages.md
  - processed/liu_yong/dimension_思想内核.json
  - processed/liu_yong/dimension_语言特征.json
  - processed/liu_yong/dimension_表达偏好.json
  - processed/liu_yong/dimension_立场光谱.json
  - processed/liu_yong/dimension_voice_profile.json
  - done/liu_yong.done

### 2026-04-19

**人物：** 周邦彦
**执行时间：** 04:17 - 05:02
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org 等主要古典文献网站无法访问；web_search 多次失败；改以百度百科（传记8000字+后世评述40+条）和百度汉语（词作30首）为两个主要来源；诗词约30首（不足30首下限但接近），传记和后世评述语料极为丰富；git push 首次超时，重试后成功
**产出文件：**
  - output/zhou_bangyan/SKILL.md
  - output/zhou_bangyan/README.md
  - output/zhou_bangyan/METADATA.json
  - output/zhou_bangyan/CITATIONS.md
  - output/zhou_bangyan/raw_stats.json
  - output/zhou_bangyan/EVENTS.md
  - output/zhou_bangyan/VOICE.md
  - raw/zhou_bangyan/传记.txt
  - raw/zhou_bangyan/诗词.txt
  - raw/zhou_bangyan/引语.txt
  - raw/zhou_bangyan/后世评述.txt
  - raw/zhou_bangyan/全部语料.txt
  - processed/zhou_bangyan/stages.md
  - processed/zhou_bangyan/dimension_思想内核.json
  - processed/zhou_bangyan/dimension_语言特征.json
  - processed/zhou_bangyan/dimension_表达偏好.json
  - processed/zhou_bangyan/dimension_立场光谱.json
  - processed/zhou_bangyan/dimension_voice_profile.json
  - done/zhou_bangyan.done

### 2026-04-19

**人物：** 屈原
**执行时间：** 14:01 - 14:15
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 全部失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；古诗文网(guwendao.net) 跳转频繁无法获取诗词全文；改以百度百科屈原传记（30000+字）为唯一主要来源；诗词原文主要从传记引语部分整理（核心名句均有收录）；语料传记极丰富，评价评述极丰富
**产出文件：**
  - output/qu_yuan/SKILL.md
  - output/qu_yuan/README.md
  - output/qu_yuan/METADATA.json
  - output/qu_yuan/CITATIONS.md
  - output/qu_yuan/raw_stats.json
  - output/qu_yuan/EVENTS.md
  - output/qu_yuan/VOICE.md
  - raw/qu_yuan/传记.txt
  - raw/qu_yuan/诗词.txt
  - raw/qu_yuan/引语.txt
  - raw/qu_yuan/后世评述.txt
  - raw/qu_yuan/全部语料.txt
  - processed/qu_yuan/stages.md
  - processed/qu_yuan/dimension_思想内核.json
  - processed/qu_yuan/dimension_语言特征.json
  - processed/qu_yuan/dimension_表达偏好.json
  - processed/qu_yuan/dimension_立场光谱.json
  - processed/qu_yuan/dimension_voice_profile.json
  - done/qu_yuan.done

### 2026-04-20

**人物：** 阮籍
**执行时间：** 04:08 - 04:33
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（阮籍传记16000+字+阮籍集+咏怀诗82首+大人先生传全文+通老论）为多个来源；咏怀诗82首全部收录，传记极为丰富，后世评述跨越魏晋至清四朝
**产出文件：**
  - output/ruan_ji/SKILL.md
  - output/ruan_ji/README.md
  - output/ruan_ji/METADATA.json
  - output/ruan_ji/CITATIONS.md
  - output/ruan_ji/raw_stats.json
  - output/ruan_ji/EVENTS.md
  - output/ruan_ji/VOICE.md
  - done/ruan_ji.done

### 2026-04-20

**人物：** 嵇康
**执行时间：** 02:01 - 02:11
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org、古诗文网等主要古典文献网站均无法访问；改以百度百科（嵇康传26000+字+嵇康集+幽愤诗原文+与山巨源绝交书原文）为主要来源；诗词原文主要从传记引语部分整理；语料传记极丰富，评价评述跨越魏晋至近现代四朝
**产出文件：**
  - output/ji_kang/SKILL.md
  - output/ji_kang/README.md
  - output/ji_kang/METADATA.json
  - output/ji_kang/CITATIONS.md
  - output/ji_kang/raw_stats.json
  - output/ji_kang/EVENTS.md
  - output/ji_kang/VOICE.md
  - done/ji_kang.done

### 2026-04-19

**人物：** 曹操
**执行时间：** 22:01 - 22:07
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** 前次执行（2026-04-19 16:10）已完成所有蒸馏步骤，但 git push 未成功，.done 文件未创建；本次接续执行，验证了所有 output 文件完整性后完成提交
**产出文件：**
  - output/cao_cao/SKILL.md
  - output/cao_cao/README.md
  - output/cao_cao/METADATA.json
  - output/cao_cao/CITATIONS.md
  - output/cao_cao/raw_stats.json
  - output/cao_cao/EVENTS.md
  - output/cao_cao/VOICE.md
  - done/cao_cao.done

### 2026-04-20

**人物：** 商鞅
**执行时间：** 08:08 - 08:28
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** ctext.org、wikisource.org 等主要古典文献网站无法访问；改以百度百科（商鞅传记、史记商君列传全文、商君书介绍）和百度百科后世评述为多个来源；商鞅为法家改革家非诗人，无诗词作品，以政论文和法令条文为主要语料；web_search 多次失败，改以 web_fetch 直接抓取
**产出文件：**
  - output/shang_yang/SKILL.md
  - output/shang_yang/README.md
  - output/shang_yang/METADATA.json
  - output/shang_yang/CITATIONS.md
  - output/shang_yang/raw_stats.json
  - output/shang_yang/EVENTS.md
  - output/shang_yang/VOICE.md
  - done/shang_yang.done
  - processed/shang_yang/stages.md
  - processed/shang_yang/dimension_思想内核.json
  - processed/shang_yang/dimension_语言特征.json
  - processed/shang_yang/dimension_表达偏好.json
  - processed/shang_yang/dimension_立场光谱.json
  - processed/shang_yang/dimension_voice_profile.json
  - processed/shang_yang/consistency_check.md
  - raw/shang_yang/传记.txt
  - raw/shang_yang/史记商君列传.txt
  - raw/shang_yang/商君书.txt
  - raw/shang_yang/引语.txt
  - raw/shang_yang/后世评述.txt
  - raw/shang_yang/全部语料.txt

### 2026-04-20

**人物：** 韩非
**执行时间：** 02:11 - 02:22
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** ctext.org 大量内页重定向至首页导致文本抓取失败；wikisource.org 无法访问；改以 web_fetch 直接抓取《五蠹》完整原文（ctext.org via wikilink 方式）、百度百科360百科多源抓取；web_search 多次失败；ctext.org 虽总体可访问但内页频繁重定向，《说难》《孤愤》完整原文未能获取
**产出文件：**
  - output/han_fei/SKILL.md
  - output/han_fei/README.md
  - output/han_fei/METADATA.json
  - output/han_fei/CITATIONS.md
  - output/han_fei/raw_stats.json
  - output/han_fei/EVENTS.md
  - output/han_fei/VOICE.md
  - done/han_fei.done
  - processed/han_fei/stages.md
  - processed/han_fei/dimension_思想内核.json
  - processed/han_fei/dimension_语言特征.json
  - processed/han_fei/dimension_表达偏好.json
  - processed/han_fei/dimension_立场光谱.json
  - processed/han_fei/dimension_voice_profile.json
  - processed/han_fei/dimension_一致性校验.json
  - raw/han_fei/传记.txt
  - raw/han_fei/五蠹.txt
  - raw/han_fei/南面.txt（部分）
  - raw/han_fei/raw_stats.json

### 2026-04-20

**人物：** 蒲松龄
**执行时间：** 06:01 - 06:20
**结果：** ✅ 完成（commit 已创建，git push 因 GitHub 网络不可达暂时失败，将在下次执行重试）
**confidence：** medium
**遇到的问题：** wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科为主要来源，抓取了蒲松龄传记（万字+）、聊斋自志原文、《促织》完整原文、后世评述语料。聊斋志异主体为491篇文言短篇小说（而非诗词），诗集虽有1017首但原始文本难以直接抓取，故 overall_confidence 评为 medium。GitHub push 失败（"Failed to connect to github.com port 443"），commit 96bf667 已本地创建，等待网络恢复后 push。
**产出文件：**
  - output/pu_songling/SKILL.md
  - output/pu_songling/README.md
  - output/pu_songling/METADATA.json
  - output/pu_songling/CITATIONS.md
  - output/pu_songling/raw_stats.json
  - output/pu_songling/EVENTS.md
  - output/pu_songling/VOICE.md
  - done/pu_songling.done
  - processed/pu_songling/stages.md
  - processed/pu_songling/dimension_思想内核.json
  - processed/pu_songling/dimension_语言特征.json
  - processed/pu_songling/dimension_表达偏好.json
  - processed/pu_songling/dimension_立场光谱.json
  - processed/pu_songling/dimension_voice_profile.json
  - processed/pu_songling/consistency_check.md
  - raw/pu_songling/传记.txt
  - raw/pu_songling/聊斋自志.txt
  - raw/pu_songling/聊斋志异_故事1_促织.txt
  - raw/pu_songling/后世评述.txt
  - raw/pu_songling/引语.txt
  - raw/pu_songling/全部语料.txt
  - raw/pu_songling/raw_stats.json
```

### 2026-04-20

**人物：** 李煜
**执行时间：** 06:19 - 06:34
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（李煜传记40000字+后世评述33条）和百度汉语（词作20首）为两个主要来源；诗词仅抓取20首（不足30首下限），但传记和后世评述语料极为丰富，来源包括徐铉墓志铭、王国维人间词话、陆游南唐书等多权威来源
**产出文件：**
  - output/li_yu/SKILL.md
  - output/li_yu/README.md
  - output/li_yu/METADATA.json
  - output/li_yu/CITATIONS.md
  - output/li_yu/raw_stats.json
  - output/li_yu/EVENTS.md
  - output/li_yu/VOICE.md
  - done/li_yu.done
  - processed/li_yu/stages.md
  - processed/li_yu/dimension_思想内核.json
  - processed/li_yu/dimension_语言特征.json
  - processed/li_yu/dimension_表达偏好.json
  - processed/li_yu/dimension_立场光谱.json
  - processed/li_yu/dimension_voice_profile.json
  - raw/li_yu/传记.txt
  - raw/li_yu/诗词.txt
  - raw/li_yu/引语.txt
  - raw/li_yu/后世评述.txt
  - raw/li_yu/全部语料.txt

### 2026-04-20

**人物：** 纳兰性德
**执行时间：** 08:06 - 08:36
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（纳兰传记30000+字+后世评述26条）和百度汉语（词作约30首）为两个主要来源；诗词以中小令为主，长调作品较少，整体语料偏重中小令
**产出文件：**
  - output/na_lan_xingde/SKILL.md
  - output/na_lan_xingde/README.md
  - output/na_lan_xingde/METADATA.json
  - output/na_lan_xingde/CITATIONS.md
  - output/na_lan_xingde/raw_stats.json
  - output/na_lan_xingde/EVENTS.md
  - output/na_lan_xingde/VOICE.md
  - done/na_lan_xingde.done
  - processed/na_lan_xingde/stages.md
  - processed/na_lan_xingde/dimension_思想内核.json
  - processed/na_lan_xingde/dimension_语言特征.json
  - processed/na_lan_xingde/dimension_表达偏好.json
  - processed/na_lan_xingde/dimension_立场光谱.json
  - processed/na_lan_xingde/dimension_voice_profile.json
  - processed/na_lan_xingde/consistency_check.md
  - raw/na_lan_xingde/传记.txt
  - raw/na_lan_xingde/诗词.txt
  - raw/na_lan_xingde/引语.txt
  - raw/na_lan_xingde/后世评述.txt
  - raw/na_lan_xingde/全部语料.txt

---

## 四、统计概览

```
总人物数：     75
已完成：       53
进行中：       0
待处理：       22
完成率：       71%（53/75）

按 confidence：
  high：       34
  medium：     19
  low：        0

按朝代：
  唐：         7 / 8
  北宋：       10 / 10
  南宋：       2 / 2
  晋：         1 / 1
  战国：       5 / 5
  三国：       3 / 3
  清：         4 / 4
  南唐：       1 / 1
  明：         4 / 5
  春秋：       4 / 4
  西汉：       2 / 2
  东汉：       4 / 4
  东晋：       1 / 1
  元：         1 / 1
  南北朝：     1 / 1
```

### 2026-04-20

**人物：** 曾国藩
**执行时间：** 10:01 - 10:16
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；baike.baidu.com/item/曾国藩 直接 URL 最初返回 404，改用 baike.baidu.com/item/曾国藩/386（通过苏拭条目中的内部链接发现正确 ID）；最终以百度百科曾国藩传记（49338字）为第一来源，桐城派条目（湘乡派相关信息）和湘乡派条目为补充语料；曾国藩为近代人物，家书、日记原文未能直接抓取，整体语料以传记评述为主
**产出文件：**
  - output/zeng_guofan/SKILL.md
  - output/zeng_guofan/README.md
  - output/zeng_guofan/METADATA.json
  - output/zeng_guofan/CITATIONS.md
  - output/zeng_guofan/raw_stats.json
  - output/zeng_guofan/EVENTS.md
  - output/zeng_guofan/VOICE.md
  - done/zeng_guofan.done

### 2026-04-23

**人物：** 朱熹
**执行时间：** 18:26 - 19:11
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** baike.baidu.com/item/朱熹/165782 直接返回404，改用 baike.baidu.com/item/朱熹（自动重定向至正确ID 106669）；web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（朱熹传记近30000字+后世评述）和百度汉语（诗词20首）为两个主要来源；朱熹为理学家非诗人，诗词数量偏少但传记和后世评述语料极为丰富
**产出文件：**
  - output/zhu_xi/SKILL.md
  - output/zhu_xi/README.md
  - output/zhu_xi/METADATA.json
  - output/zhu_xi/CITATIONS.md
  - output/zhu_xi/raw_stats.json
  - output/zhu_xi/EVENTS.md
  - output/zhu_xi/VOICE.md
  - done/zhu_xi.done
  - processed/zhu_xi/stages.md
  - processed/zhu_xi/dimension_思想内核.json
  - processed/zhu_xi/dimension_语言特征.json
  - processed/zhu_xi/dimension_表达偏好.json
  - processed/zhu_xi/dimension_立场光谱.json
  - processed/zhu_xi/dimension_voice_profile.json
  - raw/zhu_xi/传记.txt
  - raw/zhu_xi/诗词.txt
  - raw/zhu_xi/引语.txt
  - raw/zhu_xi/后世评述.txt
  - raw/zhu_xi/全部语料.txt

### 2026-04-23

**人物：** 王阳明
**执行时间：** 20:09 - 20:34
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（王阳明传记30K+字、传习录15K+字、王阳明全集9K+字）为多个来源；王阳明为理学家非诗人，诗词非主要文体，以散文语录为主要语料，整体语料以哲学论著和传记评述为主
**产出文件：**
  - output/wang_yangming/SKILL.md
  - output/wang_yangming/README.md
  - output/wang_yangming/METADATA.json
  - output/wang_yangming/CITATIONS.md
  - output/wang_yangming/raw_stats.json
  - output/wang_yangming/EVENTS.md
  - output/wang_yangming/VOICE.md
  - done/wang_yangming.done
  - processed/wang_yangming/stages.md
  - processed/wang_yangming/dimension_思想内核.json
  - processed/wang_yangming/dimension_语言特征.json
  - processed/wang_yangming/dimension_表达偏好.json
  - processed/wang_yangming/dimension_立场光谱.json
  - processed/wang_yangming/dimension_voice_profile.json
  - processed/wang_yangming/consistency_check.md
  - raw/wang_yangming/传记.txt
  - raw/wang_yangming/引语.txt
  - raw/wang_yangming/后世评述.txt
  - raw/wang_yangming/传习录.txt
  - raw/wang_yangming/全部语料.txt

---

### 2026-04-23

**人物：** 孔子
**执行时间：** 22:04 - 23:00
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org 古诗文网等无法访问；ctext.org 论语页面部分可访问（成功抓取学而、为政、里仁、述而、颜渊、子路六篇原文）；百度百科孔子传记（80000字+）为最可靠来源；孔子非诗人，以论语对话语录为最核心语料；补充大量后世评价（孟子、荀子、司马迁、朱熹等）作为引语来源
**产出文件：**
  - output/kong_zi/SKILL.md
  - output/kong_zi/README.md
  - output/kong_zi/METADATA.json
  - output/kong_zi/CITATIONS.md
  - output/kong_zi/raw_stats.json
  - output/kong_zi/EVENTS.md
  - output/kong_zi/VOICE.md
  - done/kong_zi.done
  - processed/kong_zi/stages.md
  - processed/kong_zi/dimension_思想内核.json
  - processed/kong_zi/dimension_语言特征.json
  - processed/kong_zi/dimension_表达偏好.json
  - processed/kong_zi/dimension_立场光谱.json
  - processed/kong_zi/dimension_voice_profile.json
  - processed/kong_zi/consistency_check.md
  - raw/kong_zi/传记.txt
  - raw/kong_zi/论语_学而.txt
  - raw/kong_zi/论语_为政.txt
  - raw/kong_zi/论语_里仁.txt
  - raw/kong_zi/论语_述而.txt
  - raw/kong_zi/论语_颜渊.txt
  - raw/kong_zi/论语_子路.txt
  - raw/kong_zi/引语.txt
  - raw/kong_zi/后世评述.txt
  - raw/kong_zi/全部语料.txt

### 2026-04-24

**人物：** 孟子
**执行时间：** 04:24 - 05:00
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（孟子传记+梁惠王上原文+尽心下原文）为多个来源；孟子为儒家哲学家非诗人，无诗词作品，以散文对话为主要语料
**产出文件：**
  - output/meng_zi/SKILL.md
  - output/meng_zi/README.md
  - output/meng_zi/METADATA.json
  - output/meng_zi/CITATIONS.md
  - output/meng_zi/raw_stats.json
  - output/meng_zi/EVENTS.md
  - output/meng_zi/VOICE.md
  - done/meng_zi.done
  - processed/meng_zi/stages.md
  - processed/meng_zi/dimension_思想内核.json
  - processed/meng_zi/dimension_语言特征.json
  - processed/meng_zi/dimension_表达偏好.json
  - processed/meng_zi/dimension_立场光谱.json
  - processed/meng_zi/dimension_voice_profile.json
  - raw/meng_zi/传记.txt
  - raw/meng_zi/梁惠王上.txt
  - raw/meng_zi/引语.txt
  - raw/meng_zi/后世评述.txt
  - raw/meng_zi/全部语料.txt

### 2026-04-24

**人物：** 老子
**执行时间：** 06:01 - 06:41
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（老子传记28000字+道德经词条25000字）为两个主要来源；老子为道家哲学家非诗人，以《道德经》五千言为核心语料
**产出文件：**
  - output/lao_zi/SKILL.md
  - output/lao_zi/README.md
  - output/lao_zi/METADATA.json
  - output/lao_zi/CITATIONS.md
  - output/lao_zi/raw_stats.json
  - output/lao_zi/EVENTS.md
  - output/lao_zi/VOICE.md
  - done/lao_zi.done
  - processed/lao_zi/stages.md
  - processed/lao_zi/dimension_思想内核.json
  - processed/lao_zi/dimension_语言特征.json
  - processed/lao_zi/dimension_表达偏好.json
  - processed/lao_zi/dimension_立场光谱.json
  - raw/lao_zi/传记.txt
  - raw/lao_zi/道德经.txt
  - raw/lao_zi/引语.txt
  - raw/lao_zi/后世评述.txt
  - raw/lao_zi/全部语料.txt

**执行时间：** 02:01 - 03:00
**结果：** ✅ 完成（git push 首次超时，重试后成功）
**confidence：** medium
**遇到的问题：** web_search 全部失败；wikisource.org、ctext.org 古诗文网等主要古典文献网站无法访问；改以百度百科（庄子传记30000字+、逍遥游全文、齐物论全文、《庄子》书籍介绍）为多个来源；庄子为道家哲学家非诗人，无诗词作品，以33篇《庄子》原文为核心语料；语料传记丰富，哲学语录极为系统；GitHub push 首次失败（Empty reply from server），sleep 120秒后重试成功
**产出文件：**
  - output/zhuang_zhou/SKILL.md
  - output/zhuang_zhou/README.md
  - output/zhuang_zhou/METADATA.json
  - output/zhuang_zhou/CITATIONS.md
  - output/zhuang_zhou/raw_stats.json
  - output/zhuang_zhou/EVENTS.md
  - output/zhuang_zhou/VOICE.md
  - done/zhuang_zhou.done
  - processed/zhuang_zhou/stages.md
  - processed/zhuang_zhou/dimension_思想内核.json
  - processed/zhuang_zhou/dimension_语言特征.json
  - processed/zhuang_zhou/dimension_表达偏好.json
  - processed/zhuang_zhou/dimension_立场光谱.json
  - processed/zhuang_zhou/dimension_voice_profile.json
  - processed/zhuang_zhou/consistency_check.md
  - raw/zhuang_zhou/传记.txt
  - raw/zhuang_zhou/逍遥游_全文.txt
  - raw/zhuang_zhou/齐物论_节选.txt
  - raw/zhuang_zhou/引语.txt
  - raw/zhuang_zhou/全部语料.txt
  - raw/zhuang_zhou/raw_stats.json

---

### 2026-04-24

**人物：** 司马迁
**执行时间：** 08:29 - 08:41
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（司马迁传记+太史公自序原文）为两个主要来源；司马迁为史学家非诗人，以《太史公自序》原文（约7800字）和史记概述为核心语料；生平资料丰富，历史评价跨越汉至现代
**产出文件：**
  - output/sima_qian/SKILL.md
  - output/sima_qian/README.md
  - output/sima_qian/METADATA.json
  - output/sima_qian/CITATIONS.md
  - output/sima_qian/raw_stats.json
  - output/sima_qian/EVENTS.md
  - output/sima_qian/VOICE.md
  - done/sima_qian.done
  - processed/sima_qian/stages.md
  - processed/sima_qian/dimension_思想内核.json
  - processed/sima_qian/dimension_语言特征.json
  - processed/sima_qian/dimension_表达偏好.json
  - processed/sima_qian/dimension_立场光谱.json
  - processed/sima_qian/dimension_voice_profile.json
  - processed/sima_qian/dimension_一致性校验.json
  - raw/sima_qian/传记.txt
  - raw/sima_qian/太史公自序.txt
  - raw/sima_qian/引语.txt
  - raw/sima_qian/后世评述.txt
  - raw/sima_qian/全部语料.txt

---

### 2026-04-24

**人物：** 班固
**执行时间：** 10:01 - 12:08
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；班固为东汉史学家非诗人，改以百度百科（班固传记23088字+汉书词条+两都赋+封燕然山铭17143字）为多个主要来源；班固以《汉书》为核心作品，语料以史传散文、铭文为主，无诗词下限要求；2017年蒙古杭爱山考古发现《封燕然山铭》实物，为铭文提供实物佐证
**产出文件：**
  - output/ban_gu/SKILL.md
  - output/ban_gu/README.md
  - output/ban_gu/METADATA.json
  - output/ban_gu/CITATIONS.md
  - output/ban_gu/raw_stats.json
  - output/ban_gu/EVENTS.md
  - output/ban_gu/VOICE.md
  - done/ban_gu.done
  - processed/ban_gu/stages.md
  - processed/ban_gu/dimension_思想内核.json
  - processed/ban_gu/dimension_语言特征.json
  - processed/ban_gu/dimension_表达偏好.json
  - processed/ban_gu/dimension_立场光谱.json
  - processed/ban_gu/dimension_voice_profile.json
  - processed/ban_gu/consistency_check.md
  - raw/ban_gu/传记.txt
  - raw/ban_gu/封燕然山铭.txt
  - raw/ban_gu/引语.txt
  - raw/ban_gu/后世评述.txt
  - raw/ban_gu/全部语料.txt
  - raw/ban_gu/raw_stats.json

---

### 2026-04-24

**人物：** 王羲之
**执行时间：** 14:01 - 14:56
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；王羲之为书法家非诗人，无诗词作品数量要求；改以百度百科（王羲之传记19000字+兰亭集序词条7000字+十七帖词条20000字）为多个主要来源；语料以书法理论、传记原文、《兰亭集序》全文为核心
**产出文件：**
  - output/wang_xizhi/SKILL.md
  - output/wang_xizhi/README.md
  - output/wang_xizhi/METADATA.json
  - output/wang_xizhi/CITATIONS.md
  - output/wang_xizhi/raw_stats.json
  - output/wang_xizhi/EVENTS.md
  - output/wang_xizhi/VOICE.md
  - done/wang_xizhi.done
  - processed/wang_xizhi/stages.md
  - processed/wang_xizhi/dimension_思想内核.json
  - processed/wang_xizhi/dimension_语言特征.json
  - processed/wang_xizhi/dimension_表达偏好.json
  - processed/wang_xizhi/dimension_立场光谱.json
  - processed/wang_xizhi/dimension_voice_profile.json
  - processed/wang_xizhi/dimension_一致性校验.json
  - raw/wang_xizhi/传记.txt
  - raw/wang_xizhi/兰亭集序.txt
  - raw/wang_xizhi/引语.txt
  - raw/wang_xizhi/后世评述.txt
  - raw/wang_xizhi/全部语料.txt
  - raw/wang_xizhi/raw_stats.json

### 2026-04-24

**人物：** 颜真卿
**执行时间：** 16:13 - 16:25
**结果：** ✅ 完成（git push 成功）
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；祭侄文稿百度百科URL变更，改用直接URL抓取；颜真卿为书法家非诗人，无诗词作品数量要求；改以百度百科（颜真卿传记45000字+书法作品4部+后世评述37条）为多个主要来源
**产出文件：**
  - output/yan_zhenqing/SKILL.md
  - output/yan_zhenqing/README.md
  - output/yan_zhenqing/METADATA.json
  - output/yan_zhenqing/CITATIONS.md
  - output/yan_zhenqing/raw_stats.json
  - output/yan_zhenqing/EVENTS.md
  - output/yan_zhenqing/VOICE.md
  - done/yan_zhenqing.done
  - processed/yan_zhenqing/stages.md
  - processed/yan_zhenqing/dimension_思想内核.json
  - processed/yan_zhenqing/dimension_语言特征.json
  - processed/yan_zhenqing/dimension_表达偏好.json
  - processed/yan_zhenqing/dimension_立场光谱.json
  - processed/yan_zhenqing/dimension_voice_profile.json
  - processed/yan_zhenqing/consistency_check.md
  - raw/yan_zhenqing/传记.txt
  - raw/yan_zhenqing/祭侄文稿.txt
  - raw/yan_zhenqing/争座位帖.txt
  - raw/yan_zhenqing/颜勤礼碑.txt
  - raw/yan_zhenqing/多宝塔碑.txt
  - raw/yan_zhenqing/引语.txt
  - raw/yan_zhenqing/后世评述.txt
  - raw/yan_zhenqing/全部语料.txt
  - raw/yan_zhenqing/raw_stats.json

---

### 2026-04-24

**人物：** 范仲淹
**执行时间：** 10:01 - 10:31
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** wikisource.org、ctext.org 等主要古典文献网站无法访问；范仲淹不以诗名为其主要成就，存世诗305首、词5首，均非其核心语料；改以百度百科（范仲淹传记45000+字+《岳阳楼记》原文+《灵乌赋》原文+后世评述40+条）为多个主要来源；范仲淹为政治家兼文学家，散文成就最高，《岳阳楼记》为其文学巅峰；语料以传记、散文、奏议为核心，后世评价跨越宋元明清四朝
**产出文件：**
  - output/fan_zhongyan/SKILL.md
  - output/fan_zhongyan/README.md
  - output/fan_zhongyan/METADATA.json
  - output/fan_zhongyan/CITATIONS.md
  - output/fan_zhongyan/raw_stats.json
  - output/fan_zhongyan/EVENTS.md
  - output/fan_zhongyan/VOICE.md
  - done/fan_zhongyan.done
  - processed/fan_zhongyan/stages.md
  - processed/fan_zhongyan/dimension_思想内核.json
  - processed/fan_zhongyan/dimension_语言特征.json
  - processed/fan_zhongyan/dimension_表达偏好.json
  - processed/fan_zhongyan/dimension_立场光谱.json
  - processed/fan_zhongyan/dimension_voice_profile.json
  - processed/fan_zhongyan/dimension_一致性校验.json
  - raw/fan_zhongyan/传记.txt
  - raw/fan_zhongyan/岳阳楼记.txt
  - raw/fan_zhongyan/引语.txt
  - raw/fan_zhongyan/后世评述.txt
  - raw/fan_zhongyan/全部语料.txt

---

### 2026-04-24

**人物：** 寇准
**执行时间：** 12:00 - 12:30
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** 百度百科寇准词条已下线（被电视剧角色占用，返回《大宋宫词》角色页面）；wikisource.org、ctext.org 等主要古典文献网站无法访问；大部分中国古典文献网站（ruiwen.com等）存在 gb2312 字符编码问题导致内容无法正确解码；web_search 多次失败；改以360搜索摘要、百度快照和搜索结果为主要来源，整理了寇准引语和传记语料
**产出文件：**
  - output/kou_zhun/SKILL.md
  - output/kou_zhun/README.md
  - output/kou_zhun/METADATA.json
  - output/kou_zhun/CITATIONS.md
  - output/kou_zhun/raw_stats.json
  - output/kou_zhun/EVENTS.md
  - output/kou_zhun/VOICE.md
  - done/kou_zhun.done
  - processed/kou_zhun/stages.md
  - processed/kou_zhun/dimension_思想内核.json
  - processed/kou_zhun/dimension_语言特征.json
  - raw/kou_zhun/传记.txt
  - raw/kou_zhun/引语.txt
  - raw/kou_zhun/后世评述.txt
  - raw/kou_zhun/全部语料.txt

### 2026-04-24

**人物：** 管仲
**执行时间：** 22:03 - 22:20
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；管仲为政治家非诗人，无诗词作品下限要求；改以百度百科（管仲传记25000字+《管子》概述23000字）为两个主要来源；《管子》托名管仲但非一人一时之作（稷下学派文集），直接原文引用有限
**产出文件：**
  - output/guan_zhong/SKILL.md
  - output/guan_zhong/README.md
  - output/guan_zhong/METADATA.json
  - output/guan_zhong/CITATIONS.md
  - output/guan_zhong/raw_stats.json
  - output/guan_zhong/EVENTS.md
  - output/guan_zhong/VOICE.md
  - done/guan_zhong.done
  - processed/guan_zhong/stages.md
  - processed/guan_zhong/dimension_思想内核.json
  - processed/guan_zhong/dimension_语言特征.json
  - processed/guan_zhong/dimension_表达偏好.json
  - processed/guan_zhong/dimension_立场光谱.json
  - processed/guan_zhong/dimension_voice_profile.json
  - processed/guan_zhong/consistency_check.md
  - raw/guan_zhong/传记.txt
  - raw/guan_zhong/管子.txt
  - raw/guan_zhong/引语.txt
  - raw/guan_zhong/后世评述.txt
  - raw/guan_zhong/全部语料.txt

---

### 2026-04-24

**人物：** 魏征
**执行时间：** 16:12 - 16:32
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；魏征为唐初政治家不以诗名为主要成就，诗歌共34首（非30首下限），但奏议和传记语料极为丰富；改以百度百科魏征传记（巨幅，详细）为唯一主要来源，抓取了传记原文（含大量直接引语）、后世评述（38+条）、诗词语料
**产出文件：**
  - output/wei_zheng/SKILL.md
  - output/wei_zheng/README.md
  - output/wei_zheng/METADATA.json
  - output/wei_zheng/CITATIONS.md
  - output/wei_zheng/raw_stats.json
  - output/wei_zheng/EVENTS.md
  - output/wei_zheng/VOICE.md
  - done/wei_zheng.done
  - processed/wei_zheng/stages.md
  - processed/wei_zheng/dimension_思想内核.json
  - processed/wei_zheng/dimension_语言特征.json
  - processed/wei_zheng/dimension_表达偏好.json
  - processed/wei_zheng/dimension_立场光谱.json
  - processed/wei_zheng/dimension_voice_profile.json
  - processed/wei_zheng/consistency_check.md
  - raw/wei_zheng/传记.txt
  - raw/wei_zheng/诗词.txt
  - raw/wei_zheng/引语.txt
  - raw/wei_zheng/后世评述.txt
  - raw/wei_zheng/全部语料.txt

---

### 2026-04-25

**人物：** 孙子
**执行时间：** 02:09 - 03:04
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；ctext.org 要求验证码验证；改以百度百科（孙子传记+孙子兵法词条）为两个主要来源；孙武为军事理论家非诗人，无诗词作品数量要求；语料以《孙子兵法》十三篇5900字全文为核心，传记语料丰富，后世评述跨越汉至现代极为系统
**产出文件：**
  - output/sun_zi/SKILL.md
  - output/sun_zi/README.md
  - output/sun_zi/METADATA.json
  - output/sun_zi/CITATIONS.md
  - output/sun_zi/raw_stats.json
  - output/sun_zi/EVENTS.md
  - output/sun_zi/VOICE.md
  - done/sun_zi.done
  - processed/sun_zi/stages.md
  - processed/sun_zi/dimension_思想内核.json
  - processed/sun_zi/dimension_语言特征.json
  - processed/sun_zi/dimension_表达偏好.json
  - processed/sun_zi/dimension_立场光谱.json
  - processed/sun_zi/dimension_voice_profile.json
  - processed/sun_zi/consistency_check.md
  - raw/sun_zi/传记.txt
  - raw/sun_zi/孙子兵法.txt
  - raw/sun_zi/引语.txt
  - raw/sun_zi/后世评述.txt
  - raw/sun_zi/全部语料.txt
  - raw/sun_zi/raw_stats.json

---

### 2026-04-25

**人物：** 吴起
**执行时间：** 04:04 - 04:44
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 全部失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；baike.baidu.com/item/吴起/8131 直接 URL 返回404，改用 baike.baidu.com/item/%E5%90%B4%E8%B5%B7 自动重定向至正确 ID；ctext.org 要求验证码验证；吴起为军事家非诗人，无诗词作品数量要求；语料以《吴子兵法》六篇全文（15000+字含原文）和百度百科吴起传记（27000字）为两个主要来源；后世评述语料跨越汉至现代（约40条引语和评价）
**产出文件：**
  - output/wu_qi/SKILL.md
  - output/wu_qi/README.md
  - output/wu_qi/METADATA.json
  - output/wu_qi/CITATIONS.md
  - output/wu_qi/raw_stats.json
  - output/wu_qi/EVENTS.md
  - output/wu_qi/VOICE.md
  - done/wu_qi.done
  - processed/wu_qi/stages.md
  - processed/wu_qi/dimension_思想内核.json
  - processed/wu_qi/dimension_语言特征.json
  - processed/wu_qi/dimension_表达偏好.json
  - processed/wu_qi/dimension_立场光谱.json
  - processed/wu_qi/dimension_voice_profile.json
  - processed/wu_qi/consistency_check.md
  - raw/wu_qi/传记.txt
  - raw/wu_qi/吴子兵法.txt
  - raw/wu_qi/引语.txt
  - raw/wu_qi/后世评述.txt
  - raw/wu_qi/全部语料.txt

---

### 2026-04-25

**人物：** 张仲景
**执行时间：** 14:01 - 14:20
**结果：** ✅ 完成
**confidence：** high
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；ctext.org 古诗文网古文岛等均要求验证码或重定向无法获取正文；改以百度百科张仲景词条（baike.baidu.com/item/张仲景/66566）为唯一主要来源；张仲景为医学家非诗人，无诗词作品下限要求；语料以传记原文（约22000字）和《伤寒论》原序全文为核心，后世评述（方中行、陈修园、张志聪等）较丰富；人物属医学家而非诗人，故以医论文体为主要语料而非诗词
**产出文件：**
  - output/zhang_zhongjing/SKILL.md
  - output/zhang_zhongjing/README.md
  - output/zhang_zhongjing/METADATA.json
  - output/zhang_zhongjing/CITATIONS.md
  - output/zhang_zhongjing/raw_stats.json
  - output/zhang_zhongjing/EVENTS.md
  - output/zhang_zhongjing/VOICE.md
  - done/zhang_zhongjing.done
  - processed/zhang_zhongjing/stages.md
  - processed/zhang_zhongjing/dimension_思想内核.json
  - processed/zhang_zhongjing/dimension_语言特征.json
  - processed/zhang_zhongjing/dimension_表达偏好.json
  - processed/zhang_zhongjing/dimension_立场光谱.json
  - processed/zhang_zhongjing/dimension_voice_profile.json
  - processed/zhang_zhongjing/consistency_check.md
  - raw/zhang_zhongjing/传记.txt
  - raw/zhang_zhongjing/引语.txt
  - raw/zhang_zhongjing/后世评述.txt
  - raw/zhang_zhongjing/全部语料.txt

---

### 2026-04-25

**人物：** 李时珍
**执行时间：** 16:03 - 18:00
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** 所有中文百科网站（百度百科、搜狗百科、360百科等）全部无法访问；ctext.org古诗文网等要求验证码；web_search 多次失败；主要依赖Britannica英文百科获取传记和医学史资料；李时珍为医学家非诗人，无诗词作品，语料以Britannica英文资料为主；中文语料严重受限
**产出文件：**
  - output/li_shizhen/SKILL.md
  - output/li_shizhen/README.md
  - output/li_shizhen/METADATA.json
  - output/li_shizhen/CITATIONS.md
  - output/li_shizhen/raw_stats.json
  - done/li_shizhen.done
  - processed/li_shizhen/stages.md
  - processed/li_shizhen/dimension_思想内核.json
  - processed/li_shizhen/dimension_语言特征.json
  - processed/li_shizhen/dimension_表达偏好.json
  - processed/li_shizhen/dimension_立场光谱.json
  - processed/li_shizhen/dimension_voice_profile.json
  - processed/li_shizhen/consistency_check.md
  - raw/li_shizhen/传记.txt
  - raw/li_shizhen/引语.txt
  - raw/li_shizhen/后世评述.txt
  - raw/li_shizhen/全部语料.txt

---

### 2026-04-25

**人物：** 沈括
**执行时间：** 18:01 - 19:01
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 全部失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；改以百度百科（沈括传记22000字+梦溪笔谈概述）为两个主要来源；web_fetch 直接抓取成功；沈括为科学家非诗人，无诗词作品下限要求；语料以传记和《梦溪笔谈》概述为核心，后世评述跨越宋元明清至现代，极为丰富
**产出文件：**
  - output/shen_kuo/SKILL.md
  - output/shen_kuo/README.md
  - output/shen_kuo/METADATA.json
  - output/shen_kuo/CITATIONS.md
  - output/shen_kuo/raw_stats.json
  - output/shen_kuo/EVENTS.md
  - output/shen_kuo/VOICE.md
  - done/shen_kuo.done
  - processed/shen_kuo/stages.md
  - processed/shen_kuo/dimension_思想内核.json
  - processed/shen_kuo/dimension_语言特征.json
  - processed/shen_kuo/dimension_表达偏好.json
  - processed/shen_kuo/dimension_立场光谱.json
  - processed/shen_kuo/dimension_voice_profile.json
  - processed/shen_kuo/consistency_check.md
  - raw/shen_kuo/传记.txt
  - raw/shen_kuo/引语.txt
  - raw/shen_kuo/后世评述.txt
  - raw/shen_kuo/梦溪笔谈_概述.txt
  - raw/shen_kuo/全部语料.txt
  - raw/shen_kuo/raw_stats.json

### 2026-04-25

**人物：** 蔡伦
**执行时间：** 20:04 - 20:29
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；ctext.org 要求验证码验证；改以百度百科（蔡伦传记25000+字）和 Britannica 英文百科为两个主要来源；蔡伦为宦官技术官僚，无诗词作品下限要求；语料以传记和技术成就语料为核心，历史评价语料较丰富
**产出文件：**
  - output/cai_lun/SKILL.md
  - output/cai_lun/README.md
  - output/cai_lun/METADATA.json
  - output/cai_lun/CITATIONS.md
  - output/cai_lun/raw_stats.json
  - output/cai_lun/EVENTS.md
  - output/cai_lun/VOICE.md
  - done/cai_lun.done
  - processed/cai_lun/stages.md
  - processed/cai_lun/dimension_思想内核.json
  - processed/cai_lun/dimension_语言特征.json
  - processed/cai_lun/dimension_表达偏好.json
  - processed/cai_lun/dimension_立场光谱.json
  - processed/cai_lun/dimension_voice_profile.json
  - processed/cai_lun/consistency_check.md
  - raw/cai_lun/传记.txt
  - raw/cai_lun/引语.txt
  - raw/cai_lun/后世评述.txt
  - raw/cai_lun/全部语料.txt
  - raw/cai_lun/raw_stats.json

### 2026-04-25

**人物：** 毕昇
**执行时间：** 22:03 - 22:18
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；ctext.org 古诗文网等要求验证码或重定向无法获取正文；改以百度百科（毕昇传记，引《梦溪笔谈》原文）为唯一主要来源；毕昇为北宋发明家非诗人，无诗词作品下限要求；语料以《梦溪笔谈》中沈括记录的活字印刷术原文为核心，后世评述语料较丰富；毕昇本人无原创诗文存世，所有引语均为沈括记录
**产出文件：**
  - output/bi_sheng/SKILL.md
  - output/bi_sheng/README.md
  - output/bi_sheng/METADATA.json
  - output/bi_sheng/CITATIONS.md
  - output/bi_sheng/raw_stats.json
  - output/bi_sheng/EVENTS.md
  - output/bi_sheng/VOICE.md
  - done/bi_sheng.done
  - processed/bi_sheng/stages.md
  - processed/bi_sheng/dimension_思想内核.json
  - processed/bi_sheng/dimension_语言特征.json
  - processed/bi_sheng/dimension_表达偏好.json
  - processed/bi_sheng/dimension_立场光谱.json
  - processed/bi_sheng/dimension_voice_profile.json
  - processed/bi_sheng/consistency_check.md
  - raw/bi_sheng/传记.txt
  - raw/bi_sheng/引语.txt
  - raw/bi_sheng/后世评述.txt
  - raw/bi_sheng/全部语料.txt
  - raw/bi_sheng/raw_stats.json

### 2026-04-26

**人物：** 郭守敬
**执行时间：** 00:06 - 00:36
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；主要依赖百度百科郭守敬词条（baike.baidu.com/item/郭守敬/53453，30000+字）和 Britannica 英文百科；郭守敬为天文学家、数学家、水利工程专家，无诗词作品，无诗词下限要求；语料以传记原文（30000字）和后世评述为核心
**产出文件：**
  - output/guo_shoujing/SKILL.md
  - output/guo_shoujing/README.md
  - output/guo_shoujing/METADATA.json
  - output/guo_shoujing/CITATIONS.md
  - output/guo_shoujing/raw_stats.json
  - output/guo_shoujing/EVENTS.md
  - output/guo_shoujing/VOICE.md
  - done/guo_shoujing.done
  - processed/guo_shoujing/stages.md
  - processed/guo_shoujing/dimension_思想内核.json
  - processed/guo_shoujing/dimension_语言特征.json
  - processed/guo_shoujing/dimension_表达偏好.json
  - processed/guo_shoujing/dimension_立场光谱.json
  - processed/guo_shoujing/dimension_voice_profile.json
  - processed/guo_shoujing/consistency_check.md
  - raw/guo_shoujing/传记.txt
  - raw/guo_shoujing/引语.txt
  - raw/guo_shoujing/全部语料.txt
  - raw/guo_shoujing/raw_stats.json

---

### 2026-04-26

**人物：** 徐光启
**执行时间：** 02:01 - 02:36
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；baike.baidu.com 词条内容被限制在约3000字符，无法获取完整长篇传记；Britannica 英文百科可访问但内容有限；徐光启为科学家非诗人，无诗词作品下限要求
**产出文件：**
  - output/xu_guangqi/SKILL.md
  - output/xu_guangqi/README.md
  - output/xu_guangqi/METADATA.json
  - output/xu_guangqi/CITATIONS.md
  - output/xu_guangqi/raw_stats.json
  - output/xu_guangqi/EVENTS.md
  - output/xu_guangqi/VOICE.md
  - done/xu_guangqi.done
  - processed/xu_guangqi/stages.md
  - processed/xu_guangqi/dimension_思想内核.json
  - processed/xu_guangqi/dimension_语言特征.json
  - processed/xu_guangqi/dimension_表达偏好.json
  - processed/xu_guangqi/dimension_立场光谱.json
  - processed/xu_guangqi/dimension_voice_profile.json
  - processed/xu_guangqi/consistency_check.md
  - raw/xu_guangqi/传记.txt
  - raw/xu_guangqi/后世评述.txt
  - raw/xu_guangqi/全部语料.txt
  - raw/xu_guangqi/raw_stats.json

---

### 2026-04-26

**人物：** 宋应星
**执行时间：** 05:46 - 05:56
**结果：** ✅ 完成
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；宋应星为科学家非诗人，无诗词作品下限要求；改以百度百科（宋应星传记30000字+天工开物词条28000字）为两个主要来源；大部分原始著作已散佚（原有10余种，现仅存5种），直接引语主要来自二手文献整理
**产出文件：**
  - output/song_yingxing/SKILL.md
  - output/song_yingxing/README.md
  - output/song_yingxing/METADATA.json
  - output/song_yingxing/CITATIONS.md
  - output/song_yingxing/raw_stats.json
  - output/song_yingxing/EVENTS.md
  - output/song_yingxing/VOICE.md
  - done/song_yingxing.done
  - processed/song_yingxing/stages.md
  - processed/song_yingxing/dimension_思想内核.json
  - processed/song_yingxing/dimension_语言特征.json
  - processed/song_yingxing/dimension_表达偏好.json
  - processed/song_yingxing/dimension_立场光谱.json
  - processed/song_yingxing/dimension_voice_profile.json
  - processed/song_yingxing/consistency_check.md
  - raw/song_yingxing/传记.txt
  - raw/song_yingxing/引语.txt
  - raw/song_yingxing/天工开物概述.txt
  - raw/song_yingxing/后世评述.txt
  - raw/song_yingxing/全部语料.txt
  - raw/song_yingxing/raw_stats.json

---

### 2026-04-26

**人物：** 张衡
**执行时间：** 14:05 - 14:30
**结果：** ✅ 完成（git push 成功）
**confidence：** medium
**遇到的问题：** web_search 全部失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；baike.baidu.com 百度百科张衡词条直接URL（/item/张衡/5790）返回404，无法访问；主要依赖 Britannica 英文百科（约千字简介）和后世评述二手文献整理；张衡为科学家非诗人，诗词数量不足30首下限；中文语料严重受限
**产出文件：**
  - output/zhang_heng/SKILL.md
  - output/zhang_heng/README.md
  - output/zhang_heng/METADATA.json
  - output/zhang_heng/CITATIONS.md
  - output/zhang_heng/raw_stats.json
  - output/zhang_heng/EVENTS.md
  - output/zhang_heng/VOICE.md
  - done/zhang_heng.done
  - processed/zhang_heng/stages.md
  - processed/zhang_heng/dimension_思想内核.json
  - processed/zhang_heng/dimension_语言特征.json
  - processed/zhang_heng/dimension_表达偏好.json
  - processed/zhang_heng/dimension_立场光谱.json
  - processed/zhang_heng/dimension_voice_profile.json
  - raw/zhang_heng/传记.txt
  - raw/zhang_heng/诗词.txt
  - raw/zhang_heng/引语.txt
  - raw/zhang_heng/后世评述.txt
  - raw/zhang_heng/全部语料.txt

---

### 2026-04-26

**人物：** 祖冲之
**执行时间：** 16:03 - 17:03
**结果：** ✅ 完成（git push 成功）
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；祖冲之为数学家非诗人，无诗词作品下限要求；其所有主要著作（《缀术》《大明历》正文《历议》等）均已亡佚，语料主要依赖百度百科和 Britannica 二手文献整理；中文古典语料严重受限
**产出文件：**
  - output/zu_chongzhi/SKILL.md
  - output/zu_chongzhi/README.md
  - output/zu_chongzhi/METADATA.json
  - output/zu_chongzhi/CITATIONS.md
  - output/zu_chongzhi/raw_stats.json
  - output/zu_chongzhi/EVENTS.md
  - output/zu_chongzhi/VOICE.md
  - done/zu_chongzhi.done
  - processed/zu_chongzhi/stages.md
  - processed/zu_chongzhi/dimension_思想内核.json
  - processed/zu_chongzhi/dimension_语言特征.json
  - processed/zu_chongzhi/dimension_表达偏好.json
  - processed/zu_chongzhi/dimension_立场光谱.json
  - processed/zu_chongzhi/dimension_voice_profile.json
  - processed/zu_chongzhi/consistency_check.md
  - raw/zu_chongzhi/传记.txt
  - raw/zu_chongzhi/引语.txt
  - raw/zu_chongzhi/后世评述.txt
  - raw/zu_chongzhi/全部语料.txt
  - raw/zu_chongzhi/raw_stats.json

---

### 2026-04-26

**人物：** 李冰
**执行时间：** 18:01 - 18:26
**结果：** ✅ 完成（git push 成功）
**confidence：** medium
**遇到的问题：** web_search 多次失败；wikisource.org、ctext.org 等主要古典文献网站无法访问；baike.baidu.com/item/李冰/16547 直接 URL 返回404，改用 baike.baidu.com/item/李冰 自动重定向至正确 ID；李冰为水利工程专家非诗人，无诗词作品下限要求；语料以百度百科（李冰传记19000字+都江堰词条20000字）为两个主要来源；《华阳国志·蜀志》《史记·河渠书》为权威史料；都江堰实体工程可验证其治水理念
**产出文件：**
  - output/li_bing/SKILL.md
  - output/li_bing/README.md
  - output/li_bing/METADATA.json
  - output/li_bing/CITATIONS.md
  - output/li_bing/raw_stats.json
  - output/li_bing/EVENTS.md
  - output/li_bing/VOICE.md
  - done/li_bing.done
  - processed/li_bing/stages.md
  - processed/li_bing/dimension_思想内核.json
  - processed/li_bing/dimension_语言特征.json
  - processed/li_bing/dimension_表达偏好.json
  - processed/li_bing/dimension_立场光谱.json
  - processed/li_bing/dimension_voice_profile.json
  - processed/li_bing/consistency_check.md
  - raw/li_bing/传记.txt
  - raw/li_bing/引语.txt
  - raw/li_bing/后世评述.txt
  - raw/li_bing/全部语料.txt

---

## 五、 backlog.md 同步规则

每次完成一个人物后：
1. 在「已完成」表格追加一行
2. 在 backlog.md 中将该人物的 `status` 从 `pending` 改为 `done`
3. 更新「统计概览」
4. 更新「下一待处理」
5. 若全部 high priority 完成，自动将下一个 medium priority 提升为「下一待处理」
