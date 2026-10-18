#!/usr/bin/env python3
"""
Editorial Allure Prompt Auditor & Translator
扫描 AI 图像/视频提示词中的高危拦截词（Gate 1: Prompt Filter），
评估后置露肤度缓解措施与动作风险（Gate 2: Output Classifier），
并根据目标平台（Google Flow / GPT / Grok）提供高定时尚与电影镜头转译建议。
"""

import argparse
import json
import re
import sys
from typing import Dict, List, Tuple

# 八维高危词与高定转译映射表
RED_FLAG_LEXICON: Dict[str, Tuple[str, List[str]]] = {
    # 1. 整体氛围与美学定性 (Mood & Framing)
    r"\bsexy\b": ("整体氛围", ["alluring", "captivating", "high-fashion editorial"]),
    r"\bhot\b": ("整体氛围", ["magnetic", "striking", "Vogue editorial style"]),
    r"\berotic\b": ("整体氛围", ["sultry mood", "intimate cinematic atmosphere"]),
    r"\bsensual\b": ("整体氛围", ["sultry", "languid elegance", "captivating mood"]),
    r"\bseductive\b": ("整体氛围", ["alluring", "enigmatic gaze", "captivating"]),
    r"\bnsfw\b": ("整体氛围", ["high-fashion editorial", "moody cinema still"]),
    r"\bporn\w*\b": ("整体氛围", ["cinematic editorial", "arthouse cinema still"]),
    r"\bfetish\b": ("整体氛围", ["Helmut Newton inspired avant-garde editorial", "sculpted haute couture"]),
    r"\bbedroom eyes\b": ("整体氛围", ["enigmatic magnetic gaze", "languid expression"]),
    # 2. 领口、背部与肩线 (Neckline & Back)
    r"\bcleavage\b": ("领口与肩线", ["deep architectural neckline", "collarbone contour", "soft cowl-neck drape"]),
    r"\blow-cut\b": ("领口与肩线", ["deep architectural V-neckline", "sculpted sweetheart neckline"]),
    r"\bunderboob\b": ("领口与肩线", ["structured couture bodice", "geometric keyhole cutout"]),
    r"\bsideboob\b": ("领口与肩线", ["draped open-back cut", "armhole couture tailoring"]),
    r"\btopless\b": ("领口与肩线", ["off-the-shoulder silk drape", "backless evening gown"]),
    # 3. 服装剪裁与角色制服 (Wardrobe & Archetypes)
    r"\blingerie\b": ("服装与剪裁", ["tailored satin corset top", "structured bustier bodice", "silk slip dress"]),
    r"\bbikini\b": ("服装与剪裁", ["sleek one-piece designer swimsuit with a loosely draped white linen shirt", "resort wear"]),
    r"\brevealing\b": ("服装与剪裁", ["form-fitting", "architectural cut", "draped backless cut"]),
    r"\bskimpy\b": ("服装与剪裁", ["tailored", "off-the-shoulder silk slip", "sculpted silhouette"]),
    r"\bsee-through\b": ("服装与剪裁", ["sheer silk organza layering", "draped liquid satin"]),
    r"\bbra\b": ("服装与剪裁", ["tailored corset top", "structured couture bodice"]),
    r"\bpanties\b": ("服装与剪裁", ["high-waisted tailored resort shorts", "asymmetric wrap skirt"]),
    r"\bunderwear\b": ("服装与剪裁", ["silk loungewear set", "tailored resort wear"]),
    r"\bskin-tight\b": ("服装与剪裁", ["form-fitting bias-cut silk", "fine-gauge ribbed knitwear"]),
    r"\bbodycon\b": ("服装与剪裁", ["form-fitting bias-cut satin dress", "sculpted couture silhouette"]),
    r"\bfrench maid\b": ("角色制服转译", ["avant-garde haute couture gothic ensemble with Chantilly lace trim"]),
    r"\bmaid outfit\b": ("角色制服转译", ["haute couture monochrome ensemble with delicate Chantilly lace ruffles"]),
    r"\bnaughty schoolgirl\b": ("角色制服转译", ["tailored preppy editorial ensemble with pleated wool skirt"]),
    # 4. 下装、裤袜与鞋履 (Lower Body & Hosiery)
    r"\bthong\b": ("腿部与下装", ["high-slit maxi skirt", "tailored high-waisted shorts"]),
    r"\bshort skirt\b": ("腿部与下装", ["high-slit floor-length maxi skirt", "asymmetric silk wrap skirt"]),
    r"\bmini skirt\b": ("腿部与下装", ["high-slit maxi skirt", "tailored resort shorts"]),
    r"\bbooty shorts\b": ("腿部与下装", ["tailored high-waisted resort shorts", "draped linen shorts"]),
    r"\bstockings\b": ("腿部与下装", ["sheer dark hosiery", "ultra-sheer 10-denier black tights"]),
    r"\bgarter belt\b": ("腿部与下装", ["Chantilly lace-trimmed sheer dark hosiery", "editorial legwear"]),
    r"\bfishnets\b": ("腿部与下装", ["patterned sheer dark hosiery", "textured editorial tights"]),
    # 5. 身体轮廓与姿态 (Silhouette & Pose)
    r"\bcurvy\b": ("身体与姿态", ["sculpted hourglass silhouette", "statuesque proportions"]),
    r"\bbusty\b": ("身体与姿态", ["sculpted silhouette", "structured haute couture bodice"]),
    r"\bvoluptuous\b": ("身体与姿态", ["statuesque proportions", "sculpted silhouette"]),
    r"\bprovocative pose\b": ("身体与姿态", ["contrapposto editorial stance", "looking back over her shoulder", "dynamic fashion pose"]),
    r"\bprovocative\b": ("身体与姿态", ["confident", "poised", "magnetic"]),
    r"\barching back\b": ("身体与姿态", ["contrapposto stance", "leaning against a minimalist architectural wall"]),
    r"\bspreading legs\b": ("身体与姿态", ["reclining with languid elegance on a chaise lounge", "poised seated posture"]),
    r"\bbending over\b": ("身体与姿态", ["leaning gracefully over a modernist balustrade", "subtle forward torso tilt"]),
    r"\bstraddling\b": ("身体与姿态", ["leaning gracefully beside on a chaise lounge", "sharing an enigmatic gaze at close proximity"]),
    # 6. 皮肤与水光质感 (Skin & Luminance)
    r"\bnaked skin\b": ("皮肤与质感", ["sun-kissed skin", "dewy complexion"]),
    r"\bnaked\b": ("皮肤与质感", ["draped in silk", "sun-kissed complexion"]),
    r"\bbare body\b": ("皮肤与质感", ["sculpted silhouette in chiaroscuro lighting", "golden hour glow on collarbone"]),
    r"\bwet body\b": ("皮肤与质感", ["sun-kissed skin with wet tousled hair", "dewy skin texture"]),
    r"\bsweaty\b": ("皮肤与质感", ["dewy complexion", "shimmering skin texture in warm light"]),
    r"\boiled\b": ("皮肤与质感", ["dewy glass-skin sheen", "warm golden-hour highlight on collarbone"]),
}

