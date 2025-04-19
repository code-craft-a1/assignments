import sys
import requests
import inquirer
import pyperclip

def map_assignments_to_links(classroom_id, github_token):
    url = f'https://api.github.com/classrooms/{classroom_id}/assignments'
    headers = {
        'Authorization': f'Bearer {github_token}',
        'Accept': 'application/vnd.github+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch assignments: {response.status_code} {response.text}')

    assignments = response.json()
    invite_links = {}
    for assignment in assignments:
        invite_links[assignment.get('slug')] = assignment.get('invite_link')
    return invite_links


def extract_unique_prefixes(assignment_links):
    prefixes = {key.split('-in-')[0] for key in assignment_links.keys()}
    return prefixes


def assignment_to_lang(assignment):
    lang_map = {
        'cpp': 'C++',
        'cs': 'C#',
        'java': 'Java',
        'py': 'Python',
        'js': 'JavaScript',
    }
    return lang_map.get(assignment.split('-in-')[1])


def assignment_links_in_md(assignment_links, selected_assignment):
    selected_links = {key: value for key, value in assignment_links.items() if key.startswith(selected_assignment)}
    md_lines = [f'[{assignment_to_lang(assignment)}]({value})' for assignment, value in selected_links.items()]
    languages_order = ['C++', 'C#', 'Java', 'Python', 'JavaScript']
    sorted_md_lines = sorted(md_lines, key=lambda line: languages_order.index(line.split(']')[0][1:]))
    md_content = '\n\n'.join(sorted_md_lines)

    return md_content


if __name__ == '__main__':
    classroom_id = '264960'  # classroom ID of code-craft-a1
    github_token = sys.argv[1]
    try:
        assignment_links = map_assignments_to_links(classroom_id, github_token)
        assignment_names = extract_unique_prefixes(assignment_links)
        questions = [
            inquirer.List(
            'assignment',
            message='Select an assignment',
            choices=list(assignment_names),
            )
        ]
        selected_assignment = inquirer.prompt(questions)['assignment']
        print(f'You selected: {selected_assignment}')
        md = assignment_links_in_md(assignment_links, selected_assignment)
        pyperclip.copy(md)
        print(md)
        print('Markdown content has been copied to the clipboard.')
    except Exception as e:
        print(f'Error: {e}')
