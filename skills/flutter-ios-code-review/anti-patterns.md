# Flutter iOS 应用常见安全 & 合规反模式速查卡

> 来源：基于「死鸭子嘴硬」项目审查经验总结。用于快速对照检查新项目。

---

## 🔴 安全红线（发现即修）

| # | 反模式 | 正确做法 |
|---|--------|---------|
| 1 | `const supabaseUrl = 'https://xxx.supabase.co'` | `dotenv.env['SUPABASE_URL']` + `.env` 文件 |
| 2 | `const supabaseAnonKey = 'eyJ...'` | 同上，或 `--dart-define` 注入 |
| 3 | `as Map<String, dynamic>` 无类型检查 | `if (response.data is! Map<String, dynamic>) throw ...` |
| 4 | Edge Function 直接插入用户输入 | 先验证：`if (msg.length > 2000) return 400` |
| 5 | 排行榜返回 `id` 字段 | select 中移除 `id`，只返回展示字段 |
| 6 | `.env` 在 `.gitignore` 中缺失 | 添加 `.env` |
| 7 | `*.xcuserstate` 未被忽略 | `.gitignore` 添加 `*.xcuserstate` 和 `*.xcuserdatad` |

---

## 🟡 iOS 发布红线（上架前必查）

| # | 反模式 | 正确做法 |
|---|--------|---------|
| 8 | Info.plist 缺少 `ITSAppUsesNonExemptEncryption` | 添加 `<false/>`（国内 App 通常为 false） |
| 9 | Info.plist 无隐私权限描述 | 相机/相册/麦克风/位置必须有描述文字 |
| 10 | Podfile `platform :ios, '12.0'` | 改为 `13.0`（supabase_flutter 要求） |
| 11 | Android `android:label="dead_duck"` | `android:label="@string/app_name"` + strings.xml |
| 12 | eas.json `appleTeamId: "YOUR_..."` | 替换为真实 Team ID |
| 13 | `UserInterfaceState.xcuserstate` 在版本库 | 删除 + `.gitignore` 排除 |

---

## 🟡 Flutter 代码红线

| # | 反模式 | 正确做法 |
|---|--------|---------|
| 14 | 在 `build()` 方法中执行 `await` | 改用 `AsyncNotifier` 或在 `main()` 中预初始化 |
| 15 | Screen 中直接 `supabase.from('xxx').insert()` | 统一走 `Repository`，Screen 不直接操作数据库 |
| 16 | 登录失败后静默标记为 `authenticated` | 登录失败应设置为 `AuthStatus.error` |
| 17 | 辩论创建逻辑在 Screen 和 Repository 各写一份 | 只在 Repository 保留一份 |
| 18 | 重复的 switch-case 分散在多个文件 | 提取为 `lib/core/utils/xxx_utils.dart` |

---

## 🟡 Supabase 安全红线

| # | 反模式 | 正确做法 |
|---|--------|---------|
| 19 | Edge Function 无输入验证 | 必做：类型 + 非空 + 长度 + 清理 |
| 20 | Edge Function 无速率限制 | 实现简单时间窗口限流 |
| 21 | `SECURITY DEFINER` 存储过程无调用者验证 | 不使用时删除，或改为 `SECURITY INVOKER` |
| 22 | 数据库表无 RLS 策略 | 每个表必须配置 RLS |
| 23 | Auth 错误被静默吞掉 | 捕获后设置错误状态，不静默标记为成功 |

---

## 🟡 文档合规红线

| # | 反模式 | 正确做法 |
|---|--------|---------|
| 24 | 无 LICENSE 文件 | 添加 MIT 或 Apache 2.0 |
| 25 | README 是 Flutter 默认模板 | 重写，包含特性/技术栈/快速开始 |
| 26 | 隐私政策邮箱是 `support@xxx.example.com` | 真实邮箱 |
| 27 | 隐私政策无数据保留期说明 | 补充"账号注销后 X 天删除" |
| 28 | 隐私政策无第三方 SDK 披露 | 列出所有第三方（MiniMax、Supabase 等） |
| 29 | 隐私政策无儿童/未成年人条款 | 补充符合 PIPL 的条款 |

---

## 🟡 依赖管理红线

| # | 反模式 | 正确做法 |
|---|--------|---------|
| 30 | pubspec 有 `cached_network_image` 但代码中未使用 | 删除 |
| 31 | pubspec 有 `shared_preferences` 但代码中未使用 | 删除或确认用途 |
| 32 | `flutter_lints: ^4.0.0` | 升级到 `^6.0.0` |
| 33 | transitive `js` 包 discontinued | 添加 `dependency_overrides: { js: ^0.7.2 }` |
| 34 | Flutter SDK 落后超过 6 个月 | 运行 `flutter upgrade` |
| 35 | `go_router` 落后超过 2 个主版本 | 分步升级（先到 N+1，测试，再 N+2） |

---

## ✅ 上线前检查清单

```
□ 所有 35 条反模式已检查并修复
□ Supabase RLS 策略通过 MCP 工具实际查询验证
□ .env 文件不在版本控制中
□ Info.plist 隐私声明完整
□ 隐私政策联系邮箱为真实地址
□ eas.json 填入真实值
□ CHANGELOG.md 存在
□ README.md 已重写
□ Android 应用名称本地化
□ Flutter pub get / build ipa --release 可正常构建
□ flutter analyze 无 error 级问题
□ Edge Function 重新部署
□ App Store Connect 隐私标签填写完毕
□ 真实联系邮箱在隐私政策中可见
□ 国内上架：软著 + ICP 备案 + APP 备案状态明确
```
