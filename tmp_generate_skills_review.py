import re
from collections import Counter

import pandas as pd


MODULES_CSV = "data/2025-2026_module_clean_with_prereq_skillsfuture.csv"
SKILLS_CSV = "data/skills_taxo.csv"
OUTPUT_MD = "abc_skills_review.md"


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "based",
    "by",
    "consideration",
    "create",
    "creates",
    "cross",
    "defined",
    "develop",
    "developed",
    "developing",
    "develops",
    "different",
    "each",
    "elements",
    "ensure",
    "ensuring",
    "for",
    "from",
    "in",
    "include",
    "includes",
    "including",
    "information",
    "into",
    "is",
    "it",
    "its",
    "level",
    "levels",
    "manage",
    "manages",
    "method",
    "methods",
    "need",
    "needs",
    "new",
    "of",
    "on",
    "or",
    "other",
    "our",
    "overall",
    "perform",
    "performs",
    "provide",
    "provides",
    "related",
    "requirements",
    "review",
    "reviews",
    "service",
    "services",
    "solution",
    "solutions",
    "stage",
    "stages",
    "standard",
    "standards",
    "support",
    "supports",
    "such",
    "system",
    "systems",
    "that",
    "the",
    "their",
    "them",
    "these",
    "this",
    "through",
    "to",
    "tool",
    "tools",
    "use",
    "used",
    "user",
    "users",
    "using",
    "various",
    "which",
    "will",
    "with",
    "within",
    "work",
    "working",
    "works",
}

NORMALIZE_MAP = {
    "analytics": "analysis",
    "analytical": "analysis",
    "analyse": "analysis",
    "analyzed": "analysis",
    "analyzing": "analysis",
    "modelling": "model",
    "modeling": "model",
    "models": "model",
    "optimisation": "optimize",
    "optimization": "optimize",
    "optimised": "optimize",
    "optimiseds": "optimize",
    "optimising": "optimize",
    "optimized": "optimize",
    "applications": "application",
    "architectures": "architecture",
    "auditing": "audit",
    "branding": "brand",
    "communications": "communication",
    "communicative": "communication",
    "computing": "compute",
    "controls": "control",
    "customers": "customer",
    "consumers": "consumer",
    "coding": "code",
    "financial": "finance",
    "forecasting": "forecast",
    "plans": "plan",
    "processes": "process",
    "programming": "program",
    "simulations": "simulation",
    "strategies": "strategy",
    "visualisation": "visualization",
    "visualisations": "visualization",
}

PHRASE_HINTS = {
    "ai": ["artificial intelligence", "machine learning", "large language models", "llms"],
    "analysis": ["analysis", "analytics", "analyse", "analyze"],
    "application": ["application", "applications", "app"],
    "architecture": ["architecture"],
    "audit": ["audit", "auditing"],
    "brand": ["brand", "branding"],
    "code": ["coding", "programming"],
    "communication": ["communication", "communications"],
    "control": ["control", "controls"],
    "data": ["data"],
    "design": ["design", "designing"],
    "finance": ["finance", "financial"],
    "forecast": ["forecast", "forecasting"],
    "governance": ["governance"],
    "market": ["market", "marketing"],
    "model": ["model", "models", "modelling", "modeling", "simulation", "forecasting"],
    "pattern": ["pattern", "patterns"],
    "plan": ["plan", "planning"],
    "process": ["process", "processes"],
    "product": ["product", "products", "new product"],
    "program": ["program", "programming", "coding", "computing"],
    "project": ["project", "capstone"],
    "quality": ["quality"],
    "research": ["research"],
    "risk": ["risk"],
    "security": ["security", "cybersecurity", "authentication"],
    "software": ["software"],
    "strategy": ["strategy", "strategic"],
    "supply": ["supply", "supply chain"],
    "system": ["system", "systems"],
    "test": ["test", "testing"],
    "text": ["text"],
    "visualization": ["visualisation", "visualization"],
}

