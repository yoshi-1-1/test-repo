import streamlit as st
import requests
import pandas as pd
import random
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

# --------------------------------------------------
# 1. ページ全体の初期設定
# --------------------------------------------------
st.set_page_config(page_title="林野火災アラート", layout="wide")
st.title("🔥 林野火災アラート 管理ダッシュボード")
st.markdown("※ 出典：気象庁ホームページの防災情報データを基に自動生成")
st.markdown("*(※プロトタイプのため、雨量データはランダムなシミュレーション値を使用しています)*")

# --------------------------------------------------
# 2. 全国エリアマスターの取得（キャッシュ化して高速化）
# --------------------------------------------------
@st.cache_data
def load_area_master():
    # 気象庁の地域コード一覧を動的に取得
    url = "https://www.jma.go.jp/bosai/common/const/area.json"
    response = requests.get(url)
    return response.json()

area_master = load_area_master()

# 都道府県（offices）の辞書を作成 { "北海道": "010000", ..., "奈良県": "290000" }
pref_dict = {info["name"]: code for code, info in area_master["offices"].items()}
pref_names = list(pref_dict.keys())

# --------------------------------------------------
# 3. ユーザーインターフェース (UI)
# --------------------------------------------------
# 初期表示を奈良県に設定（インデックスを取得）
default_index = pref_names.index("奈良県") if "奈良県" in pref_names else 0

st.sidebar.header("検索条件の設定")
selected_pref_name = st.sidebar.selectbox(
    "情報を取得する都道府県を選択", 
    pref_names, 
    index=default_index
)
pref_code = pref_dict[selected_pref_name]

# --------------------------------------------------
# 4. データ取得と判定処理
# --------------------------------------------------
if st.sidebar.button("データ取得・判定実行", type="primary"):
    with st.spinner(f"{selected_pref_name} のデータを取得中..."):
        
        # 選択された都道府県の気象データを取得
        warning_url = f"https://www.jma.go.jp/bosai/warning/data/warning/{pref_code}.json"
        try:
            warning_res = requests.get(warning_url)
            warning_res.raise_for_status()
            warning_data = warning_res.json()
            
            latest_areas = warning_data[0]["timeSeries"][0]["areas"]
            city_master = area_master["class20s"] # 全国の市町村マスター
            
            results = []
            now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            
            # 各市町村の判定
            for area in latest_areas:
                city_code = area["area"]["code"]
                
                # マスターに存在しないエリア（一部の特殊管区など）はスキップ
                if city_code not in city_master:
                    continue
                    
                city_name = city_master[city_code]["name"]
                warnings = area.get("warnings", [])
                
                has_kanso = "なし"
                has_kyofu = "なし"
                
                for w in warnings:
                    if w["code"] == "21" and w["status"] not in ["解除", "発表警報・注意報はなし"]:
                        has_kanso = "発表中"
                    if w["code"] == "18" and w["status"] not in ["解除", "発表警報・注意報はなし"]:
                        has_kyofu = "発表中"
                
                # 雨量はプロトタイプ用シミュレーション
                rain_3days = round(random.uniform(0.0, 2.0), 1)
                rain_30days = round(random.uniform(10.0, 40.0), 1)
                
                # 判定ロジック
                is_chuiho = (rain_3days <= 1.0 and rain_30days <= 30.0) or (rain_3days <= 1.0 and has_kanso == "発表中")
                
                if is_chuiho:
                    alert_level = "🔴 林野火災【警報】" if has_kyofu == "発表中" else "🟡 林野火災【注意報】"
                else:
                    alert_level = "🟢 平常"
                    
                results.append({
                    "判定日時": now,
                    "市町村名": city_name,
                    "判定結果": alert_level,
                    "乾燥注意報": has_kanso,
                    "強風注意報": has_kyofu,
                    "3日間雨量(mm)": rain_3days,
                    "30日間雨量(mm)": rain_30days
                })
            
            # --------------------------------------------------
            # 5. ダッシュボードへの結果描画
            # --------------------------------------------------
            if results:
                df = pd.DataFrame(results)
                
                # 表の表示
                st.subheader(f"📍 {selected_pref_name} の判定状況")
                st.dataframe(df, use_container_width=True)
                
                # グラフの表示
                st.subheader("📊 30日間降水量とリスク状況")
                fig, ax = plt.subplots(figsize=(12, 6))
                sns.set_theme(style="whitegrid", font="IPAexGothic")
                
                color_map = {"🟢 平常": "#2ca02c", "🟡 林野火災【注意報】": "#ff7f0e", "🔴 林野火災【警報】": "#d62728"}
                sns.barplot(data=df, x="市町村名", y="30日間雨量(mm)", hue="判定結果", palette=color_map, ax=ax, dodge=False)
                
                ax.axhline(y=30.0, color='red', linestyle='--', linewidth=2, label='注意報基準 (30mm以下)')
                plt.xticks(rotation=45, ha='right')
                plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
                plt.tight_layout()
                
                st.pyplot(fig)
                
            else:
                st.warning("データが取得できませんでした。")
                
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
