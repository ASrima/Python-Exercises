english_to_pigLatin= {
    "hello":"ellohay",
    "cat": "atcay",
    "bat": "atbay",
    "creep":"reepcay",
    "emoji": "mojieay",
    "fun":"unfay",
    "flower":"lowerfay",
    "doll":"ollday",
    "all":"llaay",
    "cool":"oolcay"
    
}
def translate(word):
    if word in english_to_pigLatin: 
        return english_to_pigLatin[word]
    else:
        return "Oh no! That word doesn't exist in Pig Latin! '%s'" % word 
        
a = translate("hello")
b= translate("fun")
c = translate("boom")
print (a)  
print (b)
print(c)
