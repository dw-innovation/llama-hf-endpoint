from typing import Dict, List, Any
from transformers import AutoTokenizer, AutoModelForCausalLM


alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

 
class EndpointHandler:
    def __init__(self, path=""):
        # load model and processor from path
        self.model = AutoModelForCausalLM.from_pretrained(path, device_map="auto")
        self.tokenizer = AutoTokenizer.from_pretrained(path)

        with open(f"{path}/zero_shot_cot_prompt.txt", 'r') as file:
            self.instruction_prompt = file.read()

 
    def __call__(self, data: Dict[str, Any]) -> Dict[str, str]:
        sentence = data.pop("inputs",data)

        inputs = self.tokenizer(
            [
                alpaca_prompt.format(
                    self.instruction_prompt,  # instruction
                    sentence,  # input
                    "",  # output - leave this blank for generation!
                )
            ], return_tensors="pt")
        
        outputs = self.model.generate(**inputs,
                    max_new_tokens=1048,
                    use_cache=True,
                    top_p=0.1,
                    temperature=0.001)
        
        outputs = self.tokenizer.batch_decode(outputs)[0]
        response = outputs.split("### Response:")[1].split("<|end_of_text|>")[0]
 
        return [{"generated_text": response}]