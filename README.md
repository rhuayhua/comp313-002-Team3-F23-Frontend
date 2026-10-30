# JPAS Frontend

![JPAS banner](banner.jpg)

**More than an AI keyword extraction.** JPAS helps job seekers improve their chances of landing their dream job by using NLP models to pull the key skills and keywords out of job postings.

This repository holds the **Streamlit web UI** for JPAS. You paste a job description, and the app sends it to the JPAS backend and shows the extracted keywords as colored tags.

## How it works

1. You paste a job posting into the text box and click **Get keywords**.
2. The app sends a `POST` request to `http://<BACKEND_HOST>:8910/ml` with this body:

   ```json
   [{ "position": "position", "jobDescription": "<your text>" }]
   ```

3. The backend replies with:

   ```json
   { "keywords": ["keyword 1", "keyword 2", "..."] }
   ```

4. The keywords are shown as tags under the text box.

## Requirements

- Python 3.9+
- A running JPAS backend, reachable on port `8910`

## Configuration

| Variable       | Description                                        | Example        |
|----------------|----------------------------------------------------|----------------|
| `BACKEND_HOST` | Hostname or IP of the JPAS backend (no port/scheme) | `192.168.2.11` |

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

export BACKEND_HOST=localhost   # Windows: set BACKEND_HOST=localhost
streamlit run jpas.py
```

Then open http://localhost:8501.

## Run with Docker

```bash
docker build -t jpas-frontend .
docker run -p 8501:8501 -e BACKEND_HOST=<backend-host> jpas-frontend
```

Then open http://localhost:8501. The container includes a health check at `/_stcore/health`.

> If the backend runs on your own machine, use `host.docker.internal` (Docker Desktop) or your machine's LAN IP as `BACKEND_HOST`, not `localhost`.

## Project structure

```
├── jpas.py            # Streamlit app
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container image (serves on port 8501)
├── banner.jpg         # Page banner
└── picture.jpg        # Header illustration
```

## License

[MIT](LICENSE)