MODULE_FAMILY_KEYWORDS = {
    "finance": {
        "accounting",
        "asset",
        "audit",
        "assurance",
        "bank",
        "capital",
        "cash",
        "compliance",
        "derivative",
        "finance",
        "fraud",
        "investment",
        "portfolio",
        "risk",
        "security",
        "trading",
        "transaction",
        "valuation",
    },
    "marketing": {
        "advertising",
        "brand",
        "consumer",
        "crm",
        "customer",
        "digital",
        "ecommerce",
        "market",
        "marketing",
        "media",
        "position",
        "pricing",
        "product",
        "retail",
        "sales",
        "segment",
        "target",
    },
    "data": {
        "ai",
        "algorithm",
        "analysis",
        "analytics",
        "compute",
        "data",
        "forecast",
        "inference",
        "intelligence",
        "learning",
        "llm",
        "machine",
        "mining",
        "model",
        "nlp",
        "pattern",
        "predict",
        "prompt",
        "statistical",
        "statistics",
        "text",
        "visualization",
    },
    "software": {
        "agile",
        "application",
        "architecture",
        "authentication",
        "cloud",
        "code",
        "coding",
        "database",
        "debug",
        "devops",
        "file",
        "kernel",
        "linux",
        "memory",
        "operating",
        "os",
        "program",
        "software",
        "system",
        "testing",
        "unix",
        "windows",
    },
    "engineering": {
        "assembly",
        "chemical",
        "control",
        "design",
        "engineering",
        "experiment",
        "facility",
        "lab",
        "laboratory",
        "manufacturing",
        "material",
        "monitor",
        "optimise",
        "optimize",
        "plant",
        "process",
        "production",
        "site",
        "technical",
    },
    "research": {
        "community",
        "investigation",
        "methodology",
        "proposal",
        "qualitative",
        "quantitative",
        "research",
        "study",
    },
    "project": {
        "capstone",
        "coordination",
        "feasibility",
        "project",
        "stakeholder",
    },
    "supply_chain": {
        "fulfilment",
        "fulfillment",
        "inventory",
        "logistics",
        "operation",
        "operations",
        "procurement",
        "scm",
        "scheduling",
        "slot",
        "sourcing",
        "supplier",
        "supply",
        "warehouse",
    },
    "real_estate": {
        "asset",
        "building",
        "estate",
        "facility",
        "facilities",
        "property",
        "real",
        "site",
    },
    "people": {
        "caregiver",
        "client",
        "communication",
        "community",
        "employee",
        "ethic",
        "governance",
        "human",
        "integrity",
        "learning",
        "policy",
        "professional",
        "stakeholder",
        "training",
    },
}

PREFIX_FAMILIES = {
    "ACC": {"finance"},
    "BT": {"data"},
    "CLC": {"research", "people"},
    "CN": {"engineering", "data"},
    "CP": {"research", "data", "software"},
    "CS": {"software", "data"},
    "DAO": {"supply_chain", "software"},
    "DBA": {"data", "finance"},
    "DOS": {"supply_chain", "data"},
    "DSA": {"data"},
    "DSC": {"data", "project", "supply_chain"},
    "DSE": {"data", "finance"},
    "EE": {"data", "engineering"},
    "EG": {"engineering", "project"},
    "ESE": {"engineering", "research"},
    "FIN": {"finance"},
    "ID": {"engineering", "research"},
    "IE": {"engineering", "data"},
    "IPM": {"project", "finance", "real_estate"},
    "IS": {"software", "data", "project"},
    "LSM": {"research", "data"},
    "ME": {"engineering"},
    "MKT": {"marketing"},
    "MNO": {"people"},
    "NM": {"research", "people"},
    "PF": {"project", "engineering", "real_estate"},
    "PL": {"research", "data"},
    "QF": {"finance", "data"},
    "RE": {"real_estate", "finance"},
    "SA": {"software", "data"},
    "ST": {"data", "software"},
    "TR": {"engineering", "project"},
}

HARD_MISMATCH_DOMAINS = {
    "aviation": {"aircraft", "airline", "airport", "slot"},
    "biopharma": {"biopharmaceutical", "biologics", "drug", "pharmaceutical"},
    "education": {"classroom", "curriculum", "learner", "school", "teaching"},
    "game_media": {"animation", "camera", "film", "gameplay", "immersive", "vfx"},
    "healthcare": {"caregiver", "clinical", "medical", "patient"},
    "hr": {"employee", "hr", "talent", "workforce"},
    "marine": {"conversion", "offshore", "rig", "ship", "vessel"},
    "retail": {"merchandise", "retail"},
}

