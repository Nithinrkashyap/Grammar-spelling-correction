from textblob import TextBlob
# from gingerit.gingerit import GingerIt
import spacy
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        self.tool=language_tool_python.LanguageTool('en-us')
        self.nlp= spacy.load("en_core_web_sm")
        
    def correct_spell(self,text):
        #helo hi guys
        #* tokenize
        words=text.split()
        corrected_words=[]
        #[helo ,hi ,guys]
        for word in words:
            corrected_word=str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)
    
    
    def correct_grammar(self,text):
        doc=self.nlp(text)
        #* matches [Match({'ruleId': 'MORFOLOGIK_RULE_EN_US', 'message': 'Possible spelling mistake found.', 'replacements': ['machine', 'mashing'], 'offsetInContext': 20, 'context': 'Hello world. I like mashine learning. appple. bananana', 'offset': 20, 'errorLength': 7, 'category': 'TYPOS', 'ruleIssueType': 'misspelling', 'sentence': 'I like mashine learning.'}), Match({'ruleId': 'UPPERCASE_SENTENCE_START', 'message': 'This sentence does not start with an uppercase letter.', 'replacements': ['Appple'], 'offsetInContext': 38, 'context': 'Hello world. I like mashine learning. appple. bananana', 'offset': 38, 'errorLength': 6, 'category': 'CASING', 'ruleIssueType': 'typographical', 'sentence': 'appple.'}), Match({'ruleId': 'UPPERCASE_SENTENCE_START', 'message': 'This sentence does not start with an uppercase letter.', 'replacements': ['Bananana'], 'offsetInContext': 43, 'context': '...world. I like mashine learning. appple. bananana', 'offset': 46, 'errorLength': 8, 'category': 'CASING', 'ruleIssueType': 'typographical', 'sentence': 'bananana'})]
        #& matches contains error words
        matches=self.tool.check(text)
        incorrect_words=[]
        corrected_words=[]
        #& reverses in decresing order
        matches.sort(key=lambda x: x.offset, reverse=True)
        for match in matches:
            start=match.offset
            end=start+match.errorLength
            #^ start=20 end=20+7  [20,26] includes in incorrect word
            incorrect_word=text[start:end]
            incorrect_words.append(incorrect_word)
            incorrect_words_count=len(incorrect_words)
            corrected_words.append(match.replacements[0])
            text=text[:start]+match.replacements[0]+text[end:]
        print("corrected text",text)    
        correct_text=text
        return incorrect_words,incorrect_words_count,correct_text
        
        
        
        
        
if __name__ == "__main__":
    
    obj=SpellCheckerModule()
    message = "hello world I like mashine learning appple bananana"  

#* (['bananana', 'appple', 'mashine', 'hello'], 4, 'Hello world I like machine learning Apple banana') its a tuple
    incorrect_words,incorrect_words_count,correct_text=obj.correct_grammar(message) 
    print(obj.correct_spell(message))    
    # print("spell check",obj.spell_check)
    print(obj.correct_grammar(message))    
    correct_spell=obj.correct_spell(message)
    print("correct_spell",correct_spell)
    print("incorrected words",incorrect_words)