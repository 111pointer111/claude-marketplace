# Flutter iOS 应用代码审查 Skill

## 触发条件

当用户发送以下类似消息时自动激活：
- "帮我审查代码"
- "代码审查"
- "review 我的项目"
- "检查代码问题"
- "审查 Flutter 项目"
- "帮我看看这个项目有没有问题"
- "代码有没有安全隐患"

## 审查范围

对 Flutter + iOS + Supabase 架构的应用进行全方位上线前审查，涵盖以下 5 个维度：

1. **iOS 发布配置安全** — Info.plist、Entitlements、Podfile、签名配置
2. **Flutter 代码架构与质量** — 状态管理、错误处理、安全性、内存泄漏
3. **Supabase 后端安全** — RLS 策略、Edge Function 输入验证、速率限制
4. **依赖管理与可维护性** — 包版本、unused 依赖、Flutter SDK
5. **文档与合规** — README、隐私政策、App Store 配置、LICENSE

## 审查流程

### 步骤 1：项目扫描（并行）

读取以下关键文件：

```
pubspec.yaml
lib/main.dart
lib/app.dart
analysis_options.yaml
ios/Runner/Info.plist
ios/Runner/Release.entitlements (如果存在)
ios/Podfile
ios/Flutter/Release.xcconfig
ios/Flutter/Generated.xcconfig
ios/Runner.xcworkspace/xcuserdata/** (检查 .xcuserstate)
android/app/src/main/AndroidManifest.xml
eas.json
.gitignore
.env.example (如果存在)
```

### 步骤 2：代码层审查（并行）

对 lib/ 目录下所有 Dart 文件审查：
- `lib/main.dart` — Supabase 初始化、凭证管理
- `lib/features/**/providers/*.dart` — Riverpod 状态管理规范
- `lib/features/**/data/repositories/*.dart` — 数据层安全性
- `lib/features/**/presentation/screens/*.dart` — UI 层问题
- `lib/shared/widgets/*.dart` — 共享组件
- `lib/core/**/*.dart` — 常量、主题、工具类

### 步骤 3：后端安全审查（并行）

Supabase MCP 工具查询：
- `mcp__supabase__list_tables` — 获取所有表
- `mcp__supabase__execute_sql` — 查询 RLS 策略
- `mcp__supabase__list_edge_functions` — 列出所有 Edge Function

审查 supabase/ 目录下的所有 Edge Function 代码：
- `supabase/functions/**/index.ts` — 输入验证、速率限制、API 调用

### 步骤 4：依赖审查

执行命令：
```bash
cd <项目目录>
flutter pub outdated
dart pub outdated
flutter analyze
```

### 步骤 5：合规审查

读取文档目录：
- `README.md`
- `LICENSE`
- `CHANGELOG.md`
- `docs/privacy.html` (隐私政策)
- `docs/technical.md`
- `docs/design.md`

---

## 审查清单

### 🔴 iOS 发布配置安全

#### 严重
- [ ] Info.plist 包含 `ITSAppUsesNonExemptEncryption`（出口合规性声明）
- [ ] Info.plist 包含所有必要的隐私权限声明：
  - `NSPhotoLibraryUsageDescription` — 如使用相册
  - `NSMicrophoneUsageDescription` — 如使用麦克风
  - `NSLocationWhenInUseUsageDescription` — 如使用定位
  - `NSCameraUsageDescription` — 如使用相机
- [ ] Info.plist 包含 `CFBundleURLTypes`（如使用深度链接/Supabase Auth 回调）
- [ ] Supabase URL 和 Anon Key 不硬编码在 Dart 源码中
- [ ] `.env` 文件不在版本控制中（`.gitignore` 包含 `.env`）
- [ ] `ios/Runner.xcworkspace/xcuserdata/**` 不在版本控制中（`.gitignore` 包含 `*.xcuserstate` 和 `*.xcuserdatad`）

#### 警告
- [ ] Podfile 设置 `platform :ios` 为 13.0 或更高
- [ ] `ios/Flutter/Generated.xcconfig` 确认在 `.gitignore` 中（避免硬编码路径泄漏）
- [ ] `ios/Runner/Release.entitlements` 存在且配置正确（如需要推送通知、沙盒化等）
- [ ] Release.xcconfig 或编译配置中 `DART_OBFUSCATION=true`
- [ ] Release.xcconfig 中 `TRACK_WIDGET_CREATION=false`

