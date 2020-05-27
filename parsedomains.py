file_in = open("domainsblockraw.txt", "r")
file_out = open("blockedsites.js", "w")

line = file_in.readline()
file_out.write("var blocked_sites = [\n")

first = True
while(line):
    if("[" not in line):
        if not first:
             file_out.write(",\n")
        first = False
        line = (line.lstrip("||")).rstrip("^\n")
        parsed_line = "*://*." + line + "/*"
        file_out.write("\"" + parsed_line + "\"")
    line = file_in.readline()
file_out.write("]")
file_out.close()
file_in.close()