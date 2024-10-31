from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os

# Define the LLM with the updated model and API key
llm = LLM(
    model="cerebras/llama3.1-8b",  # Replace with accessible model if 8b is restricted
    base_url="https://api.cerebras.ai/v1",
    api_key=os.getenv("CEREBRAS_API_KEY")  # Use environment variable for security
)

@CrewBase
class MarketingCampaignReviewerCrew():
    """MarketingCampaignReviewer crew with demographic-specific agents for campaign critique."""

    # Define each agent representing a different demographic group
    @agent
    def young_adult_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['young_adult_reviewer'],
            verbose=True,
            llm=llm
        )

    @agent
    def senior_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_reviewer'],
            verbose=True,
            llm=llm
        )

    @agent
    def international_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['international_reviewer'],
            verbose=True,
            llm=llm
        )

    @agent
    def middle_income_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['middle_income_reviewer'],
            verbose=True,
            llm=llm
        )

    @agent
    def diverse_background_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['diverse_background_reviewer'],
            verbose=True,
            llm=llm
        )

    # Define tasks that these agents will carry out
    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
            output_file='demographic_feedback_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingCampaignReviewer crew with demographic-specific agents."""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Reviews processed one after another
            verbose=True,
            # process=Process.parallel, # Use parallel if simultaneous reviews are needed
        )
