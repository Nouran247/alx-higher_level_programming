#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    all_names = dir(hidden_4)
    for i in all_names:
        if i[0] != '_' and i[1] != '_':
            print(i)
