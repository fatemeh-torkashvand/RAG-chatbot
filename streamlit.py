import streamlit as st
from rag import query


# Page Config 
st.set_page_config(
    page_title="Floriashop",
    page_icon="🛍️",
    layout="centered"
)


# RTL + Style 
st.markdown("""
<style>
    /* کل صفحه راست‌چین */
    .stApp, .main, .block-container, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
    }
    
    /* فونت */
    html, body, [class*="css"] {
        font-family: Tahoma, sans-serif;
    }
    
    /* پیام‌های چت */
    [data-testid="stChatMessage"] {
        direction: rtl;
        text-align: right;
    }
    
    [data-testid="stChatMessage"] p {
        direction: rtl;
        text-align: right;
    }
    
    /* Input چت */
    .stChatInput textarea,
    [data-testid="stChatInput"] textarea {
        direction: rtl;
        text-align: right;
        font-family: Tahoma, sans-serif;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        direction: rtl;
        text-align: right;
    }
    
    section[data-testid="stSidebar"] * {
        direction: rtl;
        text-align: right;
    }
    
    /* Expander */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] summary {
        direction: rtl;
        text-align: right;
    }
    
    /* Caption (زمان) */
    .stCaption, [data-testid="stCaptionContainer"] {
        direction: rtl;
        text-align: right;
    }
    
    /* Spinner */
    .stSpinner {
        direction: rtl;
        text-align: right;
    }
    
    /* عنوان */
    h1 {
        color: #8e24aa;
        text-align: center;
        font-family: Tahoma, sans-serif;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        margin-bottom: 2rem;
    }
    
    /* دکمه */
    .stButton button {
        background: #8e24aa;
        color: white;
        border: none;
        border-radius: 8px;
        font-family: Tahoma, sans-serif;
    }
    
    .stButton button:hover {
        background: #6a1b9a;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


#  Header 
st.title("🛍️ Floriashop")
st.markdown('<div class="subtitle">آرایشی، دیجیتال و اکسسوری</div>', unsafe_allow_html=True)
st.divider()


#  Sidebar 
with st.sidebar:
    st.header("درباره Floriashop")
    st.write("""
    فروشگاه آنلاین.
    
    محصولات:
    - آرایشی و بهداشتی
    - دیجیتال و لوازم جانبی
    - اکسسوری و زیورآلات
    
    خدمات:
    - ارسال سریع به سراسر کشور
    - ۷ روز ضمانت بازگشت
    - ضمانت اصالت کالا
    """)

    st.divider()
    
    if st.button("پاک کردن تاریخچه", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.caption("نسخه ۱.۰")


#  Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


#  Input
if prompt := st.chat_input("سوال خود را بنویسید..."):

    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("در حال جستجو..."):
            result = query(prompt)
        
        st.write(result["answer"])
        st.caption(f"زمان پاسخ: {result['latency']} ثانیه")
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"]
    })