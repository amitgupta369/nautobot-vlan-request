# Nautobot VLAN Request App Architecture

## Root Files

### `.gitignore`

Defines files and folders Git should ignore (venv, pycache, logs, local configs).

### `pyproject.toml`

Defines package metadata, dependencies, and build configuration.

### `README.md`

Provides installation, usage, and project overview documentation.

### `ARCHITECTURE.md`

Documents app structure, file responsibilities, and development guidelines.

---

## Application Package (`nautobot_vlan_request/`)

### `__init__.py`

Registers the Nautobot app and defines plugin configuration.

### `models.py`

Defines database models and relationships.

### `forms.py`

Defines UI forms and input validation logic.

### `tables.py`

Defines table layouts for list views.

### `views.py`

Handles UI page logic and object operations.

### `urls.py`

Maps UI routes to views.

### `filters.py`

Defines filtering and search logic for UI/API.

### `navigation.py`

Adds app menu items to Nautobot navigation.

### `jobs.py`

Defines automation workflows and background tasks.

---

## API Layer (`api/`)

### `api/__init__.py`

Marks the API directory as a Python package.

### `api/serializers.py`

Converts models into JSON and JSON into models.

### `api/views.py`

Handles REST API CRUD operations.

### `api/urls.py`

Registers API endpoints.

---

## Database Layer

### `migrations/`

Tracks database schema changes over time.

### `migrations/__init__.py`

Marks migrations as a Python package.

---

## Development Flow

models.py → forms.py → tables.py → views.py → urls.py
models.py → serializers.py → api/views.py → api/urls.py
models.py → jobs.py → signals.py → automation execution
