#!/usr/bin/env python3
"""Static invariant tests for the Dopamine 2.0 design harness.

The harness is instruction files, not code, so these tests check the things that
actually break it: dangling references, stage-gate chains that don't line up,
design-system constants that drift apart between files, and protocol rules that
one file states and another quietly contradicts.

Run:  python3 tests/test_harness.py
Exit: 0 all pass, 1 any failure.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / ".claude/skills/dopamine"
REF = SKILL / "reference"

RESULTS = []


def check(name, condition, detail=""):
    RESULTS.append((name, bool(condition), detail))


def read(p):
    return (ROOT / p).read_text() if not Path(p).is_absolute() else Path(p).read_text()


def all_md():
    """Every markdown file that makes up the harness."""
    return (
        [SKILL / "SKILL.md", ROOT / "CLAUDE.md", ROOT / "README.md"]
        + sorted(REF.glob("*.md"))
        + sorted((REF / "ideate").glob("*.md"))
    )


def corpus():
    return {p: p.read_text() for p in all_md()}


C = corpus()
BLOB = "\n".join(C.values())


# --------------------------------------------------------------------------
# 1. Structure — references resolve, nothing orphaned, nothing undocumented
# --------------------------------------------------------------------------

REF_PATTERN = re.compile(r"`?(?:\.\./)?(?:reference/)?(ideate/[a-z-]+\.md|[a-z-]+\.md)`?")


def test_references_resolve():
    missing = set()
    for path, text in C.items():
        for m in REF_PATTERN.finditer(text):
            target = m.group(1)
            if target in ("SKILL.md", "CLAUDE.md", "README.md", "PRODUCT.md",
                          "WIREFRAME.md", "DESIGN_DECISIONS.md"):
                continue
            if (ROOT / "tests" / target).exists():  # tests/ docs, not references
                continue
            # a bare name inside reference/ideate/ may refer to a sibling
            candidates = [REF / target, REF / "ideate" / target]
            if not any(c.exists() for c in candidates):
                missing.add(f"{path.name} -> {target}")
    check("all internal references resolve", not missing, "; ".join(sorted(missing)))


def test_no_orphan_reference_files():
    """Every reference file must be reachable by name from another harness file."""
    orphans = []
    for p in sorted(REF.glob("*.md")) + sorted((REF / "ideate").glob("*.md")):
        name = p.name
        referrers = [q.name for q, t in C.items() if q != p and name in t]
        if not referrers:
            orphans.append(name)
    check("no orphaned reference files", not orphans, ", ".join(orphans))


def test_readme_documents_every_file():
    readme = C[ROOT / "README.md"]
    undocumented = []
    for p in sorted(REF.glob("*.md")) + sorted((REF / "ideate").glob("*.md")):
        rel = p.relative_to(SKILL).as_posix()  # reference/foo.md
        if rel not in readme:
            undocumented.append(rel)
    check("README documents every reference file", not undocumented, ", ".join(undocumented))


def test_readme_lists_no_phantom_files():
    readme = C[ROOT / "README.md"]
    phantoms = []
    for m in re.finditer(r"`(reference/(?:ideate/)?[a-z-]+\.md)`", readme):
        if not (SKILL / m.group(1)).exists():
            phantoms.append(m.group(1))
    check("README lists no phantom files", not phantoms, ", ".join(sorted(set(phantoms))))


# --------------------------------------------------------------------------
# 2. Stage gate chain — the artifact handoffs must line up end to end
# --------------------------------------------------------------------------

def test_stage_artifacts_consistent():
    ideate = C[REF / "ideate.md"]
    compose = C[REF / "compose.md"]
    polish = C[REF / "polish.md"]
    claude_md = C[ROOT / "CLAUDE.md"]
    check("ideate writes PRODUCT.md", "PRODUCT.md" in ideate)
    check("ideate writes WIREFRAME.md", "WIREFRAME.md" in ideate)
    check("compose gates on WIREFRAME.md", "WIREFRAME.md" in compose)
    check("polish writes DESIGN_DECISIONS.md", "DESIGN_DECISIONS.md" in polish)
    for art in ("PRODUCT.md", "WIREFRAME.md", "DESIGN_DECISIONS.md"):
        check(f"CLAUDE.md documents {art}", art in claude_md)


def test_ideate_names_next_stage():
    ideate = C[REF / "ideate.md"]
    check("ideate exit names /dopamine compose", "/dopamine compose" in ideate)


def test_polish_gate_rejects_broken_surface():
    polish = C[REF / "polish.md"]
    check("polish sends broken surfaces back to compose",
          "send" in polish.lower() and "compose" in polish)


def test_routing_covers_all_project_states():
    skill = C[SKILL / "SKILL.md"]
    rule = skill[skill.find("Routing rules"):]
    for state in ("No `PRODUCT.md`", "no `WIREFRAME.md`", "composed surface"):
        check(f"routing rule 1 handles: {state}", state in rule)


# --------------------------------------------------------------------------
# 3. Design-system constants — the DS-wins rule, mechanised
# --------------------------------------------------------------------------

def test_spacing_rhythm():
    check("4px rhythm stated", "4px rhythm" in BLOB)
    check("no competing 8px base rhythm", "8px base" not in BLOB)
    # the canonical scale must not drift
    scale = "0, 2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40"
    check("canonical spacing scale intact", scale in BLOB)


def test_touch_targets():
    check("48dp default stated", "48dp" in BLOB)
    check("high-stakes 48+12dp stated", "48+12dp" in BLOB)
    bad = re.findall(r"(?:at least|minimum)\s*`?4[04][-–]?4?4?px", BLOB)
    check("no sub-48dp touch target floor", not bad, str(bad))


def test_radii_set():
    check("canonical radii set intact", "0, 2, 4, 6, 8, 12, 16" in BLOB)


def test_brand_colour():
    corals = set(re.findall(r"#[fF]{2}5443", BLOB))
    check("brand coral consistent", len(corals) <= 1, str(corals))


def test_typography_rule():
    check("Cabinet Grotesk display-only >=24pt", "24pt" in BLOB and "Cabinet Grotesk" in BLOB)
    ip = C[REF / "interface-principles.md"]
    check("interface-principles type layer matches DS",
          "Cabinet Grotesk" in ip,
          "expressive type must be Cabinet Grotesk, not Figtree")


def test_viewport():
    check("360px viewport stated", "360" in BLOB)
    check("no other-device escape hatch", "unless another device" not in BLOB)


def test_wireframe_palette_consistent():
    wf = C[REF / "ideate" / "wireframe.md"]
    for hexval in ("#ffffff", "#f0f0f0", "#999999", "#333333", "#000000"):
        check(f"wireframe palette defines {hexval}", hexval in wf)


# --------------------------------------------------------------------------
# 4. Vocabulary — one name per concept, no leftovers from the earlier merge
# --------------------------------------------------------------------------

BRANCH_NAMES = ("Research not needed", "Move ahead with assumptions", "Stop for research first")
LEGACY_NAMES = ("Move forward", "Move carefully", "Learn first")


def test_branch_vocabulary():
    for n in BRANCH_NAMES:
        check(f"branch decision '{n}' present", n in BLOB)
    for n in LEGACY_NAMES:
        hits = [p.name for p, t in C.items() if n in t]
        check(f"no legacy mode name '{n}'", not hits, ", ".join(hits))


def test_exact_response_headings():
    ideate = C[REF / "ideate.md"]
    for h in ("Answer me few questions", "Shall I proceed with"):
        check(f"exact heading declared: {h}", h in ideate)
        used = [p.name for p, t in C.items() if h in t]
        check(f"heading '{h}' used in a phase file", len(used) > 1, ", ".join(used))


def test_no_scope_refusals():
    """The harness defers to a later stage; it never refuses design-system work."""
    banned = ["design-system conformance", "must not produce"]
    hits = []
    for p, t in C.items():
        for b in banned:
            if b in t:
                hits.append(f"{p.name}:{b}")
    check("no blanket scope refusals", not hits, ", ".join(hits))


# --------------------------------------------------------------------------
# 5. Protocol invariants — rules one file states that another could contradict
# --------------------------------------------------------------------------

def test_research_halt_is_enforced_everywhere():
    """'Stop for research first' must block artifacts in every file that could make one."""
    producers = ["ideate.md", "ideate/understand.md", "ideate/explore.md",
                 "ideate/frame.md", "ideate/read-input.md"]
    missing = []
    for rel in producers:
        p = REF / rel
        if "Stop for research first" not in p.read_text():
            missing.append(rel)
    check("research halt stated in every artifact-producing file", not missing, ", ".join(missing))


def test_consent_gate_present():
    check("consent gate in ideate router", "Consent gate" in C[REF / "ideate.md"])
    wf = C[REF / "ideate" / "wireframe.md"]
    check("wireframe requires explicit permission", "Entry permission" in wf)
    check("wireframe preflight is referenced", "wireframe-preflight.md" in wf)


def test_competitive_research_default_is_single_valued():
    """The source skill contradicted itself here; the harness must not."""
    cr = C[REF / "ideate" / "competitive-research.md"]
    router = C[REF / "ideate.md"]
    check("competitive-research defaults to skip", "Default to skipping" in cr)
    check("router agrees: default skip", "default to skip" in router.lower())
    check("router does not default to Run for healthcare",
          "default to **Run**" not in router)


def test_effort_brake_is_loaded():
    router = C[REF / "ideate.md"]
    check("effort-and-speed always loaded", "effort-and-speed.md" in router)
    eas = C[REF / "effort-and-speed.md"]
    check("wireframe state budget stated", "four essential" in eas)


def test_interface_principles_cross_stage():
    ip = C[REF / "interface-principles.md"]
    check("overriding bias stated", "beat delight" in ip.lower() or "beats delight" in ip.lower())
    check("interface-principles used by ideate", "interface-principles.md" in C[REF / "ideate.md"])
    check("interface-principles wired into polish", "interface-principles" in C[REF / "polish.md"],
          "polish.md has a parallel audit vocabulary that was never merged")


def test_stage1_accessibility_numbers_match_source():
    """Stage 1 asserts accessibility rules without loading accessibility.md.

    A behavioural run confirmed the agent never loads accessibility.md during
    Stage 1 (it is Stage 2's mandatory reference), yet wireframe.md's check list
    hardcodes touch-target and truncation rules. Those numbers must not drift
    from their source.
    """
    acc = C[REF / "accessibility.md"]
    wf = C[REF / "ideate" / "wireframe.md"]
    for constant in ("48dp", "48+12dp"):
        check(f"wireframe check agrees with accessibility.md on {constant}",
              constant in acc and constant in wf,
              f"{constant} present in accessibility.md={constant in acc}, wireframe.md={constant in wf}")
    check("wireframe check carries the truncation ban",
          "truncat" in wf.lower() and "truncat" in acc.lower())


def test_accessibility_hard_floor_alignment():
    """Every hard-floor topic in polish must exist in accessibility.md."""
    acc = C[REF / "accessibility.md"].lower()
    topics = ["contrast", "touch target", "focus", "screen reader",
              "text scaling", "truncat", "reduced-motion", "grade 7"]
    missing = [t for t in topics if t not in acc]
    check("polish hard floor is backed by accessibility.md", not missing, ", ".join(missing))


# --------------------------------------------------------------------------
# 6. Tooling — does the declared permission set cover what the protocol demands?
# --------------------------------------------------------------------------

def test_allowed_tools_cover_protocol():
    skill = C[SKILL / "SKILL.md"]
    fm = skill.split("---")[1]
    allowed = fm[fm.find("allowed-tools"):]

    # `MCP(...)` is invalid: Claude Code skips mcp__ rules written with parentheses,
    # and the server segment cannot be globbed. Must be mcp__<literal-server>__<tool|*>.
    check("no invalid MCP(...) permission syntax",
          not re.search(r"MCP\(", allowed),
          "MCP(...) is not valid allowed-tools syntax for MCP servers; use mcp__server__*")
    for entry in re.findall(r"mcp__[A-Za-z0-9_\-]+__\*?", allowed):
        check(f"MCP entry well-formed: {entry}", entry.count("__") >= 2)

    # Stage 1 mandates visually inspecting supplied boards and screenshots.
    needs_board = "read-input.md" in C[REF / "ideate.md"]
    check("board/Figma reading is permitted",
          not needs_board or "figma" in allowed.lower(),
          "read-input.md mandates opening Figma/FigJam frames, but allowed-tools grants no Figma MCP")

    # Stage 1 mandates one rendered visual verification of the HTML wireframe.
    needs_render = "rendered visual verification" in C[REF / "ideate" / "wireframe.md"]
    check("renderer/browser is permitted",
          not needs_render or "chrome" in allowed.lower(),
          "wireframe.md mandates rendered verification, but allowed-tools grants no browser tool")

    # Stage 2 needs a design-system MCP that actually exists in the user's config.
    check("a design-system MCP is granted",
          "dopamine" in allowed.lower(),
          "no Dopamine design-system MCP granted; Stage 2 cannot reach component APIs")

    # Phases edit existing artifacts (correction loops), not just create them.
    check("Edit tool permitted for correction loops",
          "Edit" in allowed,
          "user story / brief correction loops modify existing files but only Write is granted")


# --------------------------------------------------------------------------
# 7. Stage completeness
# --------------------------------------------------------------------------

def test_stage_two_is_implemented():
    compose = C[REF / "compose.md"]
    # Match stub markers precisely — "placeholder" appears legitimately in prose
    # ("not placeholder length"), so substring matching gives false positives.
    stubs = [ln for ln in compose.splitlines()
             if re.match(r"^#+ .*to be written|^> This reference will be completed", ln.strip())]
    check("Stage 2 protocol is written", not stubs,
          f"compose.md still carries stub markers: {stubs}")
    check("Stage 2 is substantial", len(compose.splitlines()) > 150,
          f"only {len(compose.splitlines())} lines")
    for phase in ("Resolve the candidates", "Resolve the tokens", "Compose", "Verify"):
        check(f"Stage 2 has phase: {phase}", phase in compose)
    check("Stage 2 has a degraded mode for MCP failure", "Degraded mode" in compose)
    check("Stage 2 names its exit to polish", "/dopamine polish" in compose)


def test_stage_two_uses_real_mcp_tools():
    """compose.md must name tools the server actually serves, not invented ones."""
    compose = C[REF / "compose.md"]
    real = {"list_components", "search_components", "get_component_docs",
            "list_patterns", "get_pattern_docs", "get_general_docs",
            "get_tokens", "get_agent_rules", "preview_component", "preview_pattern"}
    named = set(re.findall(r"`(\w+)`", compose)) & (real | {"list_storybook", "get_story"})
    check("Stage 2 names real MCP tools", named & real, f"found: {sorted(named)}")
    check("Stage 2 names no invented MCP tools", not (named - real), f"invented: {sorted(named - real)}")
    # the tools that actually carry the stage
    for t in ("search_components", "get_component_docs", "get_tokens"):
        check(f"Stage 2 uses {t}", t in compose)


def test_token_naming_matches_live_system():
    """Token names verified against the live get_tokens response."""
    blob = BLOB
    check("semantic brand role named correctly",
          "branding.1mg" in blob or "branding-1mg" in blob,
          "live system exposes semantic.color.branding.1mg")
    check("base brand primitive named correctly", "base.color.brand.coral" in blob)
    check("top-level scales use flat names",
          "--space-16" in blob and "--radius-8" in blob)


def test_focus_ring_fact_surfaces_wherever_accessibility_runs():
    """Ruled by the DS team: Dopamine components are mobile UI and carry no
    focus-ring styling by design.

    This is a stated fact, not an open question. It must surface at every point
    the accessibility pass runs, so a reader knows focus was considered and
    correctly found not applicable — rather than silently skipped.
    """
    for rel in ("accessibility.md", "compose.md", "polish.md"):
        t = C[REF / rel].lower()
        check(f"focus-ring fact stated in {rel}",
              "mobile ui" in t and "focus" in t and "by design" in t,
              "the fact must be pushed wherever the accessibility pass runs")
    check("SKILL.md carries the fact", "focus is not applicable" in C[SKILL / "SKILL.md"].lower())

    # And it must not have reverted to a requirement anywhere.
    for p, t in C.items():
        check(f"no focus-ring requirement in {p.name}",
              "never strip it" not in t and "Strip focus rings" not in t,
              "focus rings are not required on Dopamine mobile components")


def test_seven_states_became_six():
    """Focus dropped out of the interactive-state list — the count must follow."""
    stale = [p.name for p, t in C.items()
             if re.search(r"[Ss]even (?:interactive )?states", t)]
    check("no stale 'seven states' claim", not stale, ", ".join(stale))
    check("six applicable states stated", "six applicable" in BLOB.lower())


def main():
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
            except Exception as e:  # a crashing test is a failing test
                check(name, False, f"raised {type(e).__name__}: {e}")

    passed = [r for r in RESULTS if r[1]]
    failed = [r for r in RESULTS if not r[1]]

    for name, ok, detail in RESULTS:
        if not ok:
            print(f"FAIL  {name}" + (f"\n        {detail}" if detail else ""))
    print(f"\n{len(passed)} passed, {len(failed)} failed, {len(RESULTS)} total")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
