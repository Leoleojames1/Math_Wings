"""Tool for the Arxiv API."""

from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool

from langchain_community.utilities.arxiv import ArxivAPIWrapper


class ArxivInput(BaseModel):
    """Input for the Arxiv tool."""
    query: str = Field(description="search query to look up, max 5 words")


# you have ArxivQueryRun: taking as arguments: query and max_results
#"A wrapper around Arxiv.org "
#"Useful for when you need to answer questions about Artificial Inteligence, Machine Physics, Mathematics, "
#"Computer Science, Quantitative Biology, Quantitative Finance, Statistics, "
#"Electrical Engineering, and Economics "
#"from scientific articles on arxiv.org. "
#"Input should be a search query using parameter query."

# param: query: str = "cat=cs.AI and dying neurons"
# param: max_results: int = 5



class ArxivQueryRun(BaseTool):
    """Tool that searches the Arxiv API."""

    name: str = "arxiv"
    description: str = (
        "A wrapper around Arxiv.org "
        "Useful for when you need to answer questions about Physics, Mathematics, "
        "Computer Science, Quantitative Biology, Quantitative Finance, Statistics, "
        "Electrical Engineering, and Economics "
        "from scientific articles on arxiv.org. "
        "Input should be a query of keywords to search for using parameter query."
        "Only use described arguments"
    )
    api_wrapper: ArxivAPIWrapper = Field(default_factory=ArxivAPIWrapper)
    args_schema: Type[BaseModel] = ArxivInput

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Arxiv tool."""
        return self.api_wrapper.run(query)
arxiv = ArxivQueryRun(api_wrapper=ArxivAPIWrapper(doc_content_chars_max=512, load_max_docs=2)) 

docs = arxiv.run("cat=cs.AI and dying neurons")
docs

display(Markdown(f"## Research Papers on the Topic\n\n{docs}"))