DOMAIN_LABELS = {
    "aviation": "aviation operations",
    "biopharma": "biopharmaceutical manufacturing",
    "education": "education-specific practice",
    "game_media": "VFX / game media production",
    "healthcare": "healthcare delivery",
    "hr": "HR operations",
    "marine": "ships / rigs control systems",
    "retail": "retail operations",
}

ADJACENT_FAMILIES = {
    "data": {"finance", "marketing", "research", "software", "engineering"},
    "engineering": {"data", "project", "supply_chain"},
    "finance": {"data", "marketing", "real_estate", "project"},
    "marketing": {"data", "finance"},
    "people": {"project", "research"},
    "project": {"engineering", "finance", "real_estate", "software"},
    "real_estate": {"finance", "project", "engineering"},
    "research": {"data", "people"},
    "software": {"data", "project"},
    "supply_chain": {"engineering", "project", "data"},
}

PAIR_OVERRIDES = {
    ("BT4222", "Website Design"): ("remove", "The module is about mining and analysing web data, not designing websites or user interfaces."),
    ("CS1010", "Programming and Coding"): ("manual review", "The module clearly teaches programming fundamentals, but the taxonomy description is tied to VFX production rather than general coding."),
    ("CS1010E", "Programming and Coding"): ("manual review", "The module clearly teaches programming fundamentals, but the taxonomy description is tied to VFX production rather than general coding."),
    ("CS1010J", "Programming and Coding"): ("manual review", "The module clearly teaches programming fundamentals, but the taxonomy description is tied to VFX production rather than general coding."),
    ("CS1010", "Programme Evaluation"): ("remove", "The module covers introductory programming and debugging, not evaluating organisational or educational programmes."),
    ("CS1010E", "Programme Evaluation"): ("remove", "The module covers introductory programming and debugging, not evaluating organisational or educational programmes."),
    ("CS1010J", "Programme Evaluation"): ("remove", "The module covers introductory programming and debugging, not evaluating organisational or educational programmes."),
    ("CN4245R", "Control System Programming"): ("remove", "The module covers process characterisation and data-based modelling; the taxonomy definition is specific to ships and rigs control logic."),
    ("DSC4213", "Trend Forecasting"): ("keep", "The description explicitly includes forecasting and using analytical tools to predict business outcomes, so this skill is directly supported."),
    ("IS4108", "Artificial Intelligence Application"): ("keep", "The module is explicitly about building business AI solutions integrated with software applications."),
    ("IS4108", "Governance"): ("keep", "The description directly mentions AI governance as part of the capstone solutioning lifecycle."),
}


def split_skills(value):
    if pd.isna(value):
        return []
    return [part.strip() for part in str(value).split("|") if part.strip()]


def normalize_token(token):
    token = re.sub(r"[^a-z0-9]+", "", token.lower())
    if not token:
        return ""
    token = NORMALIZE_MAP.get(token, token)
    if len(token) > 4 and token.endswith("ies"):
        token = token[:-3] + "y"
    elif len(token) > 5 and token.endswith("ing"):
        token = token[:-3]
    elif len(token) > 4 and token.endswith("ed"):
        token = token[:-2]
    elif len(token) > 4 and token.endswith("es"):
        token = token[:-2]
    elif len(token) > 3 and token.endswith("s"):
        token = token[:-1]
    return NORMALIZE_MAP.get(token, token)


def tokenize(text):
    return [normalize_token(tok) for tok in re.findall(r"[A-Za-z0-9]+", str(text)) if normalize_token(tok)]


def slug_prefix(module_code):
    match = re.match(r"[A-Za-z]+", module_code)
    return match.group(0) if match else ""


def detect_families(text, module_code=""):
    tokens = set(tokenize(text))
    families = set()
    for family, words in MODULE_FAMILY_KEYWORDS.items():
        if tokens & words:
            families.add(family)
    families |= PREFIX_FAMILIES.get(slug_prefix(module_code), set())
    return families


def detect_mismatch_domains(text):
    tokens = set(tokenize(text))
    domains = set()
    for domain, words in HARD_MISMATCH_DOMAINS.items():
        if tokens & words:
            domains.add(domain)
    return domains


def title_tokens(skill_title):
    return [tok for tok in tokenize(skill_title) if tok and tok not in STOPWORDS]


def get_display_matches(skill_title, matched_norm_tokens):
    words = []
    for raw in re.findall(r"[A-Za-z0-9]+", skill_title):
        if normalize_token(raw) in matched_norm_tokens:
            words.append(raw)
    return words


