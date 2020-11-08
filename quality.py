import textwrap
import imperative


def get_quality(commit):
    score = 7
    commit_message = get_commit_message(commit)
    if not rule_1(commit_message):
        score -= 1

    if not rule_2(commit_message):
        score -= 1

    if not rule_3(commit_message):
        score -= 1

    if not rule_4(commit_message):
        score -= 1

    if not rule_5(commit_message):
        score -= 1

    if not rule_6(commit_message):
        score -= 1

    return score


def get_commit_message(commit):
    try:
        return commit[commit.index('') + 1:]
    except ValueError:  # '' is not in list
        return commit.split('\n')


# "Separate subject from body with a blank line"
def rule_1(message_array):
    if len(message_array) > 1 and textwrap.dedent(message_array[1]) != '':
        return False
    return True


# "Limit the subject line to 50 characters"
def rule_2(message_array):
    first_line = textwrap.dedent(message_array[0])
    return len(first_line) <= 50


# "Capitalize the subject line"
def rule_3(message_array):
    first_line = textwrap.dedent(message_array[0])
    return str.isupper(first_line[0])


# "Do not end the subject line with a period"
def rule_4(message_array):
    return message_array[0][-1] != "."


# "Use the imperative mood in the subject line"
def rule_5(message_array):
    first_line = textwrap.dedent(message_array[0])
    first_word = first_line.split(" ")[0]
    return first_word.lower() in imperative.words


# "Wrap the body at 72 characters"
def rule_6(message_array):
    if len(message_array) > 1:
        for line in message_array:
            if len(line) > 72:
                return False
    return True


# "Use the body to explain what and why vs. how"
def rule_7():
    return True