---

### 🔴 Flutter 代码架构与质量

#### 安全
- [ ] Supabase 凭证不硬编码（使用环境变量、flutter_dotenv 或 dart-define）
- [ ] 所有 API 响应进行防御性类型检查（`if (response.data is! Map)`）
- [ ] 用户输入在发送前经过长度限制和内容清理
- [ ] `!` 强制解包不存在于可能导致崩溃的路径

#### 架构
- [ ] 数据写入操作统一通过 Repository 或 Provider，不在 Screen 中直接调用 Supabase 客户端
- [ ] Riverpod Provider 使用正确模式：
  - 不在 `build()` 方法中执行异步操作
  - 使用 `AsyncNotifier` 处理异步初始化
  - `supabaseClientProvider` 语义正确
- [ ] `StreamSubscription` 和控制器正确 dispose
- [ ] `Future.delayed` 在页面 dispose 后不会触发回调访问已销毁的状态

#### 错误处理
- [ ] 所有 API 调用和数据库操作有 try-catch
- [ ] 错误信息有用户友好的展示（SnackBar/Dialog），不静默吞掉
- [ ] 认证失败/网络错误有明确的状态处理

#### 代码质量
- [ ] 无重复的 switch-case 逻辑（提取为工具函数）
- [ ] 无未使用的 import
- [ ] 无未使用的依赖包
- [ ] `prefer_const_constructors` lint 警告已消除
- [ ] `InputDecoration` 统一使用 `Theme.of(context).inputDecorationTheme`
- [ ] 硬编码字符串提取到常量（AppStrings 或类似）

#### 可访问性
- [ ] 按钮使用 `IconButton`/`InkWell` 而非纯 `GestureDetector`（支持键盘 Tab 导航）
- [ ] 重要交互元素有 `Semantics` 标签

---

### 🔴 Supabase 后端安全

#### 凭证与访问
- [ ] Supabase Anon Key 设计上可暴露在客户端（由 RLS 控制权限）
- [ ] `.env` 文件（或环境变量）存储 Supabase URL 和 Anon Key
- [ ] 服务端密钥（service_role key）绝不暴露在客户端代码中

#### RLS 策略验证（通过 MCP 工具查询 `pg_policies` 表）
- [ ] `profiles` 表：SELECT/INSERT/UPDATE 仅限本人（`auth.uid() = id`）
- [ ] `debates` 表：所有操作仅限辩论创建者（`auth.uid() = user_id`）
- [ ] `messages` 表：通过 debates 间接授权（嵌套 RLS 检查）
- [ ] `achievements` 表：所有操作仅限本人

#### Edge Function 输入验证（每个 Edge Function 必须包含）
- [ ] 所有 `req.json()` 解析后的字段进行类型检查（`typeof` 验证）
- [ ] 非空字符串验证（空字符串和 null 都需拒绝）
- [ ] 长度上限验证（如消息内容不超过 2000 字符）
- [ ] 内容清理（移除控制字符、trim 空白）
- [ ] SQL 注入防护（如有 SQL 操作）
- [ ] 速率限制（基于 IP 或用户 ID 的简单时间窗口限制）

#### API 响应
- [ ] 排行榜等接口不暴露 `id` 等主键，只返回展示用字段
- [ ] 错误响应不泄露内部实现细节（如数据库表名、列名）
- [ ] 响应包含适当的 HTTP 状态码（400/401/403/404/500）

---

### 🟡 依赖管理与可维护性

#### 版本检查
- [ ] Flutter SDK 版本为最新稳定版（运行 `flutter --version` 确认）
- [ ] 所有直接依赖无落后超过 2 个主版本的情况
- [ ] `flutter pub upgrade --major-versions` 无 breaking change 警告
- [ ] 无 discontinued 包（如 `js` 已废弃）

#### 依赖清理
- [ ] 无未使用的 direct 依赖（搜索 import 语句确认）
- [ ] `cached_network_image`、`shared_preferences` 等常见未使用包已确认用途
- [ ] `analysis_options.yaml` 配置合理的 lint 规则

