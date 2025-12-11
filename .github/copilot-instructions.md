<!-- Copilot / AI agent instructions for todo-cli -->
# Copilot instructions — todo-cli

Purpose
- Provide concise, actionable guidance for AI coding agents working on this small CLI Python app.

Quick start (how to run)
- Python version: 3.6+.
- Run locally: `python todo.py` from the repository root.
- If you use a virtualenv, activate it first, e.g. `source .venv/bin/activate`.

Big picture (architecture & data flow)
- Single-file CLI: the core program is `todo.py`.
- Local JSON storage: `tasks.json` (located in repo root) stores an array of task objects.
- Primary functions in `todo.py`: `load_tasks()`, `save_tasks(tasks)`, `show_tasks(tasks)`, `add_task(tasks, title)`, `complete_task(tasks, index)`, `delete_task(tasks, index)`, and `main()`.
- Data flow: `main()` calls `load_tasks()` once at startup to populate an in-memory list. User actions mutate that list, and `save_tasks()` persists it (on exit in current code).

Project-specific conventions & patterns
- Keep changes minimal and behaviour-preserving: this is a tiny CLI tool with no tests. Avoid large refactors that change the UX.
- Storage shape: `tasks.json` is a JSON array of objects like `{ "title": "...", "done": true|false }`. Maintain compatibility with that shape when modifying persistence.
- Indexing: the interactive menu presents task numbers starting at 1; internal functions operate on 0-based indices. Preserve this UI convention unless you intentionally update both UI and internal logic.
- No external dependencies: `todo.py` uses only the Python standard library. Prefer staying dependency-free unless a clear benefit warrants adding a package and updating `README.md`.

Examples (copyable) — how to add/complete/delete programmatically
- Add a task in code:
```python
tasks = load_tasks()
add_task(tasks, "Buy milk")
save_tasks(tasks)
```
- Mark task #2 (UI numbering) as complete in code:
```python
tasks = load_tasks()
complete_task(tasks, 1)  # 1 == UI task #2
save_tasks(tasks)
```

Safety notes / common pitfalls
- User input is not validated aggressively (e.g. `int(input(...))` calls). When adding features, guard against `ValueError` to avoid crashing the CLI.
- `FILE = 'tasks.json'` is a relative path. Running the script from a different working directory will change where the file is read/written. Use absolute paths only if you update `load_tasks()`/`save_tasks()` accordingly.
- When changing storage format (e.g., adding IDs, timestamps), provide a migration path so existing `tasks.json` files are not silently corrupted.

Developer workflows & checks
- No unit tests are present. Validate changes by running `python todo.py` and exercising the menu.
- Quick checks:
  - `python todo.py` — interact with the app
  - `cat tasks.json` — inspect persisted data

Files to inspect when changing behavior
- `todo.py` — primary source of truth
- `tasks.json` — sample data and persisted state
- `README.md` — user-facing instructions; update if you change run/install steps

PR guidance for AI agents
- Produce small, focused patches that update code + `README.md` when UX or run instructions change.
- Preserve existing `tasks.json` shape unless you include a migration and tests/manual verification steps in the PR description.

If you need clarification
- Ask: "Should feature X be backward-compatible with existing `tasks.json`?" or "Is changing the CLI menu layout acceptable?"

---
Reference: Inspect `todo.py` and `tasks.json` for examples and current behavior.
