import json

transcript_path = r'C:\Users\vigne\.gemini\antigravity\brain\421cec1d-8e0f-4a94-adcc-9d94dc20d37c\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            idx = data.get('step_index')
            if idx in (1807, 1859, 1931, 1977):
                print(f"=== STEP {idx} ===")
                print(data.get('content'))
                print()
