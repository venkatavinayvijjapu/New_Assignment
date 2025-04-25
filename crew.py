from crewai import Crew, Process
from tasks import research_task, write_task
from agents import research_agent, writer_agent

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={'topic': 'Impacts of AI in Modern Education'})
print(result)
