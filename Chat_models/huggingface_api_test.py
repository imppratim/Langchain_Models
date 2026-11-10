from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

selected_llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    device=-1,  
    pipeline_kwargs={
        "max_new_tokens": 100,
        "do_sample": False,
        "return_full_text": True,
    },
)
model = ChatHuggingFace(llm=selected_llm)

model_output = model.invoke("Do people in australia eat pork?")

print(model_output.content)
