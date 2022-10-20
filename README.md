# dumb-api
A really simple api used for development of the [filloabot-rs](https://github.com/FilloaBot/filloabot-rs/)

## 🔧 Deploy it

### 🐳 Docker (Recommended)

This is the quick way to run this standalone:

```bash
docker run -d --name filloabot-rs-dumb-api -v (pwd)/references.json:/app/references.json:ro -p 8080:5000 ghcr.io/FilloaBot/dumb-api:latest
```
If you want to run it together with the filloabot-rs, there is a docker compose in [it's repo](https://github.com/FilloaBot/filloabot-rs/)

#### Environment Variables

| Name              | Description                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------|
| `REFERENCES_FILE` | Path to the references JSON file which will be served to the filloabot-rs (no matter which guild it requests)       |

#### Build the image

```bash
git clone https://github.com/FilloaBot/dumb-api.git
cd dumb-api
docker build -t filloabot-rs-dumb-api .
```

### 💪🏻 Without Docker

You probably knew how to do this already.
	
```bash
git clone https://github.com/FilloaBot/dumb-api.git
cd dumb-api
python3 main.py
```
