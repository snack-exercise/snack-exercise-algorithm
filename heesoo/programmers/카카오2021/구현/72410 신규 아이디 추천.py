def solution(new_id):
    #1
    new_id=new_id.lower()
    
    #2
    for id in new_id:
        if id == '-' or id=='_' or id=='.' or id.isalpha() or id.isdigit():
            continue
        new_id=new_id.replace(id,'')
    
    #3
    new_str=[]
    prev=''
    for id in new_id:
        if prev!=id or prev!='.':
            new_str.append(id)
            prev=id
    new_id=''.join(new_str)
    
    #4
    if new_id[0]=='.':
        new_id=new_id[1:]
    elif new_id[-1]=='.':
        new_id=new_id[:-1]
        
    #5
    if new_id=='':
        new_id='a'
    
    #6
    if len(new_id)>=16:
        new_id=new_id[0:15]
    if new_id[-1]=='.':
        new_id=new_id[:-1]  
    
    #7
    while(len(new_id)<3):
        new_id+=new_id[-1]
    
    return new_id