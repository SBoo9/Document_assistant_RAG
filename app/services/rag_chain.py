from langchain.chains import RetrievalQA
from langchain.llms import huggingface_pipeline
from langchain.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForCasualLM, pipelines

def load_mistral():
    model_id='mistralai/Mistral-7B-Instruct-v0.1'
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model =  AutoModelForCasualLM.from_pretrained(model_id,device_maps='auto')

    pipe = pipelines(
        "Load Text",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )

    return huggingface_pipeline(pipeling=pipe)

def build_qa_chain(faiss_index: FAISS):
    llm= load_mistral()
    retreiver = faiss_index.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retreiver=retreiver,
        chain_type="stuff"
    )
    return qa_chain