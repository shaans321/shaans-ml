from pathlib import Path

replacements = [
    (
        Path(r'c:\Users\sarig\Documents\Langchain\venv\source\task3\messages_demo.py'),
        "with open('/root/messages-complete.txt', 'w') as f:\n    f.write(\"MESSAGES_COMPLETE\")\n",
        "messages_complete_path = project_root / \"messages-complete.txt\"\nmessages_complete_path.write_text(\"MESSAGES_COMPLETE\")\n",
    ),
    (
        Path(r'c:\Users\sarig\Documents\Langchain\venv\source\task3\first_model.py'),
        "# Save progress\nwith open('/root/first-model.txt', 'w') as f:\n    f.write(\"FIRST_MODEL_COMPLETE\")\n",
        "# Save progress\nfirst_model_path = project_root / \"first-model.txt\"\nfirst_model_path.write_text(\"FIRST_MODEL_COMPLETE\")\n",
    ),
]

for path, old, new in replacements:
    text = path.read_text(encoding='utf-8')
    if old in text:
        path.write_text(text.replace(old, new), encoding='utf-8')
    else:
        print(f'No match for {path}')
