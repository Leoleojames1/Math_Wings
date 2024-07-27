""" crew_tasks.py

"""
from crewai import Agent, Task
from textwrap import dedent
import os
from langchain_community.chat_models.ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain.callbacks import LangChainTracer
from langsmith import Client


# optional
from agentops.langchain_callback_handler import LangchainCallbackHandler as AgentOpsLangchainCallbackHandler
agentops_handler = AgentOpsLangchainCallbackHandler(api_key=os.environ.get('AGENTOPS_API_KEY'), tags=['CrewAI Example'])

langchain_tracer = LangChainTracer(project_name="CrewAI Example")
from IPython.display import display, Markdown

llm = ChatOllama(model="phi3",
    n_ctx=4096,
    temperature=0.9,
)

class ContentPreparationTasks():
    def research_task(self, agent, topics, subject):
        return Task(
            description=dedent(f"""\
Conduct comprehensive research on each topic already covered by my channel. Gather information on recent
news, trends and research papers about the Channel Topic.
Identify potential gaps and new directions for future content.
                        
                Topics: {topics}
                Channel Subject: {subject}"""),
            expected_output=dedent("""\
A detailed report summarizing new topics and directions to consider
for new content relevant to the channel subject."""),
            async_execution=False,
            agent=agent, 
        )

    def outline_creation_task(self, agent, new_topic, subject):
        return Task(
            description=dedent(f"""\
Analyze the current industry trends, challenges, and opportunities
relevant to the channel subject. Consider research papers, reports, recent
developments, and expert opinions to provide a comprehensive
overview of the {new_topic} for my channel about: {subject}.
Identify major trends, potential challenges, and future advancements."""),
            expected_output=dedent(f"""\
An insightful and engaging outline for content on my channel about '{subject}' that identifies major trends, potential
challenges, and future advancements about {new_topic}."""),
            async_execution=False,
            agent=agent, 
        )
	
    def cross_reference_content_task(self, agent):
        return Task(
            description=dedent("""\
Analyze the current topics and the outline of the topic to create a comprehensive
list of cross-references, and connections between the new topics and the existing ones.
This will help in creating a cohesive and well-structured narrative.

## Topics
{topics}

## New Topic
{new_topic}

## New Outline:
{new_outline}
"""),
                
            expected_output=dedent("""\
An comprehensive list of cross-references and connections between the new topics.
                """),
            async_execution=False,
            agent=agent, 
        )

    def script_writing_task(self, agent):
        return Task(
            description=dedent("""\
Develop a detailed script based on the provided outline. Ensure the script
is engaging, informative, and aligns with the overall tone and style of the channel.
Incorporate any relevant research findings and expert opinions to add depth and credibility.

##Topic 
{new_topic}

## Outline
{outline}

## Channel Subject
{subject}
            """),
            expected_output=dedent("""\
                A complete and polished script ready for production, including all necessary dialogue, transitions,
                and references to research and expert opinions, using markdown format."""),
            async_execution=False,
            agent=agent,
        )

    def visual_asset_task(self, agent):
        return Task(
            description=dedent("""\
Identify and create visual assets required for the video based on the script.
This includes images, graphics, charts, and any other visual elements that
will enhance the storytelling and provide clear, engaging content for viewers.

## Script 
{script}
                               
## Channel Subject
{subject}
            """),
            expected_output=dedent("""\
A collection of prompts to create visual assets, including images, graphics, charts, and other visual elements, ready to be
incorporated into the video production process.
            """),   
            async_execution=False,
            agent=agent,
            
        )
    
    def create_twitter_post_task(self, agent, video_url):
        return Task(
            description=dedent(f"""\
Create an engaging Twitter post to promote the newly published video. The post should include a compelling
description, relevant hashtags, and a link to the video. Respect the 140 character limit and use appropriate hashtags. 

## Video Title                               

## Video URL
{video_url}

## Channel Subject

{{subject}}
"""),
            expected_output=dedent("""\
A ready-to-publish Twitter post that includes an engaging description, relevant hashtags, and a link to the video.
Respect the 140 character limit and use appropriate hashtags.
"""),
            async_execution=False,
            agent=agent
        )

    def create_linkedin_post_task(self, agent, video_url):
        return Task(
            description=dedent(f"""\
Create an engaging LinkedIn post to promote the newly published video. The post should include a professional
description, relevant hashtags, and a link to the video. Consider the LinkedIn audience and tailor the content
to suit a professional network.

## Video URL
{video_url}
## Channel Subject
{{subject}}
            """),
            expected_output=dedent("""\
A ready-to-publish LinkedIn post that includes a professional description, relevant hashtags, and a link to the video."""),
            async_execution=False,
            agent=agent
        )

    