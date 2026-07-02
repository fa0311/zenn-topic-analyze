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

ノートブックは「問い → グラフ → 読みどころ」の8章構成（冒頭に目次あり）:

1. **セットアップ** — データロードと分析関数の定義（関数はすべてここに集約）。Zenn 側のタグ統合（`llm`→`大規模言語モデル` 等）を自動検出＋人力レビューの `TAG_MERGES` 辞書で補正し、時系列を連続にしている
2. **全体像** — Zenn 全体の年間推移（記事・トピック・スクラップ・本）
3. **何が伸びているか** — 急上昇 Top 15 / 規模×成長率の散布図 / 加速・失速の発散バー / 新規登場
4. **AI の牽引力** — AI vs 非AI / シェア推移 / AI 内部の勢力図
5. **ケーススタディ** — フロントエンド / 環境構築 / ネイティブアプリ / 言語・クラウド（`compare_topics()` で絶対数＋相対成長をセット表示）
6. **ヒートマップ** — 各トピックがいつ盛り上がったか
7. **記事以外の指標** — スクラップ・本
8. **付録** — トピック検索・関数リファレンス

## ノートブックの再構成

セル構成は `build_notebook.py` でコード管理している。構成を大きく変えるときは
このスクリプトを編集して再生成→再実行する:

```sh
uv run python build_notebook.py
uv run jupyter nbconvert --to notebook --execute --inplace analysis.ipynb
```
