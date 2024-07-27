from langchain_community.utilities import WikipediaAPIWrapper

class WikipediaQueryRun(BaseTool):
    """Tool that searches the Wikipedia API."""

    name: str = "wikipedia"
    description: str = (
        "A wrapper around Wikipedia. "
        "Useful for when you need to answer general questions about "
        "people, places, companies, facts, historical events, or other subjects. "
        "Input should be a search query. Only use described arguments."
    )
    api_wrapper: WikipediaAPIWrapper

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Wikipedia tool."""
        return self.api_wrapper.run(query)

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=512))
wikipedia_docs = wikipedia.run("backpropagation algorithms")

display(Markdown(f"## Research Papers on the Topic\n\n{wikipedia_docs}"))