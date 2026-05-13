# Architecture

## System overview

```text
Campaign media → Frontend → ngrok → Colab FastAPI → TRIBE v2 → NeuroMark vector → Emotion Tree → CRM ranking → JSON + brain plot
```

## Frontend

`frontend/index.html`

Responsibilities:
- Paste Colab ngrok base URL.
- Upload MP4/JPG/JPEG/PNG.
- Send multipart form to `/analyze_with_plot`.
- Render summary, metrics, CRM match, and base64 brain plot.

## Colab backend

`notebooks/neuromark_real_tribe_brainplot_api_colab.ipynb`

Responsibilities:
- Install dependencies.
- Login to Hugging Face.
- Load `facebook/tribev2`.
- Run FastAPI.
- Expose ngrok URL.
- Run inference and return JSON.

## TRIBE v2 layer

The notebook uses:

```python
from tribev2.demo_utils import TribeModel
from tribev2.plotting import PlotBrain
```

Main calls:

```python
df_events = model.get_events_dataframe(video_path=...)
preds, segments = model.predict(events=df_events)
```

Expected tensor:

```text
[timesteps, vertices]
```

Example:

```text
[6, 20484]
```

## NeuroMark interpretation layer

TRIBE predictions are converted into neural dynamics, then into the campaign vector.

The vector is not a native TRIBE output. It is a transparent product-layer synthesis built on top of real TRIBE predictions.

## Brain plot

The API uses `plotter.plot_timesteps(...)`, saves the figure as PNG, encodes it as base64, and returns it in `brain_plot.base64`.
