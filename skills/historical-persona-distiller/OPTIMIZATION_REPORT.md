# 历史任务蒸馏流程 — 优化分析报告

> 基于对 ARCHITECTURE.md、EXECUTION_LOGIC.md、RULES.md、DONE.md、backlog.md、persona_state.json 以及 97 条执行日志的全面审查。
> 日期：2026-05-04

---

## 🚀 一、Stage 3 并行化改造（最大收益）

### 现状

Stage 3（多维蒸馏）包含 5 个顺序执行的子步骤：

```
3.1 思想内核 → 3.2 语言特征 → 3.3 表达偏好 → 3.4 立场光谱 → 3.5 一致性校验
```

每个子步骤都是一次独立的 LLM 调用，平均耗时约 5-10 分钟，共约 30-40 分钟。

### 优化方案

**3.1-3.4 可以完全并行化**——它们的输入都是 `raw/{PID}/全部语料.txt`，彼此无依赖关系。

```
时间线（优化前）：[3.1][3.2][3.3][3.4][3.5]         = ~35分钟
时间线（优化后）：[3.1
                  3.2  (并行)
                  3.3
                  3.4  ]
                  [3.5]                               = ~15分钟
```

**实现方式：** 在 OpenClaw 调度中，将 3.1-3.4 打包为一次批量 LLM 调用（在一次 prompt 中同时要求输出 4 个维度），而不是 4 次独立调用。

**预期收益：** Stage 3 耗时降低约 60%。

---

## ⚡ 二、资料采集阶段的容错优化

### 现状

从执行日志看，**web_search 几乎每次都失败**（DuckDuckGo 连接超时），且 wikisource.org、ctext.org 等中文古典文献网站频繁不可访问。每次执行都需要现场尝试和降级，消耗大量时间（5-15 分钟试错）。

### 优化方案

#### 2.1 预定义分类回退链

为不同人物类型预定义可靠的回退源，避免现场搜索试探：

| 人物类型 | 第一优先级 | 第二优先级 | 第三优先级 |
|---------|-----------|-----------|-----------|
| 中国诗人（唐/宋） | baike.baidu.com | gushiwen.cn | 百度汉语 |
| 中国哲学家 | baike.baidu.com | ctext.org（如可用） | Stanford Encyclopedia |
| 中国科学家/帝王 | baike.baidu.com | Britannica | World History Encyclopedia |
| 西方哲学家 | Stanford Encyclopedia | Britannica | World History Encyclopedia |
| 西方文学家 | World History Encyclopedia | Britannica | Biography.com |

#### 2.2 SerpAPI 标准化

日志显示 SerpAPI（通过 web_fetch 调用）是西方人物数据最可靠的来源。建议将其标准化为所有西方人物的数据采集管道，而非事后补救措施。

#### 2.3 预缓存常用来源 URL

百度百科的 URL ID 经常变化（如 `/item/曾国藩` 与 `/item/曾国藩/386`），每次试错浪费 1-2 分钟。建议在 backlog.md 中增加 `fallback_urls` 字段：

```
| 曾国藩 | 清 | low | 桐城派殿军 | ✅ done 2026-04-20 |
  fallback: baike.baidu.com/item/曾国藩/386, gushiwen.cn
```

---

## 📊 三、DONE.md 数据一致性修复

### 发现的问题

| 问题 | 位置 | 说明 |
|------|------|------|
| 计数不一致 | "已完成：98" | 表格中只有 97 条记录（#1-#97） |
| 置信度值不合规范 | 亚里士多德（#78） | confidence = "A"，应为 high/medium/low |
| 置信度混合格式 | 李世民（#60）、武则天（#61） | confidence = "medium-high"，非标准值 |
| 统计字段错乱 | "high：36（已完38）" | "已完"数据与总数不匹配 |
| 条目重复 | 曹操 | 在第一批（#17）和第三批（#63）中各出现一次 |

### 修复建议

1. 将亚里士多德的 "A" 修正为 "high"
2. 将 "medium-high" 统一为 "high"（既然两者都满足 high 标准）
3. 修正统计概览的数字
4. 在 backlog.md 中删除重复的曹操条目

---

## 📂 四、文件管理和目录清理

### 发现的问题

| 问题 | 说明 |
|------|------|
| 中间产物保留 | `raw/` 和 `processed/` 在 git push 后仍保留，累积 ≈ 300+ 文件 |
| 文件名不统一 | 部分 `consistency_check.md`，部分 `dimension_一致性校验.json` |
| raw_stats.json 位置重复 | 既在 `raw/` 中，又在 `output/` 中 |
| 状态文件分散 | DONE.md + backlog.md + persona_state.json 三个文件管理状态 |

### 优化方案

#### 4.1 考虑将 raw/ 和 processed/ 加入 .gitignore

```
# .gitignore
skills/historical-persona-distiller/raw/
skills/historical-persona-distiller/processed/
```

这些中间文件可以随时从 source URL 重新生成，不需要保留在 Git 中。Git 只保留 `output/` 和 `done/` 的最终产物。

