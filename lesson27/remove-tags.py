# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(s):
    splited = []
    if(s.find('<') == -1):
        return s.split()
    while True:
        start_tag = s.find('<')
        if(start_tag != -1):
            splited.extend(s[0:start_tag].split())
            s = s[s.find('>',start_tag)+1:]
        else:
            splited.extend(s[s.find('>',start_tag)+1:].split())
            break
    return splited
    
print remove_tags('<br />This line starts with a tag')
#>>> ['Title','This','is','a','link','.']

#print remove_tags('''<table cellpadding='3'>
#                     <tr><td>Hello</td><td>World!</td></tr>
#                     </table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

#print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
