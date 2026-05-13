# API Reference

## GET /health

Returns server and GPU status.

## GET /logs

Returns recent request logs.

## POST /analyze

Runs analysis without returning the base64 brain plot.

## POST /analyze_with_plot

Runs full analysis and returns the base64 plot.

### Form fields

- `file`: MP4/JPG/JPEG/PNG
- `target_emotion`: default `Urgency`
- `target_audience`: default `Students preparing for exams`
- `objective`: campaign objective
- `use_short_clip`: `true` or `false`
- `short_seconds`: integer, usually `5`
- `return_brain_plot`: `true`

### Response highlights

```json
{
  "status": "success",
  "real_tribe_evidence": {
    "preds_shape": [6, 20484],
    "num_timesteps": 6,
    "num_vertices": 20484
  },
  "neuromark_marketing_vector": {},
  "emotion_measurement": {},
  "crm_matching": {},
  "brain_plot": {
    "mime_type": "image/png",
    "base64": "..."
  }
}
```
