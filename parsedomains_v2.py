file_in = open("domainsblockraw_v2.txt", "r")
file_out = open("blockedsites_v2.js", "w")

line = file_in.readline()
file_out.write("var blocked_sites_v2 = [\n")

first = True
while(line):
    if("# [" in line):
        if not first:
             file_out.write(",\n")
        first = False
        line = (line.lstrip("# [")).rstrip("]\n")
        parsed_line = "*://*." + line + "/*"
        file_out.write("\"" + parsed_line + "\"")
    line = file_in.readline()
file_out.write("]")
file_out.close()
file_in.close()