import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import research_agent, writer_agent

# Setup Crew
if "crew" not in st.session_state:
    st.session_state.crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_task],
    process=Process.sequential
    )

# Streamlit UI
st.set_page_config(page_title="🎓 AI Education Chatbot", layout="centered")
st.title("🤖 AI in Education Assistant")
st.markdown("Ask a topic, and our agents will research & generate insights.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# User input
# topic = st.chat_input("Enter a topic:", placeholder="e.g. Impacts of AI in Modern Education")

if topic := st.chat_input("Ask your Web Research question here..."):
    
    if topic:
        st.session_state.messages.append({"role": "user", "content": topic})
        with st.chat_message("user"):
            st.markdown(topic)
        with st.spinner("Agents are working..."):
            result = st.session_state.crew .kickoff(inputs={'topic': topic})
            st.session_state.messages.append({"role": "assistant", "content": result})
            with st.expander("Click to check with output"):
                st.text_area("Agent Output", result, height=400)
                # with st.button("Download readMd File"):
                #     st.session_state.messages = []
                #     st.experimental_rerun()
            with st.chat_message("assistant"):
                st.markdown("Mission Accomplished")
        
    else:
        st.warning("Please enter a topic.")

