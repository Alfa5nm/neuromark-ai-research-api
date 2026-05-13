const formData = new FormData();
formData.append("file", selectedFile);
formData.append("target_emotion", "Urgency");
formData.append("target_audience", "Students preparing for exams");
formData.append("objective", "Get students to start a mock exam countdown");
formData.append("use_short_clip", "true");
formData.append("short_seconds", "5");
formData.append("return_brain_plot", "true");

const response = await fetch(`${API_BASE_URL}/analyze_with_plot`, {
  method: "POST",
  headers: { "ngrok-skip-browser-warning": "true" },
  body: formData
});

const result = await response.json();
console.log(result);
