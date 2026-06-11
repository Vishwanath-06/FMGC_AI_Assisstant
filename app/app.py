import streamlit as st
from agent import create_fmcg_agent

st.set_page_config(page_title="FMCG AI Assistant", page_icon="📊", layout="wide")

st.title("🍹 FMCG AI Assistant")
st.markdown("Ask conversational questions about sales, promotions, inventory, and products.")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    provider = st.selectbox("LLM Provider", ["Google Gemini", "OpenAI"])
    api_key = st.text_input(f"{provider} API Key", type="password")
    
    st.markdown("---")
    st.markdown("""
    ### Example Questions:
    - What were the top 3 selling products last week?
    - How did the 'Price Cut' promotion affect 'Spark Lemon Sparkling Water' sales?
    - Which region has the highest revenue overall?
    - Were there any stockouts for Bolt Energy Drink?
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask about your FMCG data..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not api_key:
        with st.chat_message("assistant"):
            st.error("Please enter your API Key in the sidebar to continue.")
        st.session_state.messages.append({"role": "assistant", "content": "Please enter your API Key in the sidebar to continue."})
    else:
        with st.spinner("Analyzing data..."):
            try:
                # Initialize agent
                agent = create_fmcg_agent(provider, api_key)
                
                # Get response
                response = agent.invoke({"input": prompt})
                output = response["output"]
                
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(output)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": output})
                
            except Exception as e:
                with st.chat_message("assistant"):
                    st.error(f"An error occurred: {str(e)}")
                st.session_state.messages.append({"role": "assistant", "content": f"An error occurred: {str(e)}"})
