# Rick and Morty API + UI Test Suite

## Overview

This test suite covers basic automated tests for the Rick and Morty public API and its web UI.

- ✅ API tests: Characters, filters, status codes
- ✅ UI tests: Landing page, character cards, Docs link
- ✅ Logging and parametric tests
- ✅ CI with GitHub Actions
- ✅ Docker support

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest tests/
```

## Docker

```bash
docker-compose up --build
```

## Assumptions

- The Rick and Morty API is stable and publicly accessible.
- The UI structure (e.g., class names) may change and could break UI selectors.

## Bonus Features

- GitHub Actions CI
- Docker support
- Parametric API tests
- Page Object Model for UI
