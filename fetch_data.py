"""zenn-icons リポジトリの metadata.json の全スナップショットを data/ にダウンロードする。

コミット履歴から metadata.json を変更した全コミットを取得し、
各時点のファイルを data/<コミット日 YYYY-MM-DD>.json として保存する。
ダウンロード済みのファイルはスキップするため再実行可能。
"""

import json
from pathlib import Path

import requests

REPO = "fa0311/zenn-icons"
DATA_DIR = Path(__file__).parent / "data"


def list_snapshots() -> list[tuple[str, str]]:
    """metadata.json を変更したコミットの (日付, SHA) 一覧を古い順に返す。"""
    res = requests.get(
        f"https://api.github.com/repos/{REPO}/commits",
        params={"path": "metadata.json", "per_page": 100},
        timeout=30,
    )
    res.raise_for_status()
    commits = [(c["commit"]["author"]["date"][:10], c["sha"]) for c in res.json()]
    return sorted(commits)


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    snapshots = list_snapshots()
    print(f"{len(snapshots)} snapshots found")

    for date, sha in snapshots:
        dest = DATA_DIR / f"{date}.json"
        if dest.exists():
            print(f"skip  {date} ({sha[:8]})")
            continue
        url = f"https://raw.githubusercontent.com/{REPO}/{sha}/metadata.json"
        res = requests.get(url, timeout=60)
        res.raise_for_status()
        data = res.json()  # JSONとして妥当か検証してから保存する
        dest.write_text(json.dumps(data, ensure_ascii=False))
        print(f"saved {date} ({sha[:8]}) topics={len(data)}")


if __name__ == "__main__":
    main()
