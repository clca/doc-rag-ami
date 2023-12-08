
# docu-rag-ami

This template contains a reference architecture for Retrieval Augmented Generation against a set of documents using Docugami's XML Knowledge Graph (KG-RAG).


## Setup

You need to set the following environment variables before using your new app based on this template:

1. `OPENAI_API_KEY`: you can request one in the [openai site](https://platform.openai.com/account/api-keys).
2. `DOCUGAMI_API_KEY`: from the [Docugami Developer Playground](https://help.docugami.com/home/docugami-api)

```shell
export OPENAI_API_KEY=<openapi key>
export DOCUGAMI_API_KEY=<docugami api key>
```

### Process Documents in Docugami (before you use this template)

Before you use this template, you must have some documents already processed in Docugami. Here's what you need to get started:

1. Create a [Docugami workspace](https://app.docugami.com/) (free trials available)
2. Add your documents to Docugami for processing:
    - Upload via the simple Docugami web experience. [Detailed instructions](https://help.docugami.com/home/adding-documents).
    - Upload via the Docugami API, specifically the [documents](https://api-docs.docugami.com/#tag/documents/operation/upload-document) endpoint. In this case you need to get an access token via the Developer Playground for your workspace. [Detailed instructions](https://help.docugami.com/home/docugami-api). You can find code samples for python and JavaScript or use the [docugami](https://pypi.org/project/docugami/) python library.
3. Organize documents in DocSets: Docugami organizes documents in sets, you can either create a DocSet (Document Set) manually or let Docugami group them by similarity of content. Note: Docugami KG-RAG is currently limited to 1 DocSet so you should add all the documents that you want to query in the same Document Set.  
4. Monitor Processing status: before you can star querying documents, they all need to be fully processed by Docugami. You can monitor status in the Docugami webapp, or use a [webhook](https://api-docs.docugami.com/#tag/webhooks). 

You can also find detailed instruction on how to manage the upload and 'documents in ready state' process in the [Docugami RAG over XML Knowledge Graphs (KG-RAG) Cookbook](https://github.com/langchain-ai/langchain/blob/master/cookbook/docugami_xml_kg_rag.ipynb). 

## Usage

### Indexing
1. build your index in Chroma. See [index.py](./index.py) which you can run via `poetry run python index.py`. The CLI will query docsets in the workspace corresponding to your `DOCUGAMI_API_KEY` and let you pick which Document Sets you want to index. You can find more details on how the indexing process works in this [documentation](https://python.langchain.com/docs/integrations/document_loaders/do cugami) for details.


### Create an App
2. Install LangChain CLI :

```shell
pip install -U langchain-cli
```

3. Create a new LangChain project:

```shell
langchain app new my-app --package git+https://github.com/docugami/langchain-template-docugami-kg-rag.git
```

If you want to add this to an existing project:

```shell
langchain app add git+https://github.com/docugami/langchain-template-docugami-kg-rag.git
```

4. Add the following code to your `my-app/app/server.py` file:
```python
from docugami_kg_rag import chain as docugami_kg_rag_chain

add_routes(app, docugami_kg_rag, path="/docugami-kg-rag")
```

[Optional] configure LangSmith to trace, monitor and debug LangChain applications. 
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/). 

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

### Running app
5. From inside the app directory, spin up a LangServe instance:

```shell
langchain serve
```
* Playground at [http://127.0.0.1:8000/playground](http://127.0.0.1:8000/playground)
* FastAPI app at [http://localhost:8000](http://localhost:8000)
* All templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can access the template from code with:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/docugami-kg-rag")
```
