# 五维词汇降敏与高定视觉转译词典 (Lexicon Matrix)

本词典用于将易触发前置黑名单（Prompt Filter）或导致后置裸露度超标（Output Classifier）的生理、暴露、擦边词汇，精准转译为 **Vogue 级商业时尚摄影术语** 与 **电影摄影指导（DP）镜头语言**。

---

## 1. 整体氛围与美学定性 (Mood & Editorial Framing)

| 视觉意图 | ❌ 高危拦截词 (Red Flags) | ✅ 安全高定转译词 (Editorial Replacements) | 适用平台与效果说明 |
| :--- | :--- | :--- | :--- |
| 性感迷人 | `Sexy`, `Hot`, `Erotic`, `Pornographic`, `NSFW` | `Alluring`, `Captivating`, `Magnetic presence`, `High-fashion editorial`, `Vogue September issue style` | 全平台通用；将“肉欲”拉升为“杂志大片的吸引力” |
| 撩人/微醺暧昧 | `Seductive`, `Sensual`, `Tempting`, `Flirty`, `Steamy` | `Sultry mood`, `Intimate cinematic atmosphere`, `Enigmatic gaze`, `Languid elegance` | 全平台通用；`Sultry` 与 `Languid`（慵懒优雅）极出电影感 |
| 私房/卧室感 | `Bedroom eyes`, `Boudoir`（Flow/GPT 慎用）, `Undressed` | `Morning architectural loft aesthetic`, `Intimate portrait in soft daylight`, `Quiet luxury lounge mood` | Flow/GPT 推荐用建筑感晨光替代直白卧室；Grok 可直接用 `Boudoir photography style` |

---

## 2. 服装剪裁与高级面料 (Tailoring, Cut & Fabric)

**核心心法**：不要写“穿得少（Revealing/Skimpy）”，要写“怎么剪裁（Architectural cut）”和“什么面料贴合轮廓（Draped silk/Form-fitting knit）”。

| 视觉意图 | ❌ 高危拦截词 (Red Flags) | ✅ 安全高定转译词 (Editorial Replacements) | 视觉控制作用 |
| :--- | :--- | :--- | :--- |
| 内衣/贴身衣物 | `Lingerie`, `Bra`, `Panties`, `Underwear`, `See-through` | `Tailored corset top`（剪裁胸衣式上衣）, `Structured bustier bodice`（结构感胸衣下摆）, `Silk loungewear set`（真丝家居套装） | 用高定成衣结构词替代内衣词，完全避开前置拦截 |
| 吊带/露背/晚礼服 | `Revealing dress`, `Skimpy outfit`, `Low-cut` | `Off-the-shoulder silk slip dress`（露肩真丝吊带裙）, `Backless evening gown`（露背晚礼服）, `Bias-cut draped satin dress`（斜裁垂坠缎面裙） | 斜裁真丝（Bias-cut silk）会自然贴合身体曲线且极其高级 |
| 比基尼/泳装 | `Bikini`, `Micro bikini`, `String bikini`, `Swimsuit`（Flow 垫图慎用） | `Sleek one-piece designer swimsuit`（利落设计师连体泳衣）, `Tailored white linen shirt loosely draped over resort swimwear`（宽松白亚麻衬衫半搭度假泳装） | 外搭半敞亚麻衬衫可大幅降低皮肤像素占比，绕过第二道墙 |
| 紧身展现曲线 | `Tight clothes`, `Skin-tight`, `Latex`, `Bodycon` | `Form-fitting ribbed knitwear`（修身罗纹针织）, `Sculpted haute couture silhouette`（雕塑感高定剪裁）, `Second-skin merino wool turtleneck` | Google Flow 垫图（Ingredients）首选，零露肤却极具曲线张力 |

---

## 3. 腿部、下装与鞋履 (Lower Body & Hosiery)

