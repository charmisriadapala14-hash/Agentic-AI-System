from agents import (
    research_agent,
    planning_agent,
    execution_agent,
    review_agent
)

from memory import agent_memory


class AgentOrchestrator:

    def run_workflow(self, task):

        results = {}

        # Step 1: Research
        research = research_agent.execute(task)
        results["Research"] = research

        # Step 2: Planning
        planning = planning_agent.execute(
            f"Create an action plan based on this research:\n{research}"
        )
        results["Planning"] = planning

        # Step 3: Execution
        execution = execution_agent.execute(
            f"Execute this plan:\n{planning}"
        )
        results["Execution"] = execution

        # Step 4: Review
        review = review_agent.execute(
            f"Review and improve this result:\n{execution}"
        )
        results["Review"] = review

        # Save to memory
        agent_memory.add_memory(task, review)

        return results


orchestrator = AgentOrchestrator()
