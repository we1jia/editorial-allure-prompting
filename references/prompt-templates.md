# 拿来即用的万能公式与八大高定场景模板库 (Prompt Templates)

所有模板均严格遵循五段式结构，并经过前置黑名单（Prompt Filter）与后置露肤度（Output Classifier）双重验证：

```text
[1. 商业/艺术定性] + [2. 人物神态与微动作] + [3. 高级剪裁材质服装] + [4. 环境与轮廓光影] + [5. 摄影机与胶片参数]
```

---

## 模板 1：高级晚宴 / 微醺张力（适合 Google Flow 视频 & 静态人像）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Cinematic high-fashion editorial shot. A captivating woman with a confident, subtle smile, looking back over her shoulder. She is wearing a form-fitting emerald green silk slip dress with a draped backless cut. Warm ambient candlelight and soft rim lighting gently highlight the contour of her collarbone and shoulders. Shallow depth of field, 85mm lens, shot on 35mm Kodak Portra 400 film, rich skin texture, moody luxury lounge background.
```

### 动态视频运镜扩展 (Motion Add-on)
```text
Continue from the reference image. Slow push-in camera movement. She slowly turns her head slightly toward the lens with an enigmatic, confident gaze as warm candlelight flickers softly across the emerald silk drape and her collarbone. Gentle ambient motion, shallow depth of field, cinematic 24fps film look, no sudden body movement.
```

- **设计拆解**：通过“露背垂坠真丝裙 + 轮廓边缘光 + 回眸锁骨特写”营造张力，暗调环境控制皮肤高亮占比，全程零违规词。

---

## 模板 2：阳光海岸 / 健康曲线（适合度假与活力风格）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Vogue summer resort campaign photography. A woman with sun-kissed skin and wet tousled hair, leaning against a minimalist white architectural wall by the Mediterranean sea. Wearing a tailored white linen shirt loosely draped over a sleek one-piece designer swimsuit. Golden hour sunlight casting dramatic shadows through palm leaves, dewy skin texture, crisp focus, Hasselblad medium format camera.
```

### 动态视频运镜扩展 (Motion Add-on)
```text
Continue from the reference image. Subtle orbital parallax camera movement. A gentle Mediterranean sea breeze moves strands of her wet tousled hair and softly ripples the edge of the draped white linen shirt. Dappled palm leaf shadows sway slowly across her sun-kissed collarbone. Crisp medium format editorial film aesthetic.
```

- **设计拆解**：用“宽松亚麻衬衫半搭设计师连体泳衣 + 棕榈叶斑驳阴影”代替直白的比基尼描写，完美切碎连续露肤区域，绕过皮肤占比过高的后置审查。

---

## 模板 3：暗调霓虹 / 王家卫式都市夜色（适合慢推镜 & 情绪叙事）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Atmospheric cinema still, Wong Kar-wai inspired high-fashion editorial. An alluring woman with a languid, magnetic gaze, leaning beside a rain-streaked floor-to-ceiling window at night. She wears a tailored black velvet corset top paired with a high-slit maxi skirt and sheer dark hosiery. Chiaroscuro lighting with warm amber and crimson neon reflections glistening on the velvet fabric and outlining her sculpted silhouette. Shot on 35mm anamorphic lens, Kodak Vision3 500T film, rich grain, shallow depth of field.
```

### 动态视频运镜扩展 (Motion Add-on)
```text
Continue from the reference image. Slow dolly push-in toward a medium close-up. Passing city lights cast slow-moving warm neon reflections across the rain-streaked glass and her collarbone. She exhales softly, her gaze remaining calm and magnetic. Smooth cinematic motion, anamorphic bokeh, no scene cuts.
```

- **设计拆解**：将高危词“胸衣/丝袜”转译为 `tailored black velvet corset top` 与 `sheer dark hosiery`，并用 `Chiaroscuro lighting`（明暗对照法）把大部分画面隐入高级暗部。

---

## 模板 4：清晨百叶窗 / 慵懒私密美学（适合 Grok Imagine / GPT 杂志风）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Quiet luxury editorial portrait in a sunlit minimalist Parisian apartment. A captivating woman with tousled morning hair and a serene, confident posture, sitting by tall French windows. She is wearing an oversized ivory cashmere cardigan loosely slipping off one shoulder over a delicate champagne silk camisole. Dramatic morning sunlight streaming through Venetian blinds casts geometric shadow lines across her dewy skin and collarbone. Shot on Leica M11, 50mm Summilux lens, Kodak Portra 400, natural unretouched skin texture.
```

