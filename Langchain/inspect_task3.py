from pathlib import Path

for file_name in ['messages_demo.py', 'first_model.py']:
    path = Path(r'c:\Users\sarig\Documents\Langchain\venv\source\task3') / file_name
    text = path.read_text(encoding='utf-8')
    print('FILE:', file_name)
    idx = text.rfind("with open('/root")
    if idx == -1:
        idx = text.rfind('# Save progress')
    print('INDEX:', idx)
    print(repr(text[idx:idx+200]))
    print('-' * 80)
