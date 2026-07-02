# zenn-topic-analyze

[fa0311/zenn-icons](https://github.com/fa0311/zenn-icons) に毎月コミットされる `metadata.json`（Zenn 全トピックのスナップショット）を分析するプロジェクト。

## セットアップ

```sh
uv sync
uv run python fetch_data.py   # data/ に全スナップショットをダウンロード（約70MB）
```

## 分析

`analysis.ipynb` を Jupyter で開く:

```sh
uv run jupyter lab analysis.ipynb
```

ノートブックは6セクション構成（冒頭に目次あり）:

1. **セットアップとデータロード**
2. **ランキング** — 急上昇 `rising_ranking()` / 相対成長率 `growth_ranking()` / モメンタム `momentum_ranking()` / 新規登場 `newcomer_ranking()`
3. **トピック比較** — 基本形は `compare_topics([...])`（絶対数と相対成長をセット表示）。AI / フロントエンド / Nix・環境構築 / ネイティブアプリ / テーマ別
4. **マクロ視点** — シェア推移 / AI vs 非AI / 成長ヒートマップ `plot_growth_heatmap()`
5. **記事以外の指標** — スクラップ・本（`metric=` の差し替え）
6. **付録** — トピック検索 `search_topics("キーワード")`

## ノートブックの再構成

セル構成は `build_notebook.py` でコード管理している。構成を大きく変えるときは
このスクリプトを編集して再生成→再実行する:

```sh
uv run python build_notebook.py
uv run jupyter nbconvert --to notebook --execute --inplace analysis.ipynb
```
