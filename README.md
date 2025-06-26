# Rick and Morty API + UI Test Suite

## Overview

This test suite covers basic automated tests for the Rick and Morty public API and its web UI.

- ✅ API tests: Characters, filters, status codes
- ✅ UI tests: Landing page, character cards, Docs link
- ✅ Logging and parametric tests
- ✅ Partial - CI with GitHub Actions
- ✅ Partial - Docker support

## Tech Stacks
pytest + requests for the api tests
pytest + selenium for the ui tests


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

### Saving results
```bash
pytest tests/ &> test_run.output
```

## Docker

```bash
# Currently has an network error. I ran out of time to investigate.
docker-compose up --build
```

## Assumptions

- The Rick and Morty API is stable and publicly accessible.
- The UI structure (e.g., class names) may change and could break UI selectors.

## Bonus Features

- GitHub Actions CI - partial has an error
- Docker support - partial has an error
- Parametric API tests
- Page Object Model for UI

## To Do
# Fix GA and Docker support
# Longer running tests that click multiple links
# Performance tests
# More edge cases, especially for the api
# Add some retry logic for stability
