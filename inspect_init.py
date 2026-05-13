import json
path = "notebooks/neuromark_real_tribe_brainplot_api_colab.ipynb"
with open(path, "r", encoding="utf-8") as f: nb = json.load(f)
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] == "code":
        src = "".join(c["source"])
        if "from_pretrained" in src or "FastAPI" in src or "ngrok" in src:
            print(f"CELL {i}")
            print(src[:200])
