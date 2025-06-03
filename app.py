import streamlit as st

# بيانات الأطعمة
food_data = {
    'دجاج': {'calories': 1.65, 'protein': 0.309, 'carbs': 0, 'fat': 0.352},
    'لحم': {'calories': 2.89, 'protein': 0.24, 'carbs': 0, 'fat': 0.207},
    'سمك': {'calories': 2.1, 'protein': 0.237, 'carbs': 0, 'fat': 1.3},
    'أرز': {'calories': 1.3, 'protein': 0.027, 'carbs': 0.28, 'fat': 0.0028},
    'بيض': {'calories': 1.55, 'protein': 0.126, 'carbs': 0.012, 'fat': 0.106},
    'بطاطس': {'calories': 0.77, 'protein': 0.02, 'carbs': 0.174, 'fat': 0.00094},
    'لبن': {'calories': 0.64, 'protein': 0.035, 'carbs': 0.055, 'fat': 0.03},
    'سلطه': {'calories': 0.396, 'protein': 0.0093, 'carbs': 0.045, 'fat': 0.0186},
    'عدس': {'calories': 1.16, 'protein': 0.009, 'carbs': 0.202, 'fat': 0.00404},
    'معكرونه': {'calories': 1.41, 'protein': 0.0477, 'carbs': 0.2835, 'fat': 0.0064},
    'شوفان': {'calories': 3.85, 'protein': 0.25, 'carbs': 0.66, 'fat': 0.024},
    'زبده فول': {'calories': 6.25, 'protein': 0.25, 'carbs': 0.1875, 'fat': 0.53125},
    'سودانى': {'calories': 5.674, 'protein': 0.258, 'carbs': 0.161, 'fat': 0.492},
    'فول صويا': {'calories': 1.73, 'protein': 0.16627, 'carbs': 0.099, 'fat': 0.0895},
    'موز': {'calories': 0.8898, 'protein': 0.011, 'carbs': 0.2288, 'fat': 0.00338},
    'عسل': {'calories': 3.038, 'protein': 0.00285, 'carbs': 0.8238, 'fat': 0},
    'تمر': {'calories': 2.3883, 'protein': 0.0283, 'carbs': 0.625, 'fat': 0.00583},
    'تفاح': {'calories': 0.52, 'protein': 0.00289, 'carbs': 0.1384, 'fat': 0.00145},
    'عصير برتقال': {'calories': 0.5052, 'protein': 0, 'carbs': 0.1276, 'fat': 0},
    'حمص': {'calories': 1.657, 'protein': 0.0785, 'carbs': 0.1428, 'fat': 0.09285},
    'واى': {'calories': 3.8235, 'protein': 0.706, 'carbs': 0, 'fat': 0},
    'لبن خ': {'calories': 0.36, 'protein': 0.033, 'carbs': 0.052, 'fat': 0.002},
}

# تهيئة الجلسة
if "total_calories" not in st.session_state:
    st.session_state.total_calories = 0
    st.session_state.total_protein = 0
    st.session_state.total_carbs = 0
    st.session_state.total_fat = 0

st.title("🔥 حساب السعرات الحرارية والعناصر الغذائية")

# Tabs
tab1, tab2 = st.tabs(["🍽️ أضف طعام", "📊 حساب الاحتياج اليومي"])

with tab1:
    st.subheader("أضف طعام:")
    food = st.selectbox("اختر نوع الطعام", list(food_data.keys()))
    quantity = st.number_input("الكمية (بالجرام)", min_value=0.0, step=10.0)

    if st.button("إضافة"):
        if food in food_data:
            data = food_data[food]
            st.session_state.total_calories += data['calories'] * quantity
            st.session_state.total_protein += data['protein'] * quantity
            st.session_state.total_carbs += data['carbs'] * quantity
            st.session_state.total_fat += data['fat'] * quantity
            st.success("تمت الإضافة بنجاح")

    st.markdown("---")
    st.subheader("الإجمالي:")
    st.info(f"🍛 السعرات الحرارية: {st.session_state.total_calories:.2f} kcal")
    st.info(f"💪 البروتين: {st.session_state.total_protein:.2f} g")
    st.info(f"🍞 الكربوهيدرات: {st.session_state.total_carbs:.2f} g")
    st.info(f"🧈 الدهون: {st.session_state.total_fat:.2f} g")

    if st.button("🔄 إعادة تعيين"):
        for key in ["total_calories", "total_protein", "total_carbs", "total_fat"]:
            st.session_state[key] = 0
        st.success("تم إعادة التعيين")

with tab2:
    st.subheader("أدخل بياناتك:")
    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input("📏 الطول (سم)", min_value=50.0)
        weight = st.number_input("⚖️ الوزن (كجم)", min_value=20.0)
        age = st.number_input("📅 العمر (سنة)", min_value=10)
    with col2:
        gender = st.selectbox("👤 النوع", ["ذكر", "أنثى"])
        goal = st.radio("🎯 الهدف", ["زيادة الوزن", "نقصان الوزن"])

    activity_factor = st.selectbox("⚡ مستوى النشاط", [
        "غير نشيط (قليل أو لا تمارين)",
        "خفيف (1-3 أيام)",
        "متوسط (3-5 أيام)",
        "عالي (6-7 أيام)",
        "شديد جدًا (عمل بدني)"
    ])

    factor_values = {
        "غير نشيط (قليل أو لا تمارين)": 1.2,
        "خفيف (1-3 أيام)": 1.375,
        "متوسط (3-5 أيام)": 1.55,
        "عالي (6-7 أيام)": 1.725,
        "شديد جدًا (عمل بدني)": 1.9,
    }

    if st.button("احسب الاحتياج"):
        try:
            g = 'male' if gender == "ذكر" else 'female'
            f = factor_values[activity_factor]

            if g == 'male':
                bmr = (13.397 * weight) + (4.799 * height) - (5.677 * age) + 88.362
            else:
                bmr = (9.247 * weight) + (3.098 * height) - (4.330 * age) + 447.593

            total = bmr * f
            if goal == "زيادة الوزن":
                total += 500
            else:
                total -= 500

            protein = (0.25 * total) / 4
            carbs = (0.65 * total) / 4
            fat = (0.10 * total) / 9

            st.success(f"""
            ✅ إجمالي السعرات المطلوبة: {total:.2f} kcal  
            💪 بروتين: {protein:.2f} g  
            🍞 كارب: {carbs:.2f} g  
            🧈 دهون: {fat:.2f} g  
            """)
        except:
            st.warning("⚠️ الرجاء التأكد من إدخال بيانات صحيحة.")