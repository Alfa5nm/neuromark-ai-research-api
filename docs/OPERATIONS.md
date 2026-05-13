# Operations Guide

## Colab

1. Open `notebooks/neuromark_real_tribe_brainplot_api_colab.ipynb`.
2. Set Runtime to T4 GPU.
3. Run Cell 1.
4. Run the restart cell.
5. Continue from environment verification.
6. Enter Hugging Face token and ngrok token when prompted.
7. Run until the notebook prints a public ngrok URL.

## Frontend

1. Open `frontend/index.html`.
2. Paste the ngrok URL.
3. Click `Check Server`.
4. Upload MP4/JPG/JPEG/PNG.
5. Click `Analyze + Brain Plot`.

## Recommended demo settings

- Use short clip: true
- Short clip seconds: 5
- Target emotion: Urgency or Trust
- Use MP4 under 30 seconds for fast demos

## Outputs

The Colab notebook writes generated files to:

```text
/content/neuromark_research_api/outputs/
```

Typical outputs:
- JSON report
- marketing vector CSV
- CRM ranking CSV
- TRIBE brain plot PNG