def family_adjacent(skill_families, module_families):
    for family in skill_families:
        if module_families & ADJACENT_FAMILIES.get(family, set()):
            return True
    return False


def escape_md(text):
    text = str(text).replace("\n", " ").strip()
    return text.replace("|", "\\|")


def oxford_join(items):
    items = [item for item in items if item]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


modules_df = pd.read_csv(MODULES_CSV).fillna("")
skills_df = pd.read_csv(SKILLS_CSV).fillna("")
skill_desc_map = dict(zip(skills_df["parent_skill_title"], skills_df["parent_skill_description"]))
valid_skill_titles = set(skill_desc_map)

modules_df["skill_list"] = modules_df["extracted_skills"].apply(split_skills)
modules_df["skill_count"] = modules_df["skill_list"].apply(len)
qualifying = modules_df[modules_df["skill_count"] >= 10].copy()

all_module_docs = []
for _, row in modules_df.iterrows():
    all_module_docs.append(set(tokenize(f"{row['title']} {row['description']}")))

doc_frequency = Counter()
for doc_tokens in all_module_docs:
    doc_frequency.update(doc_tokens)

rare_cutoff = max(2, int(len(all_module_docs) * 0.01))


def evaluate_skill(module_row, skill_title):
    module_code = module_row["moduleCode"]
    if (module_code, skill_title) in PAIR_OVERRIDES:
        decision, rationale = PAIR_OVERRIDES[(module_code, skill_title)]
        return {
            "skill": skill_title,
            "skill_description": skill_desc_map[skill_title],
            "decision": decision,
            "rationale": rationale,
        }

    module_text = f"{module_row['title']} {module_row['description']}"
    module_title_text = module_row["title"]
    skill_desc = skill_desc_map[skill_title]

    module_tokens = set(tokenize(module_text))
    module_title_tokens = set(tokenize(module_title_text))
    skill_title_norm = title_tokens(skill_title)
    skill_desc_tokens = [tok for tok in tokenize(skill_desc) if tok and tok not in STOPWORDS]
    skill_desc_token_set = set(skill_desc_tokens)

    matched_title = set()
    matched_in_title = set()
    module_text_lower = module_text.lower()
    for token in skill_title_norm:
        hints = PHRASE_HINTS.get(token, [token])
        if token in module_tokens or any(hint in module_text_lower for hint in hints):
            matched_title.add(token)
        if token in module_title_tokens:
            matched_in_title.add(token)

    title_ratio = len(matched_title) / max(1, len(skill_title_norm))
    module_title_ratio = len(matched_in_title) / max(1, len(skill_title_norm))
    desc_overlap = skill_desc_token_set & module_tokens
    desc_ratio = len(desc_overlap) / max(1, len(skill_desc_token_set))

    module_families = detect_families(module_text, module_code)
    skill_families = detect_families(f"{skill_title} {skill_desc}")
    aligned_families = module_families & skill_families
    adjacent = family_adjacent(skill_families, module_families)

    mismatch_domains = detect_mismatch_domains(skill_desc) - detect_mismatch_domains(module_text)
    rare_missing = sorted(
        {
            tok
            for tok in skill_desc_token_set
            if doc_frequency.get(tok, 0) <= rare_cutoff and tok not in module_tokens and tok not in skill_title_norm and len(tok) > 3
        }
    )

    severe_mismatch = bool(mismatch_domains) or (len(rare_missing) >= 4 and not aligned_families)
    moderate_support = (
        title_ratio >= 0.5
        or module_title_ratio > 0
        or desc_ratio >= 0.18
        or (aligned_families and (title_ratio >= 0.33 or desc_ratio >= 0.1))
        or adjacent
    )
    strong_support = (
        module_title_ratio >= 0.5
        or (aligned_families and title_ratio >= 0.75)
        or (aligned_families and title_ratio >= 0.5 and desc_ratio >= 0.2)
        or (title_ratio >= 0.75 and desc_ratio >= 0.15 and not severe_mismatch)
    )

    if strong_support and aligned_families and not severe_mismatch:
        decision = "keep"
    elif strong_support and severe_mismatch:
        decision = "manual review"
    elif aligned_families and (title_ratio >= 0.5 or desc_ratio >= 0.22) and not severe_mismatch:
        decision = "keep"
    elif not moderate_support and (severe_mismatch or (title_ratio == 0 and desc_ratio < 0.12 and not aligned_families and not adjacent)):
        decision = "remove"
    elif severe_mismatch and title_ratio < 0.5 and desc_ratio < 0.1 and not aligned_families:
        decision = "remove"
    elif moderate_support:
        decision = "manual review"
    else:
        decision = "remove"

    display_matches = get_display_matches(skill_title, matched_title)
    evidence_bits = []
    if module_title_ratio >= 0.5:
        evidence_bits.append("the module title itself aligns closely")
    elif display_matches:
        evidence_bits.append(f"the description overlaps with {oxford_join(display_matches[:3])}")

    if aligned_families:
        evidence_bits.append(f"the skill fits the module's {oxford_join(sorted(aligned_families))} focus")

    mismatch_text = ""
    if mismatch_domains:
        mismatch_text = oxford_join([DOMAIN_LABELS[name] for name in sorted(mismatch_domains)])

    if decision == "keep":
        if evidence_bits:
            rationale = f"{oxford_join(evidence_bits)}."
        else:
            rationale = "The module description directly supports this skill."
    elif decision == "manual review":
        if mismatch_text:
            rationale = (
                f"There is some support from the module text, but the taxonomy description is more specific to "
                f"{mismatch_text} than the module description states."
            )
        elif evidence_bits:
            rationale = f"{oxford_join(evidence_bits)}, but the evidence is indirect rather than fully explicit."
        else:
            rationale = "The skill is plausible, but the module description does not support it confidently enough to keep outright."
    else:
        if mismatch_text:
            rationale = f"The taxonomy description is oriented to {mismatch_text}, which is not supported by the module description."
        elif title_ratio == 0 and desc_ratio < 0.12:
            rationale = "Neither the module title nor the description directly supports this skill."
        else:
            rationale = "The overlap is too weak to justify keeping this skill for the module."

    return {
        "skill": skill_title,
        "skill_description": skill_desc,
        "decision": decision,
        "rationale": rationale,
    }


