def notes(newnote):
    list = newnote.split(' ')
    newnote = newnote.strip(list[0])
    if list[0] == "add":
        target = open("notes.txt", 'a+')
        target.write("%s\n" % newnote)
        target.close()
        return "Note has been added."
    elif list[0] == "delete" or list[0] == "del":
        if list[1] == "all":
            target = open("notes.txt", 'w')
            target.close()
            return "File has been wiped. Goodbye."
        elif list[1].isdigit():
            num = int(list[1]) - 1
            
            target = open("notes.txt", 'r')
            lines = target.readlines()
            target.close()
            if num <= len(lines) and num >= 0:
                target = open("notes.txt", 'w')
                for line in lines:
                    if line != lines[num]:
                        target.write(line)
                target.close()
                return "Note deleted"
            else:
                return "Invalid argument: No item at index %d" % num
        else:
            return "Invalid argument"
    elif list[0] == "last":
        target = open("notes.txt", 'r')
        targ = target.readlines()
        print(target)
        target.close()
        return targ[len(targ) - 1]
    elif list[0] == "read":
        if list[1].isdigit():
            num = int(list[1]) - 1
            target = open("notes.txt", 'r')
            targ = target.readlines()
            target.close()
            if num <= len(targ) and num >= 0:
                return targ[num]
            else:
                return "Invalid argument: No item at index %d" % num
        else:
            return "Invalid argument" 