tools = { 'CI' : ['jenkins', 'gitlab', 'bamboo'], 'containerzation' : ['podman', 'docker'], 'Cloud' : ['aws', 'azure', 'gcp']}

for tool, name in tools.items():
    print(tool, ':', name)

