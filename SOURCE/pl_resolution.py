from inp_handler import read_file
from itertools import combinations
from itertools import product
import numpy as np


def convert_to_char(clauses):
    converted_clauses = []
    for clause in clauses:
        converted_clause = []

        if clause:
            converted_clause.extend(['-' + (chr(abs_literal + (ord('A') - 1)))
                                     if org_literal < 0
                                     else (chr(abs_literal + (ord('A') - 1)))
                                     for abs_literal, org_literal
                                     in sorted(zip(get_abs_mask(clause), clause))])

            seperator = ' OR '
            converted_clause = seperator.join(converted_clause)
            converted_clauses.append(converted_clause)
        else:
            converted_clauses.append('{}')

    return converted_clauses


def get_abs_mask(clause):
    return list(map(abs, clause))


def sort_clause(clauses):
    sorted_clauses = []
    for clause in clauses:
        sorted_clauses.append([element for _, element in sorted(zip(get_abs_mask(clause), clause))])
    return sorted_clauses


def is_subset(sub, main):
    mainset = set(map(tuple, main))
    subset = set(map(tuple, sub))

    is_sub = subset.issubset(mainset)

    if is_sub:
        return True
    else:
        return False


def to_CNF(clauses):
    return list(product(*clauses))


def negate_clauses(clauses):
    negative_clauses = []
    for clause in clauses:
        negative_clauses.append(np.negative(np.array(clause)).tolist())

    distributive_clauses = to_CNF(negative_clauses)

    negators = []
    for element in distributive_clauses:
        negators.append(list(set(element)))

    negators = list(set(map(tuple, sort_clause(negators))))

    eliminated_negators = []
    for clause in negators:
        is_valid = True
        for literal in clause:
            if -literal in clause:
                is_valid = False
                break
        if is_valid:
            eliminated_negators.append(clause)

    eliminated_negators.sort(key=len)

    not_alpha = []
    for idx, clause in enumerate(eliminated_negators):
        if idx == 0:
            not_alpha.append(clause)
        else:
            if all(element is False for element in [set(alpha_clause).issubset(set(clause))
                                                    for alpha_clause in not_alpha]):
                not_alpha.append(clause)

    not_alpha = list(map(list, not_alpha))

    return not_alpha


def pl_resolve(pair):
    clause_1, clause_2 = pair

    clause_1 = set(clause_1)
    clause_2 = set(np.negative(np.array(clause_2)).tolist())

    intersect = clause_1.intersection(clause_2)

    if len(intersect) == 0:
        return []
    elif len(intersect) == 1:
        resolvents = []

        clause_1 -= intersect
        clause_2 -= intersect

        clause_2 = set(np.negative(np.array(list(clause_2))).tolist())

        union = clause_1.union(clause_2)

        resolvent = list(union)

        resolvents.append(resolvent)

        return resolvents
    else:
        return [[None]]


def pl_resolution(KB, alpha, index):
    """ Open file stream """
    out_file = open(r'..\OUTPUT\output' + str(index + 1) + '.txt', 'w')

    """ Negate the alpha clauses to add it into KB """
    not_alpha = negate_clauses(alpha)

    """ Add KB AND NOT alpha into KB """
    # Unpack lists of lists
    clauses = [*KB, *not_alpha]

    while True:
        new = []
        cannot_resolved = False

        clauses_pairs = list(combinations(clauses, 2))

        for pair in clauses_pairs:
            resolvents = pl_resolve(pair)
            if (not resolvents) or (resolvents[0] == [None]):
                continue
            elif not resolvents[0]:
                cannot_resolved = True
                if (not is_subset(resolvents, clauses)) and (not is_subset(resolvents, new)):
                    new.append(resolvents[0])
            else:
                resolvents = sort_clause(resolvents)
                if (not is_subset(resolvents, clauses)) and (not is_subset(resolvents, new)):
                    new.append(resolvents[0])

        normal_form = convert_to_char(new)
        out_file.write(str(len(new)) + '\n')
        for clause in normal_form:
            out_file.writelines(clause + '\n')

        if cannot_resolved:
            out_file.write('YES')
            out_file.close()
            return True

        if is_subset(new, clauses):
            out_file.write('NO')
            out_file.close()
            return False
        clauses.extend(new)


if __name__ == '__main__':
    for idx in range(9):
        KB, alpha = read_file(r'..\INPUT\input' + str(idx + 1) + '.txt')

        is_entailed = pl_resolution(KB, alpha, idx)