#### 构建配置
- [ ] `eas.json` 的 `appleTeamId` 和 `ascAppId` 替换为真实值（非占位符）
- [ ] Android `AndroidManifest.xml` 的 `android:label` 使用字符串资源而非硬编码
- [ ] `pubspec.yaml` 的 `version` 符合语义化版本（SemVer）

---

### 🟡 文档与合规

#### 必要文件
- [ ] `LICENSE` 文件存在（推荐 MIT 或 Apache 2.0）
- [ ] `README.md` 已重写（非 Flutter 默认模板），包含：应用简介、功能特性、技术栈、快速开始
- [ ] `CHANGELOG.md` 存在，使用 Keep a Changelog 格式

#### 隐私政策（docs/privacy.html）
- [ ] 联系方式为真实邮箱（非 `example.com` 等占位域名）
- [ ] 包含数据收集范围的完整说明
- [ ] 包含第三方 SDK（如 MiniMax API）的隐私政策链接
- [ ] 包含数据保留期（如"账号注销后30天删除"）
- [ ] 包含用户数据导出权利（PIPL/GDPR 合规）
- [ ] 包含数据存储地点说明
- [ ] 包含未成年人隐私条款（《个人信息保护法》合规）
- [ ] 版本号与 App 版本对应

#### App Store 发布
- [ ] 有 App Store 上架检查清单文档（应用描述、关键词、截图计划、年龄分级）
- [ ] 有隐私标签映射文档（将隐私政策映射到 App Store Connect 隐私标签）
- [ ] 年龄分级正确（根据内容，辩论类通常 4+ 或 9+）
- [ ] 如有国内上架需求：软著、ICP 备案、APP 备案状态明确

#### 用户协议
- [ ] 有用户协议/服务条款文档（如 `docs/terms.html`）

---

## 输出格式

### 1. 总览表格

| 维度 | 严重 | 警告 | 建议 |
|------|------|------|------|
| iOS 发布配置 | X | X | X |
| Flutter 代码架构 | X | X | X |
| Supabase 后端安全 | X | X | X |
| 依赖管理 | X | X | X |
| 文档与合规 | X | X | X |
| **合计** | **X** | **X** | **X** |

### 2. 严重问题列表（按优先级排序）

每项包含：
- **问题描述**
- **位置**（文件:行号）
- **风险**（安全/合规/稳定性）
- **修复建议**（具体代码或操作步骤）

### 3. 警告问题列表

同上，分维度列出。

### 4. 建议问题列表

简略列出优化项。

### 5. 上线前行动路线图

```markdown
P0（立即修复，否则无法上架）:
  - [ ] ...
  - [ ] ...

P1（上线前必须修）:
  - [ ] ...
  - [ ] ...

P2（提升质量）:
  - [ ] ...
  - [ ] ...
```

### 6. 已确认无问题的方面

列出审查通过、无需修改的部分，增强信心。

---

## 修复执行

审查完成后，用户说"帮我修复"时，按以下优先级分批执行：

**P0 修复批次**（可并行）：
1. 移除硬编码凭证 → 环境变量
2. Info.plist 补全隐私声明
3. `.env` 加入 `.gitignore`
4. 创建 LICENSE
5. Android 应用名称本地化
6. eas.json 替换占位符

**P1 修复批次**（可并行）：
1. 统一数据写入逻辑（走 Repository）
2. Edge Function 输入验证
3. API 响应防御性类型检查
4. Podfile iOS 版本
5. 清理 .xcuserstate 文件
6. 补充隐私政策条款
7. 排行榜数据脱敏

**P2 修复批次**（可并行）：
1. 重写 README.md
2. 删除未使用依赖
3. 创建 CHANGELOG.md
4. 提取重复代码为工具类
5. 优化 analysis_options.yaml
6. 升级包版本（如 flutter_lints）

## 注意事项

- 审查时读取文件务必完整，不要断章取义
- RLS 策略验证必须通过 MCP 工具实际查询数据库，不可仅靠代码推断
- 对于 Flutter SDK 版本落后问题，需提醒用户 `flutter upgrade` 的 breaking change 风险
- 隐私政策中涉及法律合规的内容，建议用户咨询法律专业人士
- 所有修复必须先读取原文件再编辑，不可覆盖无关内容
