# Security

Never commit real Hugging Face or ngrok tokens.

The notebook uses hidden prompts:

```python
from getpass import getpass
```

If a token was exposed, revoke it immediately.

Before pushing:

```bash
git grep -n "hf_"
git grep -n "NGROK"
git grep -n "authtoken"
```