#### 4.2 统一文件名规范

所有维度文件统一用英文命名：

```
dimension_thought_core.json     (原 思想内核)
dimension_language_features.json (原 语言特征)
dimension_expression.json        (原 表达偏好)
dimension_stance_spectrum.json   (原 立场光谱)
dimension_voice_profile.json     (不变)
consistency_check.md             (原 一致性校验.json / consistency_check.md)
```

---

## 🔧 五、状态管理整合

### 现状

- `DONE.md`：已完成记录 + 下一待处理 + 统计概览 + 执行日志（Markdown）
- `backlog.md`：待处理队列（Markdown）
- `persona_state.json`：Agent 运行时状态（JSON）

三者格式不统一，容易出现同步问题。

### 优化方案

#### 5.1 下一待处理自动计算

当前下一待处理由人工在 DONE.md 中维护。可以改为：**从 backlog.md 自动查找 priority 最高且在 DONE.md 中无对应记录的人物**，消除手动更新的出错可能。

#### 5.2 考虑 `queue/` 目录的 Git 管理

当前 `DONE.md` 和 `backlog.md` 分别执行 git commit + git push。Git push 失败时（日志中频繁出现），两文件状态可能不一致。建议：

- 将 DONE.md 更新和 backlog.md 更新放在**同一个 commit** 中
- 或者在 Git push 失败时，回滚所有本地状态修改

---

## 🔄 六、并发和调度优化

### 现状

- 每天北京时间 06:00 处理 1 个人物
- 串行处理，一次一个人

### 优化建议

#### 6.1 为不同类型的蒸馏设置不同的执行频次

| 人物 priority | 建议执行策略 |
|-------------|------------|
| high | 每天 1 人（当前节奏） |
| medium | 每 2 天 1 人（降频） |
| low | 每周 2 人（降频） |

当前 backlog 中 high 剩余 36 人，medium 剩余 54 人，low 剩余 80 人。不加区分执行，high 可能会被 low 阻塞。

#### 6.2 出错自动重试

当前规则："pipeline 失败的人 → 保留在 backlog.md 中，等待人工介入"

建议增加：**Git push 失败时，自动重试最多 3 次后，改在下一个执行 slot 再重试一次**，而非标记为 "等待人工介入" 永久阻塞。

---

## 🧹 七、backlog.md 队列清理

| 问题 | 说明 |
|------|------|
| 戚继光 | backlog.md #75 标注为 pending，但实际 2026-04-27 已完成 |
| 曹操 | 第一批 #17 已 done，第三批 #63 又出现一次 |
| 孔子/孟子/老子/庄子 | 在第二批和中国哲学家中重复出现，虽然都已 done |
| 笛卡尔 | 第四批 #89 和第六批 #148 重复 |

**建议：** 统一清理 backlog，删除所有重复和误标记条目，确保 pending 状态的人物真实待处理。

---

## 📝 八、对话 Agent 优化

### 8.1 System Prompt 过长风险

当前 System Prompt 注入模板包含：
- 完整 SKILL.md（包含阶段切片、意象列表、必读篇目、原文引用等）
- 完整 EVENTS.md
- 最近 3 轮对话 + 摘要

对于文学作品丰富的人物（如李白、苏轼），SKILL.md 可能超过 5000 字。加上 EVENTS.md，合计可能接近 8000-10000 字的 system prompt。

**建议：** 在非必要场景下，只注入当前切片的子集内容，而非全量 SKILL.md。

### 8.2 Memory 文件路径

当前 memory 文件存储在 `skills/historical-persona-distiller/memory/` 下。但 `persona_state.json` 也指向同一路径。而 memory 文件本质上属于 Agent 运行时数据，放在 distiller 目录下语义不清晰。

**建议：** 将 memory 目录移到 `skills/historical-persona-agent/memory/`，明确所有权的划分。

---

## 九、优先级总结

| 优先级 | 优化项 | 预期收益 | 改动量 |
|--------|--------|---------|--------|
| P0 | Stage 3 并行化（合并 3.1-3.4 为一次调用） | Stage 3 耗时 ↓60% | 低（改 EXECUTION_LOGIC.md） |
| P0 | DONE.md 数据修复（A → high、medium-high → high、计数修正） | 数据准确 | 低 |
| P1 | 将 raw/ 和 processed/ 加入 .gitignore | Git 仓库大小 ↓30%+ | 低 |
| P1 | backlog.md 清理（重复/误标条目） | 队列准确 | 低 |
| P1 | 资料采集预定义回退链 | Stage 1 耗时 ↓50% | 中（改 RULES.md） |
| P2 | SerpAPI 标准化为西方人物主源 | 减少试错 | 低 |
| P2 | 状态文件整合 | 减少维护负担 | 中 |
| P2 | 统一维度文件名命名规范 | 减少混淆 | 中（批量重命名） |
| P3 | Agent System Prompt 切片级注入 | 节省 Token | 中 |
| P3 | 差异化的执行频次策略 | 长期产出更均衡 | 低 |