# 五段式公式要素检测关键词
FORMULA_SIGNALS: Dict[str, List[str]] = {
    "1_editorial_framing": [
        "editorial", "vogue", "campaign", "cinematic", "cinema still", "fashion", "portrait", "noir"
    ],
    "2_pose_and_expression": [
        "smile", "gaze", "looking", "shoulder", "posture", "stance", "contrapposto", "leaning",
        "reclining", "poised", "confident", "breeze", "hair", "languid"
    ],
    "3_tailored_wardrobe": [
        "silk", "satin", "linen", "dress", "gown", "corset", "bodice", "skirt", "hosiery",
        "tights", "swimsuit", "blazer", "knit", "cashmere", "form-fitting", "tailored",
        "draped", "backless", "halter", "camisole", "velvet"
    ],
    "4_lighting_and_shadow": [
        "light", "lighting", "chiaroscuro", "rim", "shadow", "candlelight", "golden hour",
        "neon", "sunlight", "glow", "reflections", "blinds", "dappled"
    ],
    "5_camera_and_film": [
        "35mm", "portra", "hasselblad", "85mm", "50mm", "shallow depth of field",
        "leica", "anamorphic", "film", "medium format", "grain", "cinestill", "vision3"
    ],
}

# Gate 2 后置露肤度缓解特征（物理遮蔽与切割技术）
GATE2_MITIGATIONS: Dict[str, List[str]] = {
    "shadow_masking": ["chiaroscuro", "shadow", "low-key", "venetian blind", "dappled", "dark", "moody"],
    "layered_draping": ["loosely draped", "linen shirt", "cardigan", "organza", "wrap", "blazer", "maxi skirt"],
    "framing_control": ["medium close-up", "waist up", "shallow depth of field", "collarbone", "foreground bokeh"],
}

# Google Flow 动态高危动作词
FLOW_MOTION_RISKS = [
    r"\bdancing\b", r"\btwerk\w*\b", r"\bswaying hips\b", r"\bunbutton\w*\b",
    r"\bundress\w*\b", r"\bshaking\b", r"\bgrind\w*\b"
]


