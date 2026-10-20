import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="منصة يمن موبايل الذكية",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- تنسيق CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; }
.main-header { background: linear-gradient(90deg, #00A651 0%, #007A3D 100%); padding: 20px; border-radius: 15px; color: white; text-align: center; margin-bottom: 20px; }
.card { background: white; padding: 15px; border-radius: 10px; border-right: 5px solid #00A651; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>📱 منصة يمن موبايل الذكية</h1><p>نظام تحليل البيانات وخدمة العملاء - Yemen Mobile Smart Platform</p></div>', unsafe_allow_html=True)

# --- القائمة الجانبية ---
with st.sidebar:
    st.image("https://yemenmobile.com.ye/images/logo.png", width=150)
    st.title("القائمة الرئيسية")
    menu = st.radio("اختر الخدمة:", 
        ["📊 لوحة التحكم الرئيسية", "📦 تحليل الباقات", "👥 تحليل العملاء", "💬 نظام الشكاوى الذكي", "📈 التنبؤ بالإيرادات"])
    
    st.divider()
    st.info("المطور: bjahhmadh-ui\nحالة النظام: متصل 🟢")

# --- لوحة التحكم ---
if menu == "📊 لوحة التحكم الرئيسية":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("إجمالي المشتركين", "4.2 مليون", "+12%")
    col2.metric("إيرادات اليوم", "18.5 مليون ريال", "+5%")
    col3.metric("الشكاوى المفتوحة", "127", "-8%")
    col4.metric("نسبة رضا العملاء", "92%", "+2%")

    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("استهلاك البيانات حسب المحافظة")
        data = pd.DataFrame({
            'المحافظة': ['حضرموت', 'عدن', 'صنعاء', 'تعز', 'الحديدة', 'المكلا'],
            'الاستهلاك (TB)': [450, 380, 520, 210, 180, 310]
        })
        st.bar_chart(data.set_index('المحافظة'))
    
    with c2:
        st.subheader("توزيع أنواع الباقات")
        chart_data = pd.DataFrame({
            'الباقة': ['مزايا', 'انترنت', 'فورجي', 'دولي'],
            'النسبة': [45, 30, 15, 10]
        })
        st.dataframe(chart_data, use_container_width=True)
        st.progress(92, text="اكتمال الشبكة")

elif menu == "📦 تحليل الباقات":
    st.header("📦 محلل الباقات الذكي")
    st.write("أدخل استهلاك العميل لترشيح أفضل باقة يمن موبايل")
    
    col1, col2 = st.columns(2)
    with col1:
        internet = st.slider("استهلاك الانترنت (GB)", 0, 100, 15)
        calls = st.slider("دقائق الاتصال", 0, 1000, 200)
    with col2:
        sms = st.slider("عدد الرسائل", 0, 500, 50)
        budget = st.number_input("ميزانية العميل (ريال)", 1000, 20000, 5000)

    if st.button("اقتراح الباقة المناسبة"):
        if internet > 40:
            st.success("✅ الباقة المقترحة: باقة مزايا 40GB - فورجي سوبر - 8000 ريال")
        elif internet > 20:
            st.success("✅ الباقة المقترحة: باقة مزايا 20GB - 5000 ريال")
        else:
            st.success("✅ الباقة المقترحة: باقة مزايا 10GB - 3000 ريال")
        st.balloons()

elif menu == "👥 تحليل العملاء":
    st.header("تحليل سلوك العملاء")
    uploaded = st.file_uploader("ارفع ملف بيانات العملاء (CSV)", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df.head())
    else:
        st.info("مثال: سيتم عرض تحليل تلقائي")
        dummy = pd.DataFrame({
            'رقم': ['777xxxx01', '777xxxx02', '777xxxx03'],
            'الاستهلاك': [12, 45, 8],
            'خطر المغادرة': ['منخفض', 'مرتفع 🔴', 'منخفض']
        })
        st.table(dummy)

elif menu == "💬 نظام الشكاوى الذكي":
    st.header("نظام تصنيف الشكاوى التلقائي")
    complaint = st.text_area("اكتب شكوى العميل هنا:", "الانترنت بطيء في المكلا...")
    if st.button("تحليل الشكوى"):
        if "بطيء" in complaint or "نت" in complaint:
            st.warning("التصنيف: مشكلة شبكة - انترنت\nالأولوية: عالية\nالتحويل إلى: قسم الدعم الفني - حضرموت")
        elif "رصيد" in complaint:
            st.warning("التصنيف: مالي - رصيد\nالأولوية: متوسطة")
        else:
            st.info("التصنيف: عام\nسيتم الرد خلال 24 ساعة")

elif menu == "📈 التنبؤ بالإيرادات":
    st.header("التنبؤ بالإيرادات")
    months = st.slider("عدد الأشهر للتنبؤ", 1, 12, 3)
    base = 50000000
    forecast = [base + np.random.randint(-5000000, 10000000) for _ in range(months)]
    df_f = pd.DataFrame({"الشهر": [f"شهر {i+1}" for i in range(months)], "الإيراد المتوقع": forecast})
    st.line_chart(df_f.set_index("الشهر"))
    st.metric("إجمالي متوقع", f"{sum(forecast):,} ريال")

st.divider()
st.caption("© 2026 Yemen Mobile - منصة ذكية مطورة بواسطة bjahhmadh-ui - جميع الحقوق محفوظة")
