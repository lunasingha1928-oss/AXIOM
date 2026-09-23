import json

transcript_path = r'C:\Users\vigne\.gemini\antigravity\brain\421cec1d-8e0f-4a94-adcc-9d94dc20d37c\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            content = data.get('content', '')
            if 'drift' in content.lower() or 'sanity' in content.lower() or 'range' in content.lower():
                print(f"Step {data.get('step_index')}:")
                print(content)
                print("="*50)
