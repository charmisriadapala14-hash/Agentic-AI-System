import streamlit as st
from openai import OpenAI

st.set_page_config(
page_title="Agentic AI System",
page_icon="🤖"
)

st.title("🤖 Agentic AI System")
st.write("An AI system that uses agents to plan, execute and review tasks.")

api_key = st.sidebar.text_input(
"OpenRouter API Key",
type="password"
)

task = st.text_area(
"Enter Your Task",
placeholder="Example: Explain Artificial Intelligence"
)

def run_agent(client, role, task):
response = client.chat.completions.create(
model="openai/gpt-4o-mini",
messages=[
{
"role": "system",
"content": role
},
{
"role": "user",
"content": task
}
]
)

return response.choices[0].message.content

if st.button("Run AI Agents"):

if not api_key or not task.strip():
    st.warning("Please enter API key and task.")

else:
    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        with st.spinner("Planner Agent is creating a plan..."):
            plan = run_agent(
                client,
                "You are a planning agent. Break the user's task into clear steps.",
                task
            )

        with st.spinner("Execution Agent is completing the task..."):
            result = run_agent(
                client,
                "You are an execution agent. Complete the task using the provided plan.",
                f"Task: {task}\nPlan:\n{plan}"
            )

        with st.spinner("Review Agent is reviewing the result..."):
            review = run_agent(
                client,
                "You are a review agent. Check the result for clarity and completeness. Do not invent facts.",
                f"Task: {task}\nResult:\n{result}"
            )

        st.subheader("📋 Planner Agent")
        st.write(plan)

        st.subheader("⚙️ Execution Agent")
        st.write(result)

        st.subheader("🔍 Review Agent")
        st.write(review)

    except Exception as e:
        st.error(f"Error: {e}")
