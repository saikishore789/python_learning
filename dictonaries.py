tools = { 'CI' : ['jenkins', 'gitlab', 'bamboo'], 'containerzation' : ['podman', 'docker'], 'Cloud' : ['aws', 'azure', 'gcp']}

x = tools.items()

print(x)

for tool, name in tools.items():
    print(tool, ':', name)

