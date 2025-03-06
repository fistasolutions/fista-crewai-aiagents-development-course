from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BlogsCrew:
    """Blogs Crew"""
    agent_config = "config/agents.yaml"
    task_config = "config/tasks.yaml"

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
        )
    @task
    def write_blog(self) -> Task:
        return Task(
            config=self.tasks_config["write_blog"],
        )
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
