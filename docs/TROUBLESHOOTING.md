# Troubleshooting

## No plot appears

Use `/analyze_with_plot`, not `/analyze`.

Check response JSON includes:

```json
"brain_plot": {
  "base64": "..."
}
```

## Server check fails

Rerun the FastAPI server cell and ngrok cell. Paste the new URL into frontend.

## Hugging Face error 401/403

Accept model access on Hugging Face and rerun login.

## ngrok token error

Use a real ngrok authtoken, not a placeholder.

## NumPy errors

Factory reset runtime, rerun install, restart, continue.

## Slow runtime

Use short clip mode with 5 seconds.
