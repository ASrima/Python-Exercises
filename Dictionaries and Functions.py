'''Make a dictionary with 10 or so items (key/value pairs) whose keys are in English, and whose values are in another language
you know (or make up). Each key/value pair will be an English word and its translation in your chosen language. 
You can call this dictionary whatever you want, but an example would be english_to_mermish.

Below your dictionary, write a function called translate that takes an English word.
Inside this function, use a conditional statement (remember those?) to (a) return the translation if the word is in your dictionary,
or (b) return a message like 'Oh no! That word doesn't exist in Mermish!' if the word is not in your dictionary.

Call the function you just created, passing in an English word from your dictionary, and save the output to a new variable.
Print that variable.

Make another function call, this time with an English word not in your dictionary. As above, save the output to a variable,
and print the variable.
'''





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
