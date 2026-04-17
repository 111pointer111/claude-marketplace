# Persona ID 命名规范

> persona_id 是每个人物在系统中的唯一标识符，用于目录名、文件路径、API 引用等所有场景。
> 一旦确定，**永不更改**。

---

## 一、基本规则

```
persona_id = 姓名汉语拼音全拼（小写）+ 下划线连接各字
```

**示例：**

| 人物 | persona_id |
|------|-----------|
| 苏轼 | su_shi |
| 李白 | li_bai |
| 杜甫 | du_fu |
| 王维 | wang_wei |
| 白居易 | bai_juyi |
| 辛弃疾 | xin_qiji |
| 陶渊明 | tao_yuanming |
| 李清照 | li_qingzhao |

---

## 二、复姓处理

复姓两个字合并拼写，中间**不加下划线**。

| 人物 | persona_id |
|------|-----------|
| 欧阳修 | ouyang_xiu |
| 司马迁 | sima_qian |
| 诸葛亮 | zhuge_liang |
| 上官婉儿 | shangguan_waner |

---

## 三、单名人物

姓 + 名单独拼接，规则不变。

| 人物 | persona_id |
|------|-----------|
| 韩愈 | han_yu |
| 柳永 | liu_yong |
| 曹操 | cao_cao |
| 王羲之 | wang_xizhi |

---

## 四、多音字处理

以**最常用读音**为准，不标声调。

| 人物 | 多音字 | 正确读音 | persona_id |
|------|--------|---------|-----------|
| 韩愈 | 愈（yù/yú） | yù | han_yu |
| 柳永 | 永（yǒng） | yǒng | liu_yong |
| 召（shào/zhāo） | shào | shao_you |
| 什（shí/shén） | shí | shi_zhen |

> 如有疑问，以《现代汉语词典》常用读音为准。

---

## 五、特殊人物

| 人物 | persona_id | 说明 |
|------|-----------|------|
| 蒲松龄 | pu_songling | 标准拼写 |
| 纳兰性德 | nalan_xingde | 复姓"纳兰"，按单姓处理 |
| 曾国藩 | zeng_guofan | 标准拼写 |
| 李煜 | li_yu | 五代南唐末帝 |

---

## 六、唯一性保证

**规则：同一 persona_id 只对应一人，永不重复。**

命名冲突时，按以下优先级处理：

```
1. 优先使用姓名（姓+名）全拼
2. 如姓名全拼在系统中已有同名人物，追加字号（hao）区分
3. 如字号仍重复，追加生卒年
```

**冲突示例：**

| 人物 | persona_id | 区分方式 |
|------|-----------|---------|
| 王献之（东晋，书画家） | wang_xianzhi | 与王献之（其他）区分 |
| 王献之 + 字号"子敬" | wang_xianzhi_zijing | 追加字号 |

> **注意：** 同一人物可能有多个称呼（如杜甫字子美），统一使用**姓名**，不混入字号。

---

## 七、生成规则（Pipeline 自动执行）

```
Step 1: 读取 backlog.md 中人物的"人物"列
Step 2: 转换为拼音全拼（小写）
Step 3: 姓与名之间加下划线
Step 4: 检查是否与已有 persona_id 冲突
Step 5: 如冲突，按 Section 六规则处理
Step 6: 将最终 persona_id 写入 METADATA.json
```

**Python 参考实现：**

```python
def to_persona_id(name: str) -> str:
    """
    将中文姓名转换为 persona_id
    规则：拼音全拼 + 下划线连接各字，小写
    """
    import pypinyin
    # 获取不带声调的拼音列表
    pinyin_list = pypinyin.lazy_pinyin(list(name))
    return '_'.join(pinyin_list)

# 示例
print(to_persona_id("苏轼"))     # su_shi
print(to_persona_id("欧阳修"))   # ouyang_xiu
print(to_persona_id("韩愈"))     # han_yu
```

---

## 八、已确定 persona_id 列表（backlog 对照）

| 人物 | persona_id | 备注 |
|------|-----------|------|
| 苏轼 | su_shi | |
| 杜甫 | du_fu | |
| 李白 | li_bai | |
| 辛弃疾 | xin_qiji | |
| 陶渊明 | tao_yuanming | |
| 王维 | wang_wei | |
| 白居易 | bai_juyi | |
| 李清照 | li_qingzhao | |
| 欧阳修 | ouyang_xiu | 复姓 |
| 苏辙 | su_zhe | |
| 韩愈 | han_yu | |
| 柳宗元 | liu_zongyuan | |
| 王安石 | wang_anshi | |
| 柳永 | liu_yong | |
| 周邦彦 | zhou_bangyan | |
| 屈原 | qu_yuan | |
| 曹操 | cao_cao | |
| 嵇康 | ji_kang | 多音字"嵇"读jī |
| 阮籍 | ruan_ji | |
| 蒲松龄 | pu_songling | |
| 商鞅 | shang_yang | |
| 韩非 | han_fei | |
| 李煜 | li_yu | |
| 纳兰性德 | nalan_xingde | 复姓 |
| 曾国藩 | zeng_guofan | |
