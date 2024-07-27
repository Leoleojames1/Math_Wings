from langchain.agents import load_tools
tools = load_tools(
    [wikipedia, arxiv],
) 

tools


class ContentPreparationAgents:
    def __init__(self, llm):
        self.llm = llm

    # Define the agents involved in the content creation process
    def create_researcher(self,tools=[]):
        return Agent(
            role="Research Agent",

            backstory="""\
            Ray was a former investigative journalist who has a knack for uncovering the latest trends and insights.
            After years of digging deep into stories, Ray transitioned into the digital content world, leveraging his skills to help content creators stay ahead of the curve.""",
            
            goal="To provide comprehensive and up-to-date research that helps shape the direction of the channel’s content.",
            llm=self.llm,
            
            tools=tools,
            allow_delegation=False,
			verbose=True,
            full_output=True
        )

    def create_outline_writer(self,tools=[]):
        return Agent(
            role="Outline Creation Agent",
            backstory="""\
            Olivia was once a strategy consultant for major media firms, known for her ability to synthesize complex information into clear, actionable plans.
            She now uses her talents to help content creators map out their content effectively.""",

            goal="To create detailed and engaging outlines that guide the content creation process seamlessly.",
            llm=self.llm,
            tools=tools,
            allow_delegation=False,
			verbose=True,
            full_output=True
    )
    
    def create_content_agent(self, tools=[]):
        return Agent(
            role="Content Integration Agent",

            backstory="""\
            Chris has a background in library sciences and data management.
            His expertise in organizing and cross-referencing large volumes of information makes him perfect for ensuring new content fits well within existing frameworks.""",
            
            goal="To build a cohesive narrative by connecting new content with existing topics.",

            tools=tools,
            llm=self.llm,
            allow_delegation=False,
			verbose=True,
            full_output=True
        )

    def create_script_writer(self,tools=[]):
        return Agent(
        role="Script Writing Agent",
        backstory="""\
            Sam is a former screenwriter with experience in both film and digital media.
            His storytelling skills ensure that every piece of content is engaging and informative.""",

        goal="To craft scripts that are compelling and aligned with the channel's voice and vision.",
        tools=tools,
        llm=self.llm,
        allow_delegation=False,
		verbose=True,
        full_output=True
    )

    def create_visual_asset_creator(self,tools=[]):
        return Agent(
        role="Visual Asset Creation Agent",

        backstory="""\
        Vicky is a graphic designer and visual artist who has worked with numerous brands to create eye-catching visuals.
        Her ability to translate concepts into compelling visuals and their prompt is unparalleled.""",
        
        goal="To create visual assets that enhance the storytelling of the content.",
        tools=tools,
        llm=self.llm,
        allow_delegation=False,
		verbose=True,
        full_output=True
    )

    def create_social_media_agent(self,tools=[]):
        return Agent(
        role="Social Media and Community Engagement Agent",

        backstory="""\
        Casey is a social media strategist who has successfully managed online communities for various brands.
        With expertise in crafting engaging posts and interacting with audiences, Casey ensures that the content reaches and resonates with a wide audience.""",

        goal="To create and schedule engaging posts for Twitter and LinkedIn that promote the new video content effectively.",
        tools=tools,
        llm=self.llm,
        allow_delegation=False,
		verbose=True,
        full_output=True
    )
        
        
from crewai import Crew, Process

tasks = ContentPreparationTasks()
agents = ContentPreparationAgents(llm)

content_agent = agents.create_content_agent(tools)
outline_writer = agents.create_outline_writer(tools)
researcher = agents.create_researcher(tools)
script_writer = agents.create_script_writer(tools)
visual_asset_creator = agents.create_visual_asset_creator(tools)
social_media_agent = agents.create_social_media_agent(tools)

youtuber_crew = Crew(
    agents=[
        researcher,
        content_agent,
        outline_writer,
        researcher,
        script_writer,
        visual_asset_creator,
        social_media_agent
    ], 
    tasks=[
        tasks.research_task(researcher, "AI, Machine Learning, Neural Networks", "Artificial Intelligence"),

        tasks.outline_creation_task(outline_writer, "Backpropagation Algorithms", "Artificial Intelligence"),
            
        tasks.cross_reference_content_task(content_agent),

        tasks.script_writing_task(script_writer),

        tasks.visual_asset_task(visual_asset_creator),

        tasks.create_twitter_post_task(social_media_agent, "https://youtube.com/video"),
        tasks.create_linkedin_post_task(social_media_agent, "https://youtube.com/video")
    ],
    manager=llm,
    memory=True,
    verbose=True,
    output_log_file="interaction_logs.log",
    full_output=True,
    process=Process.sequential,
)

youtuber_crew.kickoff()