import re
import datetime

# 10 dynamic states rotating or randomized
ACTIVITIES = [
    {
        "agent": "agent-executor",
        "gif": "leroy/leroy-laptop.gif",
        "status": "Shipping low-latency FiveM Lua modules & QBox net-events.",
        "fuel": "Fresh Carrot Crisps",
        "mood": "Hyper-focused dev mode 💻"
    },
    {
        "agent": "agent-ideation",
        "gif": "leroy/leroy-munch.gif",
        "status": "Munching through hardware protocol RFCs & backlog issues.",
        "fuel": "Organic Timothy Hay 🥕",
        "mood": "Brainstorming next architecture 💡"
    },
    {
        "agent": "agent-deployer",
        "gif": "leroy/leroy-binky.gif",
        "status": "Final push landed with 100% test pass. Executing victory binky!",
        "fuel": "Sweet Apple Slice 🍏",
        "mood": "Pure deployment joy 🚀"
    },
    {
        "agent": "agent-watcher",
        "gif": "leroy/leroy-peek.gif",
        "status": "Peeking background UDP sockets & printer toner sentinels.",
        "fuel": "Dandelion greens 🌿",
        "mood": "Vigilant sentinel patrol 👁️"
    },
    {
        "agent": "agent-optimizer",
        "gif": "leroy/leroy-zoomies.gif",
        "status": "Running zoomies across database query plans & sub-ms tick caches.",
        "fuel": "High-octane parsley ⚡",
        "mood": "Maximum speed optimization 🏎️"
    },
    {
        "agent": "agent-debugger",
        "gif": "leroy/leroy-flop.gif",
        "status": "Pancake flop achieved. Root-causing pesky edge cases from the carpet.",
        "fuel": "Dried Banana Chip 🍌",
        "mood": "Deep stack-trace dissection 🥞"
    },
    {
        "agent": "agent-builder",
        "gif": "leroy/leroy-sleep.gif",
        "status": "Compilation daemon humming smoothly in background while Leroy recharges.",
        "fuel": "Cozy blanket snooze 💤",
        "mood": "Resting between build triggers 😴"
    },
    {
        "agent": "agent-sentinel",
        "gif": "leroy/leroy-sniff.gif",
        "status": "Sniffing out dependency anomalies, memory leaks & security perimeters.",
        "fuel": "Clover buds 🍀",
        "mood": "Periscope posture scanning 🔍"
    },
    {
        "agent": "agent-evaluator",
        "gif": "leroy/leroy-love.gif",
        "status": "Pair reviewing diffs with human-in-the-loop and sending good vibes.",
        "fuel": "Cuddle breaks & chin scratches ❤️",
        "mood": "Constructive code review ✨"
    },
    {
        "agent": "agent-linter",
        "gif": "leroy/leroy-clean.gif",
        "status": "Washing paws and pruning dead code & unused imports.",
        "fuel": "Clean grooming session 🧼",
        "mood": "Zero technical debt hygiene 🧹"
    }
]

def get_current_activity():
    # Deterministic rotation based on 6-hour slots throughout the year
    now = datetime.datetime.now(datetime.timezone.utc)
    slot = int(now.timestamp() // (6 * 3600))
    return ACTIVITIES[slot % len(ACTIVITIES)], now.strftime("%Y-%m-%d %H:%M UTC")

def update_readme():
    act, timestamp = get_current_activity()
    status_block = f"""<!-- LEROY_STATUS_START -->
<div align="center">
  <table style="border: 1px solid #363530; background: #1c1b18; border-radius: 8px;">
    <tr>
      <td width="72" align="center" style="border: none;">
        <img src="{act['gif']}" width="58" alt="Leroy" />
      </td>
      <td align="left" style="border: none; padding-left: 12px;">
        <b>🐰 Leroy Live Duty: <code>{act['agent']}</code></b><br/>
        <sub>{act['status']}</sub><br/>
        <sub><b>Current Fuel:</b> {act['fuel']} &bull; <b>Status:</b> {act['mood']} &bull; <i>Updated: {timestamp}</i></sub>
      </td>
    </tr>
  </table>
</div>
<!-- LEROY_STATUS_END -->"""

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"<!-- LEROY_STATUS_START -->[\s\S]*?<!-- LEROY_STATUS_END -->")
    if pattern.search(content):
        updated = pattern.sub(status_block, content)
    else:
        # Insert directly after the typing SVG container closing div
        target = '</div>\n\n---\n\n### 🐰 About & What I Build'
        replacement = f'</div>\n\n<br/>\n\n{status_block}\n\n---\n\n### 🐰 About & What I Build'
        norm_content = content.replace("\r\n", "\n")
        assert target in norm_content, "Target marker not found in README"
        updated = norm_content.replace(target, replacement)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)
    print("README updated with live Leroy status!")

if __name__ == "__main__":
    update_readme()
