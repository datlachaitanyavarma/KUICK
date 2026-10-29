import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="KUICK Super App", page_icon="🚀", layout="centered")

# --- CUSTOM CSS FOR MOBILE LOOK ---
st.markdown("""
<style>
    /* Hide Streamlit default top menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Mobile container simulation */
    .block-container {
        max-width: 480px;
        padding-top: 1rem;
        padding-bottom: 80px; /* Space for bottom nav */
    }
    
    /* Instagram-like Stories CSS */
    .story-container {
        display: flex;
        overflow-x: auto;
        padding-bottom: 10px;
    }
    .story {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-right: 15px;
    }
    .story-circle {
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
        padding: 3px;
    }
    .story-inner {
        width: 100%;
        height: 100%;
        background-color: white;
        border-radius: 50%;
        border: 2px solid white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }
    .story-text {
        font-size: 10px;
        margin-top: 5px;
        color: #fff;
    }
    
    /* Feed Placeholder */
    .reel-placeholder {
        background-color: #1e1e1e;
        border-radius: 10px;
        height: 500px;
        margin-top: 15px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 15px;
        color: white;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# --- BOTTOM NAVIGATION BAR ---
# Using option_menu at the very bottom of the logic
selected = option_menu(
    menu_title=None,
    options=["Chat", "Content", "Pulse", "KUICK"],
    icons=["whatsapp", "instagram", "twitter", "box-seam"],
    menu_icon="cast",
    default_index=3,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#000000", "border-top": "1px solid #333", "position": "fixed", "bottom": "0", "max-width": "480px", "z-index": "999"},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"font-size": "12px", "text-align": "center", "margin":"0px", "--hover-color": "#333", "color": "white"},
        "nav-link-selected": {"background-color": "#E50914"},
    }
)

# --- TAB 1: CHAT (WhatsApp Like) ---
if selected == "Chat":
    st.header("💬 Chat")
    st.caption("End-to-End Encrypted Messaging")
    st.info("Your conversations with clients and gig workers will appear here.")
    
    # Mock Chat
    st.markdown("**Gig Worker (Ramu):** I have reached the location.")
    st.markdown("**You:** Please check if the store is open.")

# --- TAB 2: CONTENT (Instagram Like) ---
if selected == "Content":
    st.header("📸 Reels & Portfolio")
    
    # Stories UI matching your screenshot
    st.markdown("""
    <div class="story-container">
        <div class="story">
            <div class="story-circle"><div class="story-inner">➕</div></div>
            <div class="story-text" style="color: black;">Your story</div>
        </div>
        <div class="story">
            <div class="story-circle"><div class="story-inner">👨‍🔧</div></div>
            <div class="story-text" style="color: black;">carpenter_vizag</div>
        </div>
        <div class="story">
            <div class="story-circle"><div class="story-inner">👩‍🍳</div></div>
            <div class="story-text" style="color: black;">home_baker</div>
        </div>
        <div class="story">
            <div class="story-circle"><div class="story-inner">🛵</div></div>
            <div class="story-text" style="color: black;">delivery_pro</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Reel/Feed UI
    st.markdown("""
    <div class="reel-placeholder">
        <h3>Interior Design Setup in MVP Colony 🛋️</h3>
        <p>Book this service directly below.</p>
        <button style="background: #E50914; color: white; border: none; padding: 10px; border-radius: 5px;">Book via KUICK</button>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 3: PULSE (Twitter Like) ---
if selected == "Pulse":
    st.header("🐦 Vizag Pulse")
    st.text_area("Post a public request...", placeholder="Need someone to deliver a laptop to Dwaraka Nagar in 30 mins...")
    st.button("Broadcast Request")
    st.divider()
    st.markdown("**@TechStore_Vizag** ‧ 2m ago\nNeed a quick document pickup from Siripuram. ₹150.\n\n👍 12 💬 2")

# --- TAB 4: KUICK (Delivery/Task Engine) ---
if selected == "KUICK":
    st.title("🚀 KUICK Tasks")
    st.subheader("The Physical World, On Demand.")
    
    with st.form("task_engine"):
        st.text_input("What do you need done?")
        st.text_input("Location")
        col1, col2 = st.columns(2)
        with col1:
            st.number_input("Budget (₹)", min_value=50, step=10)
        with col2:
            st.selectbox("Urgency", ["Flexible", "Within 1 Hour", "ASAP"])
        st.form_submit_button("Find a Worker", use_container_width=True)
        
