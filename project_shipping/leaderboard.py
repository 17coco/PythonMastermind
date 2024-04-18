'''
    leaderboard related fucntions of MasterMind
'''
def read(filename):
    ''' read file and return as in_file'''
    with open(filename, mode = 'r') as in_file:
        in_file = in_file.read()
    return in_file

def write(filename, output):
    '''write output string to given file'''
    with open(filename, mode = 'w') as out_file:
        out_file.write(output)

def leader_board_reader(in_file):
    '''reads leaderboard str; returns a nested list'''
    in_file = in_file.split("\n")
    in_file.pop()
    score_list = []
    for each in in_file:
        each = each.split(': ')
        score_list.append(each)

    return score_list

def leaderboard_requencer(score_list, new_record):
    '''
    resequence
    parameters:
    score_list should be a nested list (sorted)
    whose element is a list of username and score
    new_record is a list of username and score
    '''
    new_list = []
    new_score = new_record[1]

    if score_list:
        added = False
        for each in score_list:
            score = each[1]

            if int(score) > int(new_score) and not added:
                new_list.append(new_record)
                added = True

            if len(new_list) >= 5: # store up to 5 best scores
                break

            new_list.append(each)
        # if iteration is done and there's less than 5 scores stored
        # and the new rocord is not added yet
        if not added and len(new_list) < 5:
            # append the new socre at the end
            new_list.append(new_record)
    else:
        new_list.append(new_record)

    return new_list

def leaderboard_output(score_list):
    '''convert score list to ready-to-write format'''
    output_str = ''
    for each in score_list:
        each = ': '.join(each)
        each += '\n'
        output_str += each
    return output_str

def main():
    write('leaderboard.txt', "33: 4\nTrem: 7\n")
    in_file = read('leaderboard.txt')
    new_record = ["Tremolo", '4']
    print(leaderboard_output(leaderboard_requencer(
        leader_board_reader(in_file), new_record)))

if __name__ == "__main__":
    main()
