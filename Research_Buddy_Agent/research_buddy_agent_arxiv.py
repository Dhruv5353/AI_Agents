import os
import arxiv
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

for m in genai.list_models():
    print(m.name)

def suggest_research_ideas(domain):
    prompt = f"Suggest 5 innovative and practical research project ideas in the domain of {domain} for postgraduate students."
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # <-- updated model name
    response = model.generate_content(prompt)
    return response.text.strip()

def summarize_abstract(abstract):
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # <-- updated model name
    prompt = f"Summarize the following abstract in 3-4 lines:\n\n{abstract}"
    response = model.generate_content(prompt)
    return response.text.strip()

def fetch_arxiv_papers(query, max_results=3):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    return list(client.results(search))

def main():
    print("📚 Welcome to Research Buddy Agent (arXiv version)")
    domain = input("Enter your research domain (e.g., machine learning, bioinformatics): ")

    print("\n💡 Suggested Research Ideas:")
    print(suggest_research_ideas(domain))

    print("\n📖 Fetching relevant papers from arXiv...")
    papers = fetch_arxiv_papers(domain)

    for i, paper in enumerate(papers):
        print(f"\n🔹 Title {i+1}: {paper.title}")
        print(f"🔗 Link: {paper.entry_id}")
        print("📄 Summary:")
        print(summarize_abstract(paper.summary))

if __name__ == "__main__":
    main()
