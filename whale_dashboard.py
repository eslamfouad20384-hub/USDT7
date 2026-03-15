import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="🦈 لوحة الحيتان الملونة", layout="wide")
st.title("🦈 لوحة تحكم الحيتان - النسخة المجمعة 23 مؤشر + أكبر 10 محافظ + التوصية الملونة")
st.markdown("كل المؤشرات + نشاط أكبر 10 محافظ + التوصية النهائية ملونة حسب الحالة")

# بيانات وهمية
market_cap = 800000000000
total_volume = 50000000000
fear_value = 35
whale_activity = {"BTC": 300, "ETH": 200, "SOL": 80, "ADA": 150, "TRX": 50}
whale_signal = "🟢 تجميع قوي"
top_wallets = {f"Wallet {i}": np.random.randint(1,1000) for i in range(1,11)}
support, resistance = 27, 37
whale_fear = 40
stable_in, stable_out = 3000000, 2000000
big_candle = True
trap_signal = "🟡 لا يوجد"
explosion_prob = 65
entry_signal = "🟢 دخول قوي"
strategy_signal = "🟢 تجمع"
manip_signal = "🟢 طبيعي"
final_signal = np.random.choice(["🟢 شراء","🔴 بيع","🟡 انتظر"])
volumes = np.random.randint(5000000000, 10000000000, size=7)
momentum = 55
daily_vol = 3500000000
whale_pct = 45
avg_price = 33
market_trend = "صاعد"
internal_liq = 60
price_deviation = -2

# جمع المؤشرات
indicators = {
    "السيولة العامة": f"${market_cap:,.0f}",
    "حجم التداول الإجمالي": f"${total_volume:,.0f}",
    "مؤشر الخوف والطمع": fear_value,
    "نشاط الحيتان": whale_activity,
    "تجميع الحيتان": whale_signal,
    "الدعم": support,
    "المقاومة": resistance,
    "مؤشر ضغط الحيتان": whale_fear,
    "تدفقات الستابل": f"{stable_in} داخل / {stable_out} خارج",
    "الشموع الكبيرة": big_candle,
    "كشف الفخاخ": trap_signal,
    "احتمال الانفجار": f"{explosion_prob}%",
    "أفضل لحظة دخول": entry_signal,
    "استراتيجية الحيتان": strategy_signal,
    "كشف التلاعب": manip_signal,
    "التوصية النهائية": final_signal,
    "رسم السيولة 7 أيام": "مرفق بالشارت",
    "مؤشر الزخم": momentum,
    "حجم التداول اليومي": daily_vol,
    "نسبة الحيتان": f"{whale_pct}%",
    "متوسط سعر 24 ساعة": avg_price,
    "اتجاه السوق": market_trend,
    "السيولة الداخلية": internal_liq,
    "انحراف السعر": price_deviation
}

df_summary = pd.DataFrame(list(indicators.items()), columns=["المؤشر", "القيمة"])
st.subheader("📋 جميع المؤشرات الرئيسية")

# تلوين التوصية النهائية
def color_final(val):
    if val == "🟢 شراء":
        return 'background-color: #99ff99; font-weight: bold'
    elif val == "🔴 بيع":
        return 'background-color: #ff4d4d; font-weight: bold'
    elif val == "🟡 انتظر":
        return 'background-color: #ffff66; font-weight: bold'
    return ''

st.dataframe(df_summary.style.applymap(lambda v: color_final(v) if v == final_signal else '', subset=["القيمة"]), use_container_width=True)

# جدول أكبر 10 محافظ مع تلوين حسب النشاط
st.subheader("🐋 نشاط أكبر 10 محافظ (ملون حسب النشاط)")
wallet_df = pd.DataFrame(list(top_wallets.items()), columns=["محفظة", "نشاط"])
def color_wallet(val):
    if val > 700:
        color = 'background-color: #ff4d4d'  # أحمر
    elif val > 300:
        color = 'background-color: #ffff66'  # أصفر
    else:
        color = 'background-color: #99ff99'  # أخضر
    return color
st.dataframe(wallet_df.style.applymap(color_wallet, subset=["نشاط"]), use_container_width=True)

# شارت السيولة آخر 7 أيام
st.subheader("📊 رسم السيولة خلال آخر 7 أيام")
dates = [datetime.today() - timedelta(days=i) for i in range(7)][::-1]
fig, ax = st.pyplot.subplots()
ax.plot(dates, volumes, marker='o')
ax.set_ylabel("السيولة بالدولار")
ax.set_xlabel("التاريخ")
ax.set_title("السيولة اليومية خلال 7 أيام")
st.pyplot(fig)

st.info("✨ كل المؤشرات + أكبر 10 محافظ + التوصية النهائية ملونة حسب الحالة + شارت السيولة.")
