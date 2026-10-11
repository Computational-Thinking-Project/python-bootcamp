# Team Roster & Roles — Team 04

CSC10014 — Smart Virtual Assistant, HCMUS.

Names, student IDs, GitHub usernames, and task assignments were supplied by
the team. Nguyen Ba Duy is the project manager, with Pham Khanh Tam responsible
for documentation.
The roster is sorted by student ID in ascending order.

| No | Full Name | Student ID | GitHub Username | Role |
|:---|:---|:---|:---|:---|
| 1 | Duong Trung Anh | 25127012 | [@philip-kkk](https://github.com/philip-kkk) | QA / Test Engineer |
| 2 | Ha Tran Boi Anh | 25127013 | [@htbaax](https://github.com/htbaax) | DevOps / Tooling |
| 3 | Truong Thanh Dat | 25127035 | [@Thanhdat3010](https://github.com/Thanhdat3010) | UI/UX Designer |
| 4 | Nguyen Ba Duy | 25127040 | [@johannguyen015](https://github.com/johannguyen015) | Project Manager / Config |
| 5 | Nguyen Nhat Quynh | 25127131 | [@nhatquynh1107](https://github.com/nhatquynh1107) | Backend Engineer |
| 6 | Pham Khanh Tam | 25127135 | [@AI-WFox](https://github.com/AI-WFox) | Documentation Lead |
| 7 | Nguyen Dinh Hung | 25127194 | [@benalexx007](https://github.com/benalexx007) | Data Specialist |

## Branches and ownership

Roster numbers indicate display order. Task numbers below follow the original
seven-task plan, so sorting the roster does not change task ownership.

| Task | Owner | Branch | Assigned files |
|:---|:---|:---|:---|
| 1 | Nguyen Ba Duy | `feat/config` | `.gitignore`, `requirements.txt`, `pyproject.toml` |
| 2 | Nguyen Nhat Quynh | `feat/backend` | `src/assistant/__init__.py`, `src/assistant/rules.py`, `src/assistant/__main__.py` |
| 3 | Ha Tran Boi Anh | `feat/scripts` | `scripts/check_env.py` |
| 4 | Nguyen Dinh Hung | `feat/data` | `data/offices.csv`, `data/README.md` |
| 5 | Duong Trung Anh | `feat/tests` | `tests/test_smoke.py` |
| 6 | Truong Thanh Dat | `feat/ui` | `ui/README.md` |
| 7 | Pham Khanh Tam | `feat/docs` | `README.md`, `docs/README.md`, `docs/team.md` |

This table records the planned skeleton assignment. The corresponding files
are delivered through their owners' separate PRs.

## Review and milestone responsibilities

Each member opens a PR from their branch into the team repository's `main`.
A teammate or the project manager reviews the change before merging. The
recommended merge order is config, backend, scripts, data, tests, UI, then docs.
After all seven PRs are merged and setup checks pass, the project manager
(Nguyen Ba Duy) creates and pushes the `v0.1-setup` tag.
