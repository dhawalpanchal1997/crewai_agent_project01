from crewai import Agent, LLM
from tools import tool

llm = LLM(model="gemini/gemini-2.0-flash", temperature=0.5, verbose=True,
          api_key= "AIzaSyCNsQK1yHPiaSNy8mYhenG8bInhL1rsMUM")

# Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    memory=True,
    verbose=True,
    backstory='''Driven by curiosity, you're at the forefront of.innovation, eager to explore and share knowledge that could change the world.''',
    tools=[tool],
    llm=llm,
    allow_deletion=True
)

# Creating a writer agent with custom tools responsible in writing news blog
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