lines = [
    "# Skills Review Report",
    "",
    "Scope: modules in `data/2025-2026_module_clean_with_prereq_skillsfuture.csv` with `10` or more extracted skills, reviewed against exact `parent_skill_title` matches in `data/skills_taxo.csv`.",
    "",
]

reviewed_module_count = 0
decision_counter = Counter()

for _, module_row in qualifying.sort_values(["moduleCode", "title"]).iterrows():
    matched_skills = [skill for skill in module_row["skill_list"] if skill in valid_skill_titles]
    if not matched_skills:
        continue

    reviewed_module_count += 1
    evaluations = [evaluate_skill(module_row, skill) for skill in matched_skills]
    keep_skills = [item["skill"] for item in evaluations if item["decision"] == "keep"]
    manual_skills = [item["skill"] for item in evaluations if item["decision"] == "manual review"]

    for item in evaluations:
        decision_counter[item["decision"]] += 1

    lines.append(f"## {module_row['moduleCode']} {module_row['title']}")
    lines.append("")
    lines.append(f"Module description: {module_row['description']}")
    lines.append("")
    lines.append(f"Original extracted skills: {module_row['extracted_skills']}")
    lines.append("")
    lines.append("| Skill | Skill Description | Decision | Rationale |")
    lines.append("| --- | --- | --- | --- |")
    for item in evaluations:
        lines.append(
            f"| {escape_md(item['skill'])} | {escape_md(item['skill_description'])} | {item['decision']} | {escape_md(item['rationale'])} |"
        )
    lines.append("")
    lines.append(f"Proposed cleaned skills: {', '.join(keep_skills) if keep_skills else 'None'}")
    lines.append("")
    lines.append(f"Manual review skills: {', '.join(manual_skills) if manual_skills else 'None'}")
    lines.append("")

lines.append("## Aggregate Summary")
lines.append("")
lines.append(f"- Number of reviewed modules: {reviewed_module_count}")
lines.append(f"- Reviewed exact-match skills: {sum(decision_counter.values())}")
lines.append(f"- Keep decisions: {decision_counter['keep']}")
lines.append(f"- Manual review decisions: {decision_counter['manual review']}")
lines.append(f"- Remove decisions: {decision_counter['remove']}")
lines.append("")

with open(OUTPUT_MD, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines))

print(f"Wrote {OUTPUT_MD} with {reviewed_module_count} reviewed modules.")
