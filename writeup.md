
## Project: Marketing Campaign Critic Platform

### Overview
This project aims to build a **web-based platform** where users can specify details for a marketing campaign (such as campaign name, company, target audience) and select a set of AI-driven agents with diverse demographics. The platform will simulate a critique and discussion session, generating feedback and insights from each agent's perspective, leveraging **Cerebras' high-performance AI capabilities** to ensure fast and accurate responses. This provides marketing teams with valuable, targeted feedback on how their campaign resonates with different demographic groups.

### Completed Tasks

1. **Initial Setup and Project Structure**:
   - **Repository Structure**: The project repository has been organized with directories for configuration files, code, and output reports.
   - **Requirements**: Dependencies are managed in `requirements.txt` for easy installation.
   - **CrewAI and Cerebras Setup**: CrewAI is integrated with Cerebras’ API to support high-speed inference and handle complex tasks, enabling the agents to provide rapid, nuanced feedback.

2. **Agent and Task Configuration**:
   - **Agents**: Five agents are configured to represent distinct demographic perspectives:
     - Young Adult Reviewer
     - Senior Reviewer
     - International Reviewer
     - Middle-Income Reviewer
     - Diverse Background Reviewer
   - **Tasks**: Task configurations in `tasks.yaml` outline the specific review tasks each agent performs, such as analyzing content appeal, cultural sensitivity, messaging clarity, and inclusivity.
   - **Cerebras-Powered Insights**: Each agent uses Cerebras’ LLM models to generate fast, accurate responses. By leveraging Cerebras’ high-speed processing, the agents can handle large inputs and provide real-time insights on complex campaigns, ensuring timely and relevant feedback.

3. **Main Execution Script**:
   - **Campaign Inputs**: `main.py` has been set up to accept input parameters for the campaign (such as campaign name, description, and target audience) and pass them to the CrewAI agents for review.
   - **Run Command**: The project supports running the crew with `crewai run`, utilizing Cerebras models for inference, which reduces processing times and enhances the quality of insights.

4. **Feedback Output**:
   - **Report Generation**: Feedback from agents is stored in a markdown file, `demographic_feedback_report.md`, summarizing insights from each agent’s perspective. The rapid response enabled by Cerebras ensures that reports are generated efficiently, even for complex campaigns requiring in-depth analysis.

### To-Do

#### 1. Develop the Front-End Interface
   - **Objective**: Create a user-friendly web interface where users can enter campaign details, specify the target audience, and select the number and type of agents (based on demographics).
   - **Tasks**:
     - Set up a local server using a web framework (e.g., Flask or Django).
     - Design input forms to capture campaign details (name, company, description) and target audience.
     - Create an interactive section for users to select agent demographics and preferences (e.g., ethnicity, age group).

#### 2. Back-End Integration with CrewAI and Cerebras
   - **Objective**: Link the web interface inputs to CrewAI and Cerebras, enabling dynamic agent configuration and real-time feedback generation.
   - **Tasks**:
     - Capture form data and map it to agent configuration (demographics and ethnicity).
     - Use Cerebras’ API to deploy and scale agents dynamically based on user-defined parameters.
     - Pass user-defined parameters to CrewAI, adjusting agent setup and task inputs, then trigger CrewAI to run the crew and return results to the web interface.

#### 3. Real-Time Agent Discussion Simulation
   - **Objective**: Enable a discussion simulation where agents generate responses to each other's feedback, creating a dynamic, multi-agent conversation.
   - **Tasks**:
     - Extend CrewAI tasks to allow agents to reference each other's feedback and generate follow-up comments, leveraging Cerebras for fast inference on complex dialogues.
     - Develop a looping mechanism where agents respond to a predefined number of conversational turns.
     - Format the output as a structured dialogue in the feedback report, enriched by the depth of Cerebras models.

#### 4. Display Results on the Web Interface
   - **Objective**: Present the generated feedback and discussion to users in a readable, organized format on the web interface.
   - **Tasks**:
     - Design result display sections on the web page, with agent feedback and discussion organized by demographic group.
     - Implement download functionality for users to export feedback as a PDF or markdown report.

### Role of Cerebras

Cerebras plays a crucial role in this platform by powering the AI agents with **high-speed language model inference**. This ensures that each agent can handle complex review tasks and produce rapid, accurate feedback. By integrating Cerebras’ API, the platform can:

- **Process Complex Marketing Content Efficiently**: Whether it’s an ad video, social media post, or full campaign description, Cerebras models can handle extensive input and generate insightful feedback faster than traditional setups.
- **Enable Real-Time, Multi-Agent Conversations**: With Cerebras’ rapid inference capabilities, the agents can engage in real-time discussions and provide follow-up responses, simulating a natural dialogue around the campaign.
- **Deliver High-Quality Insights**: Cerebras models ensure that agents provide nuanced, demographic-specific feedback, enhancing the relevance and actionability of the output for marketing teams.

### Future Enhancements (Optional)

- **Real-Time Analysis**: Enable real-time sentiment analysis or highlight key insights within the agent feedback, using Cerebras’ advanced NLP capabilities.
- **Expanded Agent Options**: Add more customization for agent personas (e.g., varied interests, additional demographics) to broaden the perspectives provided.

### Project Requirements

- **Technologies**: Python, CrewAI, Cerebras API, Flask/Django (for web), HTML/CSS/JavaScript (for front-end)
- **Libraries**: CrewAI, Cerebras, Pandas (optional for data handling), Flask or Django for web development
