"""
API contract reference for the Colab-hosted NeuroMark backend.
The live backend is implemented in the notebook.
"""

ENDPOINTS = {
    "health": "GET /health",
    "logs": "GET /logs",
    "analyze": "POST /analyze",
    "analyze_with_plot": "POST /analyze_with_plot",
}

FORM_FIELDS = [
    "file",
    "target_emotion",
    "target_audience",
    "objective",
    "use_short_clip",
    "short_seconds",
    "return_brain_plot",
]

RESPONSE_KEYS = [
    "schema_version",
    "status",
    "campaign",
    "real_tribe_evidence",
    "neuromark_marketing_vector",
    "emotion_measurement",
    "intent_vs_actual_gap",
    "crm_matching",
    "recommended_creative_fixes",
    "brain_plot",
    "runtime_seconds",
    "saved_files",
]
