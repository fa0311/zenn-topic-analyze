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

主な分析パターン:

- **急上昇ランキング**: `rising_ranking(months_back=1)` — 期間別の記事数増加 Top 20（`ascending=True` で下降）
- **相対成長率ランキング**: `growth_ranking(months_back=3, min_start=50)` — 規模フィルタ付きの伸び率
- **モメンタム**: `momentum_ranking()` — 直近で加速・失速しているトピック
- **新規登場トピック**: `newcomer_ranking(months_back=6)` — 期間中に初登場したトピック
- **時系列推移**: `plot_topics(["claudecode", "react", ...])` — 折れ線比較（`rate=True` で増加ペース、`normalize=True` で指数化、`metric=` で scraps 等に切替）
- **テーマ別 small multiples / シェア推移 / 成長ヒートマップ**: ノートブック内の各セクション参照
- **トピック検索**: `search_topics("キーワード")`