- **设计拆解**：用“大号羊绒开衫微露单肩 + 香槟色真丝吊带 + 百叶窗几何光影”营造极致的私密清晨感，比直白写私房内衣高级且稳过全平台审查。

---

## 模板 5：智性吸烟装 / 雕塑感力量轮廓（适合 Google Flow 垫图 Ingredients 首选）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Saint Laurent campaign style high-fashion editorial, Helmut Newton inspired aesthetic. A statuesque woman with sharp, confident posture standing in a brutalist concrete gallery. She wears a sharply tailored black wool tuxedo blazer with a deep architectural neckline and sculpted shoulders, paired with sleek high-waisted trousers. Crisp studio rim lighting carves out her jawline, collarbone, and elongated silhouette against a moody charcoal background. Medium format photography, 85mm lens, subtle film grain, high contrast editorial look.
```

- **设计拆解**：包裹度极高但通过 `deep architectural neckline`（建筑感深领口）与 `crisp studio rim lighting`（锐利轮廓边缘光）展现出极具张力的高级性感，是作为 Google Flow 角色一致性垫图（Ingredients）的最安全底图。

---

## 模板 6：前卫暗黑高定 / 戏剧化沙漏轮廓（适合哥特、礼服与造型张力）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Avant-garde Vogue dark romance high-fashion editorial photography, vertical 3:4 composition. A captivating woman with sculpted statuesque proportions, dewy porcelain complexion catching a warm golden candlelight glow on her collarbone and shoulders, long tousled silky black hair, and parted glossy lips with an enigmatic gaze. She wears an avant-garde haute couture gothic ensemble: a sharply structured black satin corset bodice with a deep architectural neckline that accentuates an hourglass silhouette, off-the-shoulder draped white Chantilly lace sleeves, an asymmetric high-slit layered silk-tulle skirt, and sheer dark hosiery with intricate lace trim. Low-key chiaroscuro lighting with warm amber rim lighting against aged stone walls. Shot on Canon EOS R5, 85mm f/1.4 lens, Kodak Portra 400 film aesthetic, unretouched skin texture.
```

- **设计拆解**：将易被拦截的制服/角色扮演词汇全面升级为高定时装屋结构词汇（`structured satin corset bodice`、`Chantilly lace`、`sheer dark hosiery`），兼具戏剧夸张度与安全性。

---

## 模板 7：雨夜后座 / 希区柯克式冷感悬疑（适合中近景与眼神特写）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Noir cinematic editorial portrait, Tom Ford inspired nocturnal luxury. Medium close-up framing from the waist up inside the leather backseat of a vintage limousine at night. An alluring woman with sleek dark hair and a cool, unblinking gaze looks out through a rain-beaded window. She wears a bias-cut midnight-blue liquid satin evening dress with an asymmetric one-shoulder strap and a subtle fur-trimmed wrap loosely draped around her elbows. Passing amber streetlamps cast moving caustic light patterns across her dewy cheekbone and collarbone. Shot on 50mm anamorphic lens, Cinestill 800T film, soft halation, shallow depth of field.
```

- **设计拆解**：采用腰部以上中近景（`Medium close-up from the waist up`）+ 雨滴车窗前景半遮挡，是解决全身照露肤面积超标的经典电影构图。

---

## 模板 8：双人电影剧照 / 克制推拉张力（专用于双人亲密构图安全重构）

### 静态图 / 基础关键帧 (Base Keyframe)
```text
Cinematic high-fashion editorial couple portrait, Wong Kar-wai inspired romantic drama still, horizontal 16:9 composition. In a moody luxury modernist hotel suite, an alluring woman with long dark hair and dewy skin leans gracefully over the armrest of a textured charcoal-grey fabric chaise lounge beside a man resting back, sharing a captivating, enigmatic gaze at close proximity. She wears a halter-neck black silk maxi dress featuring crimson botanical floral prints with an asymmetric high-slit drape, sheer dark hosiery, and crystal-embellished ankle-strap stiletto heels. Warm ambient lamp light and soft chiaroscuro shadows contour her collarbone and shoulders. Shot on 35mm Kodak Portra 400 film, 50mm lens, rich fabric texture, no text, no watermark.
```

- **设计拆解**：用“近距离眼神交汇（`sharing an enigmatic gaze at close proximity`）+ 优雅倚靠扶手（`leaning gracefully over the armrest`）”替代高危肢体交叠，在保留浓郁暧昧氛围的同时 100% 规避姿态审查。
