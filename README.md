# NeuroMark AI — Real TRIBE v2 Research API

NeuroMark AI is a research/demo system that turns campaign media into a **TRIBE v2-derived cognitive-emotional campaign report**.

It connects:

```text
Frontend HTML
→ ngrok public URL
→ Google Colab FastAPI server
→ real TRIBE v2 inference
→ NeuroMark campaign vector
→ Emotion Tree classification
→ CRM-style audience ranking
→ TRIBE brain-response plot
→ JSON response back to frontend
```

## What is included

```text
notebooks/neuromark_real_tribe_brainplot_api_colab.ipynb
frontend/index.html
docs/ARCHITECTURE.md
docs/OPERATIONS.md
docs/API_REFERENCE.md
docs/USE_CASES.md
docs/SAFETY_AND_CLAIMS.md
docs/TROUBLESHOOTING.md
backend_reference/api_contract.py
examples/sample_response.json
examples/sample_frontend_payload.js
requirements-colab.txt
.env.example
SECURITY.md
```

## What it produces

For each uploaded campaign asset, the system can return:

- Real TRIBE v2 evidence: prediction shape, timesteps, vertices, segments, neural stats.
- A Colab-generated TRIBE brain-response plot.
- A NeuroMark marketing vector:
  - visual_attention
  - emotional_warmth
  - motivation_reward
  - cognitive_load
  - memory_encoding
  - trust_safety
  - urgency
  - confusion_risk
  - calm_aesthetic_style
  - theme_fit
- Emotion Tree output:
  - detected emotion
  - dominant layer
  - emotion scores
  - chaos spike timestamp
  - explanation
- CRM-style audience ranking:
  - recommended segment
  - platform
  - audience score
- Creative recommendations.

## Quick start

### 1. Open the Colab notebook

Open:

```text
notebooks/neuromark_real_tribe_brainplot_api_colab.ipynb
```

in Google Colab.

Set:

```text
Runtime → Change runtime type → T4 GPU
```

Run cells in order.

The notebook will:

1. Install dependencies.
2. Restart runtime.
3. Ask for Hugging Face and ngrok tokens through hidden prompts.
4. Load real TRIBE v2.
5. Start a FastAPI server.
6. Start an ngrok tunnel.
7. Print a public API URL.

You need Hugging Face access to:

- `facebook/tribev2`
- `meta-llama/Llama-3.2-3B`

Use a Hugging Face **Read** token.

### 2. Open the frontend

Open:

```text
frontend/index.html
```

Paste the ngrok base URL printed by Colab, for example:

```text
https://xxxx.ngrok-free.app
```

Do **not** include `/analyze_with_plot`.

Then click:

```text
Check Server
```

Expected health result:

```json
{
  "status": "ok",
  "cuda_available": true,
  "gpu": "Tesla T4"
}
```

### 3. Analyze an asset

Upload an MP4/JPG/JPEG/PNG and click:

```text
Analyze + Brain Plot
```

The frontend calls:

```text
POST /analyze_with_plot
```

and renders the NeuroMark report plus the TRIBE brain plot.

## Operational hierarchy

```text
Layer 1: Campaign Asset
  MP4/JPG/JPEG/PNG uploaded by user.

Layer 2: Frontend
  Browser sends multipart/form-data to Colab through ngrok.

Layer 3: Colab API Gateway
  FastAPI receives asset and campaign metadata.

Layer 4: Asset Preparation
  Video is optionally clipped.
  Image is converted to a short static MP4.

Layer 5: TRIBE v2 Inference
  TRIBE extracts events and predicts cortical response activity.

Layer 6: Neural Dynamics
  Predictions become global activity, peak activity, variance, spread, change, sustained response.

Layer 7: NeuroMark Vector
  Neural dynamics become campaign metrics.

Layer 8: Emotion Tree
  Metrics become response category, dominant layer, chaos spike, explanation.

Layer 9: CRM Matching
  Vector is compared to historical campaign vectors.

Layer 10: Report + Plot
  API returns JSON and base64 PNG to the frontend.
```

## Safe claim

> NeuroMark uses real TRIBE v2 predicted cortical response activity as an input signal, then applies a transparent product interpretation layer to create campaign vectors, response categories, CRM-style audience recommendations, creative recommendations, and a brain-response visualization.

## Do not claim

- It reads minds.
- It clinically measures emotion.
- It guarantees sales or conversion.
- It replaces real user studies.
- It directly measures viewer fMRI/EEG.

## GitHub push

```bash
unzip neuromark-ai-research-api-github.zip
cd neuromark-ai-research-api
git init
git add .
git commit -m "Initial NeuroMark AI Real TRIBE v2 research API"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
