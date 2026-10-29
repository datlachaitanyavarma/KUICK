import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="KUICK - The Super App", page_icon="🚀", layout="centered")

# Initialize Session State for Data Storage (Simulation)
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "tweets" not in st.session_state:
    st.session_state.tweets = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "posts" not in st.session_state:
    st.session_state.posts = []

st.title("🚀 KUICK: The Physical World, On Demand")
st.markdown("**(Delivery + Chat + Pulse Feed + Visual Portfolio)**")

# Create 4 Tabs for the 4 Pillars
tab1, tab2, tab3, tab4 = st.tabs(["📦 Delivery", "💬 Chat (WhatsApp)", "🐦 Pulse (Twitter)", "📸 Portfolio (Insta)"])

# ==========================================
# TAB 1: DELIVERY & TASKS (Core Engine)
# ==========================================
with tab1:
    st.header("Post a Physical Task")
    with st.form("task_form"):
        task_title = st.text_input("What do you need? (e.g., Get medicines, RTO line)")
        location = st.text_input("Location (e.g., MVP Colony)")
        budget = st.number_input("Budget (₹)", min_value=50, step=10)
        submitted = st.form_submit_button("Post Task")
        
        if submitted and task_title:
            st.session_state.tasks.append({
                "task": task_title, "location": location, "budget": budget, "status": "Pending Match"
            })
            st.success("Task Posted Successfully!")

    st.divider()
    st.subheader("Live Task Board")
    if st.session_state.tasks:
        df_tasks = pd.DataFrame(st.session_state.tasks)
        st.dataframe(df_tasks, use_container_width=True)
    else:
        st.info("No active tasks in your area yet.")

# ==========================================
# TAB 2: SECURE CHAT (WhatsApp Alternative)
# ==========================================
with tab2:
    st.header("Secure Task Chat")
    st.caption("End-to-End Encrypted Coordination")
    
    # Display Chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Chat Input
    chat_input = st.chat_input("Message your worker/customer...")
    if chat_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": chat_input})
        st.rerun()

# ==========================================
# TAB 3: PULSE FEED (Twitter Alternative)
# ==========================================
with tab3:
    st.header("Local Vizag Pulse")
    st.caption("Real-time updates, local needs, and broadcasts")
    
    tweet_text = st.text_area("What's happening in Vizag?", max_chars=280)
    if st.button("Broadcast"):
        if tweet_text:
            st.session_state.tweets.insert(0, {
                "time": datetime.now().strftime("%I:%M %p"),
                "text": tweet_text
            })
            st.success("Broadcasted!")
            
    st.divider()
    for t in st.session_state.tweets:
        st.markdown(f"**@LocalUser** ‧ {t['time']}")
        st.write(t['text'])
        st.markdown("💬 🔄 ❤️")
        st.divider()

# ==========================================
# TAB 4: VISUAL PORTFOLIO (Instagram Alternative)
# ==========================================
with tab4:
    st.header("Worker & Business Portfolios")
    st.caption("Discover local talent and products visually")
    
    uploaded_file = st.file_uploader("Upload a photo/video of your work", type=["jpg", "png", "mp4"])
    caption = st.text_input("Caption")
    
    if st.button("Post to Portfolio"):
        if uploaded_file is not None:
            st.session_state.posts.insert(0, {"file": uploaded_file, "caption": caption})
            st.success("Posted!")
            
    st.divider()
    
    # Display Posts in a Grid Simulation
    for post in st.session_state.posts:
        st.image(post["file"], use_container_width=True)
        st.write(f"**@WorkerPro** {post['caption']}")
        st.button("Book this Worker 📦", key=post["caption"])
        st.divider()
      
