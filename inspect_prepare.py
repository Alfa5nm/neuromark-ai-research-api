import json
path = "notebooks/neuromark_real_tribe_brainplot_api_colab.ipynb"
with open(path, "r", encoding="utf-8") as f: nb = json.load(f)
for c in nb["cells"]:
    if c["cell_type"] == "code":
        src = "".join(c["source"])
        if "def prepare_asset_for_tribe" in src:
            print(src)