def audit_prompt(prompt: str, platform: str = "flow") -> dict:
    """对输入提示词进行双层安全关卡审计、五段式结构评分与后置缓解评估。"""
    hits = []
    rewritten = prompt

    for pattern, (category, replacements) in RED_FLAG_LEXICON.items():
        matches = list(re.finditer(pattern, prompt, flags=re.IGNORECASE))
        if matches:
            matched_words = sorted({m.group(0) for m in matches})
            hits.append({
                "category": category,
                "matched": matched_words,
                "recommended_replacements": replacements,
            })
            rewritten = re.sub(pattern, replacements[0], rewritten, flags=re.IGNORECASE)

    lower_prompt = prompt.lower()
    formula_coverage = {}
    missing_sections = []
    for section, keywords in FORMULA_SIGNALS.items():
        matched_kw = [kw for kw in keywords if kw in lower_prompt]
        formula_coverage[section] = matched_kw
        if not matched_kw:
            missing_sections.append(section)

    # 评估 Gate 2 物理遮蔽与露肤度控制特征
    active_mitigations = {}
    for m_type, keywords in GATE2_MITIGATIONS.items():
        found = [kw for kw in keywords if kw in lower_prompt]
        if found:
            active_mitigations[m_type] = found

    platform_warnings = []
    if platform == "flow":
        if not formula_coverage["4_lighting_and_shadow"]:
            platform_warnings.append(
                "[Google Flow] 缺少明确的光影遮蔽词（如 Chiaroscuro lighting / Rim lighting），容易因画面露肤占比过高触发后置拦截。"
            )
        if not active_mitigations:
            platform_warnings.append(
                "[Google Flow] 未检测到后置露肤缓解技术（暗部遮蔽 / 半搭叠穿 / 中近景控制），若生成全身照极易在 90% 进度时报 Sexual or suggestive content。"
            )
        for motion_pat in FLOW_MOTION_RISKS:
            if re.search(motion_pat, prompt, flags=re.IGNORECASE):
                platform_warnings.append(
                    f"[Google Flow] 检测到高危大幅度动作词 ({motion_pat})，极易触发 Veo 动态姿态拦截，建议改为 Slow push-in camera movement 或 Looking over the shoulder。"
                )
        if re.search(r"\bswimsuit\b|\bswimwear\b|\bboudoir\b", prompt, flags=re.IGNORECASE) and "draped" not in lower_prompt:
            platform_warnings.append(
                "[Google Flow] 检测到独立泳装/私房类词汇且无外搭遮蔽；建议叠加 loosely draped white linen shirt 或改用修身晚礼服。"
            )
    elif platform == "gpt":
        if not formula_coverage["1_editorial_framing"]:
            platform_warnings.append(
                "[GPT Image] 缺少商业/艺术杂志语境定性（如 Vogue campaign / High-fashion editorial），GPT 容易触发意图猜测并把衣服强行改厚。"
            )
    elif platform == "grok":
        if not formula_coverage["5_camera_and_film"]:
            platform_warnings.append(
                "[Grok Imagine] 缺少胶片与镜头质感词（如 Shot on 35mm film, Kodak Portra 400, unretouched skin texture），生成画面容易出现廉价网红塑料感。"
            )

    passed = len(hits) == 0 and len(platform_warnings) == 0
    return {
        "status": "PASS" if passed else ("FAIL_RED_FLAGS" if hits else "WARN_STRUCTURE"),
        "platform": platform,
        "red_flag_count": len(hits),
        "red_flags": hits,
        "missing_formula_sections": missing_sections,
        "gate2_mitigations": active_mitigations,
        "platform_warnings": platform_warnings,
        "suggested_rewrite": rewritten,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="审计并转译时尚/电影感提示词，规避 Google Flow / GPT / Grok 安全拦截。"
    )
    parser.add_argument("--prompt", "-p", required=True, help="待检测的英文或中英混合提示词")
    parser.add_argument(
        "--platform",
        choices=["flow", "gpt", "grok"],
        default="flow",
        help="目标生成平台 (默认: flow)",
    )
    parser.add_argument("--json", action="store_true", help="以 JSON 格式输出结果")
    args = parser.parse_args()

    result = audit_prompt(args.prompt, args.platform)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["red_flag_count"] == 0 else 1

    print(f"=== Editorial Allure Prompt Audit [{result['platform'].upper()}] ===")
    print(f"状态: {result['status']}")

    if result["red_flags"]:
        print("\n[Gate 1] 发现极易触发前置拦截的高危词:")
        for item in result["red_flags"]:
            words = ", ".join(item["matched"])
            repls = " / ".join(item["recommended_replacements"])
            print(f"  - [{item['category']}] 命中: '{words}' -> 建议替换为: {repls}")
        print("\n[Gate 1] 自动降敏替换草稿:")
        print(f"  {result['suggested_rewrite']}")
    else:
        print("\n[Gate 1] 未发现前置黑名单高危词 (Passed)。")

    if result["gate2_mitigations"]:
        mit_keys = ", ".join(result["gate2_mitigations"].keys())
        print(f"[Gate 2] 已激活后置露肤缓解策略: {mit_keys}")

    if result["missing_formula_sections"]:
        print("\n[Formula] 五段式公式缺失维度:")
        for sec in result["missing_formula_sections"]:
            print(f"  - 缺少: {sec}")

    if result["platform_warnings"]:
        print("\n[Platform] 平台针对性优化建议:")
        for warn in result["platform_warnings"]:
            print(f"  - {warn}")

    return 0 if result["red_flag_count"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
