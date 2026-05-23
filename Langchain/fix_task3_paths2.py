from pathlib import Path

patches = [
    {
        "path": Path(r"c:\Users\sarig\Documents\Langchain\venv\source\task3\messages_demo.py"),
        "old": "with open('/root/messages-complete.txt', 'w') as f:\n    f.write(\"MESSAGES_COMPLETE\")",
        "new": "messages_complete_path = project_root / \"messages-complete.txt\"\nmessages_complete_path.write_text(\"MESSAGES_COMPLETE\")",
    },
    {
        "path": Path(r"c:\Users\sarig\Documents\Langchain\venv\source\task3\first_model.py"),
        "old": "# Save progress\nwith open('/root/first-model.txt', 'w') as f:\n    f.write(\"FIRST_MODEL_COMPLETE\")",
        "new": "# Save progress\nfirst_model_path = project_root / \"first-model.txt\"\nfirst_model_path.write_text(\"FIRST_MODEL_COMPLETE\")",
    },
]

for patch in patches:
    path = patch["path"]
    text = path.read_text(encoding="utf-8")
    if patch["old"] in text:
        text = text.replace(patch["old"], patch["new"])
        path.write_text(text, encoding="utf-8")
        print(f"patched {path}")
    else:
        print(f"no match for {path}")
