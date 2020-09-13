def read_file(file_name):
    file = open(file_name, "r")

    alpha_no = int(file.readline())

    alpha_clauses = []

    for idx in range(alpha_no):
        clause_txt = file.readline().replace('\n', '').split(' OR ')

        clause = []
        for character in clause_txt:
            if len(character) == 1:
                clause.append(ord(character[0]) - (ord('A') - 1))
            else:
                clause.append(-(ord(character[1]) - (ord('A') - 1)))

        alpha_clauses.append(clause)

    KB_no = int(file.readline())

    KB_clauses = []

    for idx in range(KB_no):
        clause_txt = file.readline().replace('\n', '').split(' OR ')

        clause = []
        for character in clause_txt:
            if len(character) == 1:
                clause.append(ord(character[0]) - (ord('A') - 1))
            else:
                clause.append(-(ord(character[1]) - (ord('A') - 1)))

        KB_clauses.append(clause)

    file.close()

    return KB_clauses, alpha_clauses
