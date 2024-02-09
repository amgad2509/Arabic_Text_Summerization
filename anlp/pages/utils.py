import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
m_name = "marefa-nlp/summarization-arabic-english-news" 
tokenizer = AutoTokenizer.from_pretrained(m_name)        
model_nlp = AutoModelWithLMHead.from_pretrained(m_name).to(device)

def get_summary(text, tokenizer, model_nlp, device="cpu", num_beams=2):
    if len(text.strip()) < 50:
        return ["Please provide more longer text"]
    
    text = "summarize: <paragraph> " + " <paragraph> ".join([ s.strip() for s in sent_tokenize(text) if s.strip() != ""]) + " </s>"
    text = text.strip().replace("\n","")
    
    tokenized_text = tokenizer.encode(text, return_tensors="pt").to(device)
    
    summary_ids = model_nlp.generate(
            tokenized_text,
            max_length=512,
            num_beams=num_beams,
            repetition_penalty=1.5, 
            length_penalty=1.0, 
            early_stopping=True
    )
    
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    #result = [ s.strip() for s in output.split("<hl>") if s.strip()!=""]
    return [ s.strip() for s in output.split("<hl>") if s.strip() != "" ]
samples = """
        قال المدافع الإيطالي ليوناردو بونوتشي إن منتخب بلاده ليس خائفا من مواجهة نظيره الانجليزي على أرضه في المباراة النهائية في بطولة يورو 2020 لكرة القدم، في حين وصف المدافع الانجليزي جون ستونز المباراة المرتقبة بأنها ستكون "أكثر تميزا".
        وسوف تقام المباراة في استاد ويمبلي، شمال غربي لندن، يوم الأحد.
        وتسعى إيطاليا لإحراز اللقب الأوروبي للمرة الثانية بعد فوزها به أول مرة عام 1968.
        ولم يفز الفريق الانجليزي بهذا اللقب القاري من قبل. والبطولة الرئيسية الوحيدة التي فازت بها انجلترا هي كأس العالم عام 1966 الذي أقيمت مباراته النهائية في استادويمبلي."""
print (get_summary(samples, tokenizer, model_nlp,device))