| 视觉意图 | ❌ 高危拦截词 (Red Flags) | ✅ 安全高定转译词 (Editorial Replacements) | 视觉控制作用 |
| :--- | :--- | :--- | :--- |
| 短裙/露腿 | `Short skirt`, `Mini skirt`, `Thong`, `Booty shorts` | `High-slit floor-length maxi skirt`（高开叉及地长裙）, `Asymmetric wrap skirt`（不对称裹身裙）, `Tailored high-waisted shorts`（精裁高腰短裤） | 高开叉长裙既有修长腿部线条，又靠裙摆面积压低总露肤率 |
| 丝袜/吊带袜 | `Stockings`, `Garter belt`, `Fishnets`, `Nylons` | `Sheer dark hosiery`（微透暗色裤袜）, `Translucent black tights`, `Monochrome editorial legwear` | `Stockings` 极易被安全模型关联到成人标签，改为 `Sheer dark hosiery` 100% 过审 |

---

## 4. 身体轮廓、姿态与神态 (Silhouette, Pose & Micro-Expression)

| 视觉意图 | ❌ 高危拦截词 (Red Flags) | ✅ 安全高定转译词 (Editorial Replacements) | 适用场景（静图/视频） |
| :--- | :--- | :--- | :--- |
| 丰满/曲线身材 | `Curvy`, `Busty`, `Cleavage`, `Thick`, `Voluptuous` | `Sculpted silhouette`（雕塑感轮廓）, `Graceful statuesque proportions`（修长雕塑比例）, `Athletic toned physique`（健康紧致体态） | 全平台通用；配合边缘光（Rim light）直接用光影勾勒曲线 |
| 撩人姿势 | `Provocative pose`, `Spreading legs`, `Arching back`, `Bending over` | `Looking back over the shoulder`（回眸）, `Leaning against a minimalist wall`（倚靠极简墙面）, `Confident poised posture`（自信从容仪态）, `Dynamic fashion editorial pose` | 绝不写大幅度扭曲肢体的词，回眸与微倚靠最具电影故事感 |
| 眼神与微动作（视频） | `Seductive wink`, `Biting lip`, `Licking lips`, `Twerking` | `Subtle confident smile`（微妙自信笑意）, `Unblinking magnetic gaze into the lens`, `Fingers lightly brushing collarbone`（指尖轻触锁骨）, `Gentle breeze moving hair across face` | 专为 Google Flow / Veo 动态视频设计，克制微动不触发姿态报警 |

---

## 5. 皮肤质感、光影遮蔽与摄影胶片 (Skin, Lighting & Camera Specs)

这是**绕过第二道墙（后置裸露度分类器）并消除 AI 网红塑料感**的核心武器库：

### 皮肤与光泽 (Skin & Complexion)
- ❌ 禁用：`Naked skin`, `Bare body`, `Wet body`, `Sweaty`, `Oiled up`
- ✅ 替换为：
  - `Sun-kissed skin`（阳光亲吻肌）
  - `Dewy complexion`（水润清透肤质）
  - `Golden hour glow on collarbone and shoulders`（锁骨与肩线的夕阳光泽）
  - `Rich natural skin texture with visible pores, no plastic smoothing`（真实细腻肤质，拒绝塑料磨皮）

### 光影切割与暗部遮蔽 (Lighting as Clothing)
- `Chiaroscuro lighting`（明暗对照法：用高反差暗部自然隐藏敏感区域）
- `Soft rim lighting outlining the silhouette`（勾勒身体轮廓的柔和边缘光）
- `Warm ambient candlelight casting soft shadows`（温暖烛光投射柔和阴影）
- `Dramatic Venetian blind shadows across the figure`（百叶窗光影切割人物线条，大幅降低系统识别到的连续裸露皮肤面积）
- `Warm neon reflections on draped satin fabric`（垂坠缎面上的温暖霓虹反光）

### 摄影机与胶片参数 (Camera & Film Stock)
- `Shot on 35mm Kodak Portra 400 film, subtle film grain`（柯达 Portra 400 胶片，肤色还原极佳）
- `Hasselblad H6D medium format camera, 85mm f/1.4 portrait lens`（哈苏中画幅 + 85mm 人像镜皇，浅景深虚化杂乱背景）
- `Shallow depth of field focusing on eyes and collarbone`（焦点锁定眼神与锁骨）
- `Anamorphic cinema lens, warm halation, Wong Kar-wai inspired color grading`（变形宽银幕电影镜头，王家卫式暖调光晕